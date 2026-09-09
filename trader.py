import os, math, time, requests
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from run_strategy import run_strategy

TICKERS = ["AAPX","AGG","AGQ","AMZN","AMZU","AMZZ","BABA","BAM","BIL","BITX","BN","BND","BTAL","BX","COIN","CONL","EDC","EDZ","EEM","FAS","FAZ","FBL","GDXD","GDXU","GGLL","GLD","HOOD","IBKR","IEF","IEI","IGIB","IOO","IUSV","IVW","IWM","KKR","KMLM","MA","META","NVDL","PLTR","PSQ","QLD","QQQ","QQQE","RGTI","SCHW","SH","SHV","SOFI","SOXL","SOXS","SPXL","SPY","SQQQ","SVIX","TECL","TECS","TLT","TMF","TQQQ","TSLA","TSLR","UGL","UPRO","UVXY","V","VIXM","VIXY","VOOG","VOOV","VOX","VTR","VTV","WELL","XLF","XLK","XLP","XLY"]
W=220
NY=ZoneInfo('America/New_York')
PAPER='https://paper-api.alpaca.markets'
DATA='https://data.alpaca.markets'
KEY=os.environ['ALPACA_API_KEY']; SECRET=os.environ['ALPACA_SECRET_KEY']
TG_TOKEN=os.environ.get('TELEGRAM_BOT_TOKEN',''); TG_CHAT=os.environ.get('TELEGRAM_CHAT_ID','')
HEAD={'APCA-API-KEY-ID':KEY,'APCA-API-SECRET-KEY':SECRET}

class MissingTicker(Exception): pass
class GatedPrices(dict):
    def __missing__(self,k): raise MissingTicker(f'{k} has fewer than {W} real adjusted daily bars')

def api(method,url,**kw):
    r=requests.request(method,url,headers=HEAD,timeout=30,**kw)
    if not r.ok: raise RuntimeError(f'{method} {url} -> {r.status_code}: {r.text[:500]}')
    return r.json() if r.text else {}

def tg(text):
    if not (TG_TOKEN and TG_CHAT): return
    for i in range(0,len(text),3900):
        try: requests.post(f'https://api.telegram.org/bot{TG_TOKEN}/sendMessage',json={'chat_id':TG_CHAT,'text':text[i:i+3900]},timeout=20).raise_for_status()
        except Exception as e: print('Telegram error:',e)

def clock(): return api('GET',f'{PAPER}/v2/clock')

def fetch_prices(today):
    start=(today-timedelta(days=420)).isoformat(); end=today.isoformat()
    bars={t:[] for t in TICKERS}; token=None
    while True:
        params={'symbols':','.join(TICKERS),'timeframe':'1Day','start':start,'end':end,'adjustment':'all','feed':'sip','limit':10000,'sort':'asc'}
        if token: params['page_token']=token
        data=api('GET',f'{DATA}/v2/stocks/bars',params=params)
        for t,rows in data.get('bars',{}).items(): bars[t].extend(rows)
        token=data.get('next_page_token')
        if not token: break
    prices=GatedPrices()
    for t,rows in bars.items():
        vals=[float(x['c']) for x in rows if 'c' in x]
        if len(vals)>=W: prices[t]=vals[-W:]
    return prices, bars

def positions():
    try: rows=api('GET',f'{PAPER}/v2/positions')
    except RuntimeError as e:
        if '404' in str(e): return {}
        raise
    return {p['symbol']:p for p in rows}

def account(): return api('GET',f'{PAPER}/v2/account')

def validate_assets():
    bad=[]
    for t in TICKERS:
        try:
            a=api('GET',f'{PAPER}/v2/assets/{t}')
            if not a.get('tradable',False): bad.append(t)
        except Exception: bad.append(t)
    if bad: tg('PRE-FLIGHT WARNING\nAlpaca not tradable/unavailable: '+', '.join(bad))

def submit(symbol,qty,side):
    if qty<=0:return None
    body={'symbol':symbol,'qty':str(int(qty)),'side':side,'type':'market','time_in_force':'cls','client_order_id':f'lr-{datetime.now(NY):%Y%m%d}-{symbol}-{side}'[:48]}
    return api('POST',f'{PAPER}/v2/orders',json=body)

def main():
    now=datetime.now(NY); c=clock()
    if not c.get('is_open'):
        tg(f'NO TRADE\n{now:%Y-%m-%d %H:%M ET}\nUS market is closed. Holdings unchanged.')
        return
    # Safety: never submit at/after 15:45 ET; official rejection cutoff is 15:50 ET.
    if now.hour>15 or (now.hour==15 and now.minute>=45):
        tg(f'SKIPPED - TOO LATE\n{now:%Y-%m-%d %H:%M ET}\nNo stale signal will be chased. Next trading day recalculates fresh.')
        return
    today=now.date(); prices,bars=fetch_prices(today)
    try: weights=run_strategy(prices)
    except (MissingTicker,KeyError) as e:
        tg(f'STRATEGY SKIPPED\nDate: {today}\nReason: active tree requires unavailable/young ticker: {e}\nHoldings unchanged.')
        return
    s=sum(weights.values())
    if not (0.999999<=s<=1.000001): raise RuntimeError(f'Weight sum invalid: {s}')
    acct=account(); equity=float(acct['equity']); pos=positions()
    # Reference price = latest completed adjusted daily close (d-1 or earlier).
    ref={t:float(prices[t][-1]) for t in weights}
    target_qty={t:max(0,int(math.floor(equity*w/ref[t]))) for t,w in weights.items()}
    cur={t:int(float(p['qty'])) for t,p in pos.items()}
    deltas={t:target_qty.get(t,0)-cur.get(t,0) for t in set(cur)|set(target_qty)}
    orders=[]; errors=[]
    # Sells first, then buys.
    for side in ('sell','buy'):
        for t,d in sorted(deltas.items()):
            q=(-d if side=='sell' else d)
            if q<=0: continue
            try: orders.append(submit(t,q,side))
            except Exception as e: errors.append(f'{t} {side} {q}: {e}')
    lines=[f'LEVERAGED ROTATION - MOC SUBMITTED',f'Date: {today}',f'Account equity: ${equity:,.2f}',f'Eligible history: {len(prices)}/{len(TICKERS)} tickers',f'Target assets: {len(weights)}',f'Orders submitted: {len(orders)} | errors: {len(errors)}','', 'TARGETS']
    for t,w in sorted(weights.items(), key=lambda kv:-kv[1]): lines.append(f'{t}: {w*100:.2f}% | target {target_qty[t]} sh | current {cur.get(t,0)} sh | delta {deltas[t]:+d}')
    if errors: lines += ['', 'ERRORS']+errors
    lines += ['', 'Policy: no retry/chasing of rejected or missed MOC orders; next trading day recalculates a fresh signal.']
    tg('\n'.join(lines))

if __name__=='__main__':
    try: main()
    except Exception as e:
        tg(f'FATAL ERROR\n{datetime.now(NY):%Y-%m-%d %H:%M ET}\n{type(e).__name__}: {e}\nNo stale order retry.')
        raise

from typing import Dict, Sequence

import strategy_runtime as rt


def _node_asset_EDZ_923(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDZ': 1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_923'] = _node_asset_EDZ_923


def _node_asset_BIL_924(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_924'] = _node_asset_BIL_924


def _node_wt_cash_specified_925(prices):
    return rt.combine_weighted([((float('33') / float(100)), rt.call_node('_node_asset_EDZ_923', prices)), ((float(67) / float(100)), rt.call_node('_node_asset_BIL_924', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_925'] = _node_wt_cash_specified_925


def _node_if_926(prices):
    if rt.relative_strength_index(prices['IGIB'], 15) > rt.relative_strength_index(prices['EEM'], 15):
        return rt.call_node('_node_asset_EEM_922', prices)
    return rt.call_node('_node_wt_cash_specified_925', prices)
rt.NODE_REGISTRY['_node_if_926'] = _node_if_926

def _node_wt_cash_equal_927(prices): return rt.combine_equal([rt.call_node('_node_if_926', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_927'] = _node_wt_cash_equal_927

def _node_asset_EEM_928(prices): return {'EEM': 1.0}
rt.NODE_REGISTRY['_node_asset_EEM_928'] = _node_asset_EEM_928
def _node_asset_EDZ_929(prices): return {'EDZ': 1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_929'] = _node_asset_EDZ_929
def _node_asset_BIL_930(prices): return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_930'] = _node_asset_BIL_930
def _node_wt_cash_specified_931(prices): return rt.combine_weighted([((float('33')/100),rt.call_node('_node_asset_EDZ_929',prices)),((float(67)/100),rt.call_node('_node_asset_BIL_930',prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_931'] = _node_wt_cash_specified_931
def _node_if_932(prices):
    return rt.call_node('_node_asset_EEM_928' if rt.relative_strength_index(prices['IGIB'],10)>rt.relative_strength_index(prices['SPY'],10) else '_node_wt_cash_specified_931',prices)
rt.NODE_REGISTRY['_node_if_932'] = _node_if_932
def _node_wt_cash_equal_933(prices): return rt.combine_equal([rt.call_node('_node_if_932',prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_933'] = _node_wt_cash_equal_933
def _node_combine_equal_934(prices): return rt.combine_equal([rt.call_node('_node_wt_cash_equal_927',prices),rt.call_node('_node_wt_cash_equal_933',prices)])
rt.NODE_REGISTRY['_node_combine_equal_934'] = _node_combine_equal_934
def _node_if_935(prices): return rt.call_node('_node_wt_cash_equal_921' if rt.current_price(prices['EEM'])>rt.moving_average_price(prices['EEM'],200) else '_node_combine_equal_934',prices)
rt.NODE_REGISTRY['_node_if_935'] = _node_if_935
def _node_wt_cash_equal_936(prices): return rt.combine_equal([rt.call_node('_node_if_935',prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_936'] = _node_wt_cash_equal_936
def _node_asset_EEM_937(prices): return {'EEM':1.0}
rt.NODE_REGISTRY['_node_asset_EEM_937'] = _node_asset_EEM_937
def _node_asset_EDZ_938(prices): return {'EDZ':1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_938'] = _node_asset_EDZ_938
def _node_asset_BIL_939(prices): return {'BIL':1.0}
rt.NODE_REGISTRY['_node_asset_BIL_939'] = _node_asset_BIL_939
def _node_wt_cash_specified_940(prices): return rt.combine_weighted([((float('33')/100),rt.call_node('_node_asset_EDZ_938',prices)),((float(67)/100),rt.call_node('_node_asset_BIL_939',prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_940'] = _node_wt_cash_specified_940
def _node_if_941(prices): return rt.call_node('_node_asset_EEM_937' if rt.relative_strength_index(prices['IGIB'],10)>rt.relative_strength_index(prices['SPY'],10) else '_node_wt_cash_specified_940',prices)
rt.NODE_REGISTRY['_node_if_941'] = _node_if_941
def _node_wt_cash_equal_942(prices): return rt.combine_equal([rt.call_node('_node_if_941',prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_942'] = _node_wt_cash_equal_942
def _node_if_943(prices): return rt.call_node('_node_wt_cash_equal_936' if rt.current_price(prices['SHV'])>rt.moving_average_price(prices['SHV'],50) else '_node_wt_cash_equal_942',prices)
rt.NODE_REGISTRY['_node_if_943'] = _node_if_943
def _node_wt_cash_equal_944(prices): return rt.combine_equal([rt.call_node('_node_if_943',prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_944'] = _node_wt_cash_equal_944
def _node_if_945(prices): return rt.call_node('_node_wt_cash_specified_915' if rt.relative_strength_index(prices['EEM'],10)<25.0 else '_node_wt_cash_equal_944',prices)
rt.NODE_REGISTRY['_node_if_945'] = _node_if_945
def _node_wt_cash_equal_946(prices): return rt.combine_equal([rt.call_node('_node_if_945',prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_946'] = _node_wt_cash_equal_946
def _node_wt_cash_equal_947(prices): return rt.combine_equal([rt.call_node('_node_wt_cash_equal_946',prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_947'] = _node_wt_cash_equal_947
def _node_if_948(prices): return rt.call_node('_node_wt_cash_equal_912' if rt.current_price(prices['SPY'])>rt.moving_average_price(prices['SPY'],200) else '_node_wt_cash_equal_947',prices)
rt.NODE_REGISTRY['_node_if_948'] = _node_if_948
def _node_wt_cash_equal_949(prices): return rt.combine_equal([rt.call_node('_node_if_948',prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_949'] = _node_wt_cash_equal_949
def _node_wt_cash_equal_950(prices): return rt.combine_equal([rt.call_node('_node_wt_cash_equal_949',prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_950'] = _node_wt_cash_equal_950
def _node_wt_cash_equal_951(prices): return rt.combine_equal([rt.call_node('_node_wt_cash_equal_819',prices),rt.call_node('_node_wt_cash_equal_885',prices),rt.call_node('_node_wt_cash_equal_950',prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_951'] = _node_wt_cash_equal_951
def _node_wt_cash_equal_952(prices): return rt.combine_equal([rt.call_node('_node_wt_cash_equal_331',prices),rt.call_node('_node_wt_cash_equal_661',prices),rt.call_node('_node_wt_cash_equal_951',prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_952'] = _node_wt_cash_equal_952

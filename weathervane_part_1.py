from typing import Dict, Sequence

import strategy_runtime as rt


def _node_if_238(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) > 79.0:
        return rt.call_node('_node_wt_cash_equal_181', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_237', prices)
rt.NODE_REGISTRY['_node_if_238'] = _node_if_238


def _node_wt_cash_equal_239(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_238', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_239'] = _node_wt_cash_equal_239


def _node_if_240(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLP'], 10) > 77.0:
        return rt.call_node('_node_asset_UVXY_179', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_239', prices)
rt.NODE_REGISTRY['_node_if_240'] = _node_if_240


def _node_wt_cash_specified_241(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float(100) / float(100)), rt.call_node('_node_if_240', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_241'] = _node_wt_cash_specified_241


def _node_if_242(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['UVXY'], 10) > 84.0:
        return rt.call_node('_node_asset_SOXL_178', prices)
    else:
        return rt.call_node('_node_wt_cash_specified_241', prices)
rt.NODE_REGISTRY['_node_if_242'] = _node_if_242


def _node_wt_cash_equal_243(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_242', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_243'] = _node_wt_cash_equal_243


def _node_asset_SOXL_244(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_244'] = _node_asset_SOXL_244


def _node_asset_UVXY_245(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_245'] = _node_asset_UVXY_245


def _node_asset_UVXY_246(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_246'] = _node_asset_UVXY_246


def _node_asset_UVXY_247(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_247'] = _node_asset_UVXY_247


def _node_asset_UVXY_248(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_248'] = _node_asset_UVXY_248


def _node_asset_UVXY_249(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_249'] = _node_asset_UVXY_249


def _node_asset_UVXY_250(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_250'] = _node_asset_UVXY_250


def _node_asset_UVXY_251(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_251'] = _node_asset_UVXY_251


def _node_asset_SOXL_252(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_252'] = _node_asset_SOXL_252


def _node_wt_cash_equal_253(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_252', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_253'] = _node_wt_cash_equal_253


def _node_asset_UVXY_254(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_254'] = _node_asset_UVXY_254


def _node_asset_SOXL_255(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_255'] = _node_asset_SOXL_255


def _node_if_256(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['UVXY'], 10) < 84.0:
        return rt.call_node('_node_asset_UVXY_254', prices)
    else:
        return rt.call_node('_node_asset_SOXL_255', prices)
rt.NODE_REGISTRY['_node_if_256'] = _node_if_256


def _node_wt_cash_equal_257(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_256', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_257'] = _node_wt_cash_equal_257


def _node_asset_SOXL_258(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_258'] = _node_asset_SOXL_258


def _node_wt_cash_equal_259(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_258', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_259'] = _node_wt_cash_equal_259


def _node_asset_SOXL_260(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_260'] = _node_asset_SOXL_260


def _node_wt_cash_equal_261(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_260', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_261'] = _node_wt_cash_equal_261


def _node_asset_SQQQ_262(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_SQQQ_262'] = _node_asset_SQQQ_262


def _node_wt_cash_equal_263(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SQQQ_262', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_263'] = _node_wt_cash_equal_263


def _node_asset_SOXL_264(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_264'] = _node_asset_SOXL_264


def _node_wt_cash_equal_265(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_264', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_265'] = _node_wt_cash_equal_265


def _node_if_266(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['PSQ'], 10) < 33.0:
        return rt.call_node('_node_wt_cash_equal_263', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_265', prices)
rt.NODE_REGISTRY['_node_if_266'] = _node_if_266


def _node_wt_cash_equal_267(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_266', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_267'] = _node_wt_cash_equal_267


def _node_asset_SOXL_268(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_268'] = _node_asset_SOXL_268


def _node_wt_cash_equal_269(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_268', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_269'] = _node_wt_cash_equal_269


def _node_asset_SOXL_270(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_270'] = _node_asset_SOXL_270


def _node_wt_cash_equal_271(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_270', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_271'] = _node_wt_cash_equal_271


def _node_asset_SOXL_272(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_272'] = _node_asset_SOXL_272


def _node_wt_cash_equal_273(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_272', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_273'] = _node_wt_cash_equal_273


def _node_asset_GLD_274(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'GLD': 1.0}
rt.NODE_REGISTRY['_node_asset_GLD_274'] = _node_asset_GLD_274


def _node_if_275(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) > rt.relative_strength_index(prices['TLT'], 10):
        return rt.call_node('_node_wt_cash_equal_273', prices)
    else:
        return rt.call_node('_node_asset_GLD_274', prices)
rt.NODE_REGISTRY['_node_if_275'] = _node_if_275


def _node_wt_cash_equal_276(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_275', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_276'] = _node_wt_cash_equal_276


def _node_asset_SQQQ_277(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_SQQQ_277'] = _node_asset_SQQQ_277


def _node_filter_278(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.relative_strength_index(prices['SQQQ'], 10), rt.call_node('_node_asset_SQQQ_277', prices))], 'top', int('1'))
rt.NODE_REGISTRY['_node_filter_278'] = _node_filter_278


def _node_wt_cash_equal_279(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_278', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_279'] = _node_wt_cash_equal_279


def _node_asset_TMF_280(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TMF': 1.0}
rt.NODE_REGISTRY['_node_asset_TMF_280'] = _node_asset_TMF_280


def _node_asset_TQQQ_281(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_281'] = _node_asset_TQQQ_281


def _node_wt_cash_equal_282(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_TQQQ_281', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_282'] = _node_wt_cash_equal_282


def _node_if_283(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['TLT']) > rt.moving_average_price(prices['TLT'], 200):
        return rt.call_node('_node_asset_TMF_280', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_282', prices)
rt.NODE_REGISTRY['_node_if_283'] = _node_if_283


def _node_wt_cash_equal_284(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_283', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_284'] = _node_wt_cash_equal_284


def _node_if_285(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['PSQ'], 10) > rt.relative_strength_index(prices['TLT'], 10):
        return rt.call_node('_node_wt_cash_equal_279', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_284', prices)
rt.NODE_REGISTRY['_node_if_285'] = _node_if_285


def _node_wt_cash_equal_286(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_285', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_286'] = _node_wt_cash_equal_286


def _node_if_287(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['PSQ'], 10) > 65.0:
        return rt.call_node('_node_wt_cash_equal_276', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_286', prices)
rt.NODE_REGISTRY['_node_if_287'] = _node_if_287


def _node_wt_cash_equal_288(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_287', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_288'] = _node_wt_cash_equal_288


def _node_wt_cash_equal_289(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_288', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_289'] = _node_wt_cash_equal_289


def _node_if_290(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['SPY']) > rt.moving_average_price(prices['SPY'], 30):
        return rt.call_node('_node_wt_cash_equal_271', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_289', prices)
rt.NODE_REGISTRY['_node_if_290'] = _node_if_290


def _node_wt_cash_equal_291(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_290', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_291'] = _node_wt_cash_equal_291


def _node_if_292(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) < 31.0:
        return rt.call_node('_node_wt_cash_equal_269', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_291', prices)
rt.NODE_REGISTRY['_node_if_292'] = _node_if_292


def _node_wt_cash_equal_293(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_292', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_293'] = _node_wt_cash_equal_293


def _node_if_294(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['QQQ']) > rt.moving_average_price(prices['QQQ'], 20):
        return rt.call_node('_node_wt_cash_equal_267', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_293', prices)
rt.NODE_REGISTRY['_node_if_294'] = _node_if_294


def _node_wt_cash_equal_295(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_294', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_295'] = _node_wt_cash_equal_295


def _node_if_296(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) < 30.0:
        return rt.call_node('_node_wt_cash_equal_261', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_295', prices)
rt.NODE_REGISTRY['_node_if_296'] = _node_if_296


def _node_wt_cash_equal_297(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_296', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_297'] = _node_wt_cash_equal_297


def _node_if_298(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) < 28.0:
        return rt.call_node('_node_wt_cash_equal_259', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_297', prices)
rt.NODE_REGISTRY['_node_if_298'] = _node_if_298


def _node_wt_cash_equal_299(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_298', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_299'] = _node_wt_cash_equal_299


def _node_if_300(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['UVXY'], 10) > 74.0:
        return rt.call_node('_node_wt_cash_equal_257', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_299', prices)
rt.NODE_REGISTRY['_node_if_300'] = _node_if_300


def _node_wt_cash_equal_301(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_300', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_301'] = _node_wt_cash_equal_301


def _node_if_302(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) < 18.0:
        return rt.call_node('_node_wt_cash_equal_253', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_301', prices)
rt.NODE_REGISTRY['_node_if_302'] = _node_if_302


def _node_wt_cash_equal_303(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_302', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_303'] = _node_wt_cash_equal_303


def _node_if_304(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['SOXL'], 1) < -24.0:
        return rt.call_node('_node_asset_UVXY_251', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_303', prices)
rt.NODE_REGISTRY['_node_if_304'] = _node_if_304


def _node_wt_cash_equal_305(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_304', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_305'] = _node_wt_cash_equal_305


def _node_if_306(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 60) > 52.0:
        return rt.call_node('_node_asset_UVXY_250', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_305', prices)
rt.NODE_REGISTRY['_node_if_306'] = _node_if_306


def _node_wt_cash_equal_307(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_306', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_307'] = _node_wt_cash_equal_307


def _node_if_308(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 60) > 55.0:
        return rt.call_node('_node_asset_UVXY_249', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_307', prices)
rt.NODE_REGISTRY['_node_if_308'] = _node_if_308


def _node_wt_cash_equal_309(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_308', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_309'] = _node_wt_cash_equal_309


def _node_if_310(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 6) > 78.0:
        return rt.call_node('_node_asset_UVXY_248', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_309', prices)
rt.NODE_REGISTRY['_node_if_310'] = _node_if_310


def _node_wt_cash_equal_311(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_310', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_311'] = _node_wt_cash_equal_311


def _node_if_312(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) > 77.0:
        return rt.call_node('_node_asset_UVXY_247', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_311', prices)
rt.NODE_REGISTRY['_node_if_312'] = _node_if_312


def _node_wt_cash_equal_313(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_312', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_313'] = _node_wt_cash_equal_313


def _node_if_314(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) > 72.0:
        return rt.call_node('_node_asset_UVXY_246', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_313', prices)
rt.NODE_REGISTRY['_node_if_314'] = _node_if_314


def _node_wt_cash_equal_315(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_314', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_315'] = _node_wt_cash_equal_315


def _node_if_316(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLP'], 10) > 76.0:
        return rt.call_node('_node_asset_UVXY_245', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_315', prices)
rt.NODE_REGISTRY['_node_if_316'] = _node_if_316


def _node_wt_cash_equal_317(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_316', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_317'] = _node_wt_cash_equal_317


def _node_if_318(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['UVXY'], 10) > 84.0:
        return rt.call_node('_node_asset_SOXL_244', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_317', prices)
rt.NODE_REGISTRY['_node_if_318'] = _node_if_318


def _node_wt_cash_equal_319(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_318', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_319'] = _node_wt_cash_equal_319


def _node_if_320(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['SPY']) > rt.moving_average_price(prices['SPY'], 200):
        return rt.call_node('_node_wt_cash_equal_243', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_319', prices)
rt.NODE_REGISTRY['_node_if_320'] = _node_if_320


def _node_wt_cash_equal_321(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_320', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_321'] = _node_wt_cash_equal_321


def _node_if_322(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['SOXL'], 5) < -57.0:
        return rt.call_node('_node_asset_SOXL_177', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_321', prices)
rt.NODE_REGISTRY['_node_if_322'] = _node_if_322


def _node_wt_cash_equal_323(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_322', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_323'] = _node_wt_cash_equal_323


def _node_if_324(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['SOXL'], 2) < -37.0:
        return rt.call_node('_node_asset_SOXL_176', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_323', prices)
rt.NODE_REGISTRY['_node_if_324'] = _node_if_324


def _node_wt_cash_equal_325(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_324', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_325'] = _node_wt_cash_equal_325


def _node_if_326(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['SOXL'], 1) < -31.0:
        return rt.call_node('_node_asset_SOXL_175', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_325', prices)
rt.NODE_REGISTRY['_node_if_326'] = _node_if_326


def _node_wt_cash_equal_327(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_326', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_327'] = _node_wt_cash_equal_327


def _node_if_328(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.moving_average_return(prices['QQQ'], 10) < -2.4:
        return rt.call_node('_node_asset_SOXL_174', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_327', prices)
rt.NODE_REGISTRY['_node_if_328'] = _node_if_328


def _node_wt_cash_equal_329(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_328', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_329'] = _node_wt_cash_equal_329


def _node_wt_cash_equal_330(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_329', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_330'] = _node_wt_cash_equal_330


def _node_wt_cash_equal_331(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_27', prices), rt.call_node('_node_wt_cash_equal_92', prices), rt.call_node('_node_wt_cash_equal_157', prices), rt.call_node('_node_wt_cash_equal_173', prices), rt.call_node('_node_wt_cash_equal_330', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_331'] = _node_wt_cash_equal_331


def _node_asset_GDXD_332(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'GDXD': 1.0}
rt.NODE_REGISTRY['_node_asset_GDXD_332'] = _node_asset_GDXD_332


def _node_asset_GDXU_333(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'GDXU': 1.0}
rt.NODE_REGISTRY['_node_asset_GDXU_333'] = _node_asset_GDXU_333


def _node_asset_GDXU_334(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'GDXU': 1.0}
rt.NODE_REGISTRY['_node_asset_GDXU_334'] = _node_asset_GDXU_334


def _node_asset_UVXY_335(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_335'] = _node_asset_UVXY_335


def _node_asset_UVXY_336(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_336'] = _node_asset_UVXY_336


def _node_asset_UVXY_337(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_337'] = _node_asset_UVXY_337


def _node_asset_UVXY_338(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_338'] = _node_asset_UVXY_338


def _node_asset_UVXY_339(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_339'] = _node_asset_UVXY_339


def _node_asset_UVXY_340(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_340'] = _node_asset_UVXY_340


def _node_asset_UVXY_341(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_341'] = _node_asset_UVXY_341


def _node_asset_UVXY_342(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_342'] = _node_asset_UVXY_342


def _node_asset_BIL_343(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_343'] = _node_asset_BIL_343


def _node_asset_BTAL_344(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BTAL': 1.0}
rt.NODE_REGISTRY['_node_asset_BTAL_344'] = _node_asset_BTAL_344


def _node_wt_cash_equal_345(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_343', prices), rt.call_node('_node_asset_BTAL_344', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_345'] = _node_wt_cash_equal_345


def _node_wt_cash_specified_346(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('75') / float(100)), rt.call_node('_node_asset_UVXY_342', prices)), ((float('25') / float(100)), rt.call_node('_node_wt_cash_equal_345', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_346'] = _node_wt_cash_specified_346


def _node_if_347(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLF'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_341', prices)
    else:
        return rt.call_node('_node_wt_cash_specified_346', prices)
rt.NODE_REGISTRY['_node_if_347'] = _node_if_347


def _node_wt_cash_equal_348(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_347', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_348'] = _node_wt_cash_equal_348


def _node_if_349(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['VTV'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_340', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_348', prices)
rt.NODE_REGISTRY['_node_if_349'] = _node_if_349


def _node_wt_cash_equal_350(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_349', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_350'] = _node_wt_cash_equal_350


def _node_if_351(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TQQQ'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_339', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_350', prices)
rt.NODE_REGISTRY['_node_if_351'] = _node_if_351


def _node_wt_cash_equal_352(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_351', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_352'] = _node_wt_cash_equal_352


def _node_if_353(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IOO'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_338', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_352', prices)
rt.NODE_REGISTRY['_node_if_353'] = _node_if_353


def _node_wt_cash_equal_354(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_353', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_354'] = _node_wt_cash_equal_354


def _node_if_355(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_337', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_354', prices)
rt.NODE_REGISTRY['_node_if_355'] = _node_if_355


def _node_wt_cash_equal_356(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_355', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_356'] = _node_wt_cash_equal_356


def _node_asset_UVXY_357(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_357'] = _node_asset_UVXY_357


def _node_asset_UVXY_358(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_358'] = _node_asset_UVXY_358


def _node_asset_UVXY_359(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_359'] = _node_asset_UVXY_359


def _node_asset_UVXY_360(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_360'] = _node_asset_UVXY_360


def _node_asset_UVXY_361(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_361'] = _node_asset_UVXY_361


def _node_asset_BIL_362(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_362'] = _node_asset_BIL_362


def _node_asset_BTAL_363(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BTAL': 1.0}
rt.NODE_REGISTRY['_node_asset_BTAL_363'] = _node_asset_BTAL_363


def _node_wt_cash_equal_364(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_362', prices), rt.call_node('_node_asset_BTAL_363', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_364'] = _node_wt_cash_equal_364


def _node_wt_cash_specified_365(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('75') / float(100)), rt.call_node('_node_asset_UVXY_361', prices)), ((float('25') / float(100)), rt.call_node('_node_wt_cash_equal_364', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_365'] = _node_wt_cash_specified_365


def _node_if_366(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLF'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_360', prices)
    else:
        return rt.call_node('_node_wt_cash_specified_365', prices)
rt.NODE_REGISTRY['_node_if_366'] = _node_if_366


def _node_wt_cash_equal_367(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_366', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_367'] = _node_wt_cash_equal_367


def _node_if_368(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['VTV'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_359', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_367', prices)
rt.NODE_REGISTRY['_node_if_368'] = _node_if_368


def _node_wt_cash_equal_369(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_368', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_369'] = _node_wt_cash_equal_369


def _node_if_370(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TQQQ'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_358', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_369', prices)
rt.NODE_REGISTRY['_node_if_370'] = _node_if_370


def _node_wt_cash_equal_371(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_370', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_371'] = _node_wt_cash_equal_371


def _node_if_372(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IOO'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_357', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_371', prices)
rt.NODE_REGISTRY['_node_if_372'] = _node_if_372


def _node_wt_cash_equal_373(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_372', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_373'] = _node_wt_cash_equal_373


def _node_asset_UVXY_374(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_374'] = _node_asset_UVXY_374


def _node_asset_UVXY_375(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_375'] = _node_asset_UVXY_375


def _node_asset_UVXY_376(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_376'] = _node_asset_UVXY_376


def _node_asset_UVXY_377(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_377'] = _node_asset_UVXY_377


def _node_asset_BIL_378(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_378'] = _node_asset_BIL_378


def _node_asset_BTAL_379(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BTAL': 1.0}
rt.NODE_REGISTRY['_node_asset_BTAL_379'] = _node_asset_BTAL_379


def _node_wt_cash_equal_380(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_378', prices), rt.call_node('_node_asset_BTAL_379', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_380'] = _node_wt_cash_equal_380


def _node_wt_cash_specified_381(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('75') / float(100)), rt.call_node('_node_asset_UVXY_377', prices)), ((float('25') / float(100)), rt.call_node('_node_wt_cash_equal_380', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_381'] = _node_wt_cash_specified_381


def _node_if_382(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLF'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_376', prices)
    else:
        return rt.call_node('_node_wt_cash_specified_381', prices)
rt.NODE_REGISTRY['_node_if_382'] = _node_if_382


def _node_wt_cash_equal_383(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_382', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_383'] = _node_wt_cash_equal_383


def _node_if_384(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['VTV'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_375', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_383', prices)
rt.NODE_REGISTRY['_node_if_384'] = _node_if_384


def _node_wt_cash_equal_385(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_384', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_385'] = _node_wt_cash_equal_385


def _node_if_386(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TQQQ'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_374', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_385', prices)
rt.NODE_REGISTRY['_node_if_386'] = _node_if_386


def _node_wt_cash_equal_387(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_386', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_387'] = _node_wt_cash_equal_387


def _node_asset_UVXY_388(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_388'] = _node_asset_UVXY_388


def _node_asset_UVXY_389(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_389'] = _node_asset_UVXY_389


def _node_asset_UVXY_390(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_390'] = _node_asset_UVXY_390


def _node_asset_BIL_391(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_391'] = _node_asset_BIL_391


def _node_asset_BTAL_392(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BTAL': 1.0}
rt.NODE_REGISTRY['_node_asset_BTAL_392'] = _node_asset_BTAL_392


def _node_wt_cash_equal_393(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_391', prices), rt.call_node('_node_asset_BTAL_392', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_393'] = _node_wt_cash_equal_393


def _node_wt_cash_specified_394(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('75') / float(100)), rt.call_node('_node_asset_UVXY_390', prices)), ((float('25') / float(100)), rt.call_node('_node_wt_cash_equal_393', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_394'] = _node_wt_cash_specified_394


def _node_if_395(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLF'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_389', prices)
    else:
        return rt.call_node('_node_wt_cash_specified_394', prices)
rt.NODE_REGISTRY['_node_if_395'] = _node_if_395


def _node_wt_cash_equal_396(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_395', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_396'] = _node_wt_cash_equal_396


def _node_if_397(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['VTV'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_388', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_396', prices)
rt.NODE_REGISTRY['_node_if_397'] = _node_if_397


def _node_wt_cash_equal_398(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_397', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_398'] = _node_wt_cash_equal_398


def _node_asset_UVXY_399(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_399'] = _node_asset_UVXY_399


def _node_asset_UVXY_400(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_400'] = _node_asset_UVXY_400


def _node_asset_BIL_401(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_401'] = _node_asset_BIL_401


def _node_asset_BTAL_402(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BTAL': 1.0}
rt.NODE_REGISTRY['_node_asset_BTAL_402'] = _node_asset_BTAL_402


def _node_wt_cash_equal_403(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_401', prices), rt.call_node('_node_asset_BTAL_402', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_403'] = _node_wt_cash_equal_403


def _node_wt_cash_specified_404(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('75') / float(100)), rt.call_node('_node_asset_UVXY_400', prices)), ((float('25') / float(100)), rt.call_node('_node_wt_cash_equal_403', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_404'] = _node_wt_cash_specified_404


def _node_if_405(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLF'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_399', prices)
    else:
        return rt.call_node('_node_wt_cash_specified_404', prices)
rt.NODE_REGISTRY['_node_if_405'] = _node_if_405


def _node_wt_cash_equal_406(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_405', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_406'] = _node_wt_cash_equal_406


def _node_asset_TQQQ_407(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_407'] = _node_asset_TQQQ_407


def _node_asset_SPXL_408(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SPXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SPXL_408'] = _node_asset_SPXL_408


def _node_asset_AAPX_409(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'AAPX': 1.0}
rt.NODE_REGISTRY['_node_asset_AAPX_409'] = _node_asset_AAPX_409


def _node_asset_BIL_410(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_410'] = _node_asset_BIL_410


def _node_asset_TQQQ_411(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_411'] = _node_asset_TQQQ_411


def _node_combine_equal_412(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_410', prices), rt.call_node('_node_asset_TQQQ_411', prices)])
rt.NODE_REGISTRY['_node_combine_equal_412'] = _node_combine_equal_412


def _node_if_413(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.moving_average_return(prices['AAPX'], 10) > 0.0:
        return rt.call_node('_node_asset_AAPX_409', prices)
    else:
        return rt.call_node('_node_combine_equal_412', prices)
rt.NODE_REGISTRY['_node_if_413'] = _node_if_413


def _node_wt_cash_equal_414(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_413', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_414'] = _node_wt_cash_equal_414


def _node_asset_NVDL_415(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'NVDL': 1.0}
rt.NODE_REGISTRY['_node_asset_NVDL_415'] = _node_asset_NVDL_415


def _node_asset_BIL_416(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_416'] = _node_asset_BIL_416


def _node_asset_TQQQ_417(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_417'] = _node_asset_TQQQ_417


def _node_combine_equal_418(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_416', prices), rt.call_node('_node_asset_TQQQ_417', prices)])
rt.NODE_REGISTRY['_node_combine_equal_418'] = _node_combine_equal_418


def _node_if_419(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.moving_average_return(prices['NVDL'], 10) > 0.0:
        return rt.call_node('_node_asset_NVDL_415', prices)
    else:
        return rt.call_node('_node_combine_equal_418', prices)
rt.NODE_REGISTRY['_node_if_419'] = _node_if_419


def _node_wt_cash_equal_420(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_419', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_420'] = _node_wt_cash_equal_420


def _node_asset_BITX_421(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BITX': 1.0}
rt.NODE_REGISTRY['_node_asset_BITX_421'] = _node_asset_BITX_421


def _node_asset_BIL_422(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_422'] = _node_asset_BIL_422


def _node_asset_TQQQ_423(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_423'] = _node_asset_TQQQ_423


def _node_combine_equal_424(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_422', prices), rt.call_node('_node_asset_TQQQ_423', prices)])
rt.NODE_REGISTRY['_node_combine_equal_424'] = _node_combine_equal_424


def _node_if_425(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.moving_average_return(prices['BITX'], 10) > 0.0:
        return rt.call_node('_node_asset_BITX_421', prices)
    else:
        return rt.call_node('_node_combine_equal_424', prices)
rt.NODE_REGISTRY['_node_if_425'] = _node_if_425


def _node_wt_cash_equal_426(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_425', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_426'] = _node_wt_cash_equal_426


def _node_asset_TSLR_427(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TSLR': 1.0}
rt.NODE_REGISTRY['_node_asset_TSLR_427'] = _node_asset_TSLR_427


def _node_asset_BIL_428(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_428'] = _node_asset_BIL_428


def _node_asset_TQQQ_429(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_429'] = _node_asset_TQQQ_429


def _node_combine_equal_430(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_428', prices), rt.call_node('_node_asset_TQQQ_429', prices)])
rt.NODE_REGISTRY['_node_combine_equal_430'] = _node_combine_equal_430


def _node_if_431(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.moving_average_return(prices['TSLA'], 10) > 0.0:
        return rt.call_node('_node_asset_TSLR_427', prices)
    else:
        return rt.call_node('_node_combine_equal_430', prices)
rt.NODE_REGISTRY['_node_if_431'] = _node_if_431


def _node_wt_cash_equal_432(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_431', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_432'] = _node_wt_cash_equal_432


def _node_asset_FBL_433(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'FBL': 1.0}
rt.NODE_REGISTRY['_node_asset_FBL_433'] = _node_asset_FBL_433


def _node_asset_BIL_434(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_434'] = _node_asset_BIL_434


def _node_asset_TQQQ_435(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_435'] = _node_asset_TQQQ_435


def _node_combine_equal_436(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_434', prices), rt.call_node('_node_asset_TQQQ_435', prices)])
rt.NODE_REGISTRY['_node_combine_equal_436'] = _node_combine_equal_436


def _node_if_437(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.moving_average_return(prices['META'], 10) > 0.0:
        return rt.call_node('_node_asset_FBL_433', prices)
    else:
        return rt.call_node('_node_combine_equal_436', prices)
rt.NODE_REGISTRY['_node_if_437'] = _node_if_437


def _node_wt_cash_equal_438(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_437', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_438'] = _node_wt_cash_equal_438


def _node_asset_GGLL_439(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'GGLL': 1.0}
rt.NODE_REGISTRY['_node_asset_GGLL_439'] = _node_asset_GGLL_439


def _node_asset_BIL_440(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_440'] = _node_asset_BIL_440


def _node_asset_TQQQ_441(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_441'] = _node_asset_TQQQ_441


def _node_combine_equal_442(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_440', prices), rt.call_node('_node_asset_TQQQ_441', prices)])
rt.NODE_REGISTRY['_node_combine_equal_442'] = _node_combine_equal_442


def _node_if_443(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.moving_average_return(prices['GGLL'], 10) > 0.0:
        return rt.call_node('_node_asset_GGLL_439', prices)
    else:
        return rt.call_node('_node_combine_equal_442', prices)
rt.NODE_REGISTRY['_node_if_443'] = _node_if_443


def _node_wt_cash_equal_444(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_443', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_444'] = _node_wt_cash_equal_444


def _node_asset_AMZU_445(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'AMZU': 1.0}
rt.NODE_REGISTRY['_node_asset_AMZU_445'] = _node_asset_AMZU_445


def _node_asset_BIL_446(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_446'] = _node_asset_BIL_446


def _node_asset_TQQQ_447(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_447'] = _node_asset_TQQQ_447


def _node_combine_equal_448(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_446', prices), rt.call_node('_node_asset_TQQQ_447', prices)])
rt.NODE_REGISTRY['_node_combine_equal_448'] = _node_combine_equal_448


def _node_if_449(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.moving_average_return(prices['AMZN'], 10) > 0.0:
        return rt.call_node('_node_asset_AMZU_445', prices)
    else:
        return rt.call_node('_node_combine_equal_448', prices)
rt.NODE_REGISTRY['_node_if_449'] = _node_if_449


def _node_wt_cash_equal_450(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_449', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_450'] = _node_wt_cash_equal_450


def _node_asset_RGTI_451(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'RGTI': 1.0}
rt.NODE_REGISTRY['_node_asset_RGTI_451'] = _node_asset_RGTI_451


def _node_asset_BIL_452(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_452'] = _node_asset_BIL_452


def _node_asset_TQQQ_453(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_453'] = _node_asset_TQQQ_453


def _node_combine_equal_454(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_452', prices), rt.call_node('_node_asset_TQQQ_453', prices)])
rt.NODE_REGISTRY['_node_combine_equal_454'] = _node_combine_equal_454


def _node_if_455(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.moving_average_return(prices['RGTI'], 10) > 0.0:
        return rt.call_node('_node_asset_RGTI_451', prices)
    else:
        return rt.call_node('_node_combine_equal_454', prices)
rt.NODE_REGISTRY['_node_if_455'] = _node_if_455


def _node_wt_cash_equal_456(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_455', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_456'] = _node_wt_cash_equal_456


def _node_asset_PLTR_457(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'PLTR': 1.0}
rt.NODE_REGISTRY['_node_asset_PLTR_457'] = _node_asset_PLTR_457


def _node_asset_BIL_458(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_458'] = _node_asset_BIL_458


def _node_asset_TQQQ_459(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_459'] = _node_asset_TQQQ_459


def _node_combine_equal_460(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_458', prices), rt.call_node('_node_asset_TQQQ_459', prices)])
rt.NODE_REGISTRY['_node_combine_equal_460'] = _node_combine_equal_460


def _node_if_461(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.moving_average_return(prices['PLTR'], 10) > 0.0:
        return rt.call_node('_node_asset_PLTR_457', prices)
    else:
        return rt.call_node('_node_combine_equal_460', prices)
rt.NODE_REGISTRY['_node_if_461'] = _node_if_461


def _node_wt_cash_equal_462(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_461', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_462'] = _node_wt_cash_equal_462


def _node_asset_BABA_463(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BABA': 1.0}
rt.NODE_REGISTRY['_node_asset_BABA_463'] = _node_asset_BABA_463


def _node_asset_BIL_464(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_464'] = _node_asset_BIL_464


def _node_asset_TQQQ_465(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_465'] = _node_asset_TQQQ_465


def _node_combine_equal_466(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_464', prices), rt.call_node('_node_asset_TQQQ_465', prices)])
rt.NODE_REGISTRY['_node_combine_equal_466'] = _node_combine_equal_466


def _node_if_467(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.moving_average_return(prices['BABA'], 10) > 0.0:
        return rt.call_node('_node_asset_BABA_463', prices)
    else:
        return rt.call_node('_node_combine_equal_466', prices)
rt.NODE_REGISTRY['_node_if_467'] = _node_if_467


def _node_wt_cash_equal_468(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_467', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_468'] = _node_wt_cash_equal_468


def _node_asset_CONL_469(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'CONL': 1.0}
rt.NODE_REGISTRY['_node_asset_CONL_469'] = _node_asset_CONL_469


def _node_asset_BIL_470(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_470'] = _node_asset_BIL_470


def _node_asset_TQQQ_471(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_471'] = _node_asset_TQQQ_471


def _node_combine_equal_472(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_BIL_470', prices), rt.call_node('_node_asset_TQQQ_471', prices)])
rt.NODE_REGISTRY['_node_combine_equal_472'] = _node_combine_equal_472


def _node_if_473(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.moving_average_return(prices['COIN'], 10) > 0.0:
        return rt.call_node('_node_asset_CONL_469', prices)
    else:
        return rt.call_node('_node_combine_equal_472', prices)
rt.NODE_REGISTRY['_node_if_473'] = _node_if_473


def _node_wt_cash_equal_474(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_473', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_474'] = _node_wt_cash_equal_474

from typing import Dict, Sequence

import strategy_runtime as rt


def _node_filter_475(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.standard_deviation_return(rt.synthetic_price_series(rt.call_node('_node_wt_cash_equal_414', prices), prices), 20), rt.call_node('_node_wt_cash_equal_414', prices)), (rt.standard_deviation_return(rt.synthetic_price_series(rt.call_node('_node_wt_cash_equal_420', prices), prices), 20), rt.call_node('_node_wt_cash_equal_420', prices)), (rt.standard_deviation_return(rt.synthetic_price_series(rt.call_node('_node_wt_cash_equal_426', prices), prices), 20), rt.call_node('_node_wt_cash_equal_426', prices)), (rt.standard_deviation_return(rt.synthetic_price_series(rt.call_node('_node_wt_cash_equal_432', prices), prices), 20), rt.call_node('_node_wt_cash_equal_432', prices)), (rt.standard_deviation_return(rt.synthetic_price_series(rt.call_node('_node_wt_cash_equal_438', prices), prices), 20), rt.call_node('_node_wt_cash_equal_438', prices)), (rt.standard_deviation_return(rt.synthetic_price_series(rt.call_node('_node_wt_cash_equal_444', prices), prices), 20), rt.call_node('_node_wt_cash_equal_444', prices)), (rt.standard_deviation_return(rt.synthetic_price_series(rt.call_node('_node_wt_cash_equal_450', prices), prices), 20), rt.call_node('_node_wt_cash_equal_450', prices)), (rt.standard_deviation_return(rt.synthetic_price_series(rt.call_node('_node_wt_cash_equal_456', prices), prices), 20), rt.call_node('_node_wt_cash_equal_456', prices)), (rt.standard_deviation_return(rt.synthetic_price_series(rt.call_node('_node_wt_cash_equal_462', prices), prices), 20), rt.call_node('_node_wt_cash_equal_462', prices)), (rt.standard_deviation_return(rt.synthetic_price_series(rt.call_node('_node_wt_cash_equal_468', prices), prices), 20), rt.call_node('_node_wt_cash_equal_468', prices)), (rt.standard_deviation_return(rt.synthetic_price_series(rt.call_node('_node_wt_cash_equal_474', prices), prices), 20), rt.call_node('_node_wt_cash_equal_474', prices))], 'top', int('1'))
rt.NODE_REGISTRY['_node_filter_475'] = _node_filter_475


def _node_wt_cash_equal_476(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_475', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_476'] = _node_wt_cash_equal_476


def _node_asset_AAPX_477(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'AAPX': 1.0}
rt.NODE_REGISTRY['_node_asset_AAPX_477'] = _node_asset_AAPX_477


def _node_asset_NVDL_478(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'NVDL': 1.0}
rt.NODE_REGISTRY['_node_asset_NVDL_478'] = _node_asset_NVDL_478


def _node_asset_BITX_479(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BITX': 1.0}
rt.NODE_REGISTRY['_node_asset_BITX_479'] = _node_asset_BITX_479


def _node_asset_TSLR_480(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TSLR': 1.0}
rt.NODE_REGISTRY['_node_asset_TSLR_480'] = _node_asset_TSLR_480


def _node_asset_FBL_481(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'FBL': 1.0}
rt.NODE_REGISTRY['_node_asset_FBL_481'] = _node_asset_FBL_481


def _node_asset_GGLL_482(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'GGLL': 1.0}
rt.NODE_REGISTRY['_node_asset_GGLL_482'] = _node_asset_GGLL_482


def _node_asset_AMZZ_483(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'AMZZ': 1.0}
rt.NODE_REGISTRY['_node_asset_AMZZ_483'] = _node_asset_AMZZ_483


def _node_asset_RGTI_484(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'RGTI': 1.0}
rt.NODE_REGISTRY['_node_asset_RGTI_484'] = _node_asset_RGTI_484


def _node_asset_PLTR_485(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'PLTR': 1.0}
rt.NODE_REGISTRY['_node_asset_PLTR_485'] = _node_asset_PLTR_485


def _node_asset_BABA_486(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BABA': 1.0}
rt.NODE_REGISTRY['_node_asset_BABA_486'] = _node_asset_BABA_486


def _node_asset_CONL_487(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'CONL': 1.0}
rt.NODE_REGISTRY['_node_asset_CONL_487'] = _node_asset_CONL_487


def _node_filter_488(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.moving_average_return(prices['AAPX'], 15), rt.call_node('_node_asset_AAPX_477', prices)), (rt.moving_average_return(prices['NVDL'], 15), rt.call_node('_node_asset_NVDL_478', prices)), (rt.moving_average_return(prices['BITX'], 15), rt.call_node('_node_asset_BITX_479', prices)), (rt.moving_average_return(prices['TSLR'], 15), rt.call_node('_node_asset_TSLR_480', prices)), (rt.moving_average_return(prices['FBL'], 15), rt.call_node('_node_asset_FBL_481', prices)), (rt.moving_average_return(prices['GGLL'], 15), rt.call_node('_node_asset_GGLL_482', prices)), (rt.moving_average_return(prices['AMZZ'], 15), rt.call_node('_node_asset_AMZZ_483', prices)), (rt.moving_average_return(prices['RGTI'], 15), rt.call_node('_node_asset_RGTI_484', prices)), (rt.moving_average_return(prices['PLTR'], 15), rt.call_node('_node_asset_PLTR_485', prices)), (rt.moving_average_return(prices['BABA'], 15), rt.call_node('_node_asset_BABA_486', prices)), (rt.moving_average_return(prices['CONL'], 15), rt.call_node('_node_asset_CONL_487', prices))], 'top', int('1'))
rt.NODE_REGISTRY['_node_filter_488'] = _node_filter_488


def _node_wt_cash_equal_489(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_488', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_489'] = _node_wt_cash_equal_489


def _node_asset_TECS_490(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TECS': 1.0}
rt.NODE_REGISTRY['_node_asset_TECS_490'] = _node_asset_TECS_490


def _node_asset_SOXS_491(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXS': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXS_491'] = _node_asset_SOXS_491


def _node_asset_SQQQ_492(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_SQQQ_492'] = _node_asset_SQQQ_492


def _node_wt_cash_equal_493(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_TECS_490', prices), rt.call_node('_node_asset_SOXS_491', prices), rt.call_node('_node_asset_SQQQ_492', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_493'] = _node_wt_cash_equal_493


def _node_if_494(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['KMLM']) < rt.moving_average_price(prices['KMLM'], 20):
        return rt.call_node('_node_wt_cash_equal_489', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_493', prices)
rt.NODE_REGISTRY['_node_if_494'] = _node_if_494


def _node_wt_cash_equal_495(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_494', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_495'] = _node_wt_cash_equal_495


def _node_wt_cash_equal_496(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_495', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_496'] = _node_wt_cash_equal_496


def _node_if_497(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLK'], 10) > rt.relative_strength_index(prices['KMLM'], 10):
        return rt.call_node('_node_wt_cash_equal_476', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_496', prices)
rt.NODE_REGISTRY['_node_if_497'] = _node_if_497


def _node_wt_cash_equal_498(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_497', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_498'] = _node_wt_cash_equal_498


def _node_asset_QQQ_499(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'QQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_QQQ_499'] = _node_asset_QQQ_499


def _node_wt_cash_equal_500(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_QQQ_499', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_500'] = _node_wt_cash_equal_500


def _node_asset_PSQ_501(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'PSQ': 1.0}
rt.NODE_REGISTRY['_node_asset_PSQ_501'] = _node_asset_PSQ_501


def _node_asset_TQQQ_502(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_502'] = _node_asset_TQQQ_502


def _node_asset_PSQ_503(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'PSQ': 1.0}
rt.NODE_REGISTRY['_node_asset_PSQ_503'] = _node_asset_PSQ_503


def _node_if_504(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['AGG'], 20) > rt.relative_strength_index(prices['SH'], 60):
        return rt.call_node('_node_asset_TQQQ_502', prices)
    else:
        return rt.call_node('_node_asset_PSQ_503', prices)
rt.NODE_REGISTRY['_node_if_504'] = _node_if_504


def _node_wt_cash_equal_505(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_504', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_505'] = _node_wt_cash_equal_505


def _node_if_506(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['PSQ'], 10) < 35.0:
        return rt.call_node('_node_asset_PSQ_501', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_505', prices)
rt.NODE_REGISTRY['_node_if_506'] = _node_if_506


def _node_wt_cash_equal_507(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_506', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_507'] = _node_wt_cash_equal_507


def _node_asset_PSQ_508(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'PSQ': 1.0}
rt.NODE_REGISTRY['_node_asset_PSQ_508'] = _node_asset_PSQ_508


def _node_asset_SQQQ_509(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_SQQQ_509'] = _node_asset_SQQQ_509


def _node_if_510(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IEF'], 10) > rt.relative_strength_index(prices['PSQ'], 20):
        return rt.call_node('_node_asset_PSQ_508', prices)
    else:
        return rt.call_node('_node_asset_SQQQ_509', prices)
rt.NODE_REGISTRY['_node_if_510'] = _node_if_510


def _node_wt_cash_equal_511(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_510', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_511'] = _node_wt_cash_equal_511


def _node_if_512(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['TQQQ']) > rt.moving_average_price(prices['TQQQ'], 20):
        return rt.call_node('_node_wt_cash_equal_507', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_511', prices)
rt.NODE_REGISTRY['_node_if_512'] = _node_if_512


def _node_wt_cash_equal_513(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_512', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_513'] = _node_wt_cash_equal_513


def _node_if_514(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TLT'], 20) > rt.relative_strength_index(prices['PSQ'], 20):
        return rt.call_node('_node_wt_cash_equal_500', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_513', prices)
rt.NODE_REGISTRY['_node_if_514'] = _node_if_514


def _node_asset_QLD_515(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'QLD': 1.0}
rt.NODE_REGISTRY['_node_asset_QLD_515'] = _node_asset_QLD_515


def _node_asset_BTAL_516(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BTAL': 1.0}
rt.NODE_REGISTRY['_node_asset_BTAL_516'] = _node_asset_BTAL_516


def _node_if_517(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['BND'], 10) > rt.relative_strength_index(prices['QQQ'], 10):
        return rt.call_node('_node_asset_QLD_515', prices)
    else:
        return rt.call_node('_node_asset_BTAL_516', prices)
rt.NODE_REGISTRY['_node_if_517'] = _node_if_517


def _node_wt_cash_equal_518(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_517', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_518'] = _node_wt_cash_equal_518


def _node_asset_PSQ_519(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'PSQ': 1.0}
rt.NODE_REGISTRY['_node_asset_PSQ_519'] = _node_asset_PSQ_519


def _node_asset_TQQQ_520(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_520'] = _node_asset_TQQQ_520


def _node_asset_PSQ_521(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'PSQ': 1.0}
rt.NODE_REGISTRY['_node_asset_PSQ_521'] = _node_asset_PSQ_521


def _node_if_522(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['AGG'], 20) > rt.relative_strength_index(prices['SH'], 60):
        return rt.call_node('_node_asset_TQQQ_520', prices)
    else:
        return rt.call_node('_node_asset_PSQ_521', prices)
rt.NODE_REGISTRY['_node_if_522'] = _node_if_522


def _node_wt_cash_equal_523(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_522', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_523'] = _node_wt_cash_equal_523


def _node_if_524(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['PSQ'], 10) < 35.0:
        return rt.call_node('_node_asset_PSQ_519', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_523', prices)
rt.NODE_REGISTRY['_node_if_524'] = _node_if_524


def _node_wt_cash_equal_525(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_524', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_525'] = _node_wt_cash_equal_525


def _node_asset_PSQ_526(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'PSQ': 1.0}
rt.NODE_REGISTRY['_node_asset_PSQ_526'] = _node_asset_PSQ_526


def _node_asset_SQQQ_527(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_SQQQ_527'] = _node_asset_SQQQ_527


def _node_if_528(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IEF'], 10) > rt.relative_strength_index(prices['PSQ'], 20):
        return rt.call_node('_node_asset_PSQ_526', prices)
    else:
        return rt.call_node('_node_asset_SQQQ_527', prices)
rt.NODE_REGISTRY['_node_if_528'] = _node_if_528


def _node_wt_cash_equal_529(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_528', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_529'] = _node_wt_cash_equal_529


def _node_if_530(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['TQQQ']) > rt.moving_average_price(prices['TQQQ'], 20):
        return rt.call_node('_node_wt_cash_equal_525', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_529', prices)
rt.NODE_REGISTRY['_node_if_530'] = _node_if_530


def _node_wt_cash_equal_531(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_530', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_531'] = _node_wt_cash_equal_531


def _node_if_532(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['QQQ'], 60) < -12.0:
        return rt.call_node('_node_wt_cash_equal_518', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_531', prices)
rt.NODE_REGISTRY['_node_if_532'] = _node_if_532


def _node_wt_cash_equal_533(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_532', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_533'] = _node_wt_cash_equal_533


def _node_wt_cash_equal_534(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_514', prices), rt.call_node('_node_wt_cash_equal_533', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_534'] = _node_wt_cash_equal_534


def _node_wt_cash_equal_535(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_534', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_535'] = _node_wt_cash_equal_535


def _node_if_536(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['SPY']) > rt.moving_average_price(prices['SPY'], 200):
        return rt.call_node('_node_wt_cash_equal_498', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_535', prices)
rt.NODE_REGISTRY['_node_if_536'] = _node_if_536


def _node_wt_cash_equal_537(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_536', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_537'] = _node_wt_cash_equal_537


def _node_if_538(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) < 30.0:
        return rt.call_node('_node_asset_SPXL_408', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_537', prices)
rt.NODE_REGISTRY['_node_if_538'] = _node_if_538


def _node_wt_cash_equal_539(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_538', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_539'] = _node_wt_cash_equal_539


def _node_if_540(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TQQQ'], 10) < 30.0:
        return rt.call_node('_node_asset_TQQQ_407', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_539', prices)
rt.NODE_REGISTRY['_node_if_540'] = _node_if_540


def _node_wt_cash_equal_541(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_540', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_541'] = _node_wt_cash_equal_541


def _node_if_542(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLF'], 10) > 79.0:
        return rt.call_node('_node_wt_cash_equal_406', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_541', prices)
rt.NODE_REGISTRY['_node_if_542'] = _node_if_542


def _node_wt_cash_equal_543(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_542', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_543'] = _node_wt_cash_equal_543


def _node_if_544(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['VTV'], 10) > 79.0:
        return rt.call_node('_node_wt_cash_equal_398', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_543', prices)
rt.NODE_REGISTRY['_node_if_544'] = _node_if_544


def _node_wt_cash_equal_545(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_544', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_545'] = _node_wt_cash_equal_545


def _node_if_546(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TQQQ'], 10) > 79.0:
        return rt.call_node('_node_wt_cash_equal_387', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_545', prices)
rt.NODE_REGISTRY['_node_if_546'] = _node_if_546


def _node_wt_cash_equal_547(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_546', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_547'] = _node_wt_cash_equal_547


def _node_if_548(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IOO'], 10) > 79.0:
        return rt.call_node('_node_wt_cash_equal_373', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_547', prices)
rt.NODE_REGISTRY['_node_if_548'] = _node_if_548


def _node_wt_cash_equal_549(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_548', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_549'] = _node_wt_cash_equal_549


def _node_if_550(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) > 79.0:
        return rt.call_node('_node_wt_cash_equal_356', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_549', prices)
rt.NODE_REGISTRY['_node_if_550'] = _node_if_550


def _node_wt_cash_equal_551(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_550', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_551'] = _node_wt_cash_equal_551


def _node_wt_cash_equal_552(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_551', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_552'] = _node_wt_cash_equal_552


def _node_if_553(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPXL'], 10) > 80.0:
        return rt.call_node('_node_asset_UVXY_336', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_552', prices)
rt.NODE_REGISTRY['_node_if_553'] = _node_if_553


def _node_wt_cash_equal_554(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_553', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_554'] = _node_wt_cash_equal_554


def _node_if_555(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TQQQ'], 10) > 79.0:
        return rt.call_node('_node_asset_UVXY_335', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_554', prices)
rt.NODE_REGISTRY['_node_if_555'] = _node_if_555


def _node_wt_cash_equal_556(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_555', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_556'] = _node_wt_cash_equal_556


def _node_asset_TECL_557(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TECL': 1.0}
rt.NODE_REGISTRY['_node_asset_TECL_557'] = _node_asset_TECL_557


def _node_asset_UPRO_558(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UPRO': 1.0}
rt.NODE_REGISTRY['_node_asset_UPRO_558'] = _node_asset_UPRO_558


def _node_asset_SQQQ_559(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_SQQQ_559'] = _node_asset_SQQQ_559


def _node_asset_TLT_560(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TLT': 1.0}
rt.NODE_REGISTRY['_node_asset_TLT_560'] = _node_asset_TLT_560


def _node_filter_561(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.relative_strength_index(prices['SQQQ'], 10), rt.call_node('_node_asset_SQQQ_559', prices)), (rt.relative_strength_index(prices['TLT'], 10), rt.call_node('_node_asset_TLT_560', prices))], 'top', int('1'))
rt.NODE_REGISTRY['_node_filter_561'] = _node_filter_561


def _node_wt_cash_equal_562(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_561', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_562'] = _node_wt_cash_equal_562


def _node_asset_SQQQ_563(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_SQQQ_563'] = _node_asset_SQQQ_563


def _node_asset_TQQQ_564(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_564'] = _node_asset_TQQQ_564


def _node_wt_cash_equal_565(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_TQQQ_564', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_565'] = _node_wt_cash_equal_565


def _node_if_566(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SQQQ'], 10) < 31.0:
        return rt.call_node('_node_asset_SQQQ_563', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_565', prices)
rt.NODE_REGISTRY['_node_if_566'] = _node_if_566


def _node_wt_cash_equal_567(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_566', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_567'] = _node_wt_cash_equal_567


def _node_if_568(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['TQQQ']) < rt.moving_average_price(prices['TQQQ'], 20):
        return rt.call_node('_node_wt_cash_equal_562', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_567', prices)
rt.NODE_REGISTRY['_node_if_568'] = _node_if_568


def _node_wt_cash_equal_569(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_568', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_569'] = _node_wt_cash_equal_569


def _node_if_570(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) < 30.0:
        return rt.call_node('_node_asset_UPRO_558', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_569', prices)
rt.NODE_REGISTRY['_node_if_570'] = _node_if_570


def _node_wt_cash_equal_571(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_570', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_571'] = _node_wt_cash_equal_571


def _node_if_572(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TQQQ'], 10) < 31.0:
        return rt.call_node('_node_asset_TECL_557', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_571', prices)
rt.NODE_REGISTRY['_node_if_572'] = _node_if_572


def _node_wt_cash_equal_573(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_572', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_573'] = _node_wt_cash_equal_573


def _node_if_574(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['SPY']) > rt.moving_average_price(prices['SPY'], 200):
        return rt.call_node('_node_wt_cash_equal_556', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_573', prices)
rt.NODE_REGISTRY['_node_if_574'] = _node_if_574


def _node_wt_cash_equal_575(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_574', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_575'] = _node_wt_cash_equal_575


def _node_wt_cash_equal_576(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_575', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_576'] = _node_wt_cash_equal_576


def _node_if_577(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['GDXU'], 70) < rt.cumulative_return(prices['GDXU'], 75):
        return rt.call_node('_node_asset_GDXU_334', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_576', prices)
rt.NODE_REGISTRY['_node_if_577'] = _node_if_577


def _node_wt_cash_equal_578(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_577', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_578'] = _node_wt_cash_equal_578


def _node_asset_GDXD_579(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'GDXD': 1.0}
rt.NODE_REGISTRY['_node_asset_GDXD_579'] = _node_asset_GDXD_579


def _node_asset_V_580(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'V': 1.0}
rt.NODE_REGISTRY['_node_asset_V_580'] = _node_asset_V_580


def _node_asset_SOFI_581(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOFI': 1.0}
rt.NODE_REGISTRY['_node_asset_SOFI_581'] = _node_asset_SOFI_581


def _node_asset_MA_582(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'MA': 1.0}
rt.NODE_REGISTRY['_node_asset_MA_582'] = _node_asset_MA_582


def _node_asset_BX_583(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BX': 1.0}
rt.NODE_REGISTRY['_node_asset_BX_583'] = _node_asset_BX_583


def _node_asset_SCHW_584(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SCHW': 1.0}
rt.NODE_REGISTRY['_node_asset_SCHW_584'] = _node_asset_SCHW_584


def _node_asset_KKR_585(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'KKR': 1.0}
rt.NODE_REGISTRY['_node_asset_KKR_585'] = _node_asset_KKR_585


def _node_asset_BN_586(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BN': 1.0}
rt.NODE_REGISTRY['_node_asset_BN_586'] = _node_asset_BN_586


def _node_asset_WELL_587(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'WELL': 1.0}
rt.NODE_REGISTRY['_node_asset_WELL_587'] = _node_asset_WELL_587


def _node_asset_VTR_588(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'VTR': 1.0}
rt.NODE_REGISTRY['_node_asset_VTR_588'] = _node_asset_VTR_588


def _node_asset_BAM_589(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BAM': 1.0}
rt.NODE_REGISTRY['_node_asset_BAM_589'] = _node_asset_BAM_589


def _node_asset_HOOD_590(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'HOOD': 1.0}
rt.NODE_REGISTRY['_node_asset_HOOD_590'] = _node_asset_HOOD_590


def _node_asset_IBKR_591(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'IBKR': 1.0}
rt.NODE_REGISTRY['_node_asset_IBKR_591'] = _node_asset_IBKR_591


def _node_asset_FAS_592(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'FAS': 1.0}
rt.NODE_REGISTRY['_node_asset_FAS_592'] = _node_asset_FAS_592


def _node_asset_AAPX_593(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'AAPX': 1.0}
rt.NODE_REGISTRY['_node_asset_AAPX_593'] = _node_asset_AAPX_593


def _node_asset_NVDL_594(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'NVDL': 1.0}
rt.NODE_REGISTRY['_node_asset_NVDL_594'] = _node_asset_NVDL_594


def _node_asset_BITX_595(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BITX': 1.0}
rt.NODE_REGISTRY['_node_asset_BITX_595'] = _node_asset_BITX_595


def _node_asset_TSLR_596(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TSLR': 1.0}
rt.NODE_REGISTRY['_node_asset_TSLR_596'] = _node_asset_TSLR_596


def _node_asset_FBL_597(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'FBL': 1.0}
rt.NODE_REGISTRY['_node_asset_FBL_597'] = _node_asset_FBL_597


def _node_asset_GGLL_598(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'GGLL': 1.0}
rt.NODE_REGISTRY['_node_asset_GGLL_598'] = _node_asset_GGLL_598


def _node_asset_AMZZ_599(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'AMZZ': 1.0}
rt.NODE_REGISTRY['_node_asset_AMZZ_599'] = _node_asset_AMZZ_599


def _node_asset_RGTI_600(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'RGTI': 1.0}
rt.NODE_REGISTRY['_node_asset_RGTI_600'] = _node_asset_RGTI_600


def _node_asset_PLTR_601(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'PLTR': 1.0}
rt.NODE_REGISTRY['_node_asset_PLTR_601'] = _node_asset_PLTR_601


def _node_asset_BABA_602(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BABA': 1.0}
rt.NODE_REGISTRY['_node_asset_BABA_602'] = _node_asset_BABA_602


def _node_asset_CONL_603(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'CONL': 1.0}
rt.NODE_REGISTRY['_node_asset_CONL_603'] = _node_asset_CONL_603


def _node_filter_604(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.moving_average_return(prices['AAPX'], 15), rt.call_node('_node_asset_AAPX_593', prices)), (rt.moving_average_return(prices['NVDL'], 15), rt.call_node('_node_asset_NVDL_594', prices)), (rt.moving_average_return(prices['BITX'], 15), rt.call_node('_node_asset_BITX_595', prices)), (rt.moving_average_return(prices['TSLR'], 15), rt.call_node('_node_asset_TSLR_596', prices)), (rt.moving_average_return(prices['FBL'], 15), rt.call_node('_node_asset_FBL_597', prices)), (rt.moving_average_return(prices['GGLL'], 15), rt.call_node('_node_asset_GGLL_598', prices)), (rt.moving_average_return(prices['AMZZ'], 15), rt.call_node('_node_asset_AMZZ_599', prices)), (rt.moving_average_return(prices['RGTI'], 15), rt.call_node('_node_asset_RGTI_600', prices)), (rt.moving_average_return(prices['PLTR'], 15), rt.call_node('_node_asset_PLTR_601', prices)), (rt.moving_average_return(prices['BABA'], 15), rt.call_node('_node_asset_BABA_602', prices)), (rt.moving_average_return(prices['CONL'], 15), rt.call_node('_node_asset_CONL_603', prices))], 'top', int('1'))
rt.NODE_REGISTRY['_node_filter_604'] = _node_filter_604


def _node_wt_cash_equal_605(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_604', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_605'] = _node_wt_cash_equal_605


def _node_if_606(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.moving_average_return(prices['FAS'], 10) > rt.moving_average_return(prices['QQQ'], 20):
        return rt.call_node('_node_asset_FAS_592', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_605', prices)
rt.NODE_REGISTRY['_node_if_606'] = _node_if_606


def _node_wt_cash_equal_607(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_606', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_607'] = _node_wt_cash_equal_607


def _node_filter_608(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.moving_average_return(prices['V'], 20), rt.call_node('_node_asset_V_580', prices)), (rt.moving_average_return(prices['SOFI'], 20), rt.call_node('_node_asset_SOFI_581', prices)), (rt.moving_average_return(prices['MA'], 20), rt.call_node('_node_asset_MA_582', prices)), (rt.moving_average_return(prices['BX'], 20), rt.call_node('_node_asset_BX_583', prices)), (rt.moving_average_return(prices['SCHW'], 20), rt.call_node('_node_asset_SCHW_584', prices)), (rt.moving_average_return(prices['KKR'], 20), rt.call_node('_node_asset_KKR_585', prices)), (rt.moving_average_return(prices['BN'], 20), rt.call_node('_node_asset_BN_586', prices)), (rt.moving_average_return(prices['WELL'], 20), rt.call_node('_node_asset_WELL_587', prices)), (rt.moving_average_return(prices['VTR'], 20), rt.call_node('_node_asset_VTR_588', prices)), (rt.moving_average_return(prices['BAM'], 20), rt.call_node('_node_asset_BAM_589', prices)), (rt.moving_average_return(prices['HOOD'], 20), rt.call_node('_node_asset_HOOD_590', prices)), (rt.moving_average_return(prices['IBKR'], 20), rt.call_node('_node_asset_IBKR_591', prices)), (rt.moving_average_return(rt.synthetic_price_series(rt.call_node('_node_wt_cash_equal_607', prices), prices), 20), rt.call_node('_node_wt_cash_equal_607', prices))], 'top', int('3'))
rt.NODE_REGISTRY['_node_filter_608'] = _node_filter_608


def _node_wt_cash_equal_609(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_608', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_609'] = _node_wt_cash_equal_609


def _node_asset_V_610(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'V': 1.0}
rt.NODE_REGISTRY['_node_asset_V_610'] = _node_asset_V_610


def _node_asset_SOFI_611(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOFI': 1.0}
rt.NODE_REGISTRY['_node_asset_SOFI_611'] = _node_asset_SOFI_611


def _node_asset_MA_612(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'MA': 1.0}
rt.NODE_REGISTRY['_node_asset_MA_612'] = _node_asset_MA_612


def _node_asset_BX_613(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BX': 1.0}
rt.NODE_REGISTRY['_node_asset_BX_613'] = _node_asset_BX_613


def _node_asset_SCHW_614(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SCHW': 1.0}
rt.NODE_REGISTRY['_node_asset_SCHW_614'] = _node_asset_SCHW_614


def _node_asset_KKR_615(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'KKR': 1.0}
rt.NODE_REGISTRY['_node_asset_KKR_615'] = _node_asset_KKR_615


def _node_asset_BN_616(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BN': 1.0}
rt.NODE_REGISTRY['_node_asset_BN_616'] = _node_asset_BN_616


def _node_asset_WELL_617(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'WELL': 1.0}
rt.NODE_REGISTRY['_node_asset_WELL_617'] = _node_asset_WELL_617


def _node_asset_VTR_618(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'VTR': 1.0}
rt.NODE_REGISTRY['_node_asset_VTR_618'] = _node_asset_VTR_618


def _node_asset_BAM_619(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BAM': 1.0}
rt.NODE_REGISTRY['_node_asset_BAM_619'] = _node_asset_BAM_619


def _node_asset_HOOD_620(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'HOOD': 1.0}
rt.NODE_REGISTRY['_node_asset_HOOD_620'] = _node_asset_HOOD_620


def _node_asset_IBKR_621(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'IBKR': 1.0}
rt.NODE_REGISTRY['_node_asset_IBKR_621'] = _node_asset_IBKR_621


def _node_filter_622(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.relative_strength_index(prices['V'], 10), rt.call_node('_node_asset_V_610', prices)), (rt.relative_strength_index(prices['SOFI'], 10), rt.call_node('_node_asset_SOFI_611', prices)), (rt.relative_strength_index(prices['MA'], 10), rt.call_node('_node_asset_MA_612', prices)), (rt.relative_strength_index(prices['BX'], 10), rt.call_node('_node_asset_BX_613', prices)), (rt.relative_strength_index(prices['SCHW'], 10), rt.call_node('_node_asset_SCHW_614', prices)), (rt.relative_strength_index(prices['KKR'], 10), rt.call_node('_node_asset_KKR_615', prices)), (rt.relative_strength_index(prices['BN'], 10), rt.call_node('_node_asset_BN_616', prices)), (rt.relative_strength_index(prices['WELL'], 10), rt.call_node('_node_asset_WELL_617', prices)), (rt.relative_strength_index(prices['VTR'], 10), rt.call_node('_node_asset_VTR_618', prices)), (rt.relative_strength_index(prices['BAM'], 10), rt.call_node('_node_asset_BAM_619', prices)), (rt.relative_strength_index(prices['HOOD'], 10), rt.call_node('_node_asset_HOOD_620', prices)), (rt.relative_strength_index(prices['IBKR'], 10), rt.call_node('_node_asset_IBKR_621', prices))], 'bottom', int('3'))
rt.NODE_REGISTRY['_node_filter_622'] = _node_filter_622


def _node_wt_cash_equal_623(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_622', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_623'] = _node_wt_cash_equal_623


def _node_if_624(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.moving_average_return(prices['FAS'], 50) > rt.moving_average_return(prices['FAS'], 200):
        return rt.call_node('_node_wt_cash_equal_609', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_623', prices)
rt.NODE_REGISTRY['_node_if_624'] = _node_if_624


def _node_wt_cash_equal_625(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_624', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_625'] = _node_wt_cash_equal_625


def _node_asset_TMF_626(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TMF': 1.0}
rt.NODE_REGISTRY['_node_asset_TMF_626'] = _node_asset_TMF_626


def _node_asset_FAZ_627(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'FAZ': 1.0}
rt.NODE_REGISTRY['_node_asset_FAZ_627'] = _node_asset_FAZ_627


def _node_asset_AAPX_628(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'AAPX': 1.0}
rt.NODE_REGISTRY['_node_asset_AAPX_628'] = _node_asset_AAPX_628


def _node_asset_NVDL_629(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'NVDL': 1.0}
rt.NODE_REGISTRY['_node_asset_NVDL_629'] = _node_asset_NVDL_629


def _node_asset_BITX_630(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BITX': 1.0}
rt.NODE_REGISTRY['_node_asset_BITX_630'] = _node_asset_BITX_630


def _node_asset_TSLR_631(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TSLR': 1.0}
rt.NODE_REGISTRY['_node_asset_TSLR_631'] = _node_asset_TSLR_631


def _node_asset_FBL_632(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'FBL': 1.0}
rt.NODE_REGISTRY['_node_asset_FBL_632'] = _node_asset_FBL_632


def _node_asset_GGLL_633(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'GGLL': 1.0}
rt.NODE_REGISTRY['_node_asset_GGLL_633'] = _node_asset_GGLL_633


def _node_asset_AMZZ_634(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'AMZZ': 1.0}
rt.NODE_REGISTRY['_node_asset_AMZZ_634'] = _node_asset_AMZZ_634


def _node_asset_RGTI_635(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'RGTI': 1.0}
rt.NODE_REGISTRY['_node_asset_RGTI_635'] = _node_asset_RGTI_635


def _node_asset_PLTR_636(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'PLTR': 1.0}
rt.NODE_REGISTRY['_node_asset_PLTR_636'] = _node_asset_PLTR_636


def _node_asset_BABA_637(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BABA': 1.0}
rt.NODE_REGISTRY['_node_asset_BABA_637'] = _node_asset_BABA_637


def _node_asset_CONL_638(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'CONL': 1.0}
rt.NODE_REGISTRY['_node_asset_CONL_638'] = _node_asset_CONL_638


def _node_filter_639(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.moving_average_return(prices['AAPX'], 15), rt.call_node('_node_asset_AAPX_628', prices)), (rt.moving_average_return(prices['NVDL'], 15), rt.call_node('_node_asset_NVDL_629', prices)), (rt.moving_average_return(prices['BITX'], 15), rt.call_node('_node_asset_BITX_630', prices)), (rt.moving_average_return(prices['TSLR'], 15), rt.call_node('_node_asset_TSLR_631', prices)), (rt.moving_average_return(prices['FBL'], 15), rt.call_node('_node_asset_FBL_632', prices)), (rt.moving_average_return(prices['GGLL'], 15), rt.call_node('_node_asset_GGLL_633', prices)), (rt.moving_average_return(prices['AMZZ'], 15), rt.call_node('_node_asset_AMZZ_634', prices)), (rt.moving_average_return(prices['RGTI'], 15), rt.call_node('_node_asset_RGTI_635', prices)), (rt.moving_average_return(prices['PLTR'], 15), rt.call_node('_node_asset_PLTR_636', prices)), (rt.moving_average_return(prices['BABA'], 15), rt.call_node('_node_asset_BABA_637', prices)), (rt.moving_average_return(prices['CONL'], 15), rt.call_node('_node_asset_CONL_638', prices))], 'top', int('1'))
rt.NODE_REGISTRY['_node_filter_639'] = _node_filter_639


def _node_wt_cash_equal_640(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_639', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_640'] = _node_wt_cash_equal_640


def _node_filter_641(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.moving_average_return(prices['TMF'], 15), rt.call_node('_node_asset_TMF_626', prices)), (rt.moving_average_return(prices['FAZ'], 15), rt.call_node('_node_asset_FAZ_627', prices)), (rt.moving_average_return(rt.synthetic_price_series(rt.call_node('_node_wt_cash_equal_640', prices), prices), 15), rt.call_node('_node_wt_cash_equal_640', prices))], 'top', int('1'))
rt.NODE_REGISTRY['_node_filter_641'] = _node_filter_641


def _node_wt_cash_equal_642(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_641', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_642'] = _node_wt_cash_equal_642


def _node_asset_AGQ_643(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'AGQ': 1.0}
rt.NODE_REGISTRY['_node_asset_AGQ_643'] = _node_asset_AGQ_643


def _node_asset_FAS_644(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'FAS': 1.0}
rt.NODE_REGISTRY['_node_asset_FAS_644'] = _node_asset_FAS_644


def _node_filter_645(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.relative_strength_index(prices['AGQ'], 10), rt.call_node('_node_asset_AGQ_643', prices)), (rt.relative_strength_index(prices['FAS'], 10), rt.call_node('_node_asset_FAS_644', prices))], 'top', int('1'))
rt.NODE_REGISTRY['_node_filter_645'] = _node_filter_645


def _node_wt_cash_equal_646(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_645', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_646'] = _node_wt_cash_equal_646


def _node_if_647(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['FAS'], 10) > 31.0:
        return rt.call_node('_node_wt_cash_equal_642', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_646', prices)
rt.NODE_REGISTRY['_node_if_647'] = _node_if_647


def _node_wt_cash_equal_648(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_647', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_648'] = _node_wt_cash_equal_648


def _node_asset_FAS_649(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'FAS': 1.0}
rt.NODE_REGISTRY['_node_asset_FAS_649'] = _node_asset_FAS_649


def _node_if_650(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['FAS']) < rt.moving_average_price(prices['FAS'], 100):
        return rt.call_node('_node_wt_cash_equal_648', prices)
    else:
        return rt.call_node('_node_asset_FAS_649', prices)
rt.NODE_REGISTRY['_node_if_650'] = _node_if_650


def _node_wt_cash_equal_651(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_650', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_651'] = _node_wt_cash_equal_651


def _node_if_652(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['SPY']) > rt.moving_average_price(prices['SPY'], 200):
        return rt.call_node('_node_wt_cash_equal_625', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_651', prices)
rt.NODE_REGISTRY['_node_if_652'] = _node_if_652


def _node_wt_cash_equal_653(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_652', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_653'] = _node_wt_cash_equal_653


def _node_if_654(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['TLT'], 95) < rt.cumulative_return(prices['QQQ'], 35):
        return rt.call_node('_node_asset_GDXD_579', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_653', prices)
rt.NODE_REGISTRY['_node_if_654'] = _node_if_654


def _node_wt_cash_equal_655(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_654', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_655'] = _node_wt_cash_equal_655


def _node_if_656(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['QQQ'], 90) > rt.cumulative_return(prices['QQQ'], 70):
        return rt.call_node('_node_wt_cash_equal_578', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_655', prices)
rt.NODE_REGISTRY['_node_if_656'] = _node_if_656


def _node_wt_cash_equal_657(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_656', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_657'] = _node_wt_cash_equal_657


def _node_if_658(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['GDXU'], 10) < 28.0:
        return rt.call_node('_node_asset_GDXU_333', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_657', prices)
rt.NODE_REGISTRY['_node_if_658'] = _node_if_658


def _node_wt_cash_equal_659(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_658', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_659'] = _node_wt_cash_equal_659


def _node_if_660(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['GDXU'], 10) > 81.0:
        return rt.call_node('_node_asset_GDXD_332', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_659', prices)
rt.NODE_REGISTRY['_node_if_660'] = _node_if_660


def _node_wt_cash_equal_661(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_660', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_661'] = _node_wt_cash_equal_661


def _node_asset_SOXL_662(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_662'] = _node_asset_SOXL_662


def _node_asset_SOXL_663(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_663'] = _node_asset_SOXL_663


def _node_asset_SOXL_664(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_664'] = _node_asset_SOXL_664


def _node_asset_SOXL_665(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_665'] = _node_asset_SOXL_665


def _node_asset_SOXL_666(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_666'] = _node_asset_SOXL_666


def _node_asset_UVXY_667(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_667'] = _node_asset_UVXY_667


def _node_asset_UVXY_668(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_668'] = _node_asset_UVXY_668


def _node_wt_cash_equal_669(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_UVXY_668', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_669'] = _node_wt_cash_equal_669


def _node_asset_UVXY_670(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_670'] = _node_asset_UVXY_670


def _node_asset_UVXY_671(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_671'] = _node_asset_UVXY_671


def _node_asset_UVXY_672(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_672'] = _node_asset_UVXY_672


def _node_asset_UVXY_673(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_673'] = _node_asset_UVXY_673


def _node_asset_BIL_674(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_674'] = _node_asset_BIL_674


def _node_asset_BIL_675(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_675'] = _node_asset_BIL_675


def _node_asset_BIL_676(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_676'] = _node_asset_BIL_676


def _node_asset_BIL_677(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_677'] = _node_asset_BIL_677


def _node_asset_BIL_678(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_678'] = _node_asset_BIL_678


def _node_asset_SOXL_679(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_679'] = _node_asset_SOXL_679


def _node_asset_UVXY_680(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_680'] = _node_asset_UVXY_680


def _node_asset_TMF_681(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TMF': 1.0}
rt.NODE_REGISTRY['_node_asset_TMF_681'] = _node_asset_TMF_681


def _node_asset_SOXL_682(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_682'] = _node_asset_SOXL_682


def _node_wt_cash_equal_683(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_682', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_683'] = _node_wt_cash_equal_683


def _node_asset_SOXL_684(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_684'] = _node_asset_SOXL_684


def _node_wt_cash_equal_685(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_684', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_685'] = _node_wt_cash_equal_685


def _node_asset_SOXL_686(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_686'] = _node_asset_SOXL_686


def _node_wt_cash_equal_687(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_686', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_687'] = _node_wt_cash_equal_687


def _node_asset_SOXL_688(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_688'] = _node_asset_SOXL_688


def _node_wt_cash_equal_689(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_688', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_689'] = _node_wt_cash_equal_689


def _node_asset_UPRO_690(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UPRO': 1.0}
rt.NODE_REGISTRY['_node_asset_UPRO_690'] = _node_asset_UPRO_690


def _node_asset_TQQQ_691(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_691'] = _node_asset_TQQQ_691


def _node_wt_cash_specified_692(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('80') / float(100)), rt.call_node('_node_asset_UPRO_690', prices)), ((float(20) / float(100)), rt.call_node('_node_asset_TQQQ_691', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_692'] = _node_wt_cash_specified_692


def _node_if_693(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) < 30.0:
        return rt.call_node('_node_wt_cash_equal_689', prices)
    else:
        return rt.call_node('_node_wt_cash_specified_692', prices)
rt.NODE_REGISTRY['_node_if_693'] = _node_if_693


def _node_wt_cash_equal_694(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_693', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_694'] = _node_wt_cash_equal_694

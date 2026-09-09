from typing import Dict, Sequence

import strategy_runtime as rt


def _node_asset_UVXY_1(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_1'] = _node_asset_UVXY_1


def _node_asset_UVXY_2(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_2'] = _node_asset_UVXY_2


def _node_asset_TQQQ_3(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_3'] = _node_asset_TQQQ_3


def _node_wt_cash_equal_4(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_TQQQ_3', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_4'] = _node_wt_cash_equal_4


def _node_if_5(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPXL'], 10) > 80.0:
        return rt.call_node('_node_asset_UVXY_2', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_4', prices)
rt.NODE_REGISTRY['_node_if_5'] = _node_if_5


def _node_wt_cash_equal_6(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_5', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_6'] = _node_wt_cash_equal_6


def _node_if_7(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TQQQ'], 10) > 79.0:
        return rt.call_node('_node_asset_UVXY_1', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_6', prices)
rt.NODE_REGISTRY['_node_if_7'] = _node_if_7


def _node_wt_cash_equal_8(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_7', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_8'] = _node_wt_cash_equal_8


def _node_asset_TECL_9(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TECL': 1.0}
rt.NODE_REGISTRY['_node_asset_TECL_9'] = _node_asset_TECL_9


def _node_asset_UPRO_10(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UPRO': 1.0}
rt.NODE_REGISTRY['_node_asset_UPRO_10'] = _node_asset_UPRO_10


def _node_asset_SQQQ_11(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_SQQQ_11'] = _node_asset_SQQQ_11


def _node_asset_TLT_12(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TLT': 1.0}
rt.NODE_REGISTRY['_node_asset_TLT_12'] = _node_asset_TLT_12


def _node_filter_13(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.relative_strength_index(prices['SQQQ'], 10), rt.call_node('_node_asset_SQQQ_11', prices)), (rt.relative_strength_index(prices['TLT'], 10), rt.call_node('_node_asset_TLT_12', prices))], 'top', int('1'))
rt.NODE_REGISTRY['_node_filter_13'] = _node_filter_13


def _node_wt_cash_equal_14(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_13', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_14'] = _node_wt_cash_equal_14


def _node_asset_SQQQ_15(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_SQQQ_15'] = _node_asset_SQQQ_15


def _node_asset_TQQQ_16(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_16'] = _node_asset_TQQQ_16


def _node_if_17(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SQQQ'], 10) < 31.0:
        return rt.call_node('_node_asset_SQQQ_15', prices)
    else:
        return rt.call_node('_node_asset_TQQQ_16', prices)
rt.NODE_REGISTRY['_node_if_17'] = _node_if_17


def _node_wt_cash_equal_18(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_17', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_18'] = _node_wt_cash_equal_18


def _node_if_19(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['TQQQ']) < rt.moving_average_price(prices['TQQQ'], 20):
        return rt.call_node('_node_wt_cash_equal_14', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_18', prices)
rt.NODE_REGISTRY['_node_if_19'] = _node_if_19


def _node_wt_cash_equal_20(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_19', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_20'] = _node_wt_cash_equal_20


def _node_if_21(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) < 30.0:
        return rt.call_node('_node_asset_UPRO_10', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_20', prices)
rt.NODE_REGISTRY['_node_if_21'] = _node_if_21


def _node_wt_cash_equal_22(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_21', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_22'] = _node_wt_cash_equal_22


def _node_if_23(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TQQQ'], 10) < 31.0:
        return rt.call_node('_node_asset_TECL_9', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_22', prices)
rt.NODE_REGISTRY['_node_if_23'] = _node_if_23


def _node_wt_cash_equal_24(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_23', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_24'] = _node_wt_cash_equal_24


def _node_if_25(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['SPY']) > rt.moving_average_price(prices['SPY'], 200):
        return rt.call_node('_node_wt_cash_equal_8', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_24', prices)
rt.NODE_REGISTRY['_node_if_25'] = _node_if_25


def _node_wt_cash_equal_26(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_25', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_26'] = _node_wt_cash_equal_26


def _node_wt_cash_equal_27(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_26', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_27'] = _node_wt_cash_equal_27


def _node_asset_EDC_28(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDC': 1.0}
rt.NODE_REGISTRY['_node_asset_EDC_28'] = _node_asset_EDC_28


def _node_asset_BIL_29(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_29'] = _node_asset_BIL_29


def _node_wt_cash_specified_30(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('68') / float(100)), rt.call_node('_node_asset_EDC_28', prices)), ((float(32) / float(100)), rt.call_node('_node_asset_BIL_29', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_30'] = _node_wt_cash_specified_30


def _node_asset_EDC_31(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDC': 1.0}
rt.NODE_REGISTRY['_node_asset_EDC_31'] = _node_asset_EDC_31


def _node_asset_EDZ_32(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDZ': 1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_32'] = _node_asset_EDZ_32


def _node_if_33(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IEI'], 10) > rt.relative_strength_index(prices['IWM'], 15):
        return rt.call_node('_node_asset_EDC_31', prices)
    else:
        return rt.call_node('_node_asset_EDZ_32', prices)
rt.NODE_REGISTRY['_node_if_33'] = _node_if_33


def _node_wt_cash_equal_34(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_33', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_34'] = _node_wt_cash_equal_34


def _node_asset_EDC_35(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDC': 1.0}
rt.NODE_REGISTRY['_node_asset_EDC_35'] = _node_asset_EDC_35


def _node_asset_EDZ_36(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDZ': 1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_36'] = _node_asset_EDZ_36


def _node_if_37(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IGIB'], 15) > rt.relative_strength_index(prices['EEM'], 15):
        return rt.call_node('_node_asset_EDC_35', prices)
    else:
        return rt.call_node('_node_asset_EDZ_36', prices)
rt.NODE_REGISTRY['_node_if_37'] = _node_if_37


def _node_wt_cash_equal_38(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_37', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_38'] = _node_wt_cash_equal_38


def _node_asset_EDC_39(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDC': 1.0}
rt.NODE_REGISTRY['_node_asset_EDC_39'] = _node_asset_EDC_39


def _node_asset_EDZ_40(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDZ': 1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_40'] = _node_asset_EDZ_40


def _node_if_41(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IGIB'], 10) > rt.relative_strength_index(prices['SPY'], 10):
        return rt.call_node('_node_asset_EDC_39', prices)
    else:
        return rt.call_node('_node_asset_EDZ_40', prices)
rt.NODE_REGISTRY['_node_if_41'] = _node_if_41


def _node_wt_cash_equal_42(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_41', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_42'] = _node_wt_cash_equal_42


def _node_combine_equal_43(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_38', prices), rt.call_node('_node_wt_cash_equal_42', prices)])
rt.NODE_REGISTRY['_node_combine_equal_43'] = _node_combine_equal_43


def _node_if_44(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['EEM']) > rt.moving_average_price(prices['EEM'], 200):
        return rt.call_node('_node_wt_cash_equal_34', prices)
    else:
        return rt.call_node('_node_combine_equal_43', prices)
rt.NODE_REGISTRY['_node_if_44'] = _node_if_44


def _node_wt_cash_equal_45(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_44', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_45'] = _node_wt_cash_equal_45


def _node_asset_EDC_46(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDC': 1.0}
rt.NODE_REGISTRY['_node_asset_EDC_46'] = _node_asset_EDC_46


def _node_asset_EDZ_47(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDZ': 1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_47'] = _node_asset_EDZ_47


def _node_if_48(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IGIB'], 10) > rt.relative_strength_index(prices['SPY'], 10):
        return rt.call_node('_node_asset_EDC_46', prices)
    else:
        return rt.call_node('_node_asset_EDZ_47', prices)
rt.NODE_REGISTRY['_node_if_48'] = _node_if_48


def _node_wt_cash_equal_49(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_48', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_49'] = _node_wt_cash_equal_49


def _node_if_50(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['SHV']) > rt.moving_average_price(prices['SHV'], 50):
        return rt.call_node('_node_wt_cash_equal_45', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_49', prices)
rt.NODE_REGISTRY['_node_if_50'] = _node_if_50


def _node_wt_cash_equal_51(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_50', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_51'] = _node_wt_cash_equal_51


def _node_if_52(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['EEM'], 10) < 25.0:
        return rt.call_node('_node_wt_cash_specified_30', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_51', prices)
rt.NODE_REGISTRY['_node_if_52'] = _node_if_52


def _node_wt_cash_equal_53(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_52', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_53'] = _node_wt_cash_equal_53


def _node_wt_cash_equal_54(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_53', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_54'] = _node_wt_cash_equal_54


def _node_asset_EDC_55(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDC': 1.0}
rt.NODE_REGISTRY['_node_asset_EDC_55'] = _node_asset_EDC_55


def _node_asset_BIL_56(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_56'] = _node_asset_BIL_56


def _node_wt_cash_specified_57(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('68') / float(100)), rt.call_node('_node_asset_EDC_55', prices)), ((float(32) / float(100)), rt.call_node('_node_asset_BIL_56', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_57'] = _node_wt_cash_specified_57


def _node_asset_EEM_58(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EEM': 1.0}
rt.NODE_REGISTRY['_node_asset_EEM_58'] = _node_asset_EEM_58


def _node_asset_EDZ_59(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDZ': 1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_59'] = _node_asset_EDZ_59


def _node_asset_BIL_60(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_60'] = _node_asset_BIL_60


def _node_wt_cash_specified_61(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('33') / float(100)), rt.call_node('_node_asset_EDZ_59', prices)), ((float(67) / float(100)), rt.call_node('_node_asset_BIL_60', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_61'] = _node_wt_cash_specified_61


def _node_if_62(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IEI'], 10) > rt.relative_strength_index(prices['IWM'], 15):
        return rt.call_node('_node_asset_EEM_58', prices)
    else:
        return rt.call_node('_node_wt_cash_specified_61', prices)
rt.NODE_REGISTRY['_node_if_62'] = _node_if_62


def _node_wt_cash_equal_63(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_62', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_63'] = _node_wt_cash_equal_63


def _node_asset_EEM_64(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EEM': 1.0}
rt.NODE_REGISTRY['_node_asset_EEM_64'] = _node_asset_EEM_64


def _node_asset_EDZ_65(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDZ': 1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_65'] = _node_asset_EDZ_65


def _node_asset_BIL_66(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_66'] = _node_asset_BIL_66


def _node_wt_cash_specified_67(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('33') / float(100)), rt.call_node('_node_asset_EDZ_65', prices)), ((float(67) / float(100)), rt.call_node('_node_asset_BIL_66', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_67'] = _node_wt_cash_specified_67


def _node_if_68(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IGIB'], 15) > rt.relative_strength_index(prices['EEM'], 15):
        return rt.call_node('_node_asset_EEM_64', prices)
    else:
        return rt.call_node('_node_wt_cash_specified_67', prices)
rt.NODE_REGISTRY['_node_if_68'] = _node_if_68


def _node_wt_cash_equal_69(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_68', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_69'] = _node_wt_cash_equal_69


def _node_asset_EEM_70(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EEM': 1.0}
rt.NODE_REGISTRY['_node_asset_EEM_70'] = _node_asset_EEM_70


def _node_asset_EDZ_71(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDZ': 1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_71'] = _node_asset_EDZ_71


def _node_asset_BIL_72(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_72'] = _node_asset_BIL_72


def _node_wt_cash_specified_73(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('33') / float(100)), rt.call_node('_node_asset_EDZ_71', prices)), ((float(67) / float(100)), rt.call_node('_node_asset_BIL_72', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_73'] = _node_wt_cash_specified_73


def _node_if_74(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IGIB'], 10) > rt.relative_strength_index(prices['SPY'], 10):
        return rt.call_node('_node_asset_EEM_70', prices)
    else:
        return rt.call_node('_node_wt_cash_specified_73', prices)
rt.NODE_REGISTRY['_node_if_74'] = _node_if_74


def _node_wt_cash_equal_75(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_74', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_75'] = _node_wt_cash_equal_75


def _node_combine_equal_76(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_69', prices), rt.call_node('_node_wt_cash_equal_75', prices)])
rt.NODE_REGISTRY['_node_combine_equal_76'] = _node_combine_equal_76


def _node_if_77(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['EEM']) > rt.moving_average_price(prices['EEM'], 200):
        return rt.call_node('_node_wt_cash_equal_63', prices)
    else:
        return rt.call_node('_node_combine_equal_76', prices)
rt.NODE_REGISTRY['_node_if_77'] = _node_if_77


def _node_wt_cash_equal_78(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_77', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_78'] = _node_wt_cash_equal_78


def _node_asset_EEM_79(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EEM': 1.0}
rt.NODE_REGISTRY['_node_asset_EEM_79'] = _node_asset_EEM_79


def _node_asset_EDZ_80(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDZ': 1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_80'] = _node_asset_EDZ_80


def _node_asset_BIL_81(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_81'] = _node_asset_BIL_81


def _node_wt_cash_specified_82(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('33') / float(100)), rt.call_node('_node_asset_EDZ_80', prices)), ((float(67) / float(100)), rt.call_node('_node_asset_BIL_81', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_82'] = _node_wt_cash_specified_82


def _node_if_83(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IGIB'], 10) > rt.relative_strength_index(prices['SPY'], 10):
        return rt.call_node('_node_asset_EEM_79', prices)
    else:
        return rt.call_node('_node_wt_cash_specified_82', prices)
rt.NODE_REGISTRY['_node_if_83'] = _node_if_83


def _node_wt_cash_equal_84(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_83', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_84'] = _node_wt_cash_equal_84


def _node_if_85(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['SHV']) > rt.moving_average_price(prices['SHV'], 50):
        return rt.call_node('_node_wt_cash_equal_78', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_84', prices)
rt.NODE_REGISTRY['_node_if_85'] = _node_if_85


def _node_wt_cash_equal_86(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_85', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_86'] = _node_wt_cash_equal_86


def _node_if_87(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['EEM'], 10) < 25.0:
        return rt.call_node('_node_wt_cash_specified_57', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_86', prices)
rt.NODE_REGISTRY['_node_if_87'] = _node_if_87


def _node_wt_cash_equal_88(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_87', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_88'] = _node_wt_cash_equal_88


def _node_wt_cash_equal_89(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_88', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_89'] = _node_wt_cash_equal_89


def _node_if_90(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['SPY']) > rt.moving_average_price(prices['SPY'], 200):
        return rt.call_node('_node_wt_cash_equal_54', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_89', prices)
rt.NODE_REGISTRY['_node_if_90'] = _node_if_90


def _node_wt_cash_equal_91(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_90', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_91'] = _node_wt_cash_equal_91


def _node_wt_cash_equal_92(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_91', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_92'] = _node_wt_cash_equal_92


def _node_asset_UVXY_93(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_93'] = _node_asset_UVXY_93


def _node_asset_UVXY_94(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_94'] = _node_asset_UVXY_94


def _node_asset_UVXY_95(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_95'] = _node_asset_UVXY_95


def _node_asset_UVXY_96(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_96'] = _node_asset_UVXY_96


def _node_asset_UVXY_97(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_97'] = _node_asset_UVXY_97


def _node_asset_UVXY_98(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_98'] = _node_asset_UVXY_98


def _node_asset_UVXY_99(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_99'] = _node_asset_UVXY_99


def _node_asset_UVXY_100(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_100'] = _node_asset_UVXY_100


def _node_wt_cash_equal_101(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_UVXY_100', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_101'] = _node_wt_cash_equal_101


def _node_asset_UVXY_102(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_102'] = _node_asset_UVXY_102


def _node_asset_UVXY_103(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_103'] = _node_asset_UVXY_103


def _node_asset_UVXY_104(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_104'] = _node_asset_UVXY_104


def _node_asset_VIXM_105(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'VIXM': 1.0}
rt.NODE_REGISTRY['_node_asset_VIXM_105'] = _node_asset_VIXM_105


def _node_asset_SPXL_106(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SPXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SPXL_106'] = _node_asset_SPXL_106


def _node_if_107(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 21) > 30.0:
        return rt.call_node('_node_asset_VIXM_105', prices)
    else:
        return rt.call_node('_node_asset_SPXL_106', prices)
rt.NODE_REGISTRY['_node_if_107'] = _node_if_107


def _node_wt_cash_equal_108(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_107', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_108'] = _node_wt_cash_equal_108


def _node_wt_cash_equal_109(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_108', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_109'] = _node_wt_cash_equal_109


def _node_asset_TECL_110(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TECL': 1.0}
rt.NODE_REGISTRY['_node_asset_TECL_110'] = _node_asset_TECL_110


def _node_asset_SOXL_111(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_111'] = _node_asset_SOXL_111


def _node_asset_SPXL_112(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SPXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SPXL_112'] = _node_asset_SPXL_112


def _node_asset_TECL_113(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TECL': 1.0}
rt.NODE_REGISTRY['_node_asset_TECL_113'] = _node_asset_TECL_113


def _node_asset_SOXL_114(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_114'] = _node_asset_SOXL_114


def _node_filter_115(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.relative_strength_index(prices['TECL'], 10), rt.call_node('_node_asset_TECL_113', prices)), (rt.relative_strength_index(prices['SOXL'], 10), rt.call_node('_node_asset_SOXL_114', prices))], 'bottom', int('1'))
rt.NODE_REGISTRY['_node_filter_115'] = _node_filter_115


def _node_wt_cash_equal_116(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_115', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_116'] = _node_wt_cash_equal_116


def _node_asset_SQQQ_117(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_SQQQ_117'] = _node_asset_SQQQ_117


def _node_asset_TLT_118(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TLT': 1.0}
rt.NODE_REGISTRY['_node_asset_TLT_118'] = _node_asset_TLT_118


def _node_filter_119(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.relative_strength_index(prices['SQQQ'], 10), rt.call_node('_node_asset_SQQQ_117', prices)), (rt.relative_strength_index(prices['TLT'], 10), rt.call_node('_node_asset_TLT_118', prices))], 'top', int('1'))
rt.NODE_REGISTRY['_node_filter_119'] = _node_filter_119


def _node_wt_cash_equal_120(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_119', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_120'] = _node_wt_cash_equal_120


def _node_if_121(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLK'], 10) > rt.relative_strength_index(prices['KMLM'], 10):
        return rt.call_node('_node_wt_cash_equal_116', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_120', prices)
rt.NODE_REGISTRY['_node_if_121'] = _node_if_121


def _node_wt_cash_equal_122(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_121', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_122'] = _node_wt_cash_equal_122


def _node_wt_cash_equal_123(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_122', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_123'] = _node_wt_cash_equal_123


def _node_wt_cash_equal_124(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_123', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_124'] = _node_wt_cash_equal_124


def _node_if_125(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPXL'], 10) < 30.0:
        return rt.call_node('_node_asset_SPXL_112', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_124', prices)
rt.NODE_REGISTRY['_node_if_125'] = _node_if_125


def _node_wt_cash_equal_126(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_125', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_126'] = _node_wt_cash_equal_126


def _node_if_127(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SOXL'], 10) < 30.0:
        return rt.call_node('_node_asset_SOXL_111', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_126', prices)
rt.NODE_REGISTRY['_node_if_127'] = _node_if_127


def _node_wt_cash_equal_128(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_127', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_128'] = _node_wt_cash_equal_128


def _node_if_129(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TQQQ'], 10) < 30.0:
        return rt.call_node('_node_asset_TECL_110', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_128', prices)
rt.NODE_REGISTRY['_node_if_129'] = _node_if_129


def _node_wt_cash_equal_130(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_129', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_130'] = _node_wt_cash_equal_130


def _node_wt_cash_equal_131(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_130', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_131'] = _node_wt_cash_equal_131


def _node_if_132(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['UVXY'], 21) > 65.0:
        return rt.call_node('_node_wt_cash_equal_109', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_131', prices)
rt.NODE_REGISTRY['_node_if_132'] = _node_if_132


def _node_wt_cash_equal_133(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_132', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_133'] = _node_wt_cash_equal_133


def _node_wt_cash_equal_134(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_133', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_134'] = _node_wt_cash_equal_134


def _node_if_135(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) > 80.0:
        return rt.call_node('_node_asset_UVXY_104', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_134', prices)
rt.NODE_REGISTRY['_node_if_135'] = _node_if_135


def _node_wt_cash_equal_136(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_135', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_136'] = _node_wt_cash_equal_136


def _node_if_137(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['FAS'], 10) > 80.0:
        return rt.call_node('_node_asset_UVXY_103', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_136', prices)
rt.NODE_REGISTRY['_node_if_137'] = _node_if_137


def _node_wt_cash_equal_138(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_137', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_138'] = _node_wt_cash_equal_138


def _node_if_139(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLY'], 10) > 80.0:
        return rt.call_node('_node_asset_UVXY_102', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_138', prices)
rt.NODE_REGISTRY['_node_if_139'] = _node_if_139


def _node_wt_cash_equal_140(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_139', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_140'] = _node_wt_cash_equal_140


def _node_if_141(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TQQQ'], 10) > 79.0:
        return rt.call_node('_node_wt_cash_equal_101', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_140', prices)
rt.NODE_REGISTRY['_node_if_141'] = _node_if_141


def _node_wt_cash_equal_142(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_141', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_142'] = _node_wt_cash_equal_142


def _node_if_143(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLP'], 10) > 75.0:
        return rt.call_node('_node_asset_UVXY_99', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_142', prices)
rt.NODE_REGISTRY['_node_if_143'] = _node_if_143


def _node_wt_cash_equal_144(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_143', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_144'] = _node_wt_cash_equal_144


def _node_if_145(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['VOOV'], 10) > 79.0:
        return rt.call_node('_node_asset_UVXY_98', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_144', prices)
rt.NODE_REGISTRY['_node_if_145'] = _node_if_145


def _node_wt_cash_equal_146(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_145', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_146'] = _node_wt_cash_equal_146


def _node_if_147(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['VOOG'], 10) > 79.0:
        return rt.call_node('_node_asset_UVXY_97', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_146', prices)
rt.NODE_REGISTRY['_node_if_147'] = _node_if_147


def _node_wt_cash_equal_148(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_147', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_148'] = _node_wt_cash_equal_148


def _node_if_149(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TECL'], 10) > 79.0:
        return rt.call_node('_node_asset_UVXY_96', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_148', prices)
rt.NODE_REGISTRY['_node_if_149'] = _node_if_149


def _node_wt_cash_equal_150(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_149', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_150'] = _node_wt_cash_equal_150


def _node_if_151(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['VOX'], 10) > 79.0:
        return rt.call_node('_node_asset_UVXY_95', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_150', prices)
rt.NODE_REGISTRY['_node_if_151'] = _node_if_151


def _node_wt_cash_equal_152(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_151', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_152'] = _node_wt_cash_equal_152


def _node_if_153(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['VTV'], 10) > 79.0:
        return rt.call_node('_node_asset_UVXY_94', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_152', prices)
rt.NODE_REGISTRY['_node_if_153'] = _node_if_153


def _node_wt_cash_equal_154(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_153', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_154'] = _node_wt_cash_equal_154


def _node_if_155(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQE'], 10) > 79.0:
        return rt.call_node('_node_asset_UVXY_93', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_154', prices)
rt.NODE_REGISTRY['_node_if_155'] = _node_if_155


def _node_wt_cash_equal_156(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_155', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_156'] = _node_wt_cash_equal_156


def _node_wt_cash_equal_157(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_156', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_157'] = _node_wt_cash_equal_157


def _node_asset_GDXD_158(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'GDXD': 1.0}
rt.NODE_REGISTRY['_node_asset_GDXD_158'] = _node_asset_GDXD_158


def _node_asset_UGL_159(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UGL': 1.0}
rt.NODE_REGISTRY['_node_asset_UGL_159'] = _node_asset_UGL_159


def _node_asset_UGL_160(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UGL': 1.0}
rt.NODE_REGISTRY['_node_asset_UGL_160'] = _node_asset_UGL_160


def _node_asset_BIL_161(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_161'] = _node_asset_BIL_161


def _node_if_162(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['UGL'], 70) < rt.cumulative_return(prices['UGL'], 75):
        return rt.call_node('_node_asset_UGL_160', prices)
    else:
        return rt.call_node('_node_asset_BIL_161', prices)
rt.NODE_REGISTRY['_node_if_162'] = _node_if_162


def _node_wt_cash_equal_163(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_162', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_163'] = _node_wt_cash_equal_163


def _node_asset_GDXD_164(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'GDXD': 1.0}
rt.NODE_REGISTRY['_node_asset_GDXD_164'] = _node_asset_GDXD_164


def _node_asset_BIL_165(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_165'] = _node_asset_BIL_165


def _node_if_166(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['TLT'], 95) < rt.cumulative_return(prices['QQQ'], 35):
        return rt.call_node('_node_asset_GDXD_164', prices)
    else:
        return rt.call_node('_node_asset_BIL_165', prices)
rt.NODE_REGISTRY['_node_if_166'] = _node_if_166


def _node_wt_cash_equal_167(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_166', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_167'] = _node_wt_cash_equal_167


def _node_if_168(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['QQQ'], 90) > rt.cumulative_return(prices['QQQ'], 70):
        return rt.call_node('_node_wt_cash_equal_163', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_167', prices)
rt.NODE_REGISTRY['_node_if_168'] = _node_if_168


def _node_wt_cash_equal_169(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_168', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_169'] = _node_wt_cash_equal_169


def _node_if_170(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['UGL'], 10) < 28.0:
        return rt.call_node('_node_asset_UGL_159', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_169', prices)
rt.NODE_REGISTRY['_node_if_170'] = _node_if_170


def _node_wt_cash_equal_171(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_170', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_171'] = _node_wt_cash_equal_171


def _node_if_172(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['UGL'], 10) > 81.0:
        return rt.call_node('_node_asset_GDXD_158', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_171', prices)
rt.NODE_REGISTRY['_node_if_172'] = _node_if_172


def _node_wt_cash_equal_173(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_172', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_173'] = _node_wt_cash_equal_173


def _node_asset_SOXL_174(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_174'] = _node_asset_SOXL_174


def _node_asset_SOXL_175(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_175'] = _node_asset_SOXL_175


def _node_asset_SOXL_176(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_176'] = _node_asset_SOXL_176


def _node_asset_SOXL_177(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_177'] = _node_asset_SOXL_177


def _node_asset_SOXL_178(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_178'] = _node_asset_SOXL_178


def _node_asset_UVXY_179(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_179'] = _node_asset_UVXY_179


def _node_asset_UVXY_180(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_180'] = _node_asset_UVXY_180


def _node_wt_cash_equal_181(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_UVXY_180', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_181'] = _node_wt_cash_equal_181


def _node_asset_UVXY_182(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_182'] = _node_asset_UVXY_182


def _node_asset_UVXY_183(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_183'] = _node_asset_UVXY_183


def _node_asset_UVXY_184(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_184'] = _node_asset_UVXY_184


def _node_asset_UVXY_185(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_185'] = _node_asset_UVXY_185


def _node_asset_UVXY_186(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_186'] = _node_asset_UVXY_186


def _node_asset_UVXY_187(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_187'] = _node_asset_UVXY_187


def _node_asset_VIXY_188(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'VIXY': 1.0}
rt.NODE_REGISTRY['_node_asset_VIXY_188'] = _node_asset_VIXY_188


def _node_asset_VIXY_189(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'VIXY': 1.0}
rt.NODE_REGISTRY['_node_asset_VIXY_189'] = _node_asset_VIXY_189


def _node_asset_VIXY_190(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'VIXY': 1.0}
rt.NODE_REGISTRY['_node_asset_VIXY_190'] = _node_asset_VIXY_190


def _node_asset_SOXL_191(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_191'] = _node_asset_SOXL_191


def _node_asset_UVXY_192(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_192'] = _node_asset_UVXY_192


def _node_asset_TMF_193(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TMF': 1.0}
rt.NODE_REGISTRY['_node_asset_TMF_193'] = _node_asset_TMF_193


def _node_asset_SOXL_194(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_194'] = _node_asset_SOXL_194


def _node_wt_cash_equal_195(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_194', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_195'] = _node_wt_cash_equal_195


def _node_asset_SOXL_196(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_196'] = _node_asset_SOXL_196


def _node_wt_cash_equal_197(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_196', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_197'] = _node_wt_cash_equal_197


def _node_asset_SOXL_198(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_198'] = _node_asset_SOXL_198


def _node_wt_cash_equal_199(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_198', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_199'] = _node_wt_cash_equal_199


def _node_asset_SOXL_200(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_200'] = _node_asset_SOXL_200


def _node_wt_cash_equal_201(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_200', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_201'] = _node_wt_cash_equal_201


def _node_asset_UPRO_202(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UPRO': 1.0}
rt.NODE_REGISTRY['_node_asset_UPRO_202'] = _node_asset_UPRO_202


def _node_asset_TQQQ_203(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_203'] = _node_asset_TQQQ_203


def _node_wt_cash_specified_204(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('80') / float(100)), rt.call_node('_node_asset_UPRO_202', prices)), ((float(20) / float(100)), rt.call_node('_node_asset_TQQQ_203', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_204'] = _node_wt_cash_specified_204


def _node_if_205(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) < 31.0:
        return rt.call_node('_node_wt_cash_equal_201', prices)
    else:
        return rt.call_node('_node_wt_cash_specified_204', prices)
rt.NODE_REGISTRY['_node_if_205'] = _node_if_205


def _node_wt_cash_equal_206(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_205', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_206'] = _node_wt_cash_equal_206


def _node_if_207(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) < 31.0:
        return rt.call_node('_node_wt_cash_equal_199', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_206', prices)
rt.NODE_REGISTRY['_node_if_207'] = _node_if_207


def _node_wt_cash_equal_208(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_207', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_208'] = _node_wt_cash_equal_208


def _node_if_209(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) > 99.0:
        return rt.call_node('_node_wt_cash_equal_197', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_208', prices)
rt.NODE_REGISTRY['_node_if_209'] = _node_if_209


def _node_wt_cash_equal_210(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_209', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_210'] = _node_wt_cash_equal_210


def _node_if_211(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) > 56.0:
        return rt.call_node('_node_wt_cash_equal_195', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_210', prices)
rt.NODE_REGISTRY['_node_if_211'] = _node_if_211


def _node_wt_cash_equal_212(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_211', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_212'] = _node_wt_cash_equal_212


def _node_if_213(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['SOXL'], 1) < -16.0:
        return rt.call_node('_node_asset_TMF_193', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_212', prices)
rt.NODE_REGISTRY['_node_if_213'] = _node_if_213


def _node_wt_cash_equal_214(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_213', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_214'] = _node_wt_cash_equal_214


def _node_if_215(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['SOXL'], 1) < -20.0:
        return rt.call_node('_node_asset_UVXY_192', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_214', prices)
rt.NODE_REGISTRY['_node_if_215'] = _node_if_215


def _node_wt_cash_equal_216(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_215', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_216'] = _node_wt_cash_equal_216


def _node_if_217(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['SOXL'], 1) < -25.0:
        return rt.call_node('_node_asset_SOXL_191', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_216', prices)
rt.NODE_REGISTRY['_node_if_217'] = _node_if_217


def _node_wt_cash_equal_218(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_217', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_218'] = _node_wt_cash_equal_218


def _node_if_219(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 200) > 57.0:
        return rt.call_node('_node_asset_VIXY_190', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_218', prices)
rt.NODE_REGISTRY['_node_if_219'] = _node_if_219


def _node_wt_cash_equal_220(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_219', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_220'] = _node_wt_cash_equal_220


def _node_wt_cash_equal_221(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_220', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_221'] = _node_wt_cash_equal_221


def _node_if_222(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 60) > 63.0:
        return rt.call_node('_node_asset_VIXY_189', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_221', prices)
rt.NODE_REGISTRY['_node_if_222'] = _node_if_222


def _node_wt_cash_equal_223(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_222', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_223'] = _node_wt_cash_equal_223


def _node_if_224(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 14) > 99.0:
        return rt.call_node('_node_asset_VIXY_188', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_223', prices)
rt.NODE_REGISTRY['_node_if_224'] = _node_if_224


def _node_wt_cash_equal_225(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_224', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_225'] = _node_wt_cash_equal_225


def _node_if_226(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 60) > 67.0:
        return rt.call_node('_node_asset_UVXY_187', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_225', prices)
rt.NODE_REGISTRY['_node_if_226'] = _node_if_226


def _node_wt_cash_equal_227(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_226', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_227'] = _node_wt_cash_equal_227


def _node_if_228(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 60) > 68.0:
        return rt.call_node('_node_asset_UVXY_186', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_227', prices)
rt.NODE_REGISTRY['_node_if_228'] = _node_if_228


def _node_wt_cash_equal_229(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_228', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_229'] = _node_wt_cash_equal_229


def _node_if_230(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 6) > 86.0:
        return rt.call_node('_node_asset_UVXY_185', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_229', prices)
rt.NODE_REGISTRY['_node_if_230'] = _node_if_230


def _node_wt_cash_equal_231(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_230', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_231'] = _node_wt_cash_equal_231


def _node_if_232(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 5) > 92.0:
        return rt.call_node('_node_asset_UVXY_184', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_231', prices)
rt.NODE_REGISTRY['_node_if_232'] = _node_if_232


def _node_wt_cash_equal_233(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_232', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_233'] = _node_wt_cash_equal_233


def _node_if_234(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 5) > 88.0:
        return rt.call_node('_node_asset_UVXY_183', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_233', prices)
rt.NODE_REGISTRY['_node_if_234'] = _node_if_234


def _node_wt_cash_equal_235(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_234', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_235'] = _node_wt_cash_equal_235


def _node_if_236(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) > 81.0:
        return rt.call_node('_node_asset_UVXY_182', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_235', prices)
rt.NODE_REGISTRY['_node_if_236'] = _node_if_236


def _node_wt_cash_equal_237(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_236', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_237'] = _node_wt_cash_equal_237

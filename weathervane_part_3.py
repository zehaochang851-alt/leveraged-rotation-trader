from typing import Dict, Sequence

import strategy_runtime as rt


def _node_if_695(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) < 30.0:
        return rt.call_node('_node_wt_cash_equal_687', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_694', prices)
rt.NODE_REGISTRY['_node_if_695'] = _node_if_695


def _node_wt_cash_equal_696(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_695', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_696'] = _node_wt_cash_equal_696


def _node_if_697(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) > 95.0:
        return rt.call_node('_node_wt_cash_equal_685', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_696', prices)
rt.NODE_REGISTRY['_node_if_697'] = _node_if_697


def _node_wt_cash_equal_698(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_697', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_698'] = _node_wt_cash_equal_698


def _node_if_699(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) > 60.0:
        return rt.call_node('_node_wt_cash_equal_683', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_698', prices)
rt.NODE_REGISTRY['_node_if_699'] = _node_if_699


def _node_wt_cash_equal_700(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_699', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_700'] = _node_wt_cash_equal_700


def _node_if_701(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['SOXL'], 1) < -16.0:
        return rt.call_node('_node_asset_TMF_681', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_700', prices)
rt.NODE_REGISTRY['_node_if_701'] = _node_if_701


def _node_wt_cash_equal_702(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_701', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_702'] = _node_wt_cash_equal_702


def _node_if_703(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['SOXL'], 1) < -20.0:
        return rt.call_node('_node_asset_UVXY_680', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_702', prices)
rt.NODE_REGISTRY['_node_if_703'] = _node_if_703


def _node_wt_cash_equal_704(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_703', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_704'] = _node_wt_cash_equal_704


def _node_if_705(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['SOXL'], 1) < -25.0:
        return rt.call_node('_node_asset_SOXL_679', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_704', prices)
rt.NODE_REGISTRY['_node_if_705'] = _node_if_705


def _node_wt_cash_equal_706(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_705', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_706'] = _node_wt_cash_equal_706


def _node_if_707(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 200) > 55.0:
        return rt.call_node('_node_asset_BIL_678', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_706', prices)
rt.NODE_REGISTRY['_node_if_707'] = _node_if_707


def _node_wt_cash_equal_708(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_707', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_708'] = _node_wt_cash_equal_708


def _node_wt_cash_equal_709(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_708', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_709'] = _node_wt_cash_equal_709


def _node_if_710(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 60) > 60.0:
        return rt.call_node('_node_asset_BIL_677', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_709', prices)
rt.NODE_REGISTRY['_node_if_710'] = _node_if_710


def _node_wt_cash_equal_711(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_710', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_711'] = _node_wt_cash_equal_711


def _node_if_712(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 14) > 95.0:
        return rt.call_node('_node_asset_BIL_676', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_711', prices)
rt.NODE_REGISTRY['_node_if_712'] = _node_if_712


def _node_wt_cash_equal_713(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_712', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_713'] = _node_wt_cash_equal_713


def _node_if_714(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 60) > 65.0:
        return rt.call_node('_node_asset_BIL_675', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_713', prices)
rt.NODE_REGISTRY['_node_if_714'] = _node_if_714


def _node_wt_cash_equal_715(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_714', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_715'] = _node_wt_cash_equal_715


def _node_if_716(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 60) > 65.0:
        return rt.call_node('_node_asset_BIL_674', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_715', prices)
rt.NODE_REGISTRY['_node_if_716'] = _node_if_716


def _node_wt_cash_equal_717(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_716', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_717'] = _node_wt_cash_equal_717


def _node_if_718(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 6) > 85.0:
        return rt.call_node('_node_asset_UVXY_673', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_717', prices)
rt.NODE_REGISTRY['_node_if_718'] = _node_if_718


def _node_wt_cash_equal_719(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_718', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_719'] = _node_wt_cash_equal_719


def _node_if_720(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 5) > 90.0:
        return rt.call_node('_node_asset_UVXY_672', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_719', prices)
rt.NODE_REGISTRY['_node_if_720'] = _node_if_720


def _node_wt_cash_equal_721(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_720', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_721'] = _node_wt_cash_equal_721


def _node_if_722(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 5) > 90.0:
        return rt.call_node('_node_asset_UVXY_671', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_721', prices)
rt.NODE_REGISTRY['_node_if_722'] = _node_if_722


def _node_wt_cash_equal_723(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_722', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_723'] = _node_wt_cash_equal_723


def _node_if_724(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) > 80.0:
        return rt.call_node('_node_asset_UVXY_670', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_723', prices)
rt.NODE_REGISTRY['_node_if_724'] = _node_if_724


def _node_wt_cash_equal_725(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_724', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_725'] = _node_wt_cash_equal_725


def _node_if_726(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) > 79.0:
        return rt.call_node('_node_wt_cash_equal_669', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_725', prices)
rt.NODE_REGISTRY['_node_if_726'] = _node_if_726


def _node_wt_cash_equal_727(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_726', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_727'] = _node_wt_cash_equal_727


def _node_if_728(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLP'], 10) > 75.0:
        return rt.call_node('_node_asset_UVXY_667', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_727', prices)
rt.NODE_REGISTRY['_node_if_728'] = _node_if_728


def _node_wt_cash_specified_729(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float(100) / float(100)), rt.call_node('_node_if_728', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_729'] = _node_wt_cash_specified_729


def _node_if_730(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['UVXY'], 10) > 84.0:
        return rt.call_node('_node_asset_SOXL_666', prices)
    else:
        return rt.call_node('_node_wt_cash_specified_729', prices)
rt.NODE_REGISTRY['_node_if_730'] = _node_if_730


def _node_wt_cash_equal_731(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_730', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_731'] = _node_wt_cash_equal_731


def _node_asset_SOXL_732(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_732'] = _node_asset_SOXL_732


def _node_asset_UVXY_733(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_733'] = _node_asset_UVXY_733


def _node_asset_BIL_734(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_734'] = _node_asset_BIL_734


def _node_asset_BIL_735(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_735'] = _node_asset_BIL_735


def _node_asset_BIL_736(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_736'] = _node_asset_BIL_736


def _node_asset_BIL_737(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_737'] = _node_asset_BIL_737


def _node_asset_BIL_738(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_738'] = _node_asset_BIL_738


def _node_asset_UVXY_739(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_739'] = _node_asset_UVXY_739


def _node_asset_SOXL_740(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_740'] = _node_asset_SOXL_740


def _node_wt_cash_equal_741(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_740', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_741'] = _node_wt_cash_equal_741


def _node_asset_BIL_742(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_742'] = _node_asset_BIL_742


def _node_asset_SOXL_743(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_743'] = _node_asset_SOXL_743


def _node_if_744(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['UVXY'], 10) < 84.0:
        return rt.call_node('_node_asset_BIL_742', prices)
    else:
        return rt.call_node('_node_asset_SOXL_743', prices)
rt.NODE_REGISTRY['_node_if_744'] = _node_if_744


def _node_wt_cash_equal_745(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_744', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_745'] = _node_wt_cash_equal_745


def _node_asset_SOXL_746(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_746'] = _node_asset_SOXL_746


def _node_wt_cash_equal_747(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_746', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_747'] = _node_wt_cash_equal_747


def _node_asset_SOXL_748(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_748'] = _node_asset_SOXL_748


def _node_wt_cash_equal_749(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_748', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_749'] = _node_wt_cash_equal_749


def _node_asset_SQQQ_750(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_SQQQ_750'] = _node_asset_SQQQ_750


def _node_wt_cash_equal_751(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SQQQ_750', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_751'] = _node_wt_cash_equal_751


def _node_asset_SOXL_752(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_752'] = _node_asset_SOXL_752


def _node_wt_cash_equal_753(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_752', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_753'] = _node_wt_cash_equal_753


def _node_if_754(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['PSQ'], 10) < 30.0:
        return rt.call_node('_node_wt_cash_equal_751', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_753', prices)
rt.NODE_REGISTRY['_node_if_754'] = _node_if_754


def _node_wt_cash_equal_755(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_754', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_755'] = _node_wt_cash_equal_755


def _node_asset_SOXL_756(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_756'] = _node_asset_SOXL_756


def _node_wt_cash_equal_757(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_756', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_757'] = _node_wt_cash_equal_757


def _node_asset_SOXL_758(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_758'] = _node_asset_SOXL_758


def _node_wt_cash_equal_759(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_758', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_759'] = _node_wt_cash_equal_759


def _node_asset_SOXL_760(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_760'] = _node_asset_SOXL_760


def _node_wt_cash_equal_761(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_SOXL_760', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_761'] = _node_wt_cash_equal_761


def _node_asset_GLD_762(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'GLD': 1.0}
rt.NODE_REGISTRY['_node_asset_GLD_762'] = _node_asset_GLD_762


def _node_if_763(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) > rt.relative_strength_index(prices['TLT'], 10):
        return rt.call_node('_node_wt_cash_equal_761', prices)
    else:
        return rt.call_node('_node_asset_GLD_762', prices)
rt.NODE_REGISTRY['_node_if_763'] = _node_if_763


def _node_wt_cash_equal_764(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_763', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_764'] = _node_wt_cash_equal_764


def _node_asset_SQQQ_765(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_SQQQ_765'] = _node_asset_SQQQ_765


def _node_asset_TLT_766(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TLT': 1.0}
rt.NODE_REGISTRY['_node_asset_TLT_766'] = _node_asset_TLT_766


def _node_filter_767(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.relative_strength_index(prices['SQQQ'], 10), rt.call_node('_node_asset_SQQQ_765', prices)), (rt.relative_strength_index(prices['TLT'], 10), rt.call_node('_node_asset_TLT_766', prices))], 'top', int('1'))
rt.NODE_REGISTRY['_node_filter_767'] = _node_filter_767


def _node_wt_cash_equal_768(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_767', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_768'] = _node_wt_cash_equal_768


def _node_asset_TMF_769(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TMF': 1.0}
rt.NODE_REGISTRY['_node_asset_TMF_769'] = _node_asset_TMF_769


def _node_asset_TQQQ_770(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_TQQQ_770'] = _node_asset_TQQQ_770


def _node_wt_cash_equal_771(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_TQQQ_770', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_771'] = _node_wt_cash_equal_771


def _node_if_772(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['TLT']) > rt.moving_average_price(prices['TLT'], 200):
        return rt.call_node('_node_asset_TMF_769', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_771', prices)
rt.NODE_REGISTRY['_node_if_772'] = _node_if_772


def _node_wt_cash_equal_773(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_772', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_773'] = _node_wt_cash_equal_773


def _node_if_774(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['PSQ'], 10) > rt.relative_strength_index(prices['TLT'], 10):
        return rt.call_node('_node_wt_cash_equal_768', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_773', prices)
rt.NODE_REGISTRY['_node_if_774'] = _node_if_774


def _node_wt_cash_equal_775(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_774', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_775'] = _node_wt_cash_equal_775


def _node_if_776(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['PSQ'], 10) > 65.0:
        return rt.call_node('_node_wt_cash_equal_764', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_775', prices)
rt.NODE_REGISTRY['_node_if_776'] = _node_if_776


def _node_wt_cash_equal_777(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_776', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_777'] = _node_wt_cash_equal_777


def _node_wt_cash_equal_778(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_777', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_778'] = _node_wt_cash_equal_778


def _node_if_779(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['SPY']) > rt.moving_average_price(prices['SPY'], 30):
        return rt.call_node('_node_wt_cash_equal_759', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_778', prices)
rt.NODE_REGISTRY['_node_if_779'] = _node_if_779


def _node_wt_cash_equal_780(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_779', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_780'] = _node_wt_cash_equal_780


def _node_if_781(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) < 30.0:
        return rt.call_node('_node_wt_cash_equal_757', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_780', prices)
rt.NODE_REGISTRY['_node_if_781'] = _node_if_781


def _node_wt_cash_equal_782(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_781', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_782'] = _node_wt_cash_equal_782


def _node_if_783(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['QQQ']) > rt.moving_average_price(prices['QQQ'], 20):
        return rt.call_node('_node_wt_cash_equal_755', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_782', prices)
rt.NODE_REGISTRY['_node_if_783'] = _node_if_783


def _node_wt_cash_equal_784(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_783', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_784'] = _node_wt_cash_equal_784


def _node_if_785(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) < 30.0:
        return rt.call_node('_node_wt_cash_equal_749', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_784', prices)
rt.NODE_REGISTRY['_node_if_785'] = _node_if_785


def _node_wt_cash_equal_786(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_785', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_786'] = _node_wt_cash_equal_786


def _node_if_787(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) < 30.0:
        return rt.call_node('_node_wt_cash_equal_747', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_786', prices)
rt.NODE_REGISTRY['_node_if_787'] = _node_if_787


def _node_wt_cash_equal_788(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_787', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_788'] = _node_wt_cash_equal_788


def _node_if_789(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['UVXY'], 10) > 74.0:
        return rt.call_node('_node_wt_cash_equal_745', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_788', prices)
rt.NODE_REGISTRY['_node_if_789'] = _node_if_789


def _node_wt_cash_equal_790(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_789', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_790'] = _node_wt_cash_equal_790


def _node_if_791(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) < 20.0:
        return rt.call_node('_node_wt_cash_equal_741', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_790', prices)
rt.NODE_REGISTRY['_node_if_791'] = _node_if_791


def _node_wt_cash_equal_792(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_791', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_792'] = _node_wt_cash_equal_792


def _node_if_793(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['SOXL'], 1) < -24.0:
        return rt.call_node('_node_asset_UVXY_739', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_792', prices)
rt.NODE_REGISTRY['_node_if_793'] = _node_if_793


def _node_wt_cash_equal_794(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_793', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_794'] = _node_wt_cash_equal_794


def _node_if_795(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 60) > 50.0:
        return rt.call_node('_node_asset_BIL_738', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_794', prices)
rt.NODE_REGISTRY['_node_if_795'] = _node_if_795


def _node_wt_cash_equal_796(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_795', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_796'] = _node_wt_cash_equal_796


def _node_if_797(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 60) > 55.0:
        return rt.call_node('_node_asset_BIL_737', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_796', prices)
rt.NODE_REGISTRY['_node_if_797'] = _node_if_797


def _node_wt_cash_equal_798(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_797', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_798'] = _node_wt_cash_equal_798


def _node_if_799(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 6) > 75.0:
        return rt.call_node('_node_asset_BIL_736', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_798', prices)
rt.NODE_REGISTRY['_node_if_799'] = _node_if_799


def _node_wt_cash_equal_800(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_799', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_800'] = _node_wt_cash_equal_800


def _node_if_801(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQ'], 10) > 75.0:
        return rt.call_node('_node_asset_BIL_735', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_800', prices)
rt.NODE_REGISTRY['_node_if_801'] = _node_if_801


def _node_wt_cash_equal_802(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_801', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_802'] = _node_wt_cash_equal_802


def _node_if_803(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) > 70.0:
        return rt.call_node('_node_asset_BIL_734', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_802', prices)
rt.NODE_REGISTRY['_node_if_803'] = _node_if_803


def _node_wt_cash_equal_804(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_803', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_804'] = _node_wt_cash_equal_804


def _node_if_805(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLP'], 10) > 75.0:
        return rt.call_node('_node_asset_UVXY_733', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_804', prices)
rt.NODE_REGISTRY['_node_if_805'] = _node_if_805


def _node_wt_cash_equal_806(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_805', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_806'] = _node_wt_cash_equal_806


def _node_if_807(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['UVXY'], 10) > 84.0:
        return rt.call_node('_node_asset_SOXL_732', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_806', prices)
rt.NODE_REGISTRY['_node_if_807'] = _node_if_807


def _node_wt_cash_equal_808(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_807', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_808'] = _node_wt_cash_equal_808


def _node_if_809(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['SPY']) > rt.moving_average_price(prices['SPY'], 200):
        return rt.call_node('_node_wt_cash_equal_731', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_808', prices)
rt.NODE_REGISTRY['_node_if_809'] = _node_if_809


def _node_wt_cash_equal_810(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_809', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_810'] = _node_wt_cash_equal_810


def _node_if_811(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['SOXL'], 5) < -57.0:
        return rt.call_node('_node_asset_SOXL_665', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_810', prices)
rt.NODE_REGISTRY['_node_if_811'] = _node_if_811


def _node_wt_cash_equal_812(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_811', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_812'] = _node_wt_cash_equal_812


def _node_if_813(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['SOXL'], 2) < -37.0:
        return rt.call_node('_node_asset_SOXL_664', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_812', prices)
rt.NODE_REGISTRY['_node_if_813'] = _node_if_813


def _node_wt_cash_equal_814(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_813', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_814'] = _node_wt_cash_equal_814


def _node_if_815(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.cumulative_return(prices['SOXL'], 1) < -31.0:
        return rt.call_node('_node_asset_SOXL_663', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_814', prices)
rt.NODE_REGISTRY['_node_if_815'] = _node_if_815


def _node_wt_cash_equal_816(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_815', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_816'] = _node_wt_cash_equal_816


def _node_if_817(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.moving_average_return(prices['QQQ'], 10) < -2.4:
        return rt.call_node('_node_asset_SOXL_662', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_816', prices)
rt.NODE_REGISTRY['_node_if_817'] = _node_if_817


def _node_wt_cash_equal_818(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_817', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_818'] = _node_wt_cash_equal_818


def _node_wt_cash_equal_819(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_818', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_819'] = _node_wt_cash_equal_819


def _node_asset_UVXY_820(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_820'] = _node_asset_UVXY_820


def _node_asset_UVXY_821(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_821'] = _node_asset_UVXY_821


def _node_asset_UVXY_822(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_822'] = _node_asset_UVXY_822


def _node_asset_UVXY_823(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_823'] = _node_asset_UVXY_823


def _node_asset_UVXY_824(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_824'] = _node_asset_UVXY_824


def _node_asset_UVXY_825(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_825'] = _node_asset_UVXY_825


def _node_asset_UVXY_826(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_826'] = _node_asset_UVXY_826


def _node_asset_UVXY_827(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_827'] = _node_asset_UVXY_827


def _node_wt_cash_equal_828(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_asset_UVXY_827', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_828'] = _node_wt_cash_equal_828


def _node_asset_UVXY_829(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_829'] = _node_asset_UVXY_829


def _node_asset_UVXY_830(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_830'] = _node_asset_UVXY_830


def _node_asset_UVXY_831(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'UVXY': 1.0}
rt.NODE_REGISTRY['_node_asset_UVXY_831'] = _node_asset_UVXY_831


def _node_asset_VIXM_832(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'VIXM': 1.0}
rt.NODE_REGISTRY['_node_asset_VIXM_832'] = _node_asset_VIXM_832


def _node_asset_SPXL_833(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SPXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SPXL_833'] = _node_asset_SPXL_833


def _node_if_834(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 21) > 30.0:
        return rt.call_node('_node_asset_VIXM_832', prices)
    else:
        return rt.call_node('_node_asset_SPXL_833', prices)
rt.NODE_REGISTRY['_node_if_834'] = _node_if_834


def _node_wt_cash_equal_835(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_834', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_835'] = _node_wt_cash_equal_835


def _node_wt_cash_equal_836(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_835', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_836'] = _node_wt_cash_equal_836


def _node_asset_TECL_837(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TECL': 1.0}
rt.NODE_REGISTRY['_node_asset_TECL_837'] = _node_asset_TECL_837


def _node_asset_SOXL_838(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_838'] = _node_asset_SOXL_838


def _node_asset_SPXL_839(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SPXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SPXL_839'] = _node_asset_SPXL_839


def _node_asset_TECL_840(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TECL': 1.0}
rt.NODE_REGISTRY['_node_asset_TECL_840'] = _node_asset_TECL_840


def _node_asset_SOXL_841(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SOXL': 1.0}
rt.NODE_REGISTRY['_node_asset_SOXL_841'] = _node_asset_SOXL_841


def _node_asset_SVIX_842(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SVIX': 1.0}
rt.NODE_REGISTRY['_node_asset_SVIX_842'] = _node_asset_SVIX_842


def _node_filter_843(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.relative_strength_index(prices['TECL'], 10), rt.call_node('_node_asset_TECL_840', prices)), (rt.relative_strength_index(prices['SOXL'], 10), rt.call_node('_node_asset_SOXL_841', prices)), (rt.relative_strength_index(prices['SVIX'], 10), rt.call_node('_node_asset_SVIX_842', prices))], 'bottom', int('1'))
rt.NODE_REGISTRY['_node_filter_843'] = _node_filter_843


def _node_wt_cash_equal_844(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_843', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_844'] = _node_wt_cash_equal_844


def _node_asset_SQQQ_845(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'SQQQ': 1.0}
rt.NODE_REGISTRY['_node_asset_SQQQ_845'] = _node_asset_SQQQ_845


def _node_asset_TLT_846(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'TLT': 1.0}
rt.NODE_REGISTRY['_node_asset_TLT_846'] = _node_asset_TLT_846


def _node_filter_847(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.select_filter([(rt.relative_strength_index(prices['SQQQ'], 10), rt.call_node('_node_asset_SQQQ_845', prices)), (rt.relative_strength_index(prices['TLT'], 10), rt.call_node('_node_asset_TLT_846', prices))], 'top', int('1'))
rt.NODE_REGISTRY['_node_filter_847'] = _node_filter_847


def _node_wt_cash_equal_848(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_filter_847', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_848'] = _node_wt_cash_equal_848


def _node_if_849(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLK'], 10) > rt.relative_strength_index(prices['KMLM'], 10):
        return rt.call_node('_node_wt_cash_equal_844', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_848', prices)
rt.NODE_REGISTRY['_node_if_849'] = _node_if_849


def _node_wt_cash_equal_850(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_849', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_850'] = _node_wt_cash_equal_850


def _node_wt_cash_equal_851(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_850', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_851'] = _node_wt_cash_equal_851


def _node_wt_cash_equal_852(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_851', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_852'] = _node_wt_cash_equal_852


def _node_if_853(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPXL'], 10) < 30.0:
        return rt.call_node('_node_asset_SPXL_839', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_852', prices)
rt.NODE_REGISTRY['_node_if_853'] = _node_if_853


def _node_wt_cash_equal_854(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_853', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_854'] = _node_wt_cash_equal_854


def _node_if_855(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SOXL'], 10) < 30.0:
        return rt.call_node('_node_asset_SOXL_838', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_854', prices)
rt.NODE_REGISTRY['_node_if_855'] = _node_if_855


def _node_wt_cash_equal_856(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_855', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_856'] = _node_wt_cash_equal_856


def _node_if_857(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TQQQ'], 10) < 30.0:
        return rt.call_node('_node_asset_TECL_837', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_856', prices)
rt.NODE_REGISTRY['_node_if_857'] = _node_if_857


def _node_wt_cash_equal_858(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_857', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_858'] = _node_wt_cash_equal_858


def _node_wt_cash_equal_859(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_858', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_859'] = _node_wt_cash_equal_859


def _node_if_860(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['UVXY'], 21) > 65.0:
        return rt.call_node('_node_wt_cash_equal_836', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_859', prices)
rt.NODE_REGISTRY['_node_if_860'] = _node_if_860


def _node_wt_cash_equal_861(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_860', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_861'] = _node_wt_cash_equal_861


def _node_wt_cash_equal_862(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_861', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_862'] = _node_wt_cash_equal_862


def _node_if_863(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['SPY'], 10) > 80.0:
        return rt.call_node('_node_asset_UVXY_831', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_862', prices)
rt.NODE_REGISTRY['_node_if_863'] = _node_if_863


def _node_wt_cash_equal_864(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_863', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_864'] = _node_wt_cash_equal_864


def _node_if_865(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['FAS'], 10) > 80.0:
        return rt.call_node('_node_asset_UVXY_830', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_864', prices)
rt.NODE_REGISTRY['_node_if_865'] = _node_if_865


def _node_wt_cash_equal_866(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_865', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_866'] = _node_wt_cash_equal_866


def _node_if_867(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLY'], 10) > 80.0:
        return rt.call_node('_node_asset_UVXY_829', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_866', prices)
rt.NODE_REGISTRY['_node_if_867'] = _node_if_867


def _node_wt_cash_equal_868(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_867', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_868'] = _node_wt_cash_equal_868


def _node_if_869(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TQQQ'], 10) > 79.0:
        return rt.call_node('_node_wt_cash_equal_828', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_868', prices)
rt.NODE_REGISTRY['_node_if_869'] = _node_if_869


def _node_wt_cash_equal_870(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_869', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_870'] = _node_wt_cash_equal_870


def _node_if_871(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['XLP'], 10) > 75.0:
        return rt.call_node('_node_asset_UVXY_826', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_870', prices)
rt.NODE_REGISTRY['_node_if_871'] = _node_if_871


def _node_wt_cash_equal_872(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_871', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_872'] = _node_wt_cash_equal_872


def _node_if_873(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IUSV'], 10) > 79.0:
        return rt.call_node('_node_asset_UVXY_825', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_872', prices)
rt.NODE_REGISTRY['_node_if_873'] = _node_if_873


def _node_wt_cash_equal_874(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_873', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_874'] = _node_wt_cash_equal_874


def _node_if_875(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IVW'], 10) > 79.0:
        return rt.call_node('_node_asset_UVXY_824', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_874', prices)
rt.NODE_REGISTRY['_node_if_875'] = _node_if_875


def _node_wt_cash_equal_876(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_875', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_876'] = _node_wt_cash_equal_876


def _node_if_877(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['TECL'], 10) > 79.0:
        return rt.call_node('_node_asset_UVXY_823', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_876', prices)
rt.NODE_REGISTRY['_node_if_877'] = _node_if_877


def _node_wt_cash_equal_878(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_877', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_878'] = _node_wt_cash_equal_878


def _node_if_879(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['VOX'], 10) > 79.0:
        return rt.call_node('_node_asset_UVXY_822', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_878', prices)
rt.NODE_REGISTRY['_node_if_879'] = _node_if_879


def _node_wt_cash_equal_880(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_879', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_880'] = _node_wt_cash_equal_880


def _node_if_881(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['VTV'], 10) > 79.0:
        return rt.call_node('_node_asset_UVXY_821', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_880', prices)
rt.NODE_REGISTRY['_node_if_881'] = _node_if_881


def _node_wt_cash_equal_882(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_881', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_882'] = _node_wt_cash_equal_882


def _node_if_883(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['QQQE'], 10) > 79.0:
        return rt.call_node('_node_asset_UVXY_820', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_882', prices)
rt.NODE_REGISTRY['_node_if_883'] = _node_if_883


def _node_wt_cash_equal_884(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_883', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_884'] = _node_wt_cash_equal_884


def _node_wt_cash_equal_885(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_884', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_885'] = _node_wt_cash_equal_885


def _node_asset_EDC_886(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDC': 1.0}
rt.NODE_REGISTRY['_node_asset_EDC_886'] = _node_asset_EDC_886


def _node_asset_BIL_887(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_887'] = _node_asset_BIL_887


def _node_wt_cash_specified_888(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('68') / float(100)), rt.call_node('_node_asset_EDC_886', prices)), ((float(32) / float(100)), rt.call_node('_node_asset_BIL_887', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_888'] = _node_wt_cash_specified_888


def _node_asset_EDC_889(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDC': 1.0}
rt.NODE_REGISTRY['_node_asset_EDC_889'] = _node_asset_EDC_889


def _node_asset_EDZ_890(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDZ': 1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_890'] = _node_asset_EDZ_890


def _node_if_891(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IEI'], 10) > rt.relative_strength_index(prices['IWM'], 15):
        return rt.call_node('_node_asset_EDC_889', prices)
    else:
        return rt.call_node('_node_asset_EDZ_890', prices)
rt.NODE_REGISTRY['_node_if_891'] = _node_if_891


def _node_wt_cash_equal_892(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_891', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_892'] = _node_wt_cash_equal_892


def _node_asset_EDC_893(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDC': 1.0}
rt.NODE_REGISTRY['_node_asset_EDC_893'] = _node_asset_EDC_893


def _node_asset_EDZ_894(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDZ': 1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_894'] = _node_asset_EDZ_894


def _node_if_895(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IGIB'], 15) > rt.relative_strength_index(prices['EEM'], 15):
        return rt.call_node('_node_asset_EDC_893', prices)
    else:
        return rt.call_node('_node_asset_EDZ_894', prices)
rt.NODE_REGISTRY['_node_if_895'] = _node_if_895


def _node_wt_cash_equal_896(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_895', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_896'] = _node_wt_cash_equal_896


def _node_asset_EDC_897(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDC': 1.0}
rt.NODE_REGISTRY['_node_asset_EDC_897'] = _node_asset_EDC_897


def _node_asset_EDZ_898(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDZ': 1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_898'] = _node_asset_EDZ_898


def _node_if_899(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IGIB'], 10) > rt.relative_strength_index(prices['SPY'], 10):
        return rt.call_node('_node_asset_EDC_897', prices)
    else:
        return rt.call_node('_node_asset_EDZ_898', prices)
rt.NODE_REGISTRY['_node_if_899'] = _node_if_899


def _node_wt_cash_equal_900(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_899', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_900'] = _node_wt_cash_equal_900


def _node_combine_equal_901(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_896', prices), rt.call_node('_node_wt_cash_equal_900', prices)])
rt.NODE_REGISTRY['_node_combine_equal_901'] = _node_combine_equal_901


def _node_if_902(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['EEM']) > rt.moving_average_price(prices['EEM'], 200):
        return rt.call_node('_node_wt_cash_equal_892', prices)
    else:
        return rt.call_node('_node_combine_equal_901', prices)
rt.NODE_REGISTRY['_node_if_902'] = _node_if_902


def _node_wt_cash_equal_903(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_902', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_903'] = _node_wt_cash_equal_903


def _node_asset_EDC_904(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDC': 1.0}
rt.NODE_REGISTRY['_node_asset_EDC_904'] = _node_asset_EDC_904


def _node_asset_EDZ_905(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDZ': 1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_905'] = _node_asset_EDZ_905


def _node_if_906(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IGIB'], 10) > rt.relative_strength_index(prices['SPY'], 10):
        return rt.call_node('_node_asset_EDC_904', prices)
    else:
        return rt.call_node('_node_asset_EDZ_905', prices)
rt.NODE_REGISTRY['_node_if_906'] = _node_if_906


def _node_wt_cash_equal_907(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_906', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_907'] = _node_wt_cash_equal_907


def _node_if_908(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.current_price(prices['SHV']) > rt.moving_average_price(prices['SHV'], 50):
        return rt.call_node('_node_wt_cash_equal_903', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_907', prices)
rt.NODE_REGISTRY['_node_if_908'] = _node_if_908


def _node_wt_cash_equal_909(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_908', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_909'] = _node_wt_cash_equal_909


def _node_if_910(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['EEM'], 10) < 25.0:
        return rt.call_node('_node_wt_cash_specified_888', prices)
    else:
        return rt.call_node('_node_wt_cash_equal_909', prices)
rt.NODE_REGISTRY['_node_if_910'] = _node_if_910


def _node_wt_cash_equal_911(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_910', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_911'] = _node_wt_cash_equal_911


def _node_wt_cash_equal_912(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_wt_cash_equal_911', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_912'] = _node_wt_cash_equal_912


def _node_asset_EDC_913(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDC': 1.0}
rt.NODE_REGISTRY['_node_asset_EDC_913'] = _node_asset_EDC_913


def _node_asset_BIL_914(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_914'] = _node_asset_BIL_914


def _node_wt_cash_specified_915(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('68') / float(100)), rt.call_node('_node_asset_EDC_913', prices)), ((float(32) / float(100)), rt.call_node('_node_asset_BIL_914', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_915'] = _node_wt_cash_specified_915


def _node_asset_EEM_916(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EEM': 1.0}
rt.NODE_REGISTRY['_node_asset_EEM_916'] = _node_asset_EEM_916


def _node_asset_EDZ_917(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EDZ': 1.0}
rt.NODE_REGISTRY['_node_asset_EDZ_917'] = _node_asset_EDZ_917


def _node_asset_BIL_918(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'BIL': 1.0}
rt.NODE_REGISTRY['_node_asset_BIL_918'] = _node_asset_BIL_918


def _node_wt_cash_specified_919(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_weighted([((float('33') / float(100)), rt.call_node('_node_asset_EDZ_917', prices)), ((float(67) / float(100)), rt.call_node('_node_asset_BIL_918', prices))])
rt.NODE_REGISTRY['_node_wt_cash_specified_919'] = _node_wt_cash_specified_919


def _node_if_920(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    if rt.relative_strength_index(prices['IEI'], 10) > rt.relative_strength_index(prices['IWM'], 15):
        return rt.call_node('_node_asset_EEM_916', prices)
    else:
        return rt.call_node('_node_wt_cash_specified_919', prices)
rt.NODE_REGISTRY['_node_if_920'] = _node_if_920


def _node_wt_cash_equal_921(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.combine_equal([rt.call_node('_node_if_920', prices)])
rt.NODE_REGISTRY['_node_wt_cash_equal_921'] = _node_wt_cash_equal_921


def _node_asset_EEM_922(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return {'EEM': 1.0}
rt.NODE_REGISTRY['_node_asset_EEM_922'] = _node_asset_EEM_922

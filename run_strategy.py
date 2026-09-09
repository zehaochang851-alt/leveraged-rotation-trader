from typing import Dict, Sequence
import strategy_runtime as rt
import weathervane_part_0, weathervane_part_1, weathervane_part_2, weathervane_part_3, weathervane_part_4  # noqa: F401

def run_strategy(prices: Dict[str, Sequence[float]]) -> Dict[str, float]:
    return rt.call_node('_node_wt_cash_equal_952', prices)

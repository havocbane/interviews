from typing import List, Tuple, Union

NO_SOLUTION = 'No Solution'


def stocks_best_buy(prices: List[float]) -> Union[Tuple[float, float], str]:
    if len(prices) < 2:
        return NO_SOLUTION
    buy = sell = prices[0]
    potential_buy = None
    for i, price in enumerate(prices[1:]):
        if price > sell:
            sell = price
            if potential_buy:
                buy = potential_buy
                potential_buy = None
        elif price < buy:
            potential_buy = price
    if buy == sell:
        return NO_SOLUTION
    return buy, sell

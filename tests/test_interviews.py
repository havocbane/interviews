from itertools import chain

from interviews import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_stocks_best_buy_empty():
    from interviews.stocks import stocks_best_buy
    # Given an empty list of stock prices,
    prices = []
    # when we look for the best buy/sell,
    result = stocks_best_buy(prices)
    # then we get no solution.
    assert result == 'No Solution'


def test_stocks_best_buy_single_price():
    from interviews.stocks import stocks_best_buy
    # Given a list containing a single stock price,
    prices = [
        10.0,
    ]
    # when we look for the best buy/sell,
    result = stocks_best_buy(prices)
    # then we get no solution.
    assert result == 'No Solution'


def test_stocks_best_buy_plateau():
    from interviews.stocks import stocks_best_buy
    # Given a plateau of stock prices,
    prices = [
        float(10) for _ in range(10)
    ]
    # when we look for the best buy/sell,
    result = stocks_best_buy(prices)
    # then we get no solution.
    assert result == 'No Solution'


def test_stocks_best_buy_cliff():
    from interviews.stocks import stocks_best_buy
    # Given a stock price cliff,
    prices = [
        float(i) for i in range(10, 0, -1)
    ]
    # when we look for the best buy/sell,
    result = stocks_best_buy(prices)
    # then we get no solution.
    assert result == 'No Solution'


def test_stocks_best_buy_plateau_to_cliff():
    from interviews.stocks import stocks_best_buy
    # Given a stock price cliff following a plateau,
    prices = list(chain(
        [float(10) for _ in range(5)],
        [float(i) for i in range(9, 4, -1)],
    ))
    # when we look for the best buy/sell,
    result = stocks_best_buy(prices)
    # then we get no solution.
    assert result == 'No Solution'

# TODO cliff to plateau


def test_stocks_best_buy_hill():
    from interviews.stocks import stocks_best_buy
    # Given a stock price hill,
    prices = [
        float(i) for i in range(1, 11, 1)
    ]
    # when we look for the best buy/sell,
    result = stocks_best_buy(prices)
    # then we get the first price and the last price.
    assert result == (1.0, 10.0,)

# TODO hill to plateau
# TODO plateau to hill
# TODO cliff to hill
# TODO hill to cliff
# TODO hill to plateau to cliff
# TODO cliff to plateau to hill
# TODO More random tests

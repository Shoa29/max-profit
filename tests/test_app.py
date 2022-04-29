import datetime

from app import getQuotes, calcProfit

#global variables
test_res = []

def test_period_inbound():
    """
    Test to check api request status
    :return:
    """
    global test_res
    today = datetime.datetime.today()
    start = today - datetime.timedelta(days=365)
    test_start = start.strftime("%Y-%m-%d")
    test_end = today.strftime("%Y-%m-%d")
    test_res = getQuotes(test_start, test_end).json()
    assert getQuotes(test_start, test_end).status_code == 200



def test_dates():
    """
    Test that buy date calculated is lower than sell date
    :return:
    """
    buy, sell= calcProfit(test_res)
    buy_date = datetime.datetime.strptime(buy, "%Y-%m-%d")
    sell_date = datetime.datetime.strptime(sell, "%Y-%m-%d")
    assert buy_date<=sell_date
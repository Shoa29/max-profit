import datetime
import pytest
from upflex.app import getQuotes, calcProfit

#global variables
test_res = []

@pytest.mark.getQuotes
def test_period_inbound():
    global test_res
    today = datetime.datetime.today()
    end = today - datetime.timedelta(days=365)
    test_start = today.strftime("%Y-%m-%d")
    test_end = end.strftime("%Y-%m-%d")
    test_res = getQuotes(test_start, test_end).json()
    assert getQuotes(test_start, test_end).status_code == 200

@pytest.mark.getQuotes
def test_period_outbound():
    today = datetime.datetime.today()
    end = today - datetime.timedelta(days=1825)
    test_start = today.strftime("%Y-%m-%d")
    test_end = end.strftime("%Y-%m-%d")
    assert getQuotes(test_start, test_end) != 200

@pytest.mark.calcProfit
def test_dates():
    buy, sell= calcProfit(test_res)
    buy_date = datetime.datetime.strptime(buy, "%Y-%m-%d")
    sell_date = datetime.datetime.strptime(sell, "%Y-%m-%d")
    assert buy_date<=sell_date
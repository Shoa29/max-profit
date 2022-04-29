import datetime
import pytest
from upflex.app import getQuotes

@pytest.mark.requests
def test_getQuotes():
    today = datetime.datetime.today()
    end = today - datetime.timedelta(days=365)
    test_start = today.strftime("%Y-%m-%d")
    test_end = end.strftime("%Y-%m-%d")
    assert getQuotes(test_start, test_end) == 200

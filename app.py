import requests
from typing import List
import datetime

#global variables
min_price = 999999
max_profit = -1
buy_date = ""
sell_date = ""
ENDPOINT = "http://api.nbp.pl/api/cenyzlota/"
AMOUNT = 135000

def calcProfit(quotes: List)-> None:
    """
    Function to calculate dates to invest on to yield maximum profit

    :param quotes: list of daily gold price
    :return: None
    """
    global min_price, max_profit, buy_date, sell_date
    if min_price > quotes[0]['cena']:
        min_price = quotes[0]['cena']
        buy_date = quotes[0]['data']
    if max_profit < 0:
        max_profit = quotes[1]['cena'] - quotes[0]['cena']
        sell_date = quotes[0]['data']
    for i in range(1,len(quotes)):
        temp_dif = quotes[i]['cena'] - min_price
        if temp_dif > max_profit:
            max_profit = temp_dif
            sell_date = quotes[i]['data']
        if quotes[i]['cena'] < min_price:
            min_price = quotes[i]['cena']
            buy_date = quotes[i]['data']
    return


def getQuotes(start_date:str, end_date:str)-> None:
    """
    Get request to the API

    :param start_date: starting date to get gold price quotes from
    :param end_date: ending date
    :return: None
    """
    url = ENDPOINT + start_date + "/" + end_date
    try:
        res = requests.get(url)
        calcProfit(res.json())
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)



if __name__ == '__main__':
    today = datetime.datetime.today()
    end_itr = today - datetime.timedelta(days=1460)
    while end_itr <= today:
        start_itr = end_itr - datetime.timedelta(days=365)
        start_date = start_itr.strftime("%Y-%m-%d")
        end_date = end_itr.strftime("%Y-%m-%d")
        getQuotes(start_date,end_date)
        end_itr += datetime.timedelta(days=365)
    sell_price = max_profit + min_price
    units = int(AMOUNT/min_price)
    max_profit = units*max_profit
    print(f'Best date to BUY: {buy_date}')
    print(f'Number of Units of Gold bought: {units} At PRICE: {min_price} USD')
    print(f'Best date to SELL: {sell_date} At PRICE: {sell_price} USD')
    print(f'TOTAL PROFIT GAINED: {max_profit:.2f} USD')

from polygon import RESTClient
import constants

ticker = 'AAPL'
multiplier = 5
timeframe = 'minute'
startdate = '2025-02-14'
enddate = '2025-02-14'

def createclient():

    client = RESTClient(constants.API_KEY)
    return client

def get_aggs(client):

    aggs = client.get_aggs(
        ticker,
        multiplier,
        timeframe,
        startdate,
        enddate 
    )
    return aggs

def sort_agg(aggs):
    aggs_srtd = sorted(aggs, key=lambda x: x.high,  reverse=True)
    aggs_bkwd = sorted(aggs, key=lambda x: x.low)
    high_price = aggs_srtd[0].high
    low_price = aggs_bkwd[0].low
    print(ticker)
    print(high_price)
    print('\n')


def print_tickers():
    for t in constants.TICKERS:

        print(t)

def get_highs(client):
    
    for t in constants.TICKERS:

        global ticker
        ticker = t
        # print({ticker})
        sort_agg(get_aggs(client))
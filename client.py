from polygon import RESTClient
import confs
import json

ticker = 'AAPL'
multiplier = 5
timeframe = 'minute'
startdate = '2025-02-14'
enddate = '2025-02-14'

def createclient():

    client = RESTClient(confs.API_KEY)
    return client

def get_aggs(client):

    aggs = client.get_aggs(
        ticker,
        multiplier,
        timeframe,
        startdate,
        enddate 
    )

    aggs_srtd = sorted(aggs, key=lambda x: x.high,  reverse=True)
    aggs_bkwd = sorted(aggs, key=lambda x: x.low)
    high_price = aggs_srtd[0].high
    low_price = aggs_bkwd[0].low
    print(high_price)
    print('\n')
    print(aggs_srtd[0])
    print(aggs_srtd[1])
    print(aggs_srtd[2])
    print(aggs_srtd[3])
    print(aggs_srtd[4])
    print(aggs_srtd[5])
    print('\n')
    print(low_price)
    print('\n')
    print(aggs_bkwd[0])
    print(aggs_bkwd[1])
    print(aggs_bkwd[2])
    print(aggs_bkwd[3])
    print(aggs_bkwd[4])
    print(aggs_bkwd[5])


def get_tickers(client):
    pass
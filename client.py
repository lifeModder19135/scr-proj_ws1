from polygon import RESTClient
import confs

ticker = 'AAPL'
multiplier = 5
timeframe = 'minute'
startdate = '2025-02-14'
enddate = '2025-02-14'

def createclient():

    client = RESTClient(confs.API_KEY)

    aggs = client.get_aggs(
        ticker,
        multiplier,
        timeframe,
        startdate,
        enddate 
    )

    print(aggs)
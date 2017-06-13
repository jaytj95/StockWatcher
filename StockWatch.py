import time
import datetime
from yahoo_finance import Share

print 'Welcome to StockWatch'
delay_s = 300;
stockWatchList = ['AMZN']
# times work only in Pacific, matched to NASDAQ opening times: http://www.insider-monitor.com/market-hours.php
market_start = datetime.time(8, 00);
market_end = datetime.time(23, 50);
while True:
    current_time = datetime.datetime.now().time()
    print (market_start <= current_time <= market_end)
    print 'Current time is: ' + current_time.__str__()

    print 'Running through items in stock watch list'
    for ticker in stockWatchList:
        stockInfo = Share(ticker)
        print stockInfo.get_price()
    print 'resting...' + (delay_s/60).__str__() + ' mins'
    time.sleep(delay_s);

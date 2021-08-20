from datetime import date
from nsepy import get_history
import pandas as pd

names = ['ACC', 'ADANIPORTS', 'ADANITRANS', 'AMBUJACEM', 'ASHOKLEY', 'ASIANPAINT', 'AUROPHARMA', 'DMART', 'AXISBANK',
         'BAJAJ-AUTO', 'BAJFINANCE', 'BAJAJFINSV', 'BAJAJHLDNG', 'BANDHANBNK', 'BANKBARODA', 'BERGEPAINT', 'BPCL',
         'BHARTIARTL', 'INFRATEL', 'BIOCON', 'BOSCHLTD', 'BRITANNIA', 'CADILAHC', 'CIPLA', 'COALINDIA', 'COLPAL',
         'CONCOR', 'DLF', 'DABUR', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GAIL', 'GICRE',
         'GODREJCP', 'GRASIM', 'HCLTECH', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HAVELLS', 'HEROMOTOCO', 'HINDALCO',
         'HINDPETRO', 'HINDUNILVR', 'HINDZINC', 'HDFC', 'ICICIBANK', 'ICICIGI', 'ICICIPRULI', 'ITC', 'IBULHSGFIN',
         'IOC', 'INDUSINDBK', 'INFY', 'INDIGO', 'JSWSTEEL', 'KOTAKBANK', 'L&TFH', 'LT', 'LUPIN', 'M&M', 'MARICO', 'MARUTI', 'MOTHERSUMI', 'NHPC', 'NMDC', 'NTPC', 'NESTLEIND', 'ONGC', 'OFSS', 'PAGEIND', 'PETRONET', 'PIDILITIND', 'PEL', 'PFC', 'POWERGRID', 'PGHH', 'PNB', 'RELIANCE', 'SBILIFE', 'SHREECEM', 'SRTRANSFIN', 'SIEMENS', 'SBIN',
         'SUNPHARMA', 'TCS', 'TATAMTRDVR', 'TATAMOTORS', 'TATASTEEL', 'TECHM', 'NIACL', 'TITAN', 'UPL', 'ULTRACEMCO',
         'UBL', 'MCDOWELL-N', 'VEDL', 'IDEA', 'WIPRO', 'ZEEL']
today = str(date.today())
numb = list(map(int,today.split("-")))
window_small = 10
window_large = 20
for i in names:
    company = get_history(symbol=i,start=date(2020,5,1),end=date(numb[0],numb[1],numb[2]))
    emas = []
    emal = []
    emas = list(company['Close'].ewm(span = window_small).mean())
    emal = list(company['Close'].ewm(span = window_large).mean())
    l = len(emal)
    for j in range(20,l):
        if(emas[j-1] <= emal[j-1] and emas[j] > emal[j]):
            print(i)
            print(company.index[j], company['Close'][j], "Yes, buy it")
        if(emas[j-1] >= emal[j-1] and emas[j] < emal[j]):
            print(i)
            print(company.index[j], company['Close'][j], "Sell it")

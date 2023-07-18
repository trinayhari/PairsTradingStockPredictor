import mysql.connector
from mysql.connector import Error
import numpy as np
import pandas as pd
import yfinance as yf
# import pyodbc
import sqlite3

try:
    con = sqlite3.connect('SQLite_Python.db')
    curs = con.cursor()
    print("Database created and Successfully Connected to SQLite")

    curs.execute('''CREATE TABLE IF NOT EXISTS large_market_cap_tickers (
        id INTEGER, ticker TEXT )''')

    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'TSLA', 'META', 'AVGO', 'PEP', 'COST', 'ADBE', 'CSCO', 'AZN', 'NFLX']

    for ticker in tickers:
      curs.execute('INSERT INTO large_market_cap_tickers (ticker) VALUES (?)', (ticker,))

    con.commit()

    curs.execute('SELECT ticker FROM large_market_cap_tickers')
    print("Tickers in large_market_cap_tickers table:")
    for row in curs.fetchall():
        print(row[0])
      


    sqlite_select_Query = "select sqlite_version();"
    curs.execute(sqlite_select_Query)
    record = curs.fetchall()
    print("SQLite Database Version is: ", record)
    curs.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if con:
        con.close()
        print("The SQLite connection is closed")

        
        
      
'''
server = 'tcp:mysqlserver42069.database.windows.net' 
database = 'myStockPredictorDatabase'
username = 'azureuser' 
password = 'StockPredictor123!'
driver = '{ODBC Driver 17 for SQL Server}'

try:
    cnxn = pyodbc.connect('DRIVER=' + driver + 
                      ';SERVER=' + server + 
                      ';DATABASE=' + database + 
                      ';UID=' + username + 
                      ';PWD=' + password)

    cursor = cnxn.cursor()
    print('Connection established')
except:
    print('Cannot connect to SQL server')

'''

# def stocks(stock1,stock2):

#   df = pd.DataFrame()
#   df = yf.download(stock1, start="2023-6-7", end="2023-7-7", interval='15m',progress=False)
#   df.iloc[:,:]
  
#   df1 = pd.DataFrame()
#   df1 = yf.download(stock2, start="2023-6-7", end="2023-7-7", interval='15m',progress=False)
#   df1.iloc[:,:]
  
  
#   r = df['Close'].corr(df1['Close'])

#   return r
  
# large_market_cap = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "TSLA", "META", "AVGO", "PEP", "COST", "ADBE", "CSCO", "AZN", "NFLX"]
# medium_market_cap = ["AMD", "CMCSA", "TMUS", "TXN", "HON", "INTC", "QCOM", "SNY", "INTU", "AMAT", "AMGN", "ISRG", "SBUX", "MDLZ", "BKNG", "PDD", "ADI", "GILD", "ADP", "VRTX", "LRCX"]
# small_market_cap = ["ABNB", "PANW", "REGN", "PYPL", "EQIX", "CSX", "MU", "SNPS", "CME", "ATVI", "KLAC", "NTES", "CDNS", "FTNT", "MNST", "MELI", "WDAY", "ORLY", "MAR", "JD", "CHTR", "NXPI", "MRVL", "ROP", "BIDU", "DXCM", "CTAS", "MCHP", "LULU", "MRNA", "KDP", "TEAM", "KHC", "AEP", "ADSK", "PCAR", "IDXX", "PAYX", "EXC", "ODFL", "ON", "BIIB", "TTD", "ROST", "GEHC", "SGEN", "IBKR", "CSGP", "EA", "LI", "XEL", "GFS", "CRWD", "BKR", "CTSH", "FAST", "MBLY", "VRSK", "DLTR", "DDOG", "WBD", "CEG", "CCEP"]

# def loop(list):
  
#   max = 0
#   z = 0
#   stock1 = "" 
#   stock2 = ""
#   for x in list:
#     for y in list:
#       z = stocks(x,y)
#       if z>max and x!=y:
#         max = z
#         stock1 = x
#         stock2 = y
#   print(max)
#   print(stock1 + ","+ stock2)


# loop(large_market_cap)
# loop(medium_market_cap)
# loop(small_market_cap)






## NOTE: After using database, run the three loops and write program to analyze between the remaining 6 stocks

'''
def compare(s1,s2):
  
  ticker1 = yf.Ticker(s1)
  historical_data = ticker1.history(period='1mo')
  first_close = historical_data['Close'][0]
  last_close = historical_data['Close'][-1]
  price_change_percentage1 = ((last_close - first_close) / first_close) * 100 
  print(price_change_percentage1)
  
  ticker2 = yf.Ticker(s2)
  historical_data = ticker2.history(period='1mo')
  first_close = historical_data['Close'][0]
  last_close = historical_data['Close'][-1]
  price_change_percentage2 = ((last_close - first_close) / first_close) * 100 
  print(price_change_percentage2)
  
  if((price_change_percentage1 and price_change_percentage2) > 0):
    if(price_change_percentage1>price_change_percentage2):
      print("Buy " + s2)
    elif(price_change_percentage1<price_change_percentage2):
      print("Buy " + s1)
  
  if((price_change_percentage1 and price_change_percentage2) < 0):
    print("Don't Buy any stock. Not a Bullish market.")
    

compare(stock1,stock2)

'''



'''
  msft= yf.Ticker("MSFT")
  print(msft.info['sector'])

Screener
  s = Screener()
  
  # data is a dictionary containing the keys passed to the function
  data = s.get_screeners('ms_technology', count=25)
  
  # the majority of the data will be in the quotes key
  data['ms_technology']['quotes'][0]
  
  df = pd.DataFrame(data['ms_technology']['quotes'])
  
  data = s.get_screeners(['ms_technology', 'ms_utilities', 'ms_real_estate'])
  
  s.available_screeners

'''
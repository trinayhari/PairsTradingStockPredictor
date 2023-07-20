import mysql.connector
from mysql.connector import Error
import numpy as np
import pandas as pd
import yfinance as yf
import sqlite3

def createtables():
  try:
      con = sqlite3.connect('SQLite_Python.db')
      curs = con.cursor()
      print("Database created and Successfully Connected to SQLite")

      # Large Market Cap Tickers
      curs.execute('''CREATE TABLE IF NOT EXISTS tickers (
          id INTEGER, ticker TEXT )''')

      tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'TSLA', 'META', 'AVGO', 'PEP', 'COST', 'ADBE', 'CSCO', 'AZN', 'NFLX','AMD', 'CMCSA', 'TMUS', 'TXN', 'HON', 'INTC', 'QCOM', 'SNY', 'INTU', 'AMAT', 'AMGN', 'ISRG', 'SBUX', 'MDLZ', 'BKNG', 'PDD', 'ADI', 'GILD', 'ADP', 'VRTX', 'LRCX','ABNB', 'PANW', 'REGN', 'PYPL', 'EQIX', 'CSX', 'MU', 'SNPS', 'CME', 'ATVI', 'KLAC', 'NTES', 'CDNS', 'FTNT', 'MNST', 'MELI', 'WDAY', 'ORLY', 'MAR', 'JD', 'CHTR', 'NXPI', 'MRVL', 'ROP', 'BIDU', 'DXCM', 'CTAS', 'MCHP', 'LULU', 'MRNA', 'KDP', 'TEAM', 'KHC', 'AEP', 'ADSK', 'PCAR', 'IDXX', 'PAYX', 'EXC', 'ODFL', 'ON', 'BIIB', 'TTD', 'ROST', 'GEHC', 'SGEN', 'IBKR', 'CSGP', 'EA', 'LI', 'XEL', 'GFS', 'CRWD', 'BKR', 'CTSH', 'FAST', 'MBLY', 'VRSK', 'DLTR', 'DDOG', 'WBD', 'CEG', 'CCEP']

      for ticker in tickers:
        curs.execute('INSERT INTO tickers (ticker) VALUES(?)', (ticker,))

      con.commit()

      curs.execute('SELECT ticker FROM tickers')
      print("Tickers in tickers table:")
      for row in curs.fetchall():
          print(row[0])

  except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
  finally:
      if con:
          con.close()
          print("The SQLite connection is closed")   

def stocks(stock1,stock2):

  df = pd.DataFrame()
  df = yf.download(stock1, start="2023-6-19", end="2023-7-19", interval='15m',progress=False)
  df.iloc[:,:]
  
  df1 = pd.DataFrame()
  df1 = yf.download(stock2, start="2023-6-19", end="2023-7-19", interval='15m',progress=False)
  df1.iloc[:,:]
  
  
  r = df['Close'].corr(df1['Close'])

  return r



def loop():

  con = sqlite3.connect('SQLite_Python.db')
  curs = con.cursor()
  max = 0
  z = 0
  stock1 = "" 
  stock2 = ""
  list = curs.execute("SELECT * FROM tickers;").fetchall()
  for x in list:
    for y in list:
      z = stocks(x,y)
      if z>max and x!=y:
        max = z
        stock1 = x
        stock2 = y
    print(max)
    print(stock1 + ","+ stock2)



loop()




# def compare(s1,s2):
  
#   ticker1 = yf.Ticker(s1)
#   historical_data = ticker1.history(period='1mo')
#   first_close = historical_data['Close'][0]
#   last_close = historical_data['Close'][-1]
#   price_change_percentage1 = ((last_close - first_close) / first_close) * 100 
#   print(price_change_percentage1)
  
#   ticker2 = yf.Ticker(s2)
#   historical_data = ticker2.history(period='1mo')
#   first_close = historical_data['Close'][0]
#   last_close = historical_data['Close'][-1]
#   price_change_percentage2 = ((last_close - first_close) / first_close) * 100 
#   print(price_change_percentage2)
  
#   if((price_change_percentage1 and price_change_percentage2) > 0):
#     if(price_change_percentage1>price_change_percentage2):
#       print("Buy " + s2)
#     elif(price_change_percentage1<price_change_percentage2):
#       print("Buy " + s1)
  
#   if((price_change_percentage1 and price_change_percentage2) < 0):
#     print("Don't Buy any stock. Not a Bullish market.")
    

# compare(stock1,stock2)

# '''



# '''
#   msft= yf.Ticker("MSFT")
#   print(msft.info['sector'])

# Screener
#   s = Screener()
  
#   # data is a dictionary containing the keys passed to the function
#   data = s.get_screeners('ms_technology', count=25)
  
#   # the majority of the data will be in the quotes key
#   data['ms_technology']['quotes'][0]
  
#   df = pd.DataFrame(data['ms_technology']['quotes'])
  
#   data = s.get_screeners(['ms_technology', 'ms_utilities', 'ms_real_estate'])
  
#   s.available_screeners


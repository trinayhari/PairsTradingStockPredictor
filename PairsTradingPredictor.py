
import numpy as np
import pandas as pd
import yfinance as yf
from flask import Flask, render_template, request

Tech = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'TSLA', 'META', 'AVGO', 'PEP', 'COST', 'ADBE', 'CSCO', 'AZN', 'NFLX','AMD', 'CMCSA', 'TMUS', 'TXN', 'HON', 'INTC', 'QCOM', 'SNY', 'INTU', 'AMAT', 'AMGN', 'ISRG', 'SBUX', 'MDLZ', 'BKNG', 'PDD', 'ADI', 'GILD', 'ADP', 'VRTX', 'LRCX','ABNB', 'PANW', 'REGN', 'PYPL', 'EQIX', 'CSX', 'MU', 'SNPS', 'CME', 'ATVI', 'KLAC', 'NTES', 'CDNS', 'FTNT', 'MNST', 'MELI', 'WDAY', 'ORLY', 'MAR', 'JD', 'CHTR', 'NXPI', 'MRVL', 'ROP', 'BIDU', 'DXCM', 'CTAS', 'MCHP', 'LULU', 'MRNA', 'KDP', 'TEAM', 'KHC', 'AEP', 'ADSK', 'PCAR', 'IDXX', 'PAYX', 'EXC', 'ODFL', 'ON', 'BIIB', 'TTD', 'ROST', 'GEHC', 'SGEN', 'IBKR', 'CSGP', 'EA', 'LI', 'XEL', 'GFS', 'CRWD', 'BKR', 'CTSH', 'FAST', 'MBLY', 'VRSK', 'DLTR', 'DDOG', 'WBD', 'CEG', 'CCEP']
Materials = ['LIN', 'BHP', 'BHPLF', 'RTNTF', 'RTPPF', 'RIO', 'AIQUY', 'AIQUF', 'GLCNF', 'GLNCY', 'SHW', 'APD', 'VALE', 'CTA-PB', 'SHECY', 'SHECF', 'SCCO', 'FCX', 'ECL', 'CTA-PA', 'FSUMF', 'FSUGY', 'SXYAY', 'BASFY', 'BFFAF', 'SKFOF', 'ZIJMF', 'AAUKF', 'NUE', 'NGLOY', 'CRHCF', 'CRH', 'GMBXF', 'PKX', 'CTVA', 'HCMLF', 'HCMLY', 'DOW', 'DD', 'NEM', 'PPG', 'NTR', 'GVDBF', 'GVDNY', 'LYB', 'GOLD', 'VMC', 'FNV', 'MLM', 'AEM', 'KLBAY', 'SLMNP', 'ALB', 'MT', 'TECK', 'IFF', 'SQM', 'NPSCY', 'WPM', 'NPPHY', 'ANFGF', 'FQVLF', 'STLD', 'CMCLF', 'UPMMY', 'AHCHY', 'UPMKF', 'RS', 'WLK', 'AHCHF', 'NCMGY', 'NCMGF', 'CF', 'HLBZF', 'GNENY', 'AVTR', 'GNENF', 'SYIEY', 'SYIEF', 'HDELY', 'GFIOF', 'AKZOY', 'GFI', 'AKZOF', 'NVZMF', 'NVZMY', 'CE', 'ANGPY', 'NHYDY', 'MOS', 'NHYKF', 'JHX', 'SLVYY', 'SUZ', 'IVPAF', 'RPM', 'SOUHY', 'BNTGF', 'FMC', 'SHTLF']
Financials = ['BRK-A', 'BRK-B', 'JPM', 'V', 'MA', 'JPM-PC', 'JPM-PD', 'BAC', 'BAC-PK', 'BAC-PL', 'BML-PG', 'BML-PH', 'BML-PL', 'BAC-PE', 'BML-PJ', 'BAC-PB', 'IDCBY', 'WFC-PQ', 'WFC-PY', 'WFC-PR', 'WFC-PL', 'HDB', 'WFC', 'MS', 'ACGBY', 'HSBC', 'C-PJ', 'HBCYF', 'CICHY', 'CICHF', 'RY', 'SPGI', 'GS', 'BACHY', 'BACHF', 'CMWAY', 'BX', 'WFC-PC', 'PNGAY', 'AXP', 'PIAIF', 'TD', 'SCHW', 'C', 'CIHKY', 'BLK', 'AAIGF', 'AAGIY', 'CILJF', 'ALIZY', 'ALIZF', 'MMC', 'RY-PT', 'MBFJF', 'MUFG', 'GS-PJ', 'IBN', 'GS-PK', 'MS-PF', 'MS-PI', 'BNPQY', 'PYPL', 'BNPQF', 'CB', 'MS-PK', 'MS-PE', 'PBCRF', 'USB-PH', 'PBCRY', 'GS-PA', 'MS-PA', 'GS-PD', 'ZFSVF', 'ZURVY', 'PGR', 'SBKFF', 'UBS', 'AON', 'USB-PP', 'AXAHY', 'CME', 'AXAHF', 'KKR', 'MCO', 'ICE', 'PSTVY', 'DBSDY', 'DBSDF', 'SAN', 'BCDRF', 'IVSBF', 'BNS', 'LNSTY', 'BMO', 'SMFNF', 'LDNXF', 'SMFG', 'ITUB', 'USB', 'UNCFF']
Energy = ['XOM', 'CVX', 'SHEL', 'RYDAF', 'PCCYF', 'PBMRF', 'TTE', 'TTFNF', 'COP', 'BP', 'BPAQF', 'SNPMF', 'STOHF', 'EQNR', 'PBR', 'PBR-A', 'SLB', 'ENB', 'EOG', 'EBBNF', 'CSUAY', 'CUAEF', 'CNQ', 'EPD', 'PEXNY', 'OXY', 'MPC', 'PXD', 'E', 'PSX', 'WOPEF', 'EIPAF', 'WDS', 'HES', 'VLO', 'ET', 'WMB', 'KMI', 'SU', 'LNG', 'TRP', 'BKR', 'MPLX', 'HAL', 'CVE', 'DVN', 'NTOIY', 'NTOIF', 'IMO', 'OKE', 'FANG', 'CQP', 'EC', 'CTRA', 'REPYY', 'TS', 'TRGP', 'IPXHY', 'SSLZY', 'AKRBF', 'TRMLF', 'PBA', 'STOSF', 'YZCAY', 'IPXHF', 'MRO', 'OMVKY', 'OMVJF', 'CCJ', 'EQT', 'MMP', 'CCOZF', 'YPF', 'APA', 'IEP', 'OVV', 'TPL', 'CHK', 'WES', 'OGFGY', 'PAA', 'GLPEY', 'GLPEF', 'DINO', 'MGYOY', 'AETUF', 'FTI', 'CSAN', 'HESM', 'PTRRY', 'NOV', 'AR', 'RRC', 'VARRY', 'NE', 'CHX', 'SWN', 'KLYCY', 'MTDR', 'MUR']
Healthcare = ['UNH', 'JNJ', 'LLY', 'NVO', 'NONOF', 'MRK', 'RHHBF', 'RHHBY', 'RHHVF', 'ABBV', 'NVS', 'NVSEF', 'TMO', 'AZNCF', 'AZN', 'PFE', 'ABT', 'DHR', 'SNY', 'BMY', 'SNYNF', 'AMGN', 'MDT', 'ISRG', 'ELV', 'SYK', 'CVS', 'GILD', 'VRTX', 'CSLLY', 'ESLOY', 'ZTS', 'CI', 'ESLOF', 'CMXHF', 'BDX', 'REGN', 'HCA', 'MKGAF', 'MKKGY', 'GLAXF', 'BSX', 'GSK', 'SMMNY', 'SEMHF', 'HUM', 'BAYRY', 'EW', 'BAYZF', 'DSNKY', 'MCK', 'DSKYF', 'DXCM', 'TKPHF', 'TAK', 'CHGCY', 'MRNA', 'IDXX', 'IQV', 'LZAGY', 'LZAGF', 'ALC', 'HLN', 'HOCPY', 'HLNCF', 'BIIB', 'ABC', 'CNC', 'A', 'GEHC', 'SGEN', 'VEEV', 'RMD', 'ILMN', 'SRTOY', 'ARGX', 'ZBH', 'WUXAY', 'MTD', 'WST', 'SOAGY', 'ALPMF', 'SDMHF', 'ALPMY', 'WBA', 'SAUHY', 'CLPBF', 'CLPBY', 'GMAB', 'SUVPF', 'BNTX', 'SAUHF', 'GNMSF', 'ALGN', 'BAX', 'SARTF', 'TRUMY', 'TRUMF', 'ALNY', 'CAH']
def stocksCorrelations(stock1, stock2):
    df = pd.DataFrame()
    df = yf.download(stock1, start="2023-6-28", end="2023-7-28", interval='15m', progress=False)
    df.iloc[:, :]

    df1 = pd.DataFrame()
    df1 = yf.download(stock2, start="2023-6-28", end="2023-7-28", interval='15m', progress=False)
    df1.iloc[:, :]

    r = df['Close'].corr(df1['Close'])
    return r

def loops(sector):
    max_corr = 0
    stock_pairs = []
    tickers = None

    if sector == "Tech":
        tickers = Tech
    elif sector == "Materials":
        tickers = Materials
    elif sector == "Financials":
        tickers = Financials
    elif sector == "Energy":
        tickers = Energy
    elif sector == "Healthcare":
        tickers = Healthcare

    for i in range(len(tickers)):
        for j in range(i + 1, len(tickers)):
            stock1 = tickers[i]
            stock2 = tickers[j]
            correlation = stocksCorrelations(stock1, stock2)
            if correlation > max_corr:
                max_corr = correlation
                stock_pairs = [(stock1, stock2)]

    return stock_pairs



def stocksCorrelation(stock1,stock2):

  df = pd.DataFrame()
  df = yf.download(stock1, start="2023-6-19", end="2023-7-19", interval='15m',progress=False)
  df.iloc[:,:]
  
  df1 = pd.DataFrame()
  df1 = yf.download(stock2, start="2023-6-19", end="2023-7-19", interval='15m',progress=False)
  df1.iloc[:,:]
  
  
  r = df['Close'].corr(df1['Close'])

  return r

def loop(sector):
    max_corr = 0
    stock1 = ""
    stock2 = ""
    for x in sector:
        for y in sector:
            correlation = stocksCorrelation(x,y)
            if correlation > max_corr and x != y:
                max_corr = correlation
                stock1 = x
                stock2 = y

    return stock1, stock2
loop(Tech)
PairsTradingPredictor = Flask(__name__)

@PairsTradingPredictor.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        selected_option = request.form['menu_options']
        return f"You selected: {loops(selected_option)}"

def tech_process_button_click():
    # Your Python code here
    # This function will be executed when the button is pressed
    print("Button clicked")

@PairsTradingPredictor.route('/')
def index():
    return render_template('index.html')

@PairsTradingPredictor.route('/button_click', methods=['POST'])
def tech_button_click():
    tech_process_button_click()
    return "Button Clicked!"

if __name__ == '__main__':
    PairsTradingPredictor.run(debug=True)

# @PairsTradingPredictor.route('/result', methods=['POST'])
# def result():
#     if request.method == 'POST':
#         button_value = request.form['button_value']
#         result_texts = loops(eval(button_value))
#         return render_template('result.html', result_text=result_texts)

@PairsTradingPredictor.route('/result', methods=['GET,POST'])
def result():
    if request.method == 'GET':
        # Process the form data here (if needed)
        # For example, you can get form data using request.form.get('field_name')
        return "Form submission successful!"
    



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


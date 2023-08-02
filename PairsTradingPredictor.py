import numpy as np
import pandas as pd
import yfinance as yf
from flask import Flask, render_template, request,url_for


Tech = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'TSLA', 'META', 'AVGO', 'PEP', 'COST', 'ADBE', 'CSCO', 'AZN', 'NFLX','AMD', 'CMCSA', 'TMUS', 'TXN', 'HON', 'INTC', 'QCOM', 'SNY', 'INTU', 'AMAT', 'AMGN', 'ISRG', 'SBUX', 'MDLZ', 'BKNG', 'PDD', 'ADI', 'GILD', 'ADP', 'VRTX', 'LRCX','ABNB', 'PANW', 'REGN', 'PYPL', 'EQIX', 'CSX', 'MU', 'SNPS', 'CME', 'ATVI', 'KLAC', 'NTES', 'CDNS', 'FTNT', 'MNST', 'MELI', 'WDAY', 'ORLY', 'MAR', 'JD', 'CHTR', 'NXPI', 'MRVL', 'ROP', 'BIDU', 'DXCM', 'CTAS', 'MCHP', 'LULU', 'MRNA', 'KDP', 'TEAM', 'KHC', 'AEP', 'ADSK', 'PCAR', 'IDXX', 'PAYX', 'EXC', 'ODFL', 'ON', 'BIIB', 'TTD', 'ROST', 'GEHC', 'SGEN', 'IBKR', 'CSGP', 'EA', 'LI', 'XEL', 'GFS', 'CRWD', 'BKR', 'CTSH', 'FAST', 'MBLY', 'VRSK', 'DLTR', 'DDOG', 'WBD', 'CEG', 'CCEP']
Materials = ['LIN', 'BHP', 'BHPLF', 'RTNTF', 'RTPPF', 'RIO', 'AIQUY', 'AIQUF', 'GLCNF', 'GLNCY', 'SHW', 'APD', 'VALE', 'CTA-PB', 'SHECY', 'SHECF', 'SCCO', 'FCX', 'ECL', 'CTA-PA', 'FSUMF', 'FSUGY', 'SXYAY', 'BASFY', 'BFFAF', 'SKFOF', 'ZIJMF', 'AAUKF', 'NUE', 'NGLOY', 'CRHCF', 'CRH', 'GMBXF', 'PKX', 'CTVA', 'HCMLF', 'HCMLY', 'DOW', 'DD', 'NEM', 'PPG', 'NTR', 'GVDBF', 'GVDNY', 'LYB', 'GOLD', 'VMC', 'FNV', 'MLM', 'AEM', 'KLBAY', 'SLMNP', 'ALB', 'MT', 'TECK', 'SQM', 'NPSCY', 'WPM', 'NPPHY', 'ANFGF', 'FQVLF', 'STLD', 'CMCLF', 'UPMMY', 'AHCHY', 'UPMKF', 'RS', 'WLK', 'AHCHF', 'NCMGY', 'NCMGF', 'CF', 'HLBZF', 'GNENY', 'AVTR', 'GNENF', 'SYIEY', 'SYIEF', 'HDELY', 'GFIOF', 'AKZOY', 'GFI', 'AKZOF', 'NVZMF', 'NVZMY', 'CE', 'ANGPY', 'NHYDY', 'MOS', 'NHYKF', 'JHX', 'SLVYY', 'SUZ', 'IVPAF', 'RPM', 'SOUHY', 'BNTGF', 'FMC', 'SHTLF']
Financials = ['BRK-A', 'BRK-B', 'JPM', 'V', 'MA', 'JPM-PC', 'JPM-PD', 'BAC', 'BAC-PK', 'BAC-PL', 'BML-PG', 'BML-PH', 'BML-PL', 'BAC-PE', 'BML-PJ', 'BAC-PB', 'IDCBY', 'WFC-PQ', 'WFC-PY', 'WFC-PR', 'WFC-PL', 'HDB', 'WFC', 'MS', 'ACGBY', 'HSBC', 'C-PJ', 'HBCYF', 'CICHY', 'CICHF', 'RY', 'SPGI', 'GS', 'BACHY', 'BACHF', 'CMWAY', 'BX', 'WFC-PC', 'PNGAY', 'AXP', 'PIAIF', 'TD', 'SCHW', 'C', 'CIHKY', 'BLK', 'AAIGF', 'AAGIY', 'CILJF', 'ALIZY', 'ALIZF', 'MMC', 'RY-PT', 'MBFJF', 'MUFG', 'GS-PJ', 'IBN', 'GS-PK', 'MS-PF', 'MS-PI', 'BNPQY', 'PYPL', 'BNPQF', 'CB', 'MS-PK', 'MS-PE', 'PBCRF', 'USB-PH', 'PBCRY', 'GS-PA', 'MS-PA', 'GS-PD', 'ZFSVF', 'ZURVY', 'PGR', 'UBS', 'AON', 'USB-PP', 'AXAHY', 'CME', 'AXAHF', 'KKR', 'MCO', 'ICE', 'PSTVY', 'DBSDY', 'DBSDF', 'SAN', 'BCDRF', 'IVSBF', 'BNS', 'LNSTY', 'BMO', 'SMFNF', 'LDNXF', 'SMFG', 'ITUB', 'USB', 'UNCFF']
Energy = ['XOM', 'CVX', 'SHEL', 'RYDAF', 'PCCYF', 'PBMRF', 'TTE', 'TTFNF', 'COP', 'BP', 'BPAQF', 'SNPMF', 'STOHF', 'EQNR', 'PBR', 'PBR-A', 'SLB', 'ENB', 'EOG', 'EBBNF', 'CSUAY', 'CUAEF', 'CNQ', 'EPD', 'PEXNY', 'OXY', 'MPC', 'PXD', 'E', 'PSX', 'WOPEF', 'EIPAF', 'WDS', 'HES', 'VLO', 'ET', 'WMB', 'KMI', 'SU', 'LNG', 'TRP', 'BKR', 'MPLX', 'HAL', 'CVE', 'DVN', 'NTOIY', 'NTOIF', 'IMO', 'OKE', 'FANG', 'CQP', 'EC', 'CTRA', 'REPYY', 'TS', 'TRGP', 'IPXHY', 'SSLZY', 'AKRBF', 'TRMLF', 'PBA', 'STOSF', 'YZCAY', 'IPXHF', 'MRO', 'OMVKY', 'OMVJF', 'CCJ', 'EQT', 'MMP', 'YPF', 'APA', 'IEP', 'OVV', 'TPL', 'CHK', 'WES', 'OGFGY', 'PAA', 'GLPEY', 'GLPEF', 'MGYOY', 'AETUF', 'FTI', 'CSAN', 'HESM', 'PTRRY', 'NOV', 'AR', 'RRC', 'VARRY', 'NE', 'CHX', 'SWN', 'KLYCY', 'MTDR', 'MUR']
Healthcare = ['UNH', 'JNJ', 'LLY', 'NVO', 'NONOF', 'MRK', 'RHHBF', 'RHHBY', 'RHHVF', 'ABBV', 'NVS', 'NVSEF', 'TMO', 'AZNCF', 'AZN', 'PFE', 'ABT', 'DHR', 'SNY', 'BMY', 'SNYNF', 'AMGN', 'MDT', 'ISRG', 'ELV', 'SYK', 'CVS', 'GILD', 'CSLLY', 'ESLOY', 'ZTS', 'CI', 'ESLOF', 'CMXHF', 'BDX', 'REGN', 'HCA', 'MKGAF', 'MKKGY', 'GLAXF', 'BSX', 'GSK', 'SMMNY', 'SEMHF', 'HUM', 'BAYRY', 'EW', 'BAYZF', 'DSNKY', 'MCK', 'DSKYF', 'DXCM', 'TKPHF', 'TAK', 'CHGCY', 'MRNA', 'IDXX', 'IQV', 'LZAGY', 'LZAGF', 'ALC', 'HLN', 'HOCPY', 'HLNCF', 'BIIB', 'ABC', 'CNC', 'A', 'GEHC', 'SGEN', 'VEEV', 'RMD', 'ILMN', 'SRTOY', 'ARGX', 'ZBH', 'WUXAY', 'MTD', 'WST', 'SOAGY', 'ALPMF', 'SDMHF', 'ALPMY', 'WBA', 'SAUHY', 'CLPBF', 'CLPBY', 'GMAB', 'SUVPF', 'BNTX', 'SAUHF', 'GNMSF', 'ALGN', 'BAX', 'SARTF', 'TRUMY', 'TRUMF', 'ALNY', 'CAH']


dict_Tech = {}
for stock in Tech:
    df = yf.download(stock, start="2023-6-19", end="2023-7-19", interval='15m', progress=False)
    dict_Tech[stock] = df

dict_Materials = {}
for stock in Materials:
    df = yf.download(stock, start="2023-6-19", end="2023-7-19", interval='15m', progress=False)
    dict_Materials[stock] = df

dict_Financials = {}
for stock in Financials:
    df = yf.download(stock, start="2023-6-19", end="2023-7-19", interval='15m', progress=False)
    dict_Financials[stock] = df   

dict_Energy = {}
for stock in Energy:
    df = yf.download(stock, start="2023-6-19", end="2023-7-19", interval='15m', progress=False)
    dict_Energy[stock] = df 
    
dict_Healthcare = {}
for stock in Healthcare:
    df = yf.download(stock, start="2023-6-19", end="2023-7-19", interval='15m', progress=False)
    dict_Healthcare[stock] = df     

def stocksCorrelation(df, df1):
        r = df['Close'].corr(df1['Close'])
        return r

def loop(selected_option):
    max = 0
    z = 0
    if selected_option == "Tech":
        stock_dict = dict_Tech
    elif selected_option == "Materials":
        stock_dict = dict_Materials
    elif selected_option == "Financials":
        stock_dict = dict_Financials
    elif selected_option == "Energy":
        stock_dict = dict_Energy
    elif selected_option == "Healthcare":
        stock_dict = dict_Healthcare
    else:
        return "Invalid sector selection."
    x = "" 
    y = ""
    for stock in stock_dict:
        for stock1 in stock_dict:
            z = stocksCorrelation(stock_dict[stock],stock_dict[stock1])
            if z>max and stock!=stock1:
                max = z
                x = stock
                y = stock1
    return(x, y)

def compare(s1, s2):
    ticker1 = yf.Ticker(s1)
    historical_data1 = ticker1.history(period='1mo')
    first_close1 = historical_data1['Close'][0]
    last_close1 = historical_data1['Close'][-1]
    price_change_percentage1 = ((last_close1 - first_close1) / first_close1) * 100
    price_change_percentage1_str = str(price_change_percentage1)

    ticker2 = yf.Ticker(s2)
    historical_data2 = ticker2.history(period='1mo')
    first_close2 = historical_data2['Close'][0]
    last_close2 = historical_data2['Close'][-1]
    price_change_percentage2 = ((last_close2 - first_close2) / first_close2) * 100
    price_change_percentage2_str = str(price_change_percentage2)

    if price_change_percentage1 > 0 and price_change_percentage2 > 0:
        if price_change_percentage1 > price_change_percentage2:
            return "Buy " + s2 + " because the price change percentage of " + s2 + " is " + price_change_percentage2_str + " which means it is the underperforming stock as compared to " + s1 + " which has a price change percentage of " + price_change_percentage1_str
        elif price_change_percentage1 < price_change_percentage2:
            return "Buy " + s1 + " because the price change percentage of " + s1 + " is " + price_change_percentage1_str + " which means it is the underperforming stock as compared to " + s2 + " which has a price change percentage of " + price_change_percentage2_str

    elif price_change_percentage1 < 0 and price_change_percentage2 < 0:
        return "Don't Buy any stock. Not a Bullish market."

    elif price_change_percentage1 > 0:
        return "Buy " + s1 + " because the price change percentage of " + s1 + " is " + price_change_percentage1_str + " which means it is the only performing stock."

    elif price_change_percentage2 > 0:
        return "Buy " + s2 + " because the price change percentage of " + s2 + " is " + price_change_percentage2_str + " which means it is the only performing stock."

    return "Error: No valid comparison could be made."

PairsTradingPredictor = Flask(__name__, static_url_path='/static')

@PairsTradingPredictor.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
       selected_option = request.form['menu_options']
       stock1, stock2 = loop(selected_option)
       compare_result = compare(stock1,stock2) 
       return render_template('result.html', stock1=stock1, stock2=stock2 , x=compare_result)

       #Use compare function and print result

@PairsTradingPredictor.route('/')
def index():
    image_url = url_for('static', filename='stocks.png')
    return render_template('indexss.html', css=url_for('static', filename='css/style.css',image_url='assets/stocks.png'))

if __name__ == '__main__':
    PairsTradingPredictor.run(debug=True)
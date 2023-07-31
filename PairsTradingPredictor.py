import numpy as np
import pandas as pd
import yfinance as yf
from flask import Flask, render_template, request
Tech = ['AAPL', 'MSFT','GOOGL', 'AMZN', 'NVDA']
Techs = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'TSLA', 'META', 'AVGO', 'PEP', 'COST', 'ADBE', 'CSCO', 'AZN', 'NFLX','AMD', 'CMCSA', 'TMUS', 'TXN', 'HON', 'INTC', 'QCOM', 'SNY', 'INTU', 'AMAT', 'AMGN', 'ISRG', 'SBUX', 'MDLZ', 'BKNG', 'PDD', 'ADI', 'GILD', 'ADP', 'VRTX', 'LRCX','ABNB', 'PANW', 'REGN', 'PYPL', 'EQIX', 'CSX', 'MU', 'SNPS', 'CME', 'ATVI', 'KLAC', 'NTES', 'CDNS', 'FTNT', 'MNST', 'MELI', 'WDAY', 'ORLY', 'MAR', 'JD', 'CHTR', 'NXPI', 'MRVL', 'ROP', 'BIDU', 'DXCM', 'CTAS', 'MCHP', 'LULU', 'MRNA', 'KDP', 'TEAM', 'KHC', 'AEP', 'ADSK', 'PCAR', 'IDXX', 'PAYX', 'EXC', 'ODFL', 'ON', 'BIIB', 'TTD', 'ROST', 'GEHC', 'SGEN', 'IBKR', 'CSGP', 'EA', 'LI', 'XEL', 'GFS', 'CRWD', 'BKR', 'CTSH', 'FAST', 'MBLY', 'VRSK', 'DLTR', 'DDOG', 'WBD', 'CEG', 'CCEP']
Materials = ['LIN', 'BHP', 'BHPLF', 'RTNTF', 'RTPPF', 'RIO', 'AIQUY', 'AIQUF', 'GLCNF', 'GLNCY', 'SHW', 'APD', 'VALE', 'CTA-PB', 'SHECY', 'SHECF', 'SCCO', 'FCX', 'ECL', 'CTA-PA', 'FSUMF', 'FSUGY', 'SXYAY', 'BASFY', 'BFFAF', 'SKFOF', 'ZIJMF', 'AAUKF', 'NUE', 'NGLOY', 'CRHCF', 'CRH', 'GMBXF', 'PKX', 'CTVA', 'HCMLF', 'HCMLY', 'DOW', 'DD', 'NEM', 'PPG', 'NTR', 'GVDBF', 'GVDNY', 'LYB', 'GOLD', 'VMC', 'FNV', 'MLM', 'AEM', 'KLBAY', 'SLMNP', 'ALB', 'MT', 'TECK', 'IFF', 'SQM', 'NPSCY', 'WPM', 'NPPHY', 'ANFGF', 'FQVLF', 'STLD', 'CMCLF', 'UPMMY', 'AHCHY', 'UPMKF', 'RS', 'WLK', 'AHCHF', 'NCMGY', 'NCMGF', 'CF', 'HLBZF', 'GNENY', 'AVTR', 'GNENF', 'SYIEY', 'SYIEF', 'HDELY', 'GFIOF', 'AKZOY', 'GFI', 'AKZOF', 'NVZMF', 'NVZMY', 'CE', 'ANGPY', 'NHYDY', 'MOS', 'NHYKF', 'JHX', 'SLVYY', 'SUZ', 'IVPAF', 'RPM', 'SOUHY', 'BNTGF', 'FMC', 'SHTLF']
Financials = ['BRK-A', 'BRK-B', 'JPM', 'V', 'MA', 'JPM-PC', 'JPM-PD', 'BAC', 'BAC-PK', 'BAC-PL', 'BML-PG', 'BML-PH', 'BML-PL', 'BAC-PE', 'BML-PJ', 'BAC-PB', 'IDCBY', 'WFC-PQ', 'WFC-PY', 'WFC-PR', 'WFC-PL', 'HDB', 'WFC', 'MS', 'ACGBY', 'HSBC', 'C-PJ', 'HBCYF', 'CICHY', 'CICHF', 'RY', 'SPGI', 'GS', 'BACHY', 'BACHF', 'CMWAY', 'BX', 'WFC-PC', 'PNGAY', 'AXP', 'PIAIF', 'TD', 'SCHW', 'C', 'CIHKY', 'BLK', 'AAIGF', 'AAGIY', 'CILJF', 'ALIZY', 'ALIZF', 'MMC', 'RY-PT', 'MBFJF', 'MUFG', 'GS-PJ', 'IBN', 'GS-PK', 'MS-PF', 'MS-PI', 'BNPQY', 'PYPL', 'BNPQF', 'CB', 'MS-PK', 'MS-PE', 'PBCRF', 'USB-PH', 'PBCRY', 'GS-PA', 'MS-PA', 'GS-PD', 'ZFSVF', 'ZURVY', 'PGR', 'SBKFF', 'UBS', 'AON', 'USB-PP', 'AXAHY', 'CME', 'AXAHF', 'KKR', 'MCO', 'ICE', 'PSTVY', 'DBSDY', 'DBSDF', 'SAN', 'BCDRF', 'IVSBF', 'BNS', 'LNSTY', 'BMO', 'SMFNF', 'LDNXF', 'SMFG', 'ITUB', 'USB', 'UNCFF']
Energy = ['XOM', 'CVX', 'SHEL', 'RYDAF', 'PCCYF', 'PBMRF', 'TTE', 'TTFNF', 'COP', 'BP', 'BPAQF', 'SNPMF', 'STOHF', 'EQNR', 'PBR', 'PBR-A', 'SLB', 'ENB', 'EOG', 'EBBNF', 'CSUAY', 'CUAEF', 'CNQ', 'EPD', 'PEXNY', 'OXY', 'MPC', 'PXD', 'E', 'PSX', 'WOPEF', 'EIPAF', 'WDS', 'HES', 'VLO', 'ET', 'WMB', 'KMI', 'SU', 'LNG', 'TRP', 'BKR', 'MPLX', 'HAL', 'CVE', 'DVN', 'NTOIY', 'NTOIF', 'IMO', 'OKE', 'FANG', 'CQP', 'EC', 'CTRA', 'REPYY', 'TS', 'TRGP', 'IPXHY', 'SSLZY', 'AKRBF', 'TRMLF', 'PBA', 'STOSF', 'YZCAY', 'IPXHF', 'MRO', 'OMVKY', 'OMVJF', 'CCJ', 'EQT', 'MMP', 'CCOZF', 'YPF', 'APA', 'IEP', 'OVV', 'TPL', 'CHK', 'WES', 'OGFGY', 'PAA', 'GLPEY', 'GLPEF', 'DINO', 'MGYOY', 'AETUF', 'FTI', 'CSAN', 'HESM', 'PTRRY', 'NOV', 'AR', 'RRC', 'VARRY', 'NE', 'CHX', 'SWN', 'KLYCY', 'MTDR', 'MUR']
Healthcare = ['UNH', 'JNJ', 'LLY', 'NVO', 'NONOF', 'MRK', 'RHHBF', 'RHHBY', 'RHHVF', 'ABBV', 'NVS', 'NVSEF', 'TMO', 'AZNCF', 'AZN', 'PFE', 'ABT', 'DHR', 'SNY', 'BMY', 'SNYNF', 'AMGN', 'MDT', 'ISRG', 'ELV', 'SYK', 'CVS', 'GILD', 'VRTX', 'CSLLY', 'ESLOY', 'ZTS', 'CI', 'ESLOF', 'CMXHF', 'BDX', 'REGN', 'HCA', 'MKGAF', 'MKKGY', 'GLAXF', 'BSX', 'GSK', 'SMMNY', 'SEMHF', 'HUM', 'BAYRY', 'EW', 'BAYZF', 'DSNKY', 'MCK', 'DSKYF', 'DXCM', 'TKPHF', 'TAK', 'CHGCY', 'MRNA', 'IDXX', 'IQV', 'LZAGY', 'LZAGF', 'ALC', 'HLN', 'HOCPY', 'HLNCF', 'BIIB', 'ABC', 'CNC', 'A', 'GEHC', 'SGEN', 'VEEV', 'RMD', 'ILMN', 'SRTOY', 'ARGX', 'ZBH', 'WUXAY', 'MTD', 'WST', 'SOAGY', 'ALPMF', 'SDMHF', 'ALPMY', 'WBA', 'SAUHY', 'CLPBF', 'CLPBY', 'GMAB', 'SUVPF', 'BNTX', 'SAUHF', 'GNMSF', 'ALGN', 'BAX', 'SARTF', 'TRUMY', 'TRUMF', 'ALNY', 'CAH']
def stocksCorrelations(stock1, stock2):
    try:
        df = yf.download(stock1, start="2023-6-19", end="2023-7-19", interval='15m', progress=False)
        df1 = yf.download(stock2, start="2023-6-19", end="2023-7-19", interval='15m', progress=False)
        r = df['Close'].corr(df1['Close'])
        return r
    except KeyError:
        print(f"Data not available for {stock1} and/or {stock2}")
        return None
    except Exception as e:
        print(f"Error fetching data for {stock1} and/or {stock2}: {e}")
        return None

def loops(sector):
    max_corr = 0  # Initialize max_corr to None
    stock_pairs = []
    for x in sector:
        for y in sector:
            correlation = stocksCorrelation(x, y)
            if (correlation > max_corr) & (x!=y):  # Check for None and compare
                max_corr = correlation
                stock_pairs = [(x, y)]

    return stock_pairs


def loop(selected_option):
    print("Now Printing")
    max = 0
    z = 0
    if selected_option == "Tech":
        stock_list = Tech
    elif selected_option == "Materials":
        stock_list = Materials
    elif selected_option == "Financials":
        stock_list = Financials
    elif selected_option == "Energy":
        stock_list = Energy
    elif selected_option == "Healthcare":
        stock_list = Healthcare
    else:
        return "Invalid sector selection."
    stock1 = "" 
    stock2 = ""
    for x in stock_list:
        print("Now Printing")
        for y in stock_list:
            z = stocksCorrelations(x,y)
            if z>max and x!=y:
                max = z
                stock1 = x
                stock2 = y
    return stock1, stock2



def stocksCorrelation(stock1,stock2):
    try:
        df = yf.download(stock1, start="2023-6-19", end="2023-7-19", interval='15m', progress=False)
        df1 = yf.download(stock2, start="2023-6-19", end="2023-7-19", interval='15m', progress=False)
        r = df['Close'].corr(df1['Close'])
        return r
    except Exception as e:
        print(f"Error fetching data for {stock1} and/or {stock2}: {e}")
        return None


PairsTradingPredictor = Flask(__name__)

@PairsTradingPredictor.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
       selected_option = request.form['menu_options']
       stock1, stock2 = loop(selected_option)
       return render_template('result.html', stock1=stock1, stock2=stock2)

@PairsTradingPredictor.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    PairsTradingPredictor.run(debug=True)
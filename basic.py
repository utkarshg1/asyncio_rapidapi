import requests
import os 
from dotenv import load_dotenv
import time 

load_dotenv()
url = os.getenv("url")
api_key = os.getenv("api_key")
host = os.getenv("host")


def get_api_results(symbol):
    """
    This function takes symbol of company as input and returns daily stock data
    """    

    querystring = {"function":"TIME_SERIES_DAILY","symbol":symbol,"outputsize":"compact","datatype":"json"}

    headers = {
        "X-RapidAPI-Key": api_key ,
        "X-RapidAPI-Host": host
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()

def main():
    t1 = time.time()
    symbols = ['SBIN.BSE', 'HDFCBANK.BSE', 'TATAMOTORS.BSE', 'ITC.BSE', 'M&M.BSE']
    r = []
    for i in symbols:
        r.append(get_api_results(i))
    t2 = time.time()
    print(r)
    print(f'\nTime required to execute program is {t2-t1:.2f} s')

if __name__ == '__main__':
    main()
    


import asyncio
import aiohttp 
from dotenv import load_dotenv
import os
import time  

load_dotenv()
url = os.getenv("url")
api_key = os.getenv("api_key")
host = os.getenv("host")

async def get_data(symbol):
    querystring = {"function":"TIME_SERIES_DAILY","symbol":symbol,"outputsize":"compact","datatype":"json"}

    headers = {
        "X-RapidAPI-Key": api_key ,
        "X-RapidAPI-Host": host
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url+f"?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&datatype=json", headers=headers) as r:
            response = await r.json()
            return response

async def main():
    t1 = time.time()
    symbols = ['SBIN.BSE', 'HDFCBANK.BSE', 'TATAMOTORS.BSE', 'ITC.BSE', 'M&M.BSE']
    tasks = []
    for i in symbols:
        tasks.append(asyncio.create_task(get_data(i)))
    response = await asyncio.gather(*tasks)
    t2 = time.time()
    #print(response)
    print(f'Time required to complete the task is {(t2-t1)*1000:.2f} milli seconds')
    return (t2-t1)*1000

if __name__ == '__main__':
    t = []
    for _ in range(10):
        t.append(asyncio.run(main()))
    avg_time = sum(t)/len(t)
    print(f'Average time taken by async client : {avg_time:.2f} seconds')
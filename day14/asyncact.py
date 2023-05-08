import asyncio
import requests
import os 
import Tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

#async runs on single thread, but uses mulri-tasking or cooperative multi-tasking

url1 = "https://jsonplaceholder.typicode.com/photos"
url2 = "https://jsonplaceholder.typicode.com/comments"
url3 = "https://jsonplaceholder.typicode.com/todos"

async def getUrl(url):
    res = requests.get(url)
    print("fetching url")
    await asyncio.sleep(2)
    if res.status_code == 200:
        return res.json()
    return None

async def fetchUrl(url):
    res = requests.get(url)
    return res.json()

async def main():
    data = await asyncio.gather(fetchUrl(url1), fetchUrl(url2), fetchUrl(url3))
    return data


if __name__ == '__main__':
    result = asyncio.run(main())
    print(result)

# asyncio.run()
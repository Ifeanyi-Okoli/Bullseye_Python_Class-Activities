from threading import Thread
import time
import requests


#Jsonplaceholder.typicodes
# def getComments(x):
#     num = 10**x
#     for x in range(num):
#         print(x)
        


def getUrl(url):
    res = requests.get(url)
    print("fetching url")
    time.sleep(2)
    if res.status_code == 200:
        return res.json()
    return None

def fetchUrl(url):
    comments = getUrl(url)
    print(comments)


def estimatedTimeforThread(*urls):  
    timeStart = time.perf_counter()
    threads = []

    t1 = Thread(target=fetchUrl, args=(urls[0],))
    t2 = Thread(target=fetchUrl, args=(urls[1],))

    t1.start()
    t2.start()

    threads.append(t1)
    threads.append(t2)

    
    for t in threads:
        t.join()

    return time.perf_counter() - timeStart


def withoutThread(*urls):
    

    timeStart = time.perf_counter()
    
    for url in urls:
        output = fetchUrl(url)
        print(output)
    return time.perf_counter() - timeStart



url = "https://jsonplaceholder.typicode.com/photos"
url2 = "https://jsonplaceholder.typicode.com/comments"

time1 = withoutThread(url, url2)
time2 = estimatedTimeforThread(url, url2)

difference = time1 - time2
print(f"Time taken for thread: {time1}")
print(f"Time taken for without thread: {time2}")
print(f"It took {difference} seconds to complete the task with thread")
print(f"Without {time1}\nWith Thread {time2}")
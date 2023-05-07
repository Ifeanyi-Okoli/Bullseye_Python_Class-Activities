from threading import Thread
import time


class Fetch(Thread):
    def __init__(self, urls=None, **kwargs):
        self.urls = urls
        super().__init__(**kwargs)
        
    
    def getUrl(self, url):
        res = requests.get(url)
        print("fetching url")
        time.sleep(2)
        if res.status_code == 200:
            return res.json()
        return None

    def fetchUrl(self):
        comments = getUrl(url)
        print(comments)
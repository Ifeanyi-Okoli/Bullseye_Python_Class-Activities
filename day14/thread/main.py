from fetchx import Fetch
from dosome import XMO
from decouple import config
from threading import Thread
import time

class Main(Fetch, XMO):
    def __init__(self, **kwargs) -> None:
        super(Main, self).__init__(**kwargs)
        self.start()
        # Fetch.__init__(self, **kwargs)
        # XMO.__init__(self, **kwargs)
        
    def fetch(self):
        return self.fetchUrl()

    def log(self):
        self.xmo_log()
        

if __name__ == "__main__":
    
    urls = [config("URL"), config("URL2")]
    num = 5
    main = Main(urls=urls, num=num)
    data = main.fetch()
    print(data[0])
    main.log()
    print("Done")
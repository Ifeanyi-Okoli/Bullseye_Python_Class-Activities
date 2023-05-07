from threading import Thread
import time

class XMO(Thread):
    CONST = 0
    def __init__(self, num, **kwargs):
        self.num = num
        super().__init__(**kwargs)
        self.start()
        
    def xmoLog(self):
        while XMO.CONST <= 10:
            for x in range(self.num ** self.num):
                XMO.CONST += 1
                time.sleep(2)
                self.xmoLog(self)
                
    
    def logXMO(self, xmo:int) -> None:
        with open("log.txt", "a") as f:
            f.write(f"{xmo}\n")
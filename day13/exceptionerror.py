x = 5
try:
    if x < 5:
        raise ValueError("x must be greater than 5")
except Exception as err:
    print("Error: ", err)
    
else:
    print("No error occured")
    
finally:
    print("Finally block")
    
head = 6

class BigHeadError(Exception):
    def __init__(self, message="Big Heead Error"):
        self.message = message
        super().__init__(self.message)
        

if head > 5:
    raise BigHeadError("Head is too big")

import time
networkStatus = 400
trial = 0
def transferFund():
    return networkStatus
    # global trial
    # while trial < 10:
    #     time.sleep(1)
    #     trial += 1
    #     print("Trial: ", trial)
    #     if trial == 5:
    #         networkStatus = 500
    #         break
    #     elif trial == 10:
    #         networkStatus = 200
    #         break
    #     else:
    #         networkStatus = 200
    #         break

def hasTransfer():
    if networkStatus == 200:
        return True
    return False


class TransferError(Exception):
    def __init__(self, message="Big Heead Error"):
        self.message = message
        super().__init__(self.message)
        

try:
    if not hasTransfer():
        raise TransferError()
    
    
except Exception as err:
    while networkStatus != 200:
        transferFund()
        trial += 1
        print("Trying again... ", networkStatus)
        if trial == 10:
            networkStatus = 200
        time.sleep(2)
import time

networkStatus = 400
trial = 0
opened = False

class Biometrics:
    fingerPrints = ["@1234)^jd"]
    
    def login(cls, fingerPrint=None):
        if fingerPrint in cls.fingerPrints:
            return True
        return False
    
def openDoor(**kwargs):
    biometric = Biometrics()
    feedback = biometric.login(**kwargs)        
    return feedback

def hasOpened():
    global opened
    return True if opened else False

class doorNotOpenedError(Exception):
    def __init__(self, message="Invalid credentials"):
        self.message = message
        super().__init__(message)   
        

try:
    sensorReading = "@1234)^jd--=jd"    # Sensor reading
    if not openDoor(fingerPrint=sensorReading):
        raise doorNotOpenedError()
    
except doorNotOpenedError as err:
    while trial < 3:
        if openDoor(fingerPrint=sensorReading):
            print("Door Opned successfully")
        print("Please Try Again", 3 - (trial + 1), "attempts left")
        time.sleep(3)
        trial += 1
        if trial >= 2:
            sensorReading = "@1234)^jd"
else:
    print("No Error Occured")
    
finally:
    print("Runs with or without error")
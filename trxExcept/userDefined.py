class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input value is small"""
    pass

class ValueTooLargeError(Error):
    """Raised when the input value is large"""
    pass

while(True):
    try:
        num = int(input("Enter any number between the range of 10 and 50: "))
        if num < 10:
            raise ValueTooSmallError
        elif num > 50:
            raise ValueTooLargeError
        break
    except ValueTooLargeError:
        print("This value is too large, try again!")
        
    except ValueTooSmallError:
        print("This value is too small, try again!")

print("Great! value is within the range.")
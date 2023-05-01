def isPalindrome(x:int):
    strNum = str(x)
    revNum = strNum[::-1]
    if strNum == revNum:
        return True
    return False

print(isPalindrome(121))
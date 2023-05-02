def tryError():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter second number: "))
        c= a/b
        print(c)
        
    except ZeroDivisionError:
        print("Division by zero is not allowed enter a different value")
    except ValueError:
        print("Enter a valid number")
    finally:
        tryError()

tryError()
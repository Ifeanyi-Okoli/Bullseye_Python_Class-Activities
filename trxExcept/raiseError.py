def simpleInterest(amount, year, rate):
    try:
        if rate>100:
            raise ValueError("Rate cannot be greater than 100%")
        interest = (amount*year*rate)/100
        print(f"Interest is {interest}")
        return interest
    except ValueError:
        print("Enter a valid rate")
        return None

print("Case 1")
simpleInterest(800, 8, 8)

print("Case 2")
simpleInterest(800, 8, 108)
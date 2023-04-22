#dictionary consists of key-value pairs
#keyword arguments are assigned to a variable  name as a dictionary
# currency = dict(exc=740)
# print(currency)
currency = {"USD":  {"NGN": 740, "GBP": 0.75, "EUR": 0.85, "JPY": 110, "CNY": 6.5},
            "CFA":  {"USD": 740, "GBP": 0.75, "EUR": 0.85, "JPY": 110, "CNY": 6.5}
            }

symbol = "NGN/USD"


# print(currency.items())
# print(currency.keys())
# print(currency.values())

currency.update({"NGN":  {"USD": 740, "GBP": 0.75, "EUR": 0.85, "JPY": 110, "CNY": 6.5}})
currency["GBP"] = {"USD": 740, "GBP": 0.75, "EUR": 0.85, "JPY": 110, "CNY": 6.5}



def exchangeConverter(amount, symbol):
    if (symbol in currency.keys()):
        print("The exchange rate of {} is {}".format(symbol, currency[symbol]*amount))
    
    
    #pass


#dot notation does not work in python. we can access the dictionary values using the get method or the []


exchangeConverter(100, "NGN/USD")




#--------correction----------
currency = {"USD":  {"NGN": 740, "GBP": 0.75, "EUR": 0.85, "JPY": 110, "CNY": 6.5},
            "CFA":  {"USD": 740, "GBP": 0.75, "EUR": 0.85, "JPY": 110, "CNY": 6.5},
            "GCD":  {"NGN": 740, "GBP": 0.75, "EUR": 0.85, "JPY": 110, "CNY": 6.5},
            "RYD":  {"USD": 740, "GBP": 0.75, "EUR": 0.85, "JPY": 110, "CNY": 6.5}            
            }

while True:
    amount = int(input("Enter amount: "))
    symbols = int(input("choose currency type: \n\t Enter 1 for USD/NGN: \n\t \n\t Enter 2 for USD/GBP:\n\t \n\t Enter 3 for USD/EUR: \n\t \n\t Enter 4 for USD/JPY: \n\t \n\t Enter 5 for USD/CNY: \n\t \n\t Enter 6 for CFA/EUR: \n\t \n\t Enter 7 for CFA/GBP: \n\t \n\t Enter 8 for GCD/NGN: \n\t \n\t Enter 9 for RYD/USD: \n\t \n\t Enter 0 for RYD/EUR:\n\t\t"))
   
    key = {1: "USD/NGN", 2: "USD/GBP", 3: "USD/EUR", 4: "USD/JPY", 5: "USD/CNY", 6: "CFA/EUR", 7: "CFA/GBP", 8: "GCD/NGN", 9: "RYD/USD", 0: "RYD/EUR"}

    def exchnageConvert(amount, symbol):
        base_target = key.get(symbol)
        base, target = base_target.split("/")    
        return currency[base][target] * amount
        
    print(exchnageConvert(amount, symbols))
    res = input("check again? y/n ")
    
    if res.lower() == "n":
        print("GOOD BYE!")
        break
























































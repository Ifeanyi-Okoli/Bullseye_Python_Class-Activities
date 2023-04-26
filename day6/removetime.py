def shorten_to_date(long_date):
    day, month, year, _ = long_date.split(" ")
    year, _ = year.split(",")
    return day, month, year
    # return long_date.split(",")[0]
print(shorten_to_date("Monday February 2, 8pm"))


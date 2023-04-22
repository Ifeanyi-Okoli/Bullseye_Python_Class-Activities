#FV = P*(1+R/N)^(N*T)

"""Compound interest, can be calculated using the formula FV = P*(1+R/N)^(N*T), where FV is the future value of the loan or investment, P is the initial principal amount, R is the annual interest rate, N represents the number of times interest is compounded per year, and T represents time in years."""

#A = P(1 + r/n)**(n*t)

name = input("what is yur name  ")
p = int(input("input the principal amount  "))
r = 0.07
n = int(input("input the number of times interest is compounded per year  "))
t = int(input("the number of years  "))
A = p*((1 + r/n)**(n*t))
print((A//10)*10)

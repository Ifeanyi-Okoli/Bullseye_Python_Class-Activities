num = input("Enter a credit card number: ")
def credit_card():
    res=""
    odd = sum = 0
    nums=str(num)
    a = len(nums)-1
    for i in range(a,-1,-1):
        b=int(nums[i])
        if i%2==0:
            b=b*2
            if b>9:
                b=b-9
                res=res+str(b)
            else:
                res=res+str(b)
        else:
            odd = odd + int(nums[i])
    for i in range(0,len(res)):
            sum = sum + int(nums[i])
    if (sum+odd)%10==0:
        print("This is a valid credit card")
    else:
        print("This is an invalid credit card")
credit_card()
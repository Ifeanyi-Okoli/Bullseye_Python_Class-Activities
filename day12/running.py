import tkinter as tk

class CheckNum:
    def __init__(self, nums) -> None:\
        self.nums = nums
        
    def check_odd(self):
        return [num for num in self.nums if num % 2 != 0]
    
    def check_even(self):
        return [num for num in self.nums if num % 2 == 0]


if __name__ == '__main__':
    running = True

    nums = [x for x in range(1, 101)]

    check = CheckNum(nums)
    
    while running:
        options = input("1. check odd \n2. check even \n3. exit \n")
        if options not in "123":
            print("Invalid option, ch[se between 1 - 3")
            continue
        
        if options == "1":
            pass
        elif options == "2":
            pass
print(options)
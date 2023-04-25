#Static method does not change anything. They only act as a function inside a class
class Math:
    @staticmethod
    def add5(x):
        return x + 5


    @staticmethod
    def add10(x):
        return x + 10
    
    @staticmethod
    def pr():
        print("run")
    
print(Math.add5(5))

print(Math.add10(5))

Math.pr()
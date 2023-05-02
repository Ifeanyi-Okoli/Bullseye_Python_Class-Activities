def sumItems(num):
    return sum(num)

def average(sum, n):
    return sum/n
    
    
def finalData(data):
    for item in data:
        print('the average is ', average(sumItems(item), len(item)))

list1 = [10, 20, 30, 40, 50]
list2 = [100, 200, 300, 400, 500]
list3 =[]
lists = [list1, list2, list3]

finalData(lists)
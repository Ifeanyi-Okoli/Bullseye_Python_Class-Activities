from multiprocessing import Process, Queue, Pool, cpu_count, memory_info
import time

def calcAvg(nums):
    average = 0
    
    for i in nums:
        average += i
    return average / len(nums)

noCountCPU = max(1, cpu_count() - 1)

print(f"CPU Count: {cpu_count}")


if __name__ == "__main__":
    t1 = time.perf_counter()
    noCountCPU = max(1, cpu_count() - 1)
    

    with Pool(noCountCPU) as pool:
        args = range(1000, 100000)
        result = Process(calcAvg, args= (args,))
        # result = pool.map(calcAvg, range(1000, 100000))
        print(result)

# t1 = time.perf_counter()

# for x in range(1000, 100000):
#     print(calcAvg(x))
    

t2 = time.perf_counter()

print(f"Took: {t2 - t1} seconds to complete")

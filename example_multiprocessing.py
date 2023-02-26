#Богомаз Алексей multiprocessing
import multiprocessing
from datetime import datetime
import time

print('Number of cpu:', multiprocessing.cpu_count())

def timeit(func): # создаём декоратор
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

@timeit 
def thread_fibonachi(n):
    l = [0, 1]
    a1 = a2 = 1
    for _ in range(3, n + 1):
        a1, a2 = a2, a1 + a2
        l.append(a2)
    print('Finished'+'\n')

process = []

for i in range(4):
    p = multiprocessing.Process(target=thread_fibonachi, args=[300000])
    process.append(p)
    p.start()

for p in process:
    p.join()
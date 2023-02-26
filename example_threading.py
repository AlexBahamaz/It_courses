#Богомаз Алексей threading
from datetime import datetime
import time
from threading import Thread

def timeit(func): # создаём декоратор
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

@timeit #Используем декоратор timeit
def thread_sleep():
    time.sleep(5)
    print()

@timeit 
def thread_fibonachi(n):
    l = [0, 1]
    a1 = a2 = 1
    for _ in range(3, n + 1):
        a1, a2 = a2, a1 + a2
        l.append(a2)
    print('Finished')

def main(): #создаём и запускаем потоки. Важна очерёдность создания и запуска.
    t_1 = Thread(target=thread_sleep)
    t_1.start()
    t_2 = Thread(target=thread_fibonachi(300000))
    t_2.start()
    t_1.join()
    t_2.join()

if __name__ =="__main__":
    main()
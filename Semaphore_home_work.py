#Богомаз Алексей
import threading, random, time
# СЕМАФОРЫ

class ActivePool:
   

    start = time.time()

    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()

    def makeRequest(self, name):
        with self.lock:
            self.active.append(name)
            tm = time.time() - self.start
            print(f'Время: {round(tm, 3)} Running: {self.active}')

    def gotRequest(self, name):
        with self.lock:
            self.active.remove(name)
            print(f'{name} получил ответ и удалён из пула')
            tm = time.time() - self.start
            print(f'Время: {round(tm, 3)} ждут ответ: {self.active}')


def worker(sem, pool):
    with sem:
        th_name = threading.current_thread().name
        print(f'{th_name} ожидает присоединения к пулу')
        pool.makeRequest(th_name)
        time.sleep(0.5)
        pool.gotRequest(th_name)

   
sem = threading.Semaphore(10)


pool = ActivePool()

for i in range(50):
    t = threading.Thread(
        target=worker,
        args=(sem, pool),
    )
    t.start()
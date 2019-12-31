import time
import threading


def loop():
    print("Thread %s is running" % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("Thread %s >>> %s " % (threading.current_thread().name, n))
        time.sleep(1)
    print("Thread %s ended." % threading.current_thread().name)


print("Thread %s is running" % threading.current_thread().name)
#t = threading.Thread(target=loop, name='Thread Loop')
#t.start()
#t.join()
#print("Thread %s ended" % threading.current_thread().name)

balance = 0


# 设置模型的状态
class ModelStatus:
    def __init__(self):
        self.lock = threading.Lock()
        self.model_running = False

    # 如果模型未运行，返回False，否则返回True
    def check(self):
        try:
            self.lock.acquire()
            if self.model_running:
                return True
            else:
                self.model_running = True
                print('Starting model...')
                return False
        finally:
            self.lock.release()

    # 将运行状态设为False
    def finish(self):
        try:
            self.lock.acquire()
            self.model_running = False
            print("Finishing model...")
        finally:
            self.lock.release()


status = ModelStatus()


def change_it(n):
    global balance
    global status
    if not status.check():
        balance = balance + n
        balance = balance - n
        status.finish()
    else:
        pass


def run_thread(n):
    for i in range(10):
        print("Thread %s is running" % threading.current_thread().name)
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

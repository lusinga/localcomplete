import threading


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

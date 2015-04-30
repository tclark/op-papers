import threading
from time import sleep

class Locker(threading.Thread):
    num_threads = [0]
    lock = threading.Lock()

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        self.lock.acquire()
        self.num_threads[0] += 1
        print("Thread {0} running. I am number {1}. ".format(self.name, self.num_threads[0]))
        self.lock.release()
        sleep(1)
        self.lock.acquire()
        self.num_threads[0] -= 1
        self.lock.release()
        

if __name__ == "__main__":
    t1 = Locker("t1")
    t2 = Locker("t2")
    t3 = Locker("t3")
    t4 = Locker("t4")

    t1.start()
    t2.start()
    t3.start()
    t4.start()

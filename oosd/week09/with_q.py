import os, re, threading, Queue

class PingCheck(threading.Thread):
    received_packages = re.compile(r"(\d) received")

    def __init__ (self,in_q, out_q):
        threading.Thread.__init__(self)
        self.in_q = in_q
        self.out_q = out_q
        self.daemon = True

    def run(self):
        while True:
            ip = self.in_q.get()
            print(ip)
            ping_out = os.popen("ping -q -c2 "+ ip,"r")
            line = ping_out.readline()
            n_received = re.findall(self.received_packages,line)
            result = "IP address {0}: {1} received".format(ip, n_received)
            self.out_q.put(result)
            self.in_q.task_done()



if __name__ == "__main__":
    in_queue = Queue.Queue()
    out_queue = Queue.Queue()

    for suffix in range(1,255):
        ip = "192.168.1."+str(suffix)
        in_queue.put(ip)

    for n in xrange(10):
        check = PingCheck(in_queue, out_queue)
        check.start()

    out = raw_input()

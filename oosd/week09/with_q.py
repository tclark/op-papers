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
            result = self.do_ping(ip)
            self.out_q.put(result)
            self.in_q.task_done()

    def do_ping(self, ip):
       ping_out = os.popen("ping -q -c2 "+ ip,"r")
       while True:
           line = ping_out.readline()
           if not line: break
           n_received = re.findall(self.received_packages,line)
           if n_received:
                result = "IP address {0}: {1} received".format(ip, n_received[0])
       return result


class PingReporter(threading.Thread):

    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q
        self.daemon = True

    def run(self):
        while True:
            print(self.q.get())
            self.q.task_done()

if __name__ == "__main__":
    in_queue = Queue.Queue()
    out_queue = Queue.Queue()

    r = PingReporter(out_queue)
    r.start()
    for suffix in range(1,255):
        ip = "10.25.1."+ str(suffix)
        in_queue.put(ip)

    for n in xrange(10):
        check = PingCheck(in_queue, out_queue)
        check.start()

    out = raw_input()

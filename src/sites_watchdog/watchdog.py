#coding=utf-8
from threading import Thread
import subprocess
from Queue import Queue
from mail import send_mail

num_threads = 4
queue = Queue()
ips = ["202.107.200.69", "202.107.200.83", "202.107.200.88", "202.107.200.89"]
error_message = []
#wraps system ping command
def pinger(i, q):
    """Pings subnet"""
    while True:
        ip = q.get()
        print "Thread %s: Pinging %s" % (i, ip)
        ret = subprocess.call("ping -c 1 %s" % ip,
                        shell=True,
                        stdout=open('/dev/null', 'w'),
                        stderr=subprocess.STDOUT)
        if ret == 0:
            print "%s: is alive" % ip
        else:
            error_message.append("%s" % ip)
        q.task_done()
#Spawn thread pool
for i in range(num_threads):

    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()
#Place work in queue
for ip in ips:
    queue.put(ip)
#Wait until worker threads are done to exit    
queue.join()
print error_message
if error_message:
    send_mail('以下服务器停止相应',';'.join(error_message))

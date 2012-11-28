#coding=utf-8
import subprocess
from time import sleep
from mail import send_mail
import sys
from daemonize import daemonize
def watcher():
    while True:
        ip = '192.168.88.245'
        ret = subprocess.call("ping -c 1 %s" % ip,
                        shell=True,
                        stdout=open('/dev/null', 'w'),
                        stderr=subprocess.STDOUT)
        if ret == 0:
            sys.stderr.write("%s: is alive" % ip)
        else:
            send_mail('服务器停止相应:',ip)
        sleep(3)
if __name__ == '__main__':
    daemonize(stdout='/tmp/stdout.log', stderr='/tmp/stderr.log')
    watcher()

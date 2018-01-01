from multiprocessing import Process
import os
"""多进程"""

def run(name):
    print(name)
    print(os.getppid())
    print(os.getpid())


for i in range(10):
    p = Process(target=run,args=('name :%s' % i,))
    p.start()
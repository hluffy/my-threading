import threading
import time

"""通过类的方式启动线程"""
class MyThreading(threading.Thread):
    def __init__(self,n):
        super(MyThreading,self).__init__()
        self.n = n

    def run (self):
        print('running task ',self.n)
        time.sleep(2)


if __name__ == '__main__':
    t1 = MyThreading('t1')
    t2 = MyThreading('t2')


    t1.start()
    t2.start()
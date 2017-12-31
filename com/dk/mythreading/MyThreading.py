import threading
import time

def run(n):
    print('test ',n)
    time.sleep(2)
    print('test %s done'% n)


# t1 = threading.Thread(target=run,args=('t1',))
# t2 = threading.Thread(target=run,args=('t2',))
#
# t1.start()
# t2.start()

# run('t1')
# run('t2')
t_objs = []
start_time = time.time()
for i in range(50):
    t = threading.Thread(target=run,args=('t-%s' % i,))
    t.setDaemon(True)   #将当前线程设置为守护线程
    t.start()
    t_objs.append(t)


# for t in t_objs:
#     t.join()


# threading.current_thread()查看当前线程
# threading.active_count()查看当前活动的线程个数
print('end',threading.current_thread(),threading.active_count())
print('use time : ',time.time() - start_time)

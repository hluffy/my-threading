import queue
import threading,time


q = queue.Queue(maxsize=10)
def put():
    count = 1
    while True:
        q.put('食物：%s' %  count)
        print('生产了食物：%s' % count)
        count += 1



def get():
    # while q.qsize() > 0:
    while True:
        print(q.get())
        time.sleep(1)


t1 = threading.Thread(target=put)
t2 = threading.Thread(target=get)

t1.start()
t2.start()
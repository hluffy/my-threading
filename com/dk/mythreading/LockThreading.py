import threading
import time

num = 0
def run():
    # 获取锁
    # 加锁之后程序就变成了串行的
    lock.acquire()

    # 加入信号量
    semaphore.acquire()

    global num
    num += 1
    # 释放锁
    lock.release()
    # 释放信号量
    semaphore.release()

# python2需要加锁，python3不需要加锁
# 锁一次只允许一个线程运行
lock = threading.Lock()


# 信号量,允许同时有三个线程运行
semaphore = threading.BoundedSemaphore(5)

t_objs = []
for i in range(50):
    t = threading.Thread(target=run)
    t.start()
    t_objs.append(t)

print(num)



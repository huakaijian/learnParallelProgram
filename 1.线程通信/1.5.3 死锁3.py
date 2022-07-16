from threading import Thread, RLock

import time

lock1 = RLock()

lock2 = RLock()


# RLock 同样会死锁

def fun1():
    lock1.acquire()
    print("线程1 锁住了lock1")
    time.sleep(0.1)
    lock2.acquire()
    for i in range(10):
        print(f"线程1，{i}")
    lock2.release()
    lock1.release()


def fun2():
    lock2.acquire()
    print("线程2 锁住了lock2")
    time.sleep(0.1)
    lock1.acquire()
    for i in range(10):
        print(f"线程2，{i}")
    lock1.release()
    lock2.release()


t1 = Thread(target=fun1)  # 创建一个线程对象

t2 = Thread(target=fun2)  # 创建一个线程对象

t1.start()  # 开启线程的执行

t2.start()

t1.join()

t2.join()

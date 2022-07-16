from threading import Thread, RLock

lock1 = RLock()  # 创建一个互斥锁


def fun1():
    print("进入 fun1")
    lock1.acquire()
    print("线程1 锁住了lock1")
    fun2()
    lock1.release()
    print("退出 fun1")


def fun2():
    print("进入fun2")
    lock1.acquire()
    for i in range(10):
        print(f"线程1，{i}")
    lock1.release()
    print("退出fun2")


t1 = Thread(target=fun1)  # 创建一个线程对象
t1.start()
t1.join()

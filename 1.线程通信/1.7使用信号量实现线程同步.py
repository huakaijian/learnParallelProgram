import threading
import time
import random

# 斥锁同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据 ，
# 比如厕所有3个坑，那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去。
# 内部counter内部默认值是1
# 小于0则会报错
semaphore = threading.Semaphore(0)


def consumer():
    print("consumer is running")
    semaphore.acquire()
    print(f"comsumer notify:{item}")


def producer():
    global item
    time.sleep(10)
    item = random.randint(0, 1000)
    print(f"producer notify: {item}")
    semaphore.release()


if __name__ == '__main__':
    for i in range(5):
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    print("end")

import threading
import time


def function1():
    print("function1 call")
    time.sleep(1)
    print("function1 end")
    return


def function2():
    print("function2 call")
    time.sleep(2)
    print("function2 end")
    return


if __name__ == '__main__':

    t1 = threading.Thread(target=function1)
    t2 = threading.Thread(target=function2)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    print("main end")

import threading
import time


def function(i):
    time.sleep(3)
    print(f"function call {i}")
    return


threads = []

t = threading.Thread(target=function, args=(5,))
threads.append(t)
t.start()
print("当前线程数量", threading.active_count())
print("当前线线程标识符", threading.get_ident())
print("当前线程列表", threading.enumerate())
t.join()

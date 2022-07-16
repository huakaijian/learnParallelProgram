import threading
import time


class MyThread(threading.Thread):

    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self) -> None:
        print(f"start {self.name}")
        print_time(self.name, self.counter, 5)
        print(f"exiting {self.name}")


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print(f"{thread_name},{time.ctime(time.time())}")
        counter -= 1


t1 = MyThread(3, "t1", 5)
t2 = MyThread(3, "t2", 5)

t1.start()
t2.start()
t1.join()
t2.join()
print("exit main thread")

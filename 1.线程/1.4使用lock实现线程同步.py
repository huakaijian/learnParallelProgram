import threading

resource_with_lock = 0
resource_without_lock = 0

resource_lock = threading.Lock()

COUNT = 1000000


def increment_with_lock():
    global resource_with_lock
    for i in range(COUNT):
        resource_lock.acquire()
        resource_with_lock += 1
        resource_lock.release()


def decrement_with_lock():
    global resource_with_lock
    for i in range(COUNT):
        resource_lock.acquire()
        resource_with_lock -= 1
        resource_lock.release()


def increment_without_lock():
    global resource_without_lock
    for i in range(COUNT):
        resource_without_lock += 1


def decrement_without_lock():
    global resource_without_lock
    for i in range(COUNT):
        resource_without_lock -= 1


if __name__ == '__main__':
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print(f"resource_with_lock :{resource_with_lock}")
    print(f"resource_without_lock :{resource_without_lock}")

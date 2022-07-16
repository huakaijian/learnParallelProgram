import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print(f"starting {name}")
    time.sleep(3)
    print(f"exiting {name}")


if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print("process before execution:", p, p.is_alive())
    p.start()
    print("process starting", p, p.is_alive())
    p.terminate()
    print("process terminated", p, p.is_alive())
    p.join()
    print("process joined", p, p.is_alive())
    print("process exit code", p, p.exitcode)

import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print(f"starting {name}")
    time.sleep(3)
    print(f"exiting {name}")


if __name__ == '__main__':
    process_with_name = multiprocessing.Process(name="foo_process", target=foo)
    # process_with_name.daemon = True # 是否后台进行
    process_with_default_name = multiprocessing.Process(target=foo)
    process_with_name.start()
    process_with_default_name.start()

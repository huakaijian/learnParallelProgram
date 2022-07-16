# 为什么要线程池？
# 主线程可以获取某一个线程的状态或，某一个任务的状态，以及返回值
# 一个线程王朝后，主线程立即知道
# future 可以让多线程和多进程编程接口一致

from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import time


def get_html(times):
    time.sleep(times)
    # print(f"get page {times} ok")
    return times


executor = ThreadPoolExecutor(max_workers=2)
# summit 函数提交执行函数到线程池
# task1 = executor.submit(get_html, (3))  # 非阻塞
# task2 = executor.submit(get_html, (2))

# done 方法用于判定某个任务是否完成
# print(task1.done())
# print(task2.cancel())  # 执行中取消不了
# time.sleep(3)
# print(task1.done())
# print(task1.result())

# 获取已经成功的task返回

urls = [3, 2, 4]

all_task = [executor.submit(get_html, (url)) for url in urls]
wait(all_task)
print("main")
# for future in as_completed(all_task):
#     data = future.result()
#     print(f"get {data} ok")

# for data in executor.map(get_html, urls):
#     print(f"get {data} ok")

from threading import Thread, Condition
import time

items = []
condition = Condition()


class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def consume(self):
        global condition
        global items
        condition.acquire()
        if len(items) == 0:
            condition.wait()
            print("consumer notify: no item to consumer")
        items.pop()
        print(f"consumer notify:consumed 1 item,item length:{len(items)}")
        condition.notify()
        condition.release()

    def run(self) -> None:
        for i in range(20):
            time.sleep(1)
            self.consume()


class Producer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global condition
        global items
        condition.acquire()
        if len(items) == 5:
            condition.wait()
            print(f"producer notify: item length:{len(items)}")
            print("producer notify: stop item to producer")
        items.append(1)
        print(f"producer notify: total item length:{len(items)}")
        condition.notify()
        condition.release()

    def run(self) -> None:
        for i in range(20):
            time.sleep(0.1)
            self.produce()


if __name__ == '__main__':
    producer = Producer()
    consumer = Consumer()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print("END")

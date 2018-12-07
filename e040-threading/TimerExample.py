import threading


def count(**numbers):
    for i in range(numbers["from"], numbers["until"]):
        print("Thread name %s and identifier %s, number %d" % (
            threading.current_thread().getName(),
            threading.current_thread().ident,
            i))


thread1 = threading.Timer(0.3, count, kwargs={'from': 10, 'until': 15})
thread2 = threading.Timer(0.6, count, kwargs={'from': 20, 'until': 25})
thread1.start()
thread2.start()

thread1.cancel()

"""
output:
    Thread name Thread-2 and identifier 139811976316672, number 20
    Thread name Thread-2 and identifier 139811976316672, number 21
    Thread name Thread-2 and identifier 139811976316672, number 22
    Thread name Thread-2 and identifier 139811976316672, number 23
    Thread name Thread-2 and identifier 139811976316672, number 24
"""
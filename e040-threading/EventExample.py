import threading, time

event = threading.Event()

def count():
    event.wait()
    for i in range(5):
        print("%s, value: %d" % (threading.current_thread().getName(), i))



thread1 = threading.Thread(name='thread1', target=count)
thread2 = threading.Thread(name='thread2', target=count)
thread1.start()
thread2.start()

time.sleep(2)
event.set()


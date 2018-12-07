import threading

print("################### 1 ###################")
def count(n_thread, **numbers):
    for i in range(numbers["from"], numbers["until"]):
        print("Thread name %s and identifier %s, thread number %d, number %d" % (
            threading.current_thread().getName(),
            threading.current_thread().ident,
            n_thread,
            i))


for thread_n in range(3):
    thread = threading.Thread(
        target=count,
        args=(thread_n,),
        kwargs={'from': thread_n * 30,
                'until': thread_n * 30 + 5})
    thread.start()


print("################### 2 ###################")
def count10():
    for i in range(10):
        print("Thread name %s and number %d" % (
            threading.current_thread().getName(),
            i))


def count100():
    for i in range(100):
        print("Thread name %s and number %d" % (
            threading.current_thread().getName(),
            i))


thread1 = threading.Thread(name='count10',
                           target=count10)

thread2 = threading.Thread(name='count100',
                           target=count100,
                           daemon=True)
thread1.start()
thread2.start()


print("################### 3 ###################")
def count5():
    for i in range(5):
        print("Thread name %s and number %d" % (
            threading.current_thread().getName(),
            i))

for thread_n in range(0, 5):
    thread = threading.Thread(name=thread_n,
                               target=count5,
                               daemon=True)
    thread.start()


main_thread = threading.main_thread()
for thread in threading.enumerate():
    if thread is main_thread:
        continue

    print(thread.getName(),
        thread.isDaemon(),
        thread.is_alive(),
        threading.active_count())

    thread.join()


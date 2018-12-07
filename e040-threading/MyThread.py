import threading


class MyThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, kwargs=kwargs, daemon=daemon)
        self.arg1 = args[0]
        self.arg2 = args[1]
        self.arg3 = args[2]

    def run(self):
        for i in range(self.arg1, self.arg2, self.arg3):
            print("Thread name %s and number %d" % (threading.current_thread().getName(), i))


my_thread = MyThread(args=(10, 50, 10))
my_thread.start()


"""
output:
    Thread name Thread-1 and number 10
    Thread name Thread-1 and number 20
    Thread name Thread-1 and number 30
    Thread name Thread-1 and number 40
"""
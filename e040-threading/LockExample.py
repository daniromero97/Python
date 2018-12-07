import threading

total, attempts = 0, 0
lock = threading.Lock()

def count():
    global total
    global attempts
    for i in range(5):
        blocking = lock.acquire(blocking=False)
        try:
            if blocking:
                total = total + i
                print("Total", total)
            else:
                attempts += 1
        finally:
            if blocking:
                lock.release()


thread1 = threading.Thread(target=count)
thread2 = threading.Thread(target=count)
thread1.start()
thread2.start()

print("Attempts:", attempts)
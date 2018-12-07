import threading


def food_management():
    global eating
    print("Waiting:", threading.current_thread().getName())
    with threading.Semaphore(MAX):
        eating.append(threading.current_thread().getName())
        print("Currently eating ---", eating)
        eating.remove(threading.current_thread().getName())
        print("Currently eating ---", eating)


MAX = 2
eating = []
for i in range(5):
    thread = threading.Thread(target=food_management, name=str(i))
    thread.start()

import threading, random, math

def sum():
    global list, condition
    with condition:
        print("Waiting...")
        condition.wait()
        print('Sum:', math.fsum(list))


def numbers():
    global list, condition
    with condition:
        print("Generating numbers...")
        for i in range(0, 100):
            list.append(random.randint(1,100))
        condition.notifyAll()
        print("Notify...")


list = []
condition = threading.Condition()

thread1 = threading.Thread(target=sum)
thread2 = threading.Thread(target=numbers)
thread1.start()
thread2.start()
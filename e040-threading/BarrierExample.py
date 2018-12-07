import threading, random

def num():
    print("Waiting... %d" % (barrier.n_waiting))
    n = random.randint(0, 10)
    barrier.wait()
    print(n)


NUMBER = 5
barrier = threading.Barrier(NUMBER)

for i in range(NUMBER):
    thread = threading.Thread(target=num)
    thread.start()




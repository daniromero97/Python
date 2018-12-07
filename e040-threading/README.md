# threading

- To execute several simultaneously in the same process we use the class threading.
- Each execution flow is called thread or subprocess.
- Each program that we create has a main thread.
- For each thread there is a pointer.
- The execution of a thread can be stopped temporarily or indefinitely.
- A process will continue to run while at least one thread remains active.

- Running multiple threads is similar to running several programs but with some advantages:
    - The running threads of a process share the same data space as the main thread, so they can access the same information or communicate with each other more easily than if they were in separate processes.
    - Running multiple threads in the same process requires fewer resources than running multiple processes.
    - Simplifies the design of applications that perform concurrent operations.
    

### Define a threads by constructor

- Passing an invokable object to the constructor, as a function.

##### current_thread(), getName(), ident, start()

- current_thread() return the current Thread object, corresponding to the caller’s thread of control. 

##### name, target, args and kwargs

- Use of "target" to pass the name of the function and if the function has arguments we use "args" and "kwargs".
    
    ```
    def count(n_thread, **numbers):
        for i in range(numbers["from"], numbers["until"]):
            print("Thread name %s and identifier %s, thread number %d, number %d" % (
                threading.current_thread().getName(),
                threading.current_thread().ident,
                n_thread,
                i))
    
    for thread_n in range(3):
        thread = threading.Thread(
            name='count',
            target=count,
            args=(thread_n,),
            kwargs={'from': thread_n*30,
                    'until': thread_n*30+5})
        thread.start()
    ```

##### Daemons

- Daemons (special threads), the main thread of the program may end even if one or more child threads have not completed their task.    
- The daemon argument is assigned True when creating the Thread object or it is set with the set_daemon() method.

    ```
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
    ```

##### join(), is_alive(), enumerate(), active_count()

- Use of the join() method to make the main thread wait for the daemon thread to complete its work.
    
    ```
    thread.join()
    ```    

- And use the is_alive() method to know if a thread is active or not.

    ```
    thread.is_alive()
    ```    

- active_count() return the number of Thread objects currently alive. 

    ```
    threading.active_count()
    ```
            
- If we want to keep track of the active threads, we will use enumerate(), we must bear in mind that it also returns the main thread and it does not accept certain operations. 

    ```
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
    ```   
    
    
### Define a threads creating a class
    
- Creating a class that inherits from Thread in which the run() method and the __init __ () constructor is overwritten.  

    ```
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
    ```


### Lock Objects

- Allows blocking management to prevent threads from modifying shared variables at the same time.

##### acquire ()

- It allows a thread to block other threads at a point in the program where data is read and updated.

##### release ()

- Release the blockade.

```
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
```


### RLock Objects

- Same as Lock objects but these allow a block to be acquired by the same thread several times.

### Condition Objects

- They are used to synchronize the execution of several threads.
- Locks are usually linked to operations that have to be carried out before others.

##### notify() and notify_all()

- The notify() method wakes up one of the threads waiting for the condition variable, if any are waiting. 
- The notify_all() method wakes up all threads waiting for the condition variable.

```
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
```


### Semaphore Objects

- Advanced blocking object that uses an internal counter to control the number of threads that can concurrently access a part of the code.
- If the number of threads that try to access exceeds, at a given moment, the established value, a blockage will be released when the operations are completed.
- Used to restrict access to resources with limited capacity.

```
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
```


### Event Objects

- This is one of the simplest mechanisms for communication between threads: one thread signals an event and other threads wait for it.

##### set(), clear() and wait()

- An event object manages an internal flag that can be set to true with the set() method and reset to false with the clear() method. The wait() method blocks until the flag is true.

    ```
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
    ```   
    
    
### Timer Objects

- Thread type that allows to adjust the beginning of its execution with a waiting time.

##### cancel()

- In the wait its execution can be canceled.
    
    ```
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
    ``` 
    

### Barrier Objects    

- This class provides a simple synchronization primitive for use by a fixed number of threads that need to wait for each other. Each of the threads tries to pass the barrier by calling the wait() method and will block until all of the threads have made their wait() calls. At this point, the threads are released simultaneously.
- The barrier can be reused any number of times for the same number of threads.

```
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
```
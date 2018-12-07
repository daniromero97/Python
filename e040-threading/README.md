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
    

### Define a threads

##### By constructor

- Passing an invokable object to the constructor, as a function.
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
            target=count,
            args=(thread_n,),
            kwargs={'from': thread_n*30,
                    'until': thread_n*30+5})
        thread.start()
    
    
    """
    output:
        Thread name Thread-1 and identifier 140692410537728, thread number 0, number 0
        Thread name Thread-2 and identifier 140692402145024, thread number 1, number 30
        Thread name Thread-2 and identifier 140692402145024, thread number 1, number 31Thread name Thread-3 and identifier 140692324087552, thread number 2, number 60
        
        Thread name Thread-2 and identifier 140692402145024, thread number 1, number 32
        Thread name Thread-2 and identifier 140692402145024, thread number 1, number 33
        Thread name Thread-2 and identifier 140692402145024, thread number 1, number 34
        Thread name Thread-1 and identifier 140692410537728, thread number 0, number 1
        Thread name Thread-1 and identifier 140692410537728, thread number 0, number 2
        Thread name Thread-1 and identifier 140692410537728, thread number 0, number 3
        Thread name Thread-1 and identifier 140692410537728, thread number 0, number 4Thread name Thread-3 and identifier 140692324087552, thread number 2, number 61
        
        Thread name Thread-3 and identifier 140692324087552, thread number 2, number 62
        Thread name Thread-3 and identifier 140692324087552, thread number 2, number 63
        Thread name Thread-3 and identifier 140692324087552, thread number 2, number 64
    """
    ```

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
    
    
    """
    output:
        Thread name count10 and number 0
        Thread name count10 and number 1
        Thread name count10 and number 2
        Thread name count10 and number 3
        Thread name count10 and number 4Thread name count100 and number 0
        Thread name count100 and number 1
        Thread name count100 and number 2
        Thread name count100 and number 3
        Thread name count100 and number 4
        Thread name count100 and number 5
        Thread name count10 and number 5
        Thread name count10 and number 6
        Thread name count100 and number 6
        
        Thread name count10 and number 7
        Thread name count100 and number 7
        Thread name count10 and number 8
        Thread name count10 and number 9
    """
    ```

- Use of the join() method to make the main thread wait for the daemon thread to complete its work.
    
    ```
    thread2.join()
    ```    

- And use the isAlive() method to know if a thread is active or not.

    ```
    thread2.isAlive()
    ```    
    
- If we want to keep track of the active threads, we will use enumerate(), we must bear in mind that it also returns the main thread and it does not accept certain operations. 

    ```
    def count10():
        for i in range(10):
            print("Thread name %s and number %d" % (
                threading.current_thread().getName(),
                i))
    
    for thread_n in range(0, 5):
        thread = threading.Thread(name=thread_n,
                                   target=count10,
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
    
    
    """
    output:
        Thread name Thread-1 and number 0
        Thread name 1 and number 0
        Thread name 1 and number 1
        Thread name 1 and number 2
        Thread name 1 and number 3Thread name Thread-1 and number 1
        Thread name 1 and number 4
        Thread name 1 and number 5
        
        Thread name Thread-1 and number 2
        Thread name 1 and number 6
        Thread name Thread-1 and number 3Thread name 2 and number 0
        Thread name 2 and number 1
        Thread name 1 and number 7
        Thread name 2 and number 2
        Thread name 2 and number 3
        Thread name 1 and number 8
        Thread name 1 and number 9
        Thread name 2 and number 4
        
        Thread name 2 and number 5
        Thread name 2 and number 6Thread name Thread-1 and number 4
        Thread name Thread-1 and number 5
        
        Thread name 2 and number 7Thread name Thread-1 and number 6
        Thread name Thread-1 and number 7
        
        Thread name 2 and number 8
        Thread name Thread-1 and number 8
        Thread name 2 and number 9
        Thread name Thread-1 and number 9
        Thread name 3 and number 0
        Thread name 3 and number 1
        Thread name 3 and number 2
        Thread name 4 and number 0
        Thread name 4 and number 1
        3 True Thread name 4 and number 2
        Thread name 4 and number 3
        Thread name 4 and number 4
        Thread name 4 and number 5
        Thread name 4 and number 6
        Thread name 4 and number 7
        Thread name 3 and number 3
        True 3
        Thread name 3 and number 4
        Thread name 3 and number 5
        Thread name 3 and number 6Thread name 4 and number 8
        Thread name 4 and number 9
        
        Thread name 3 and number 7
        Thread name 3 and number 8
        Thread name 3 and number 9
        4 True False 1
    """
    ```   
    
    
- Creating a class that inherits from Thread in which the run () method or the __init __ () constructor is overwritten.  

    
    
    
    
    
    
    
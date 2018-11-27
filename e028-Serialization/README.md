# Serialization (marshalling)

- Process that transforms the state of an object into a format that can be stored, retrieved and transported.
- Sometimes we have the need to save an object to be able to recover it later, or it may be necessary to send an object through the network, to another program in Python running on another machine.
- In Python there are several modules (marshal, pickle, cPickle and shelve).

## Modules
### marshal
- It contains functions that can read and write Python values in binary format.
- This is not a generic persistence module. The marshal module exists above all to support the writing and reading of the "pseudo-compiled" code of the Python modules of the .pyc files.
- It only allows to serialize simple objects (most of the types included by default in Python), and does not provide any type of security mechanism or checks against corrupted or badly formatted data.
- Oficial documentation: https://docs.python.org/2/library/marshal.html

### pickle
- It allows to serialize almost any object and has some basic security mechanisms.
- It is written in Python, as marshal, so it is also much slower.
- Differences with marshal:
    - Recursive objects (that contain references to themselves): pickle keeps the account of the objects already serialized, so that subsequent references to the same object do not have to be re-serialized.
    - Shared objects (references to the same object from different places): The case is similar to that of recursive objects; pickle stores the object once and makes sure that the rest of the references point to the copy. Something that can be very important in the case of mutable objects.
    - Classes defined by the user and instances of them: pickle can save and retrieve instances of classes transparently. The definition of the class must be importable and reside in the same module it was in when the object was stored.
- It uses a printable ASCII representation (You can choose a binary format).
- It is slightly more voluminous than a binary representation. The biggest advantage is that to debug or retrieve information it is possible for a person to read the file with a text editor.
- Oficial documentation: https://docs.python.org/2/library/pickle.html

### cPickle
- The cPickle module implements the same algorithm, in C instead of Python. It is many times faster than the Python implementation, but does not allow the user to subclass.
- It is a module of Python 2, in Python 3 cPickle was renamed to _pickle and is used automatically by the pickle module whenever possible. Users of version 3.x should not use _pickle directly.
- Oficial documentation: https://docs.python.org/2/library/pickle.html#module-cPickle

### shelve
- Works on pickle and allows you to store objects like a dictionary.
- It is very useful when we want to store many objects and then access only some of them.
- Oficial documentation: https://docs.python.org/2/library/shelve.html


## Serialization examples
#### import
```
try:
    import cPickle as pickle
except ImportError:
    import pickle
```

#### dump()
```
animal_list = ["dog", "cat", "frog", "fish"]
binary_file = open("animals", "wb")
pickle.dump(animal_list, binary_file)
binary_file.close()
```

#### load()
```
binary_file = open("animals", "rb")
animal_list = pickle.load(binary_file)
print(animal_list)
```





# os

- The module os allows us to access functionalities dependent on the Operating System.
- Above all, those that tell us about the environment of the same and we allow you to manipulate the directory structure.

##### os.access(path, access_mode)

- Know if you can access a file or directory 

- Accesss_mode:
    - os.F_OK − Value to pass as the mode parameter of access() to test the existence of path.
    - os.R_OK − Value to include in the mode parameter of access() to test the readability of path.
    - os.W_OK Value to include in the mode parameter of access() to test the writability of path.
    - os.X_OK Value to include in the mode parameter of access() to determine if path can be executed.


```
print("access:", os.access("test_package/test.txt", os.R_OK))
if os.access("test_package/test.txt", os.R_OK):
    with open("test_package/test.txt") as fp:
        print("reading ->", fp.read())

"""
output:
    access: True
    reading -> this is a test
"""
```


##### os.getcwd()

- Know the current directory

```
print(os.getcwd())

"""
output:
    /home/user/exampleFolder/Python/e035-Os
"""
```


##### os.chdir(new_path)

- Change working directory

```
print(os.getcwd())
os.chdir("/home")
print(os.getcwd())

"""
output:
    /home/user/exampleFolder/Python/e035-Os
    /home
"""
```


##### os.chroot()

- Change to the root working directory

```
os.chroot("/tmp/usr")
print("Changed root path successfully!!")

"""
output:
    Changed root path successfully!!
"""
```


##### os.chmod(path, permits)

- Change the permissions of a file or directory
- Permits:
    - stat.S_ISUID − Set user ID on execution.
    - stat.S_ISGID − Set group ID on execution.
    - stat.S_ENFMT − Record locking enforced.
    - stat.S_ISVTX − Save text image after execution.
    - stat.S_IREAD − Read by owner.
    - stat.S_IWRITE − Write by owner.
    - stat.S_IEXEC − Execute by owner.
    - stat.S_IRWXU − Read, write, and execute by owner.
    - stat.S_IRUSR − Read by owner.
    - stat.S_IWUSR − Write by owner.
    - stat.S_IXUSR − Execute by owner.
    - stat.S_IRWXG − Read, write, and execute by group.
    - stat.S_IRGRP − Read by group.
    - stat.S_IWGRP − Write by group.
    - stat.S_IXGRP − Execute by group.
    - stat.S_IRWXO − Read, write, and execute by others.
    - stat.S_IROTH − Read by others.
    - stat.S_IWOTH − Write by others.
    - stat.S_IXOTH − Execute by others.

```
os.chmod("/tmp/usr.txt", stat.S_IWOTH)
print("Changed mode successfully!!")

"""
output:
    Changed mode successfully!!
"""
```


##### os.chown(path, permits)

- Change the owner of a file or directory

```
os.chown("/tmp/usr.txt", 100, -1)
print("Changed ownership successfully!!")

"""
output:
    Changed ownership successfully!!
"""
```


##### os.mkdir(path[, mode])

- Create a directory

```
os.mkdir("/test_package/test.txt", 0o755);
print("Path is created")

"""
output:
    Path is created
"""
```


##### os.mkdirs(path[, mode])

- Create directories recursively

```
os.mkdirs("/test_package/test.txt", 0o755);
print("Path is created")

"""
output:
    Path is created
"""
```


##### os.remove(path)

- Delete a file

```
os.remove("/test_package/test.txt")
print("Path is removed")

"""
output:
    Path is removed
"""
```


##### os.rmdir(path)

- Delete a directory

```
os.rmdir("/test_package/test.txt")
print("Dir is removed")

"""
output:
    Path is removed
"""
```


##### os.removedirs(path)

- Delete directories recursively

```
os.removedirs("/test_package")
print("Dirs is removed")

"""
output:
    Dirs is removed
"""
```


##### os.rename(current, new)

- Rename a file

```
os.rename("test_package/test.txt", "test_package/test2.txt")
print("Rename")

"""
output:
    Rename
"""
```

##### Oficial documentation 

- https://docs.python.org/3/library/os.html#os.chdir



















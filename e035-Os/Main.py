import os, stat

print("####################### 1 #######################")
print("access:", os.access("test_package/test.txt", os.R_OK))
if os.access("test_package/test.txt", os.R_OK):
    with open("test_package/test.txt") as fp:
        print("reading ->", fp.read())

"""
output:
    access: True
    reading -> this is a test
"""


print("####################### 2 #######################")
print(os.getcwd())

"""
output:
    /home/user/exampleFolder/Python/e035-Os
"""


print("####################### 3 #######################")
print(os.getcwd())
os.chdir("/home")
print(os.getcwd())

"""
output:
    /home/user/exampleFolder/Python/e035-Os
    /home
"""


print("####################### 4 #######################")
os.chroot("/tmp/usr")
print("Changed root path successfully!!")

"""
output:
    Changed root path successfully!!
"""


print("####################### 5 #######################")
os.chmod("/tmp/usr.txt", stat.S_IWOTH)
print("Changed mode successfully!!")

"""
output:
    Changed mode successfully!!
"""


print("####################### 6 #######################")
os.chown("/tmp/usr.txt", 100, -1)
print("Changed ownership successfully!!")

"""
output:
    Changed ownership successfully!!
"""


print("####################### 7 #######################")
os.mkdir("/test_package/test.txt", 0o755);
print("Path is created")

"""
output:
    Path is created
"""


print("####################### 8 #######################")
os.mkdirs("/test_package/test.txt", 0o755);
print("Path is created")

"""
output:
    Path is created
"""


print("####################### 9 #######################")
os.remove("/test_package/test.txt")
print("Path is removed")

"""
output:
    Path is removed
"""


print("####################### 10 #######################")
os.removedirs("/test_package")
print("Dirs is removed")

"""
output:
    Dirs is removed
"""


print("####################### 11 #######################")
os.rename("test_package/test.txt", "test_package/test2.txt")
print("Rename")

"""
output:
    Rename
"""
print("########################### 1 ############################")
a = 0
while a<5:
    print(a)
    a+=1

"""
Output:
    0
    1
    2
    3
    4
"""


print("########################### 2 ############################")
a = 0
while True:
    a += 1
    print(a)
    if a == 3:
        break

"""
Output:
    1
    2
    3
"""

print("########################### 3 ############################")
color_list = ['red', 'blue', 'green']

for color in color_list:
    print(color)

"""
Output:
    red
    blue
    green
"""
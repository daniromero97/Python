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


print("########################### 4 ############################")
for num in range(0, 5):
    print(num)

"""
Output:
    0
    1
    2
    3
    4
"""


print("########################### 5 ############################")
sentence = "I just want you to count the letters"
counter = 0
print(len(sentence))

for letter in sentence:
    if letter == ' ':
        continue
    counter+=1

print(counter)

"""
Output:
    36
    29
"""


print("########################### 6 ############################")
sentence = "I just want you to count the letters"
counter = 0
print(len(sentence))

for letter in sentence:
    pass    # Incomplete code

print(counter)

"""
Output:
    36
    0
"""

print("########################### 7 ############################")
sentence = "Count only the length of the first word"
counter = 0

for letter in sentence:
    counter += 1
    if letter == ' ':
        break
else:
    counter = 0
    print("It was not a sentence, it was a word")

print(counter)


sentence = "Test"
counter = 0

for letter in sentence:
    counter += 1
    if letter == ' ':
        break
else:
    counter = 0
    print("It was not a sentence, it was a word")

print(counter)

"""
Output:
    6
    It was not a sentence, it was a word
    0
"""
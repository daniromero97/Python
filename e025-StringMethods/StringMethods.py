print("##################### 1 #####################")
sequence = ("This is a ", "")
s = "test"
sentence = s.join(sequence)
print(sentence)

sequence = ("This is a ", " (", ")")
sentence = s.join(sequence)
print(sentence)

"""
output:
    This is a test
    This is a test (test)
"""


print("##################### 2 #####################")
sentence = "this is a test"
separator = "is a"
tuple = sentence.partition(separator)
print(tuple)

"""
output:
    ('this ', 'is a', ' test')
"""


print("##################### 3 #####################")
sentence = "this is a test, " * 4
separator = ","
list = sentence.split(separator)
print(sentence)
print(list)

"""
output:
    this is a test, this is a test, this is a test, this is a test, 
    ['this is a test', ' this is a test', ' this is a test', ' this is a test', ' ']
"""


print("##################### 4 #####################")
sentence = """line 1
line2 
line3"""

print(sentence)
print(sentence.splitlines())

"""
output:
    line 1
    line2 
    line3
    ['line 1', 'line2 ', 'line3']
"""

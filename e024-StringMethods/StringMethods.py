print("##################### 1 #####################")
sentence = "This is a test sentence."
print(sentence)
print(sentence.startswith("This"))
print(sentence.startswith("this"))
print(sentence.startswith("this", 5))

"""
output:
    This is a test sentence.
    True
    False
    False
"""


print("##################### 2 #####################")
sentence = "This is a test sentence."
print(sentence)
print(sentence.endswith("sentence."))
print(sentence.endswith("ence."))
print(sentence.endswith("a", 5, 10))

"""
output:
    This is a test sentence.
    True
    True
    False
"""


print("##################### 3 #####################")
sentence = "This is a test sentence."
print(sentence)
print(sentence.isalnum())

sentence = sentence.replace(" ", "")
print(sentence)
print(sentence.isalnum())

sentence = sentence.replace(".", "")
print(sentence)
print(sentence.isalnum())

"""
output:
    This is a test sentence.
    False
    Thisisatestsentence.
    False
    Thisisatestsentence
    True
"""


print("##################### 4 #####################")
sentence = "This is a test sentence."
print(sentence)
print(sentence.isalpha())

sentence = sentence.replace(" ", "").replace(".", "")
print(sentence)
print(sentence.isalpha())

"""
output:
    This is a test sentence.
    False
    Thisisatestsentence
    True
"""


print("##################### 5 #####################")
sentence = "12345"
print(sentence)
print(sentence.isdigit())

sentence = "123 45"
print(sentence)
print(sentence.isdigit())

"""
output:
    12345
    True
    123 45
    False
"""


print("##################### 6 #####################")
sentence = "the test"
print(sentence)
print(sentence.islower())

sentence = "the test 100"
print(sentence)
print(sentence.islower())

sentence = "the test ..."
print(sentence)
print(sentence.islower())

"""
    output:
    the test
    True
    the test 100
    True
    the test ...
    True
"""


print("##################### 7 #####################")
sentence = "the test"
print(sentence)
print(sentence.isupper())

sentence = sentence.capitalize()
print(sentence)
print(sentence.isupper())

sentence = sentence.upper()
print(sentence)
print(sentence.isupper())

"""
    the test
    False
    The test
    False
    THE TEST
    True
"""


print("##################### 8 #####################")
sentence = "the test"
print(sentence.isspace())

sentence = "      ."
print(sentence.isspace())

sentence = "      "
print(sentence.isspace())

"""
    False
    False
    True
"""


print("##################### 9 #####################")
sentence = "the test"
print(sentence.istitle())

sentence = sentence.capitalize()
print(sentence.istitle())

sentence = sentence.title()
print(sentence.istitle())

"""
    False
    False
    True
"""

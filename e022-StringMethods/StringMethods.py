print("##################### 1 #####################")
sentence = "this IS a TEST sentence."
print(sentence)
print(sentence.capitalize())

"""
output:
    this IS a TEST sentence.
    This is a test sentence.
"""


print("##################### 2 #####################")
print(sentence)
print(sentence.upper())

"""
output:
    this is a test sentence.
    THIS IS A TEST SENTENCE.
"""


print("##################### 3 #####################")
print(sentence)
print(sentence.lower())

"""
output:
    this IS a TEST sentence.
    this is a test sentence.
"""


print("##################### 4 #####################")
print(sentence)
print(sentence.swapcase())

"""
output:
    this IS a TEST sentence.
    THIS is A test SENTENCE.
"""


print("##################### 5 #####################")
print(sentence)
print(sentence.title())

"""
output:
    this IS a TEST sentence.
    This Is A Test Sentence.
"""


print("##################### 6 #####################")
print(sentence)
print(sentence.center(40, "-"))

"""
output:
    this IS a TEST sentence.
    --------this IS a TEST sentence.--------
"""


print("##################### 7 #####################")
print(sentence)
print(sentence.ljust(40, "-"))

"""
output:
    this IS a TEST sentence.
    this IS a TEST sentence.----------------
"""


print("##################### 8 #####################")
print(sentence)
print(sentence.rjust(40, "-"))

"""
output:
    this IS a TEST sentence.
    ----------------this IS a TEST sentence.
"""


print("##################### 9 #####################")
print(sentence)
print(sentence.zfill(40))

"""
output:
    this IS a TEST sentence.
    0000000000000000this IS a TEST sentence.
"""
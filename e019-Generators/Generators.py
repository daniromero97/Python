def letters(*words):
    for word in words:
        """
        for letter in word:
            yield letter
        """
        yield from word

words = letters("example ", "reading ", "letters ", "of ", "words.")

for i in range(15):
    print(next(words))

"""
output:
    e
    x
    a
    m
    p
    l
    e
     
    r
    e
    a
    d
    i
    n
    g    
"""


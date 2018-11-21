### Instruction yield from

- Returns the sub elements that make up an element.
- For example, imagine that we declare a function to which we pass by parameters lists composed in turn of other lists, to iterate on each element we should use nested loops, but with this instruction it will not be necessary.

```
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
```
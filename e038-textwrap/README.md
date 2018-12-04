# textwrap

- Format text strings to fit the desired width.

##### wrap(text, width)

- Returns a list with the text divided into substrings of the given length.

```
text = "Lorem ipsum dolor sit amet consectetur adipiscing elit senectus, sociosqu nam enim accumsan porttitor blandit justo purus magna, pretium facilisis montes quisque scelerisque consequat cursus."
print(textwrap.wrap(text, 30))

"""
output:
    ['Lorem ipsum dolor sit amet', 'consectetur adipiscing elit', 'senectus, sociosqu nam enim', 'accumsan porttitor blandit', 'justo purus magna, pretium', 'facilisis montes quisque', 'scelerisque consequat cursus.']
"""
```


##### fill(text, width)

- Returns a string with line breaks arrived at the number of characters provided.

```
text = "Lorem ipsum dolor sit amet consectetur adipiscing elit senectus, sociosqu nam enim accumsan porttitor blandit justo purus magna, pretium facilisis montes quisque scelerisque consequat cursus."
print(textwrap.fill(text, 30))

"""
output:
    Lorem ipsum dolor sit amet
    consectetur adipiscing elit
    senectus, sociosqu nam enim
    accumsan porttitor blandit
    justo purus magna, pretium
    facilisis montes quisque
    scelerisque consequat cursus.
"""
```


##### dedent(text)

- Remove spaces or tabs at the beginning of each line of the specified text.

```
text = """   Lorem 
   ipsum 
   dolor
   sit
   amet
"""
print(text)
print(textwrap.dedent(text))

text = """Lorem 
    ipsum 
"""
print(text)
print(textwrap.dedent(text))

"""
output:
       Lorem 
       ipsum 
       dolor
       sit
       amet
    
    Lorem 
    ipsum 
    dolor
    sit
    amet
    
    Lorem 
        ipsum 
    
    Lorem 
        ipsum 
"""
```

- The indentation must be common to each of the lines.


### indent(text, indent)

- Contrary to dedent().

```
text = """Lorem 
ipsum 
dolor
sit
amet
"""
print(text)
print(textwrap.indent(text, "        "))


"""
output:
    Lorem 
    ipsum 
    dolor
    sit
    amet
    
            Lorem 
            ipsum 
            dolor
            sit
            amet
"""
```


### shorten(text, width)

- It allows to shorten a text.

```
text = "Lorem ipsum dolor sit amet"
print(text)
print(textwrap.shorten(text, 15))
print(textwrap.shorten(text, 15, placeholder="..."))

"""
output:
    Lorem ipsum dolor sit amet
    Lorem [...]
    Lorem ipsum...
"""
```


##### Oficial documentation 

- https://docs.python.org/3/library/textwrap.html#module-textwrap
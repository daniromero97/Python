import textwrap

print("###################### 1 ######################")
text = "Lorem ipsum dolor sit amet consectetur adipiscing elit senectus, sociosqu nam enim accumsan porttitor blandit justo purus magna, pretium facilisis montes quisque scelerisque consequat cursus."
print(textwrap.wrap(text, 30))

"""
output:
    ['Lorem ipsum dolor sit amet', 'consectetur adipiscing elit', 'senectus, sociosqu nam enim', 'accumsan porttitor blandit', 'justo purus magna, pretium', 'facilisis montes quisque', 'scelerisque consequat cursus.']
"""


print("###################### 2 ######################")
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


print("###################### 3 ######################")
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


print("###################### 4 ######################")
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


print("###################### 5 ######################")
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
# Python 

- (1) Introduction
    - Identifiers
    - Reserved words
    - Variables
    - Constants
    - Type of data
    - Arithmetic Operators
    - Comments
    
- (2) Dictionaries
    - What are they?
    - Add key-value pairs and modify them
    - Mix of data types
    - Some functionalities
        - del and .pop(key)
        - .clear()
        - len
        - .keys()
        - .values()
        - .copy()
        - .fromkeys(list, defaultValue)
        - dict.update(dict2)

- (3) Lists
    - What are they?
    - Negative indexes
    - Slicing
    - Shortcuts
    - Add items
        - append
        - extend
        - insert
    - Delete items
        - remove
        - del
        - pop
    - Search items
        - index
        - in
    - List operators
        - "+"
        - "+="
        - "*"
        - "*="
    - Other functionalities
        - count
        - reverse
        - min and max
        - clear
 - (4) Tuples
    - What are the tuples and comparison with lists
    - Applications
        - index and in
        - len and count
        - max and min
        - list and tuple
 - (5) Control Flow Statements
    - Basic things
        - Indentation
        - Encoding
        - Multiple assignment
    - Conditional Statements
        - Relational operators
        - Logical operators
        - if Statement
        - else Statement
        - elif Statement
- (6) Control FLow Statements
    - Iterative Statements
        - While loop
        - For loop
- (7) Strings format
    - String format vs. concatenation
    - Number format
- (8) Modules and packages
    - Import modules
    - Namespaces
    - Alias
    - Import modules without namespaces
    - Good practices
    - Something not recommended
    - Example
- (9) Functions
    - What are they?
    - Parameters
    - Default parameters
    - Keywords as parameters
    - Arbitrary parameters
    - Unpacking of parameters
- (10) Functions
    - Return calls
    - How to know if a function exists
- (11) Recursion
- (12) Introduction to object oriented programming (OOP)
- (13) Encapsulation
- (14) Inheritance
    - To inherit from another class
    - Overload of methods
    - super()
- (15) Multiple inheritance
- (16) Polymorphism
- (17) OOP Functions
    - issubclass
    - isinstance
    - dir
    - vars
    - getattr
    - setattr
    - delattr
- (18) Generators
    - Functioning
    - Utilities
    - 'yield' expression
    - Examples
- (19) Generatos
    - Instruction 'yield from'
- (20) Exceptions
    - What are they? 
    - Exception control
    - Control of more than one exception
    - 'finally' expression
- (21) Exceptions
    - Own exceptions
    - 'raise' expression
    - Exceptions defined by the user
    - 'assert' expression 
- (22) String methods
    - Formatting methods
        - capitalize()
        - upper()
        - lower()
        - swapcase()
        - title()
        - center(lenght, "caracter")
        - ljust(lenght, "caracter")
        - rjust(lenght, "caracter")
        - zfill(lenght)
    - Search methods   
        - count()
        - find()
- (23) String methods
    - Substitution methods
        - format()
        - replace()
        - strip()
        - lstrip()
        - rstrip()
- (24) String methods
    - Validation Methods
        - startswith()
        - endswith()
        - isalnum()
        - isalpha()
        - isdigit()
        - islower()
        - isupper()
        - isspace()
        - istitle()
- (25) String methods
    - Methods of union and division
        - join()
        - partition()
        - split()
        - splitlines()
- (26) Files
    - Introduction
    - Open files
    - Opening Modes
    - Methods of file
        - read()
        - readline()
        - readlines()
        - write()
        - writelines()
        - seek()
        - tell()
    - File properties
        - closed
        - mode
        - name
        - encoding
    - Automatic closing
        - Use of "with"
- (27) Random
    - random()
    - randint()
    - randrange()
    - choice()
    - shuffle()
    - sample()
    - seed()
- (28) Serialization
    - Introduction
    - Modules
        - marshal
        - pickle
        - cPickle
        - shelve
    - Serialization examples
        - import
        - dump()
        - load()       
- (29) Math
    - Constants
        - pi 
        - e
    - Angular conversion
        - degrees()
        - radians()
    - Number-theoretic and representation functions
        - ceil()
        - floor()
        - trunc()
        - fabs()
        - factorial()
        - fmod()
    - Power and logarithmic functions
        - exp()
        - log()
        - log1p()
        - log10()
        - pow()
        - sqrt()
        - hypot()
    - Trigonometric functions
        - acos()
        - asin()
        - atan()
        - cos()
        - sin()
        - tan()
    - Hyperbolic functions
        - acosh()
        - asinh()
        - atanh()
        - cosh()
        - sinh()
        - tanh()
- (30) Statistics
    - Averages and measures of central location
        - mean()
        - harmonic_mean()
        - median()
        - median_low()
        - median_high()
        - median_grouped()
        - mode()
    - Measures of spread
        - pstdev()
        - pvariance()
        - stdev()
        - variance()
- (31) Decimal
    - Introduction
    - prec
    - rounding
- (32) Fractions
    - Introduction
    - limit_denominator()
    - numerator and denominator
- (33) Datetime
    - Constants
        - MINYEAR
        - MAXYEAR
    - date
    - datetime
    - timedelta
    - date formatting
- (34) Calendar
    - weekday(year, month, day)
    - isleap(year)
    - leapdays(y1, y2)
    - monthlen(year, month)
    - prevmonth(year, month) and nextmonth(year, month)
    - monthrange(year, month)
    - month(year, month)
    - calendar(year)
- (35) Os
    - access(path, access_mode)
    - getcwd()
    - chdir(new_path)
    - chroot()
    - chmod(path, permits)
    - chown(path, permits)
    - mkdir(path[, mode])
    - mkdirs(path[, mode])
    - remove(path)
    - rmdir(path)
    - removedirs(path)
    - rename(current, new)
- (36) hashlib
    - Introduction
    - constant
        - algorithms_guaranteed
        - algorithms_available
        - digest_size
        - block_size
    - methods
        - update(data)
        - digest()
        - hexdigest()
        - copy()
    - SHAKE variable length digests
- (37) secrets
    - Introduction
    - Random numbers
        - choice(sequence)
        - randbelow(n)
        - randbits(k)
    - Generating tokens
        - token_bytes([nbytes=None])
        - token_hex([nbytes=None])
        - token_urlsafe([nbytes=None])
- (38) textwrap
    - wrap(text, width)
    - fill(text, width)
    - shorten(text, width)
    - dedent(text)
    - indent(text, indent)
        

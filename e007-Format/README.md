## Strings format

- You can format values in strings.
- The most basic use is to insert values in a string with the substitute %s.

    ```
    a,b = "Message", "Hello world!!"
    print("%s = %s" % (a, b))
    
    """
    Output:
        Message = Hello world!!
    """
    ```

- The expression is evaluated as a string and each "%s" is replaced by the values enclosed in the parentheses (the tuple) in order.
- The other characters will remain as they are.

    
#### String format vs. concatenation

- "+" is the chain concatenation operator.

    ```
    a,b = "Message", "Hello world!!"
    print(a + "=" + b)
    
    """
    Output:
        Message = Hello world!!
    """
    ```

- The values are not only concatenated, there is also a conversion of types.
- And if our variable is a number?

    ```
    a,b = "Value", 3
    print(a + "=" + b)
    
    """
    Output:
        Traceback (most recent call last):
          File ".../Python/e007-Format/Format.py", line 2, in <module>
            print(a + "=" + b)
        TypeError: can only concatenate str (not "int") to str
    """
    ```

- Trying to concatenate a string with something that is not a string throws an exception. Unlike the string format, concatenation only works when everything is strings.  
- The string format works with integers specifying %d.
    
    ```
    a,b = "Value", 3
    print("%s = %d" % (a, b))
    
    """
    Output:
        Value = 3
    """
    ```
    
    ```
    a = 3
    print("Value = %d" % (a, ))
    
    """
    Output:
        Value = 3
    """
    ```     
 
 - If we look at this last example, the tuple has only one value, so that it recognizes that it is a tuple we must include a comma.
 
 
#### More formats
 
```
a = 3.5678
print("Value = %d" % (a,))
print("Value = %f" % (a,))
print("Value = %.2f" % (a,))

"""
Output:
    Value = 3
    Value = 3.567800
    Value = 3.57
"""
```

- Used "%f" for decimal numbers.
- Used "%.nf" for to truncate the value. (n will be the number of decimals)

    
    
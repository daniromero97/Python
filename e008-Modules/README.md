## MODULES AND PACKAGES

- Each file.py is called modules.
- The modules can be contained in packages.
- A package is a folder but, for a folder to be considered a package, it must contain a file called `__init__.py`.
- The file `__init__.py` does not need to contain any instructions. In fact, it can be completely empty.
- Packages can also contain other packages.


### Import modules

- The content of each module can be used by other modules, you just have to import them.
- To import a module, use the import command, followed by the package name and the name of the module (without the .py).
- Python has its own modules, which are part of its library of standard modules, which can also be imported.


### Namespaces

- To access from the module where the import was made, any element of the imported module is done through the namespace, followed by a period (.) And the name of the element that you want to obtain.
- In Python, a namespace, is the name that has been indicated after the word import.


### Alias

- It is possible to abbreviate the namespaces by means of an "alias".
- For this, during the import, the keyword "as" is assigned followed by the alias with which we will refer in the future to that imported namespace.
- Then, to access any element of the imported modules, the namespace used will be the alias indicated during the import.


### Import modules without namespaces

- It is possible to import from a module only the desired elements.
- For this the following command of the namespace is used followed by "import" and the element that you want to import.
- To import more than one element in the same instruction each element will be separated by a comma.
- If the elements have the same name, it will be necessary to use an alias for each element.


### Good practices

- The import of modules must be done at the beginning of the document, in alphabetical order of packages and modules.
- First, the Python modules must be imported.
- Then, third-party modules and finally, the modules of the application.
- Between each block of imports, a blank line should be left.


### Something not recommended

- You can import all the elements of a module without using namespaces or aliases, so these elements will be accessed with their original name.

    ```
    from package.module import *
    print(variable)
    ```


#### Example

```
import ExternalModule as exMod
from my_package.myModule2 import age as a1
from my_package.myModule3 import age as a2

print(exMod.age)
print(a1)
print(a2)

"""
output:
    21
    22
    23
"""
```    
    
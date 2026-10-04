#--------------------------------------------------------------DOCSTRINGS------------------------------------------------------------------

#A docstring (documentation string) is a string literal used to describe what a function, class, or module does.
#It is written inside triple quotes (""" """) and placed right after the definition.
def name():
    """THIS IS A DOCSTRING LETS SEE"""
    print("hello moto")
name()

#to access the docstring
print(help(name))
print(name.__doc__)

#--------------------------------------------------------ANNOTATIONS------------------------------------------------------------------

def add(a,b:int)->int :                #Annotations don’t change how Python runs — they change how well humans and tools understand your code
    print(a+b)

add(2,3)
add('f','r')                           #output is fr as python ignores annotations

#python wont check But type checkers will: mypy, pyright, VS Code / PyCharm
#Annotations allow:thousands of files, many developers, fewer runtime crashes this is why Python added type hints in Python 3.5 (PEP 484)

#annotations for variables: example: count:int=0 or sth like that




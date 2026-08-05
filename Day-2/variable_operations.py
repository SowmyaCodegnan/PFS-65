Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
myvar = 10
Myvar =10
my_var =10
myvar10 =10
my var =10
SyntaxError: invalid syntax
my@var =10
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
myvar =10
Myvar=10
_myvar=10
2myvar =10
SyntaxError: invalid decimal literal
if =10
SyntaxError: invalid syntax
m =10
M = 20
m
10
M
20

= RESTART: C:/Users/Thummala Sudhakar/Desktop/PFS-65/Day-2/keywords.py
Traceback (most recent call last):
  File "C:/Users/Thummala Sudhakar/Desktop/PFS-65/Day-2/keywords.py", line 1, in <module>
    import keywords
  File "C:\Users/Thummala Sudhakar/Desktop/PFS-65/Day-2\keywords.py", line 3, in <module>
    print(keywords.kwlist)
AttributeError: partially initialized module 'keywords' has no attribute 'kwlist' (most likely due to a circular import)

= RESTART: C:/Users/Thummala Sudhakar/Desktop/PFS-65/Day-2/keywords.py
Traceback (most recent call last):
  File "C:/Users/Thummala Sudhakar/Desktop/PFS-65/Day-2/keywords.py", line 1, in <module>
    import keywords
  File "C:\Users/Thummala Sudhakar/Desktop/PFS-65/Day-2\keywords.py", line 3, in <module>
    print(keywords.kwlist())
AttributeError: partially initialized module 'keywords' has no attribute 'kwlist' (most likely due to a circular import)

= RESTART: C:/Users/Thummala Sudhakar/Desktop/PFS-65/Day-2/keywords.py
Traceback (most recent call last):
  File "C:/Users/Thummala Sudhakar/Desktop/PFS-65/Day-2/keywords.py", line 3, in <module>
    print(keyword.kwlist())
TypeError: 'list' object is not callable

= RESTART: C:/Users/Thummala Sudhakar/Desktop/PFS-65/Day-2/keywords.py
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

= RESTART: C:/Users/Thummala Sudhakar/Desktop/PFS-65/Day-2/keywords.py
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
a = 10
a=b=c=10
a
10
b
10
c
10
a,b,c = 10,20,30
a
10
b
20
c
30
a
10
b
20
a,b = b,a
a
20
>>> b
10
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b
10
>>> b=20
>>> b
20

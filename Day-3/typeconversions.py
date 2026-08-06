Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> float(a)
10.0
>>> str(a)
'10'
>>> complex(a)
(10+0j)
>>> bool(a)
True
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
f = 13.4
int(f)
13
complex(f)
(13.4+0j)
str(f)
'13.4'
bool(f)
True
list(f)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
c = 12+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(12+3j)'
bool(c)
True
list(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
s = 'codegnan'
a = '876543'
int(s)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
int(a)
876543
float(a)
876543.0
float(s)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'codegnan'
complex(a)
(876543+0j)
bool(a)
True
list(a)
['8', '7', '6', '5', '4', '3']
list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
set(s)
{'o', 'a', 'n', 'g', 'c', 'e', 'd'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
 l =[1,2,3,4,5,6]
 
SyntaxError: unexpected indent
l =[1,2,3,4,5,6]
int(l)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
str(l)
'[1, 2, 3, 4, 5, 6]'
bool(l)
True
tuple(l)
(1, 2, 3, 4, 5, 6)
set(l)
{1, 2, 3, 4, 5, 6}
dict(l)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
t = (1,2,3,4,5,6,7)
int(t)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
bool(t)
True
str(t)
'(1, 2, 3, 4, 5, 6, 7)'
list(t)
[1, 2, 3, 4, 5, 6, 7]
set(t)
{1, 2, 3, 4, 5, 6, 7}
dict(t)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
s= {1,2,4,5,6,7}
int(s)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
str(s)
'{1, 2, 4, 5, 6, 7}'
bool(s)
True
list(s)
[1, 2, 4, 5, 6, 7]
tuple(s)
(1, 2, 4, 5, 6, 7)
dict(s)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
d = {1:1,2:2,3:3}
int(d)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
str(d)
'{1: 1, 2: 2, 3: 3}'
complex(d)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
bool(d)
True
list(d)
[1, 2, 3]
tuple(d)
(1, 2, 3)
set(d)
{1, 2, 3}
b = True
int(b)
1
float(b)
1.0
complex(b)
(1+0j)
str(b)
'True'
list(b)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    list(b)
TypeError: 'bool' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    tuple(b)
TypeError: 'bool' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    set(b)
TypeError: 'bool' object is not iterable
dict(d)
{1: 1, 2: 2, 3: 3}
dict(b)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    dict(b)
TypeError: 'bool' object is not iterable

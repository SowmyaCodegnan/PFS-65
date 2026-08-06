Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Data Types
>>> #int float complex
>>> a = 12
>>> type(a)
<class 'int'>
>>> b = 13.4
>>> type(b)
<class 'float'>
>>> c = 12+4j
>>> type(c)
<class 'complex'>
>>> c = 12+6J
>>> c
(12+6j)
>>> # str list tuple
s = 'Codegnan'
id(s)
2013913331952
s += 'Python'
s
'CodegnanPython'
id(s)
2013913282288
s='aaaaaaaaa'
s
'aaaaaaaaa'
type(s)
<class 'str'>
l = [1,2,3,4,5,5,6]
type(l)
<class 'list'>
id(l)
2013913455744
l.append(12)
l
[1, 2, 3, 4, 5, 5, 6, 12]
id(l)
2013913455744
l = [1,12.3,"str",[1,23]]
l
[1, 12.3, 'str', [1, 23]]
type(l)
<class 'list'>
t=(1,2,3,45)
type(t)
<class 'tuple'>
t
(1, 2, 3, 45)
t=(1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t=(1,12.3,4,"c")
t
(1, 12.3, 4, 'c')
# set dict
s= {80,70,24,14,25,78,78,78,78,78}
s
{80, 70, 14, 24, 25, 78}
id(s)
2013912587776
s.add(20)
s
{80, 20, 70, 14, 24, 25, 78}
id(s)
2013912587776
a={1,12.3,"str"}
a
{1, 'str', 12.3}
set(s)
{80, 20, 70, 14, 24, 25, 78}
type(s)
<class 'set'>
d = {'productname':'XYZ','pric':876,'stock':True}
d
{'productname': 'XYZ', 'pric': 876, 'stock': True}
d
{'productname': 'XYZ', 'pric': 876, 'stock': True}
s={1,2,3,4}
s = frozenset({1,1,1,116,18,2,3})
s
frozenset({1, 2, 3, 18, 116})
a = Truee
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a = Truee
NameError: name 'Truee' is not defined. Did you mean: 'True'?
a =True
b = False
type(a)
<class 'bool'>
a={}
l=[]
t=()
s=''
s = None
s
type(s)
<class 'NoneType'>

Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

t = ()
t = tuple()
t = (1,2,3,45)
t
(1, 2, 3, 45)
t = (1)
t
1
t = (1,)
t
(1,)
t = (1,1,1,1)
t
(1, 1, 1, 1)
t= (1,23.4,"str",[1,23],(1,2,3),{1,2,3},{1:1,2:2},True)
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
type(t)
<class 'tuple'>
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
(1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
(1,2,3)*4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t[1]
23.4
t[-1]
True
t[-3]
{1, 2, 3}
t[2]
'str'
t[3:7]
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
t[::-1]
(True, {1: 1, 2: 2}, {1, 2, 3}, (1, 2, 3), [1, 23], 'str', 23.4, 1)
t[:3]
(1, 23.4, 'str')
t[-1:-3:-1]
(True, {1: 1, 2: 2})
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
23.4 in t
True
'str' in t
True
True in t
True
False  in t
False
t = (12,789,32,13,76,32,453,123,7898,1321,32)
t
(12, 789, 32, 13, 76, 32, 453, 123, 7898, 1321, 32)
sorted(t)
[12, 13, 32, 32, 32, 76, 123, 453, 789, 1321, 7898]
max(t)
7898
min(t)
12
len(t)
11
t
(12, 789, 32, 13, 76, 32, 453, 123, 7898, 1321, 32)
t.index(32)
2
t.count(32)
3
all((1,2,3))
True
any((1,2,3,00,0))
True
all((1,2,3,00,0))
False
t = 1,2,3
t
(1, 2, 3)
a,b,c = t
a
1
b
2
c
3
t = (1,2,3,4,[1,2,3],5)
t
(1, 2, 3, 4, [1, 2, 3], 5)
t[4]
[1, 2, 3]
t[4].append(5)
t
(1, 2, 3, 4, [1, 2, 3, 5], 5)
t
(1, 2, 3, 4, [1, 2, 3, 5], 5)
t=(1,2,34,4)
sum(t)
41
#mu unor uni dyn he
s = {}
type(s)
<class 'dict'>
s = set()
type(s)
<class 'set'>
s = {1,2,3,4,5,6,134124,124,2345234,312}
s
{1, 2, 3, 4, 5, 6, 134124, 2345234, 312, 124}
s = {1,1,1,1,1}
s
{1}
s = set()
s.add(1)
s.add(12.3)
s.add("str")
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
s.add((1,3,4))
s.add({1,2,3})
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s.add({1,2,3})
TypeError: unhashable type: 'set'
s.add({1:1})
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    s.add({1:1})
TypeError: unhashable type: 'dict'
s.add(False)
s
{False, 1, 'str', 12.3, (1, 3, 4)}
{1,23}+{12,4}
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    {1,23}+{12,4}
TypeError: unsupported operand type(s) for +: 'set' and 'set'
{1,2}*3
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    {1,2}*3
TypeError: unsupported operand type(s) for *: 'set' and 'int'
s
{False, 1, 'str', 12.3, (1, 3, 4)}
s[0]
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
s[::1]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    s[::1]
TypeError: 'set' object is not subscriptable
a = {1,2,3,4,5}
b = {3,5,7,8,9}
2 in a
True
10 not in a
True
a | b
{1, 2, 3, 4, 5, 7, 8, 9}
a & b
{3, 5}
a - b
{1, 2, 4}
b - a
{8, 9, 7}
a ^ b
{1, 2, 4, 7, 8, 9}
a
{1, 2, 3, 4, 5}
#{1}{1,2}{1,2,3,5},{1,2,3,4,5},{4,5}{4,5,6}
a
{1, 2, 3, 4, 5}
{1}<=a
True
{1,2,3}<=a
True
{1,7,8,9}<=a
False
a>={1,2}
True
a>={15,16}
False
m={1,2,3}
n={4,5,6}
n.isdisjoint(m)
True
a.isdisjoint(b)
False
a
{1, 2, 3, 4, 5}
a ={12,43,1,7,89, 40 ,23,44}
a
{1, 7, 40, 43, 12, 44, 23, 89}
sorted(a)
[1, 7, 12, 23, 40, 43, 44, 89]
max(a)
89
min(a)
1
len(a)
8
a.index(a)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
a.count(1)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    a.count(1)
AttributeError: 'set' object has no attribute 'count'
all({1,1,23,43,13,1})
True
any({0,''})
False
any({0,'',(),True})
True
sum(a)
259
a
{1, 7, 40, 43, 12, 44, 23, 89}
a = {1,2,3}
b = a
b.add(4)
a
{1, 2, 3, 4}
b
{1, 2, 3, 4}
c = a.copy()
c
{1, 2, 3, 4}
c.add(5)
c
{1, 2, 3, 4, 5}
a
{1, 2, 3, 4}
a
{1, 2, 3, 4}
a.add(5)
a
{1, 2, 3, 4, 5}
a.add(100)
a
{1, 2, 3, 4, 5, 100}
a.add(40)
a
{1, 2, 3, 4, 5, 100, 40}
a.add(101)
a
{1, 2, 3, 4, 5, 100, 101, 40}
a.add({10,20,30,40})
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    a.add({10,20,30,40})
TypeError: unhashable type: 'set'
a.update({10,20,30,40})
a
{1, 2, 3, 4, 5, 100, 101, 40, 10, 20, 30}
a
{1, 2, 3, 4, 5, 100, 101, 40, 10, 20, 30}
a.pop()
1
a.pop()
2
a
{3, 4, 5, 100, 101, 40, 10, 20, 30}
a.pop()
3
a.pop()
4
a
{5, 100, 101, 40, 10, 20, 30}
a.remove(101)
a
{5, 100, 40, 10, 20, 30}
a.remove(100)
a.remove(100)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    a.remove(100)
KeyError: 100
>>> a
{5, 40, 10, 20, 30}
>>> a.discard(100)
>>> a.discard(30)
>>> a
{5, 40, 10, 20}
>>> a.discard(30)
... 
>>> a
{5, 40, 10, 20}
>>> a.clear()
>>> a
set()
>>> a = frozenset({1,2,3,4})
>>> a
frozenset({1, 2, 3, 4})

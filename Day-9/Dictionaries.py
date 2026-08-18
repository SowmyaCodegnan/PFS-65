Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Dictionary mutable, ordered, heterogenoues, dynamic, unique duplicate property
>>> #int, float, str, tuple, bool, are inmutabble
>>> #Values can be muatable key must immutable and keys must be unique
>>> d = {}
>>> type(d)
<class 'dict'>
>>> d = {1:4,2:8,3;13}
SyntaxError: ':' expected after dictionary key
>>> d = {1:4,2:8,3:13}
>>> d
{1: 4, 2: 8, 3: 13}
>>> d = {}
>>> d = []
>>> d = [1]=1
SyntaxError: cannot assign to literal
>>> KeyboardInterrupt
>>> d[1]=1
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d[1]=1
IndexError: list assignment index out of range
>>> d = {}
>>> d[1]=1
>>> d[12.3]=1
>>> d["str"]=1
>>> KeyboardInterrupt
>>> d[(1,2,3)]=1
>>> d[(2+3j)]=1
>>> d[True]=1
>>> #Integers will get errors
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1}
>>> d[False]=1
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1, False: 1}
>>> d[1]=1
>>> d[2]=12.3
>>> d[3]="str"
>>> d[4]=2+3j
>>> d[5]=True
>>> d[6]=[1,2,3]
>>> d[7]=(1,2,3)
>>> d[8]={1,2,3}
>>> d[9]=frozenset({1,2,3})
>>> d[10]={1:1,2:2}
>>> d[11]=None
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1, False: 1, 2: 12.3, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 2, 3), 8: {1, 2, 3}, 9: frozenset({1, 2, 3}), 10: {1: 1, 2: 2}, 11: None}
d={}
d[1]=2
d
{1: 2}
d[1]=3
d
{1: 3}
d[1]=11
d
{1: 11}
#Operations in Dictionary
#Membership checks only key
#Get method
data = {'name', 'course', 'pfs', 'batch', '65'}
data
{'pfs', '65', 'name', 'course', 'batch'}
data = ('Dinesh', 'pfs', '65')
data
('Dinesh', 'pfs', '65')
"Dinesh" in data
True
data={'name':'Dinesh','course':'pfs','batch':65}
data
{'name': 'Dinesh', 'course': 'pfs', 'batch': 65}
'dinesh' in data
False
'course' in data
True
data['name']
'Dinesh'
data['batch']
65
data.get('name')
'Dinesh'
data.get('batch')
65
data.get('age')
data.get('age','key in not present')
'key in not present'
data.get('batch','key in not present')
65
#Methods and operations in dictionary
data={'name':'Dinesh','course':'pfs','batch':65}
data
{'name': 'Dinesh', 'course': 'pfs', 'batch': 65}
data['age']=21
data
{'name': 'Dinesh', 'course': 'pfs', 'batch': 65, 'age': 21}
data['phno']=9856532597
data
{'name': 'Dinesh', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9856532597}
data.update({'email':'dinesh@mail.com','py',:2026})
SyntaxError: ':' expected after dictionary key
data.update({'email':'dinesh@mail.com','py':2026})

data.update({'email':'dinesh@mail.com','py':2026})
data
{'name': 'Dinesh', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9856532597, 'email': 'dinesh@mail.com', 'py': 2026}
id(data)
2643971916544
data['py']
2026
data['py']=2027
.
data['py']=2027
data
{'name': 'Dinesh', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9856532597, 'email': 'dinesh@mail.com', 'py': 2027}
data['age']=22
data
{'name': 'Dinesh', 'course': 'pfs', 'batch': 65, 'age': 22, 'phno': 9856532597, 'email': 'dinesh@mail.com', 'py': 2027}
id(data)
2643971916544
data.popitem()
('py', 2027)
data
{'name': 'Dinesh', 'course': 'pfs', 'batch': 65, 'age': 22, 'phno': 9856532597, 'email': 'dinesh@mail.com'}
ddaat,pop('course')
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    ddaat,pop('course')
NameError: name 'ddaat' is not defined
data.pop('course')
'pfs'
data.pop('email')
'dinesh@mail.com'
data.pop('batch')
65
data
{'name': 'Dinesh', 'age': 22, 'phno': 9856532597}
data.clear()
data
{}
data
{}
#Values, Items, copy, min, max, set-default, Keys, length
len(data)
0
data = {'name': 'Dinesh', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9856532597, 'email': 'dinesh@mail.com', 'py': 2027}
data
{'name': 'Dinesh', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9856532597, 'email': 'dinesh@mail.com', 'py': 2027}
len(data)
7
data.keys()
dict_keys(['name', 'course', 'batch', 'age', 'phno', 'email', 'py'])
data.value()
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    data.value()
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
data.values()
dict_values(['Dinesh', 'pfs', 65, 21, 9856532597, 'dinesh@mail.com', 2027])
data.items()
dict_items([('name', 'Dinesh'), ('course', 'pfs'), ('batch', 65), ('age', 21), ('phno', 9856532597), ('email', 'dinesh@mail.com'), ('py', 2027)])
data.copy()
{'name': 'Dinesh', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9856532597, 'email': 'dinesh@mail.com', 'py': 2027}
sorted(data)
['age', 'batch', 'course', 'email', 'name', 'phno', 'py']
max(data)
'py'
min.(data)
SyntaxError: invalid syntax
min(data)
'age'
d = {1:2,2:2}
m = d
m[3]=3
m
{1: 2, 2: 2, 3: 3}
d
{1: 2, 2: 2, 3: 3}
n = d.copy()
n[5]=5
n
{1: 2, 2: 2, 3: 3, 5: 5}
d
{1: 2, 2: 2, 3: 3}
data
{'name': 'Dinesh', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9856532597, 'email': 'dinesh@mail.com', 'py': 2027}
d.pop('py')
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    d.pop('py')
KeyError: 'py'
d.pop(3)
3
d
{1: 2, 2: 2}
del data('py')
SyntaxError: cannot delete function call
data
{'name': 'Dinesh', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9856532597, 'email': 'dinesh@mail.com', 'py': 2027}
del data('py')
SyntaxError: cannot delete function call
data.get("py")
2027
data.setdefault('name',2026)
'Dinesh'
data.setdefault('email',2026)
'dinesh@mail.com'
data.setdefault('email',2026)
data.setdefault('email',2026)
SyntaxError: multiple statements found while compiling a single statement
data.setdefault('email',2026)
'dinesh@mail.com'
data.setdefault('key',2026)
2026
data
{'name': 'Dinesh', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9856532597, 'email': 'dinesh@mail.com', 'py': 2027, 'key': 2026}
dict.fromkeys(['python','mysql','java'],0)
{'python': 0, 'mysql': 0, 'java': 0}
#Fromkeys^^^^
data.pop[3]
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    data.pop[3]
TypeError: 'builtin_function_or_method' object is not subscriptable
data.clear()
data
{}

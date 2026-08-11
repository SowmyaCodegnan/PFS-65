Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = 'Codegnan'
s
'Codegnan'
s="codegnan"
s
'codegnan'
type(s)
<class 'str'>
s = ''
s
''
a = 'python'
b = ' programming'
a+b
'python programming'
fname = 'sowmya'
lname = 'Tummala'
fname + lname
'sowmyaTummala'
a
'python'
a*10
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
'*'*20
'********************'
'-Codegnan-'*5
'-Codegnan--Codegnan--Codegnan--Codegnan--Codegnan-'
names = 'kalyani vishupriya lakshmi mounasri lohitha usharani'
names
'kalyani vishupriya lakshmi mounasri lohitha usharani'
s = 'codegnan'
s[7]
'n'
s[2]
'd'
s[0]
'c'
s[4]
'g'
s[-1]
'n'
s[-3]
'n'
s[-2]
'a'
names
'kalyani vishupriya lakshmi mounasri lohitha usharani'
names[:7]
'kalyani'
names[8:19]
'vishupriya '
names[19:26]
'lakshmi'
names[27:35]
'mounasri'
names[36:43]
'lohitha'
names[-8:]
'usharani'
names[-16:-8]
'lohitha '
names[::-1]
'inarahsu ahtihol irsanuom imhskal ayirpuhsiv inaylak'
names
'kalyani vishupriya lakshmi mounasri lohitha usharani'
names[-1:-9:-1]
'inarahsu'
names[:18]
'kalyani vishupriya'
names
'kalyani vishupriya lakshmi mounasri lohitha usharani'
'kalyani' in names
True
'lohitha' in names
True
'sadhana' not in names
True
'z' in names
False
'b' in names
False
'a' in names
True
names
'kalyani vishupriya lakshmi mounasri lohitha usharani'
len(names)
52
ord('a')
97
ord('v')
118
ord('A')
65
ord('G')
71
chr(100)
'd'
chr('40')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    chr('40')
TypeError: 'str' object cannot be interpreted as an integer
chr(40)
'('
chr(50)
'2'
chr(10)
'\n'
sorted(names)
[' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'h', 'h', 'h', 'h', 'h', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'k', 'k', 'l', 'l', 'l', 'm', 'm', 'n', 'n', 'n', 'o', 'o', 'p', 'r', 'r', 'r', 's', 's', 's', 's', 't', 'u', 'u', 'u', 'v', 'y', 'y']
max(names)
'y'
min(names)
' '
s= 'python Programming language'
s.upper()
'PYTHON PROGRAMMING LANGUAGE'
s.lower()
'python programming language'
s.swapcase()
'PYTHON pROGRAMMING LANGUAGE'
s.captialize()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s.captialize()
AttributeError: 'str' object has no attribute 'captialize'. Did you mean: 'capitalize'?
s.capitalize()

'Python programming language'
s.title()
'Python Programming Language'
"STRAẞEMÁLAGAÅngströmCaf".casefold()
'strassemálagaångströmcaf'
s
'python Programming language'
s.center(50,'-')
'-----------python Programming language------------'
s.center(50,'*')
'***********python Programming language************'
s.center(40,'.')
'......python Programming language.......'
s.ljust(40,'.')

'python Programming language.............'
s.rjust(40,'.')

'.............python Programming language'
'123'.zfill(4)
'0123'
'65'.zfill(5)

'00065'
'8'.zfill(2)
'08'
'83245678'.zfill(2)

'83245678'
s
'python Programming language'
s.find('python')
0
s.find('g')
10
s.find('p')
0
s.rfind('g')
25
s.rfind('a')
24
s.find('z')
-1

s.find('a')
12
s.index('a')
12
s.rindex('a')
24
s.index('z')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    s.index('z')
ValueError: substring not found
s.count('a')
3
s.count('e')
1
s.count('m')
2
s
'python Programming language'
s.replace('o')
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s.replace('o')
TypeError: replace expected at least 2 arguments, got 1
>>> s.replace('o','1')
'pyth1n Pr1gramming language'
>>> s.replace('m','2')
... 
'python Progra22ing language'
>>> s.replace('python','java')
'java Programming language'
>>> s.maketrans('aeiou','#@$&*')
{97: 35, 101: 64, 105: 36, 111: 38, 117: 42}
>>> s.translate(s.maketrans('aeiou','#@$&*'))
'pyth&n Pr&gr#mm$ng l#ng*#g@'
>>> text = "Hello 🙂"
>>> text.encode()
b'Hello \xf0\x9f\x99\x82'
>>> b'Hello \xf0\x9f\x99\x82'.decode()
'Hello 🙂'

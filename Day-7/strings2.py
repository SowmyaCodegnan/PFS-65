Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = '      Hello      world           '
s.strip()
'Hello      world'
s.lstrip()
'Hello      world           '
s.rstrip()
'      Hello      world'
s.replace(' ','')
'Helloworld'
s = 'java-python-flask-mysql-fastapi-c'
s.split('-')
['java', 'python', 'flask', 'mysql', 'fastapi', 'c']
s.split('-',2)
['java', 'python', 'flask-mysql-fastapi-c']
s.rsplit('-',2)
['java-python-flask-mysql', 'fastapi', 'c']
l = '''python'''
l = '''python
java
mysql
flask
'''
l
'python\njava\nmysql\nflask\n'
l.splitlines()
['python', 'java', 'mysql', 'flask']
c = ['python', 'java', 'mysql', 'flask']
a
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a
NameError: name 'a' is not defined
c
['python', 'java', 'mysql', 'flask']
''.join(c)
'pythonjavamysqlflask'
' '.join(c)
'python java mysql flask'
', '.join(c)
'python, java, mysql, flask'
'@'.join(c)
'python@java@mysql@flask'
'-'.join(('1','2,','3'))
'1-2,-3'
'-'.join({'1','2','3'})
'2-3-1'
a = 'strings.py'
a.partition('.')
('strings', '.', 'py')
a = 'string.py.java.png.txt'
s
'java-python-flask-mysql-fastapi-c'
a
'string.py.java.png.txt'
a.partition('.')
('string', '.', 'py.java.png.txt')
a.rpartition('.')
('string.py.java.png', '.', 'txt')
a = 'strings.png'
a.startswith('str')
True
a.startswith('list')
False
a.endswith('.py')
False
a.endswith('.png')
True
'pythnv.13'.islower()
True
'Pythnv.13'.islower()

False
'PYTHON234567@#%$^&'.isupper()
True
'estyu'.isalpha()
True
'estyu8765@'.isalpha()
False
'estyu8765@'.isalnum()
False
'estyu8765'.isalnum()
True
'serdtfyguhjkl'.isalnum()
True
'987654'.isalnum()
True
'      '.isspace()
True
'    Hello'.isspace()
False
'Hlo Wor'.istitle()
True
'HLO Word'.istitle()
False
'my_var'.isidentifier()
True
'my@var'.isidentifier()
False
a.partition('.')
('strings', '.', 'png')

False = '1'
SyntaxError: cannot assign to False
'2134567'.isdecimal()
True
>>> 'ERTYGVBGH5467'.isdecimal()
False
>>> '43567'.isdigit()
True
>>> '9876'.isnumerics()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    '9876'.isnumerics()
AttributeError: 'str' object has no attribute 'isnumerics'. Did you mean: 'isnumeric'?
>>> '9876'.isnumeric()
True

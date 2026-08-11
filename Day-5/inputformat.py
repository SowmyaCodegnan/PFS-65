Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#int float complex str list tuple set dict bool
a = input()
codegnan
a
'codegnan'
a = input()
1234
a
'1234'
a = input("Enter the value: ")
Enter the value: casgu64t37iwr46yjg4i237
a
'casgu64t37iwr46yjg4i237'
marks = input("Enter the marks: ")
Enter the marks: 98
marks
'98'
marks = int(input("Enter the marks: "))
Enter the marks: 12
marks
12
price = float(input("Enter the price: "))
Enter the price: 123.432
price
123.432
cgpa = float(input("Enter the cgpa: "))
Enter the cgpa: 9.8
cgpa
9.8
names = input()
usharani lohitha mounasri
names
'usharani lohitha mounasri'
list(names)
['u', 's', 'h', 'a', 'r', 'a', 'n', 'i', ' ', 'l', 'o', 'h', 'i', 't', 'h', 'a', ' ', 'm', 'o', 'u', 'n', 'a', 's', 'r', 'i']
names.split()
['usharani', 'lohitha', 'mounasri']
names = 'usharani,lohitha,mounasri'

names.split(',')
['usharani', 'lohitha', 'mounasri']
courses = 'python-java-c++-flask'
course.split('-')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    course.split('-')
NameError: name 'course' is not defined. Did you mean: 'courses'?
courses.split('-')
['python', 'java', 'c++', 'flask']
softskills = 'communication quickleaner'
softskills.split()
['communication', 'quickleaner']
names = input("ENter the names: ").split()
ENter the names: usharani lohitha mounasri
names
['usharani', 'lohitha', 'mounasri']
names = tuple(input("ENter the names: ").split())
ENter the names: usharani lohitha mounasri
names
('usharani', 'lohitha', 'mounasri')
names = set(input("ENter the names: ").split())
ENter the names: usharani lohitha mounasri
names
{'mounasri', 'lohitha', 'usharani'}
marks = input().split()
12 34 68 89 09
marks
['12', '34', '68', '89', '09']
map(int,marks)
<map object at 0x0000022D7CADBC70>
list(map(int,marks))
[12, 34, 68, 89, 9]
marks = list(map(int,input("Enter the marks").split()))
Enter the marks12 56 234 67 345 8 345 78
marks
[12, 56, 234, 67, 345, 8, 345, 78]
marks = tuple(map(int,input("Enter the marks").split()))
Enter the marks345 456 5678 
marks
(345, 456, 5678)
marks = set(map(int,input("Enter the marks").split()))
Enter the marks4567 5678 46578
marks
{46578, 5678, 4567}
a,b=[1,2]
a
1
b
2
a,b,c=(1,12.3,"str")
a
1
b
12.3
c
'str'
email,password = input("Enter the email, password: ").split()
Enter the email, password: sowmya@codegnan.com 12345
email
'sowmya@codegnan.com'
password
'12345'
name, marks = input("ENter the name and marks: ").split()
ENter the name and marks: teja 56
name
'teja'
marks
'56'
int(marks)
56
a,b,c = list(map(int,input().split()))
12 34 45
a
12
b
34
c
45
status = eval(input())
True
staus
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    staus
NameError: name 'staus' is not defined. Did you mean: 'status'?
status
True
type(status)
<class 'bool'>
status = eval(input())
2+3j
status
(2+3j)
type(status)
<class 'complex'>
status = eval(input())
... 
[1,2,3,4]
>>> status
[1, 2, 3, 4]
>>> status = eval(input())
(1,2,4,5)
>>> status
(1, 2, 4, 5)
>>> status = eval(input())
... 
{1:1,2:2,3:3,4:4,5:5}
>>> status
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

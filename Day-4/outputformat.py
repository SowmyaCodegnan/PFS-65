Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
b = 12.3
c = 'codegnan'
a
10
b
12.3
c
'codegnan'
print(a,b,c)
10 12.3 codegnan
print("a=",a,"b=",b,'c='c)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("a=",a,"b=",b,'c=',c)
a= 10 b= 12.3 c= codegnan
print("a=",a,"b=",b,'c=',c,sep='')
a=10b=12.3c=codegnan
print("a=",a,"b=",b,'c=',c,sep='\n')
a=
10
b=
12.3
c=
codegnan
print("a=",a,"b=",b,'c=',c,sep='\t')
a=	10	b=	12.3	c=	codegnan
print("a=",a,"b=",b,'c=',c,sep='\t',end='\n\n')
a=	10	b=	12.3	c=	codegnan

print("a=",a,"b=",b,'c=',c,sep='\t',end='@')
a=	10	b=	12.3	c=	codegnan@
>>> print(f'a={a} b={b} c={c}')
a=10 b=12.3 c=codegnan
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=12.300000 c=codegnan
>>> print('a={} b={} c={}'.format(a,b,c))
a=10 b=12.3 c=codegnan
>>> print('a={} b={} c={}'.format(b,c,a))
a=12.3 b=codegnan c=10
>>> print('a={0} b={1} c={2}'.format(a,b,c))
a=10 b=12.3 c=codegnan
>>> print('a={2} b={0} c={1}'.format(a,b,c))
a=codegnan b=10 c=12.3

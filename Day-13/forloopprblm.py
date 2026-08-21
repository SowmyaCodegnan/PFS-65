'''
12 -  [1,2,3,4,6,12]
13 - [1,13]
14 - [1,2,7,14]

n = int(input("Enter the input: "))
res = []
for i in range(1,n+1):
    if n%i==0:
        res.append(i)

print(f'Factors of {n} = {}')


s = 'python programming'
d= {}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

s = 'ppppppyyyyyttt'
c=1
res = ''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        res+= s[i]+str(c)
        c=1
print(res+s[i]+str(c))
'''






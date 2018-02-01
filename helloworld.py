#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello,world')
print(100+200+300)
print('1024*768=',1024*768)
#a=input('please input the size of a:')
a=2
print('the value of a is:',a)
b=-2
print('the abs of b is')
if b>=0:
    print(b)
else:
    print(-b)
print('''line1
line2
line3''')
print(r'''hello,\n
world''')
print('''hello,\n
world''')
c=ord('a')
print(c)
c=ord('颜')
print(c)
c=chr(89)
print(c)
c='ABC'.encode('ascii')
print(c)
c='ABC'.encode('utf-8')
print(c)
c='颜'.encode('utf-8')
print(c)
c=b'\xe9\xa2\x9c'.decode('utf-8')
print(c)
c=len('ABC')
print(c)
c=len('颜')
print(c)
c=len(b'ABC')
print(c)
c=len(b'\xe9\xa2\x9c')
print(c)
c=len('颜'.encode('utf-8'))
print(c)
print('Hello,%s'%'world')
print('Hi, %s, you have $%d'%('Jiyu Yan',100000))
print('%2d-%02d'%(3,1))
print('%.2f'%3.14159265)
print('AgeL %s. Gender: %s'%(25,True))
print('growth rate: %d %%'% 7)
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明',17.125))
s1=72
s2=85
r=(85-72)/85*100
r='%.1f'%r
r=r+'%'
print('成绩提升的百分点为%s'%r)
classmates=['Michael','Bob','Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
classmates.append('Adam')
print(classmates)
classmates.insert(1,'Jack')
print(classmates)
classmates.pop()
'Adam'
print(classmates)
classmates.pop(1)
'Jack'
print(classmates)
classmates[1]='Sarah'
print(classmates)
L=['Apple',123,True]
print(L)
s=['python','java',['asp','php'],'scheme']
print(s)
print(len(s))
p=['asp','php']
s2=['python','java',p,'scheme']
print(s2)
L=[]
print(len(L))
classmates2=('Michael','Bob','Tracy')
print(classmates2)
print(classmates2[0])
print(classmates2[1])
print(classmates2[2])
t=(1,2)
print(t)
t=()
print(t)
t=(1)
print(t)
t=(1,)
print(t)
print(len(t))
t=('a','b',['A','B'])
print(t)
t[2][0]='X'
t[2][1]='Y'
print(t)
L=[
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

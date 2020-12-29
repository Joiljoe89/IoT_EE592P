# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:25:18 2018

@author: Pinnacle
"""
#d= np.ones(1,3)
a= ([1,2,3,4,1,2,3,4,1,2,3,4])

b= ([3,4,5,6,3,4,5,6,3,4,5,6])
d=[[0,0,0,0,0,0,0,0]]
for i in range(0,12,8):
    print(i)
    c=a[i:i+8]
    d=[c]+d
    print(c)
    print(d)
#c=a+b
#d=np.concatenate((a,b),axis=0)
f=[[0,0,0,0,0,0,0,0]]
for i in range(0,12,8):
    print(i)
    e=b[i:i+8]
    f=[e]+f
    print(e)
    print(f)
f1=[[0,0,0,0,0,0,0,0]]
for i in range(0,12,8):
    print(i)
    e1=b[i:i+8]
    f1=[e1]+f1
    print(e1)
    print(f1)
h=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
for j in range(0,3):
    print('g')
    g = f[j]+d[j]+f1[j]
    h = [g]+h
    print(g)
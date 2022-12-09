# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 11:20:43 2022

@author: adam.davitt
"""


h=[0,0]
t1=[0,0]
t2=[0,0]
t3=[0,0]
t4=[0,0]
t5=[0,0]
t6=[0,0]
t7=[0,0]
t8=[0,0]
t9=[0,0]

def converge(h,t):
    if ((h[0]-t[0])**2 + (h[1]-t[1])**2 )<=2:
        return t
    else:
        if h[0]>t[0]:
            if h[1]>t[1]:
                t[0]+=1
                t[1]+=1
                return t
            elif h[1]<t[1]:
                t[0]+=1
                t[1]-=1
                return t
            else:
                t[0]+=1
                return t
        elif h[0]<t[0]:
            if h[1]>t[1]:
                t[0]-=1
                t[1]+=1
                return t
            elif h[1]<t[1]:
                t[0]-=1
                t[1]-=1
                return t
            else:
                t[0]-=1
                return t
        else:
            if h[1]>t[1]:
                t[1]+=1
                return t
            elif h[1]<t[1]:
                t[1]-=1
                return t
            else:
                print('trouble')
                return t

visited={}
visited[str(t[0])+','+str(t[1])]=1
for a in my_path:
    dirc=a[0]
    movs=a[1]
    if dirc=='R':
        for i in range(movs):
            h[0]+=1
            t1=converge(h,t1)
            t2=converge(t1,t2)
            t3=converge(t2,t3)
            t4=converge(t3,t4)
            t5=converge(t4,t5)
            t6=converge(t5,t6)
            t7=converge(t6,t7)
            t8=converge(t7,t8)
            t9=converge(t8,t9)
            visited[str(t9[0])+','+str(t9[1])]=1
    elif dirc=='L':
        for i in range(movs):
            h[0]-=1
            t1=converge(h,t1)
            t2=converge(t1,t2)
            t3=converge(t2,t3)
            t4=converge(t3,t4)
            t5=converge(t4,t5)
            t6=converge(t5,t6)
            t7=converge(t6,t7)
            t8=converge(t7,t8)
            t9=converge(t8,t9)
            visited[str(t9[0])+','+str(t9[1])]=1
    elif dirc=='U':
        for i in range(movs):
            h[1]+=1
            t1=converge(h,t1)
            t2=converge(t1,t2)
            t3=converge(t2,t3)
            t4=converge(t3,t4)
            t5=converge(t4,t5)
            t6=converge(t5,t6)
            t7=converge(t6,t7)
            t8=converge(t7,t8)
            t9=converge(t8,t9)
            visited[str(t9[0])+','+str(t9[1])]=1
    elif dirc=='D':
        for i in range(movs):
            h[1]-=1
            t1=converge(h,t1)
            t2=converge(t1,t2)
            t3=converge(t2,t3)
            t4=converge(t3,t4)
            t5=converge(t4,t5)
            t6=converge(t5,t6)
            t7=converge(t6,t7)
            t8=converge(t7,t8)
            t9=converge(t8,t9)
            visited[str(t9[0])+','+str(t9[1])]=1
    else:
        print('uh oh')
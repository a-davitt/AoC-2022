# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 09:07:33 2022

@author: adam.davitt
"""

    
    
m0=[50, 70, 89, 75, 66, 66]
m1=[85]
m2=[66, 51, 71, 76, 58, 55, 58, 60]
m3=[79, 52, 55, 51]
m4=[69, 92]
m5=[71, 76, 73, 98, 67, 79, 99]
m6=[82, 76, 69, 69, 57]
m7=[65, 79, 86]

checks=[0,0,0,0,0,0,0,0]

passes=0
while passes<20:
    # Monkey 0
    for a in m0:
        new=(a*5)//3
        if new%2==0:
            m2.append(new)
        else:
            m1.append(new)
        checks[0]+=1
    m0=[]
    # Monkey 1
    for a in m1:
        new=(a**2)//3
        if new%7==0:
            m3.append(new)
        else:
            m6.append(new)
        checks[1]+=1
    m1=[]
    # Monkey 2
    for a in m2:
        new=(a+1)//3
        if new%13==0:
            m1.append(new)
        else:
            m3.append(new)
        checks[2]+=1
    m2=[]
    # Monkey 3
    for a in m3:
        new=(a+6)//3
        if new%3==0:
            m6.append(new)
        else:
            m4.append(new)
        checks[3]+=1
    m3=[]
    # Monkey 4
    for a in m4:
        new=(a*17)//3
        if new%19==0:
            m7.append(new)
        else:
            m5.append(new)
        checks[4]+=1
    m4=[]
    # Monkey 5
    for a in m5:
        new=(a+8)//3
        if new%5==0:
            m0.append(new)
        else:
            m2.append(new)
        checks[5]+=1
    m5=[]
    # Monkey 6
    for a in m6:
        new=(a+7)//3
        if new%11==0:
            m7.append(new)
        else:
            m4.append(new)
        checks[6]+=1
    m6=[]
    # Monkey 7
    for a in m7:
        new=(a+5)//3
        if new%17==0:
            m5.append(new)
        else:
            m0.append(new)
        checks[7]+=1
    m7=[]
    passes+=1
    if passes%100==0:
        print(passes)
    
    
    
    
"""    PART 2    """ 

#LCM of 2,7,13,3,19,5,11,17 is 9699690

checks=[0,0,0,0,0,0,0,0]
passes=0
while passes<10000:
    # Monkey 0
    for a in m0:
        new=(a*5)%9699690
        if new%2==0:
            m2.append(new)
        else:
            m1.append(new)
        checks[0]+=1
    m0=[]
    # Monkey 1
    for a in m1:
        new=(a**2)%9699690
        if new%7==0:
            m3.append(new)
        else:
            m6.append(new)
        checks[1]+=1
    m1=[]
    # Monkey 2
    for a in m2:
        new=(a+1)%9699690
        if new%13==0:
            m1.append(new)
        else:
            m3.append(new)
        checks[2]+=1
    m2=[]
    # Monkey 3
    for a in m3:
        new=(a+6)%9699690
        if new%3==0:
            m6.append(new)
        else:
            m4.append(new)
        checks[3]+=1
    m3=[]
    # Monkey 4
    for a in m4:
        new=(a*17)%9699690
        if new%19==0:
            m7.append(new)
        else:
            m5.append(new)
        checks[4]+=1
    m4=[]
    # Monkey 5
    for a in m5:
        new=(a+8)%9699690
        if new%5==0:
            m0.append(new)
        else:
            m2.append(new)
        checks[5]+=1
    m5=[]
    # Monkey 6
    for a in m6:
        new=(a+7)%9699690
        if new%11==0:
            m7.append(new)
        else:
            m4.append(new)
        checks[6]+=1
    m6=[]
    # Monkey 7
    for a in m7:
        new=(a+5)%9699690
        if new%17==0:
            m5.append(new)
        else:
            m0.append(new)
        checks[7]+=1
    m7=[]
    passes+=1
    if passes%100==0:
        print(passes)
    
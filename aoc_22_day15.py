# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 08:15:55 2022

@author: adam.davitt
"""

my_in=[
[3890859,2762958,4037927,2985317],
[671793,1531646,351996,1184837],
[3699203,3052069,4037927,2985317],
[3969720,629205,4285415,81270],
[41343,57178,351996,1184837],
[2135702,1658955,1295288,2000000],
[24022,1500343,351996,1184837],
[3040604,3457552,2994959,4070511],
[357905,3997215,-101509,3502675],
[117943,3670308,-101509,3502675],
[841852,702520,351996,1184837],
[3425318,3984088,2994959,4070511],
[3825628,3589947,4299658,3299020],
[2745170,139176,4285415,81270],
[878421,2039332,1295288,2000000],
[1736736,811875,1295288,2000000],
[180028,2627284,-101509,3502675],
[3957016,2468479,3640739,2511853],
[3227780,2760865,3640739,2511853],
[1083678,2357766,1295288,2000000],
[1336681,2182469,1295288,2000000],
[3332913,1556848,3640739,2511853],
[3663725,2525708,3640739,2511853],
[2570900,2419316,3640739,2511853],
[1879148,3584980,2994959,4070511],
[3949871,2889309,4037927,2985317]
]

#Create a dictionary of spots that cannot be beacons
no_beac={}

#Iterate through the inputs
for x in my_in:
    man_dist=abs(x[0]-x[2])+abs(x[1]-x[3])
    #Add in the areas that are covered by the radius (within our y value)
    if man_dist>abs(x[1]-2000000):
        for j in range(man_dist-abs(x[1]-2000000)+1):
            no_beac[x[0]+j]=1
            no_beac[x[0]-j]=1

#Create a list of the actual beacons here since they will also be in the dict above
actual_beacs={}
for y in my_in:
    if y[3]==2000000:
        actual_beacs[x[2]]=1
        
# Total non-beacons
print(len(no_beac.keys())-len(actual_beacs.keys()))



"""       PART 2      """
# Since we have only 1 possible spot, it must be one space beyond at least 2 boundaries
spots=[]
for x in my_in:
    #Find all the spots one space beyond each boundary
    x_man_dist=abs(x[0]-x[2])+abs(x[1]-x[3])
    edge_list=[]
    edge_x=x[0]
    edge_y=x[1]-x_man_dist-1
    while edge_y<x[1]:
        if edge_x>=0 and edge_x<=4000000 and edge_y>=0 and edge_y<=4000000:
            edge_list.append([edge_x,edge_y])
        edge_y+=1
        edge_x+=1
    while edge_x>x[0]:
        if edge_x>=0 and edge_x<=4000000 and edge_y>=0 and edge_y<=4000000:
            edge_list.append([edge_x,edge_y])
        edge_y+=1
        edge_x-=1
    while edge_y>x[1]:
        if edge_x>=0 and edge_x<=4000000 and edge_y>=0 and edge_y<=4000000:
            edge_list.append([edge_x,edge_y])
        edge_y-=1
        edge_x-=1
    while edge_x<x[0]:
        if edge_x>=0 and edge_x<=4000000 and edge_y>=0 and edge_y<=4000000:
            edge_list.append([edge_x,edge_y])
        edge_y-=1
        edge_x+=1
    for y in my_in:
    # For each of these, check if it is one spot beyond any other boundary
        y_man_dist=abs(y[0]-y[2])+abs(y[1]-y[3])
        for z in edge_list:
            if abs(y[0]-z[0])+abs(y[1]-z[1])==y_man_dist+1:
                spots.append(z)
    print(x)
print('spots:'+str(len(spots)))


# Then check which of these spots are not in any other area
gd_spots=[]
for i in range(len(spots)):
    a=spots[i]
    if i%100000==0:
        print(i)
    f=0
    for b in my_in:
        man_dist=abs(b[0]-b[2])+abs(b[1]-b[3])
        if abs(b[0]-a[0])+abs(b[1]-a[1])<= man_dist:
            f=1
    if f==0:
        gd_spots.append(a)

#Deduplicate
d_spots=[]
for i in range(len(gd_spots)):
    s=gd_spots[i]
    if s not in d_spots:
        d_spots.append(s)

#This is our answer. Luckily d_spots is of length 1
print(d_spots[0][0]*4000000+d_spots[0][1])



""" Testing on sample inputs """

mini_in=[[2,18,-2,15],
[9,16,10,16],
[13,2,15,3],
[12,14,10,16],
[10,20,10,16],
[14,17,10,16],
[8,7,2,10],
[2,0,2,10],
[0,11,2,10],
[20,14,25,17],
[17,20,21,22],
[16,7,15,3],
[14,3,15,3],
[20,1,15,3]]

mini_no_beac={}

for x in mini_in:
    man_dist=abs(x[0]-x[2])+abs(x[1]-x[3])
    if man_dist>abs(x[1]-10):
        for j in range(man_dist-abs(x[1]-10)+1):
            mini_no_beac[x[0]+j]=1
            mini_no_beac[x[0]-j]=1

mini_actual_beacs={}
for y in mini_in:
    if y[3]==10:
        mini_actual_beacs[x[2]]=1
        
print(len(mini_no_beac.keys())-len(mini_actual_beacs.keys()))

""" P2 """

spots=[]
for x in mini_in:
    x_man_dist=abs(x[0]-x[2])+abs(x[1]-x[3])
    edge_list=[]
    edge_x=x[0]
    edge_y=x[1]-x_man_dist-1
    while edge_y<x[1]:
        if edge_x>=0 and edge_x<=20 and edge_y>=0 and edge_y<=20:
            edge_list.append([edge_x,edge_y])
        edge_y+=1
        edge_x+=1
    while edge_x>x[0]:
        if edge_x>=0 and edge_x<=20 and edge_y>=0 and edge_y<=20:
            edge_list.append([edge_x,edge_y])
        edge_y+=1
        edge_x-=1
    while edge_y>x[1]:
        if edge_x>=0 and edge_x<=20 and edge_y>=0 and edge_y<=20:
            edge_list.append([edge_x,edge_y])
        edge_y-=1
        edge_x-=1
    while edge_x<x[0]:
        if edge_x>=0 and edge_x<=20 and edge_y>=0 and edge_y<=20:
            edge_list.append([edge_x,edge_y])
        edge_y-=1
        edge_x+=1
    for y in mini_in:
        y_man_dist=abs(y[0]-y[2])+abs(y[1]-y[3])
        for z in edge_list:
            if abs(y[0]-z[0])+abs(y[1]-z[1])==y_man_dist+1:
                spots.append(z)
d_spots=[]
for s in spots:
    if s not in d_spots:
        d_spots.append(s)

gd_spots=[]
for a in d_spots:
    f=0
    for b in mini_in:
        man_dist=abs(b[0]-b[2])+abs(b[1]-b[3])
        if abs(b[0]-a[0])+abs(b[1]-a[1])<= man_dist:
            f=1
    if f==0:
        gd_spots.append(a)


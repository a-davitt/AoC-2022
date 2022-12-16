# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 09:32:29 2022

@author: adam.davitt
"""

my_in=[
['OQ',17,[	'NB'	,'AK'	,'KL'			]],
['HP',0,[	'ZX'	,'KQ'				]],
['GO',0,[	'HR'	,'GW'				]],
['PD',9,[	'XN'	,'EV'	,'QE'	,'MW'		]],
['NQ',0,[	'HX'	,'ZX'				]],
['DW',0,[	'IR'	,'WE'				]],
['TN',24,[	'KL'	,'EI'				]],
['JJ',0,[	'EV'	,'HR'				]],
['KH',0,[	'ZQ'	,'AA'				]],
['PH',0,[	'FN'	,'QE'				]],
['FD',0,[	'SM'	,'HX'				]],
['SM',7,[	'WW'	,'RZ'	,'FD'	,'HO'	,'KQ'	]],
['PU',0,[	'VL'	,'IR'				]],
['OM',0,[	'CM'	,'AA'				]],
['KX',20,[	'PC'					]],
['IR',3,[	'PU'	,'CM'	,'WW'	,'DW'	,'AF'	]],
['XG',0,[	'RX'	,'OF'				]],
['QE',0,[	'PH'	,'PD'				]],
['GW',0,[	'JQ'	,'GO'				]],
['HO',0,[	'SM'	,'TY'				]],
['WU',0,[	'SG'	,'RZ'				]],
['MS',0,[	'UE'	,'OF'				]],
['JS',0,[	'DO'	,'ZX'				]],
['YQ',0,[	'BC'	,'SG'				]],
['EJ',0,[	'AA'	,'LR'				]],
['EI',0,[	'BV'	,'TN'				]],
['NC',0,[	'TS'	,'BC'				]],
['AF',0,[	'IR'	,'HX'				]],
['OX',0,[	'HR'	,'BV'				]],
['BF',0,[	'JQ'	,'SY'				]],
['CA',0,[	'YD'	,'HX'				]],
['KQ',0,[	'HP'	,'SM'				]],
['NB',0,[	'OQ'	,'OF'				]],
['SY',0,[	'BF'	,'BV'				]],
['AA',0,[	'KH'	,'EJ'	,'OM'	,'TY'	,'DO'	]],
['BC',11,[	'WE'	,'RX'	,'YQ'	,'LR'	,'NC'	]],
['HR',14,[	'OX'	,'GO'	,'JJ'			]],
['WE',0,[	'DW'	,'BC'				]],
['MW',0,[	'JQ'	,'PD'				]],
['DO',0,[	'JS'	,'AA'				]],
['PC',0,[	'AK'	,'KX'				]],
['YD',0,[	'CA'	,'OF'				]],
['RX',0,[	'XG'	,'BC'				]],
['CM',0,[	'IR'	,'OM'				]],
['HX',6,[	'ZQ'	,'NQ'	,'AF'	,'FD'	,'CA'	]],
['ZQ',0,[	'KH'	,'HX'				]],
['BV',21,[	'SY'	,'OX'	,'EI'			]],
['AK',0,[	'PC'	,'OQ'				]],
['UE',0,[	'MS'	,'JQ'				]],
['LR',0,[	'BC'	,'EJ'				]],
['JQ',8,[	'MW'	,'UE'	,'BF'	,'GW'		]],
['VL',0,[	'PU'	,'ZX'				]],
['EV',0,[	'JJ'	,'PD'				]],
['TS',0,[	'NC'	,'ZX'				]],
['RZ',0,[	'SM'	,'WU'				]],
['OF',13,[	'XG'	,'YD'	,'NB'	,'MS'	,'XN'	]],
['WW',0,[	'SM'	,'IR'				]],
['TY',0,[	'HO'	,'AA'				]],
['XN',0,[	'OF'	,'PD'				]],
['SG',15,[	'WU'	,'YQ'				]],
['FN',25,[	'PH'					]],
['KL',0,[	'TN'	,'OQ'				]],
['ZX',5,[	'JS'	,'HP'	,'VL'	,'NQ'	,'TS'	]]]


# Take only those with working valves
relev=[['AA',0,0]]
for x in my_in:
    if x[1]>0:
        r=len(relev)
        relev.append([x[0],x[1],r])
# Find the length of that      
rel_len=len(relev)

#Build an array of the distances between 2 points
dist_arr=[]
for i in range(rel_len):
    dist_arr.append([])
    for j in range(rel_len):
        dist_arr[i].append(0)

# Breadth first algorithm to find distances        
def rt_finder(a,b):
    for y in my_in: 
        if y[0]==a:
            rec=y
            curr_dests=rec[2]
    if b in curr_dests:
        return 1
    depth=2
    f=0
    while f==0:
        next_dests=[]
        for c in curr_dests:
            for y in my_in: 
                if y[0]==c:
                    rec=y
            for z in rec[2]:
                next_dests.append(z)
        if b in next_dests:
            return depth
            f=1
        else:
            curr_dests=next_dests[:]
            next_dests=[]
            depth+=1
            
# Fill in for each combo
for i in range(rel_len):
    for j in range(i+1,rel_len):
        d=rt_finder(relev[i][0],relev[j][0])
        dist_arr[i][j]=d
        dist_arr[j][i]=d


curr_loc=['AA',0,0]
curr_path=['AA']
pres=0
times=0
#Function to iterate through all possible paths
def Walker(curr_path,times,pres,curr_loc):
    max_pres=0
    best_path=[]
    for x in relev:
        if x[0] not in curr_path:
            t=dist_arr[curr_loc[2]][x[2]]+1
            if times+t>30:
                if pres>max_pres:
                    max_pres=pres
                    best_path=curr_path
            else:
                p=x[1]*(30-(times+t))
                b=Walker(curr_path+[x[0]],times+t,pres+p,x)
                if b[0]>max_pres:
                    max_pres=b[0]
                    best_path=curr_path
    return [max_pres,best_path]
                    
                
P=Walker(curr_path,times,pres,curr_loc)






""" PART 2 """


curr_loc=['AA',0,0]
curr_path=['AA']
pres=0
times=0
def Walker_2(curr_path,times,pres,curr_loc,e):
    max_pres=0
    best_path=[]
    for x in relev:
        if x[0] not in curr_path:
            t=dist_arr[curr_loc[2]][x[2]]+1
            if times+t>26:
                if e==0:
                    b=Walker_2(curr_path, 0, pres, ['AA',0,0], 1)
                    if b[0]>max_pres:
                        max_pres=b[0]
                        best_path=curr_path
                if pres>max_pres:
                    max_pres=pres
                    best_path=curr_path
            else:
                p=x[1]*(26-(times+t))
                b=Walker_2(curr_path+[x[0]],times+t,pres+p,x,e)
                if b[0]>max_pres:
                    max_pres=b[0]
                    best_path=curr_path

    return [max_pres,best_path]
                    
                
P=Walker_2(curr_path,times,pres,curr_loc,0)
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:50:03 2022

@author: adam.davitt
"""


def Robots(o,c,s,g,t,o_rob,c_rob,s_rob,g_rob,path):
    #print(o,c,s,g,t,o_rob,c_rob,s_rob,g_rob)
    
    if t==23:
        return [g + g_rob , path]
    else:
        #We have 5 options on what to do next
        
        noth = Robots(o + o_rob , c + c_rob , s + s_rob, g + g_rob , t+1, o_rob, c_rob, s_rob, g_rob,path + 'n')
        b_o=[0,'']
        b_c=[0,'']
        b_s=[0,'']
        b_g=[0,'']
        
        if o >= g_cost[0] and s>=g_cost[2]:
            b_g = Robots(o + o_rob - g_cost[0] , c + c_rob , s + s_rob - g_cost[2], g + g_rob , t+1, o_rob, c_rob, s_rob, g_rob + 1,path + 'g')
        else:
            if o >= o_cost[0] and o_rob<max_o:
                b_o = Robots(o + o_rob - o_cost[0] , c + c_rob , s + s_rob, g + g_rob , t+1, o_rob + 1, c_rob, s_rob, g_rob, path + 'o')
            if o >= c_cost[0] and c_rob<max_c:
                b_c = Robots(o + o_rob - c_cost[0] , c + c_rob , s + s_rob, g + g_rob , t+1, o_rob , c_rob + 1, s_rob, g_rob, path + 'c')
            if o >= s_cost[0] and c >= s_cost[1] and s_rob<max_s:
                b_s = Robots(o + o_rob - s_cost[0] , c + c_rob - s_cost[1] , s + s_rob, g + g_rob , t+1, o_rob , c_rob, s_rob + 1, g_rob, path + 's')
    best_out = [noth,b_o,b_c,b_s,b_g][[noth[0],b_o[0],b_c[0],b_s[0],b_g[0]].index(max(noth[0],b_o[0],b_c[0],b_s[0],b_g[0]))]
    return best_out




my_in=[[[2,0,0,0],	[3,0,0,0],	[3,8,0,0],	[3,0,12,0]],
[[3,0,0,0],	[3,0,0,0],	[2,15,0,0],	[3,0,9,0]],
[[4,0,0,0],	[4,0,0,0],	[4,12,0,0],	[4,0,19,0]],
[[4,0,0,0],	[4,0,0,0],	[4,14,0,0],	[3,0,16,0]],
[[2,0,0,0],	[3,0,0,0],	[2,17,0,0],	[3,0,19,0]],
[[4,0,0,0],	[3,0,0,0],	[3,10,0,0],	[2,0,10,0]],
[[3,0,0,0],	[3,0,0,0],	[3,16,0,0],	[3,0,9,0]],
[[4,0,0,0],	[3,0,0,0],	[3,7,0,0],	[3,0,9,0]],
[[3,0,0,0],	[3,0,0,0],	[2,19,0,0],	[2,0,12,0]],
[[3,0,0,0],	[3,0,0,0],	[3,16,0,0],	[3,0,20,0]],
[[2,0,0,0],	[2,0,0,0],	[2,7,0,0],	[2,0,14,0]],
[[2,0,0,0],	[4,0,0,0],	[2,16,0,0],	[4,0,12,0]],
[[2,0,0,0],	[4,0,0,0],	[4,15,0,0],	[2,0,15,0]],
[[4,0,0,0],	[4,0,0,0],	[4,5,0,0],	[2,0,10,0]],
[[4,0,0,0],	[4,0,0,0],	[2,15,0,0],	[3,0,16,0]],
[[3,0,0,0],	[3,0,0,0],	[3,19,0,0],	[2,0,9,0]],
[[4,0,0,0],	[3,0,0,0],	[4,15,0,0],	[4,0,9,0]],
[[4,0,0,0],	[3,0,0,0],	[2,17,0,0],	[3,0,16,0]],
[[3,0,0,0],	[3,0,0,0],	[2,13,0,0],	[3,0,12,0]],
[[4,0,0,0],	[3,0,0,0],	[2,10,0,0],	[4,0,10,0]],
[[2,0,0,0],	[3,0,0,0],	[3,17,0,0],	[3,0,10,0]],
[[4,0,0,0],	[3,0,0,0],	[2,14,0,0],	[2,0,7,0]],
[[3,0,0,0],	[4,0,0,0],	[3,20,0,0],	[3,0,14,0]],
[[2,0,0,0],	[2,0,0,0],	[2,17,0,0],	[2,0,10,0]],
[[3,0,0,0],	[3,0,0,0],	[3,19,0,0],	[3,0,19,0]],
[[3,0,0,0],	[4,0,0,0],	[2,14,0,0],	[3,0,14,0]],
[[3,0,0,0],	[4,0,0,0],	[3,13,0,0],	[3,0,19,0]],
[[4,0,0,0],	[3,0,0,0],	[3,7,0,0],	[2,0,7,0]],
[[4,0,0,0],	[3,0,0,0],	[3,20,0,0],	[2,0,19,0]],
[[4,0,0,0],	[4,0,0,0],	[4,16,0,0],	[2,0,15,0]],
[[2,0,0,0],	[4,0,0,0],	[4,19,0,0],	[2,0,18,0]]]

"""
all_outs=[]

for i in range(31):
    ins=my_in[i]
    o_cost=ins[0]
    c_cost=ins[1]
    s_cost=ins[2]
    g_cost=ins[3]
    max_o=max(o_cost[0],c_cost[0],s_cost[0],g_cost[0])
    max_c=s_cost[1]
    max_s=g_cost[2]
    b=Robots(0,0,0,0,0,1,0,0,0)
    all_outs.append([i,b])
    print(i)
    
i=7
ins=my_in[i]
o_cost=ins[0]
c_cost=ins[1]
s_cost=ins[2]
g_cost=ins[3]
max_o=max(c_cost[0],s_cost[0],g_cost[0])
max_c=s_cost[1]
max_s=g_cost[2]
b=Robots(0,0,0,0,0,1,0,0,0,'')

"""






"""     PART 2     """



def Robots_2(o,c,s,g,t,o_rob,c_rob,s_rob,g_rob,path):
    #print(o,c,s,g,t,o_rob,c_rob,s_rob,g_rob)
    
    if t==31:
        return [g + g_rob , path]
    else:
        #We have 5 options on what to do next
        noth=[0,'']
        b_o=[0,'']
        b_c=[0,'']
        b_s=[0,'']
        b_g=[0,'']
        
        if o >= g_cost[0] and s>=g_cost[2]:
            b_g = Robots_2(o + o_rob - g_cost[0] , c + c_rob , s + s_rob - g_cost[2], g + g_rob , t+1, o_rob, c_rob, s_rob, g_rob + 1,path + 'g')
        elif o >= s_cost[0] and c >= s_cost[1] and s_rob<max_s:
             b_s = Robots_2(o + o_rob - s_cost[0] , c + c_rob - s_cost[1] , s + s_rob, g + g_rob , t+1, o_rob , c_rob, s_rob + 1, g_rob, path + 's')
        else:
            if o >= o_cost[0] and o_rob<max_o:
                b_o = Robots_2(o + o_rob - o_cost[0] , c + c_rob , s + s_rob, g + g_rob , t+1, o_rob + 1, c_rob, s_rob, g_rob, path + 'o')
            if o >= c_cost[0] and c_rob<max_c:
                b_c = Robots_2(o + o_rob - c_cost[0] , c + c_rob , s + s_rob, g + g_rob , t+1, o_rob , c_rob + 1, s_rob, g_rob, path + 'c')
            if b_o==[0,''] and b_c==[0,'']:
                noth= Robots_2(o + o_rob , c + c_rob , s + s_rob, g + g_rob , t+1, o_rob, c_rob, s_rob, g_rob,path + 'n')
            
    best_out = [noth,b_o,b_c,b_s,b_g][[noth[0],b_o[0],b_c[0],b_s[0],b_g[0]].index(max(noth[0],b_o[0],b_c[0],b_s[0],b_g[0]))]
    return best_out

i=3
ins=my_in[i]
o_cost=ins[0]
c_cost=ins[1]
s_cost=ins[2]
g_cost=ins[3]
max_o=max(c_cost[0],s_cost[0],g_cost[0])
max_c=s_cost[1]
max_s=g_cost[2]
b=Robots_2(0,0,0,0,0,1,0,0,0,'')
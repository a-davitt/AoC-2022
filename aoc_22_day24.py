# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 12:35:23 2023

@author: adam.davitt
"""
"""
my_in =['#.######','#>>.<^<#','#.<..<<#','#>v.><>#','#<^v^^>#','######.#']

"""
my_in = ['#.####################################################################################################',
'#<<^<<v.v^>v.<v>.^^>vvv<..^><>vvv>v>.v<>^>vv<<^><<^.<v^^<<<<<v^v><v>v^>vv>>.<^>.>^^^.<><><^^<v^><><.<#',
'#<<^<<vv^vv<<^<><>>^<^vvv><>>>^.<v^<..<.>v>v>vvv><.v<^>v^v<<<>>>>>vv<^<<<v>^<.>>vv><<.>v<.^v.v<^<>>v>#',
'#<<.v>.v<v<<^v.v>><v.<v<^.>>>.<^>^^^><<>.v><<vv.^v^.^<v>v^vv^<.>v<v><.v^.v<v<v>>><^v.v^^^<<v<^^<>v>v>#',
'#<>^v>vvv><..^..v<<^v^><.<<<<>>>^v><.<<^^vv<^v.<^^<^v^>>vv<.>v><..^><.vv>v^>>v><^v<<<^v<^v<v<<^v.vv^>#',
'#>^v<>>v<^^vv<<<v^v^<<v>v^vv^vv>><>^.^vv^<>^<v^^<.^v<.^<>^>vv.><<^>v<^^>v^<v.^.^<>v>^>v.<^vvvv<>>.>v>#',
'#<^^>><v><<^v<v>vvv>v^>v<^^^^><>^v^.<v^>.<>>vvv^v>.<v<<<^v>>>><v^^<>^v<>>^v>^^^^vvv^^><>^^^^<v<..><^>#',
'#>><<<><>^v^<<v>>.<v^^^^<vv^>>>v<v><v>>^>>^^^>v.<v^v>><><^v><vv<^.^vvvv<>.^>v><<<^>vv<^^v<v^^<><.^^v.#',
'#<>>^^>v<v.>v.v>^<<>^.>>vv^vv<^>v^><.^v<<v^<.^>v^.^v.<^.^<^<..^>><>v.>^v>vvvv<<>v^<vv<>vv>v>.>v^<^^^>#',
'#>vv<v>v<v>^<>v^<^vv<>v>^><><<>>v^<>v.<.>>>>v<v>v^<v<^v<>>v^<>v^>v>v<^<^v^^<v.<^vv<<<.>^v^><v>^^<.<>>#',
'#>v^.>vv^vv>.><<^.v^.v<>.^>v><<>v^^<<^<.^.^vv^<^^^><<>.v<<v<v<^^>v<<^<vv^^>>vvv>vvv<^vv.^.v>.<v.><^v>#',
'#<><>^v^^<.vv<v>^v<<^v>^.<v>^<.>.>^.v<<^vv.vv<v^<v<^v.>^^^<^^><^vv<<<>v<>><vv.<.<<vv<v.<<.>^>>>^>^.^>#',
'#<^><v<><v>v^^<^<vv>^^>^v^>v^>^>><v.>^<.<v<>.<^>>^<<^v^v^.><>v><<^^^vvv<><^>^^v.>><>>v<<^.v<v>^<>v^<<#',
'#>.><<<^<v<v>vv>v><.<v>.^^<<<<<><v>^.><^>vvv>v^<^<^v^<><>>.<v<v^v><^.vv^^>^vv>v^<v^<<<>^.v^<vv<v^v>.>#',
'#>.<>^><v><.^>vv.^.>v<<v^<^<><>...<>.>^<^><<>v>^>^<.^><><v<>v>>.<^v^<.<vv^v>.v^<v>vv>v>>>^.<^<v^<<..<#',
'#>^<<><<^>vvv>>>>v<<^v^>><>..^>v>>^<v>>v^^^.>.<>.^<^<v^>>v><.v>^v<v>v<^.^<^v<.v>^v>v>^>>^^v>>>>^^^^<<#',
'#>><^^v>vv>v<^<><v>vv^>^^^v^<^<><.<<^^>><<>v><><<>^<^>v^v^v<><v.><v>>..v^><v>><v^<^vvv>v.^^<<><>v.<><#',
'#>^^vv<<>>^^^>v<<<<v>.v^>v>v>vvv<^^<<v<.^^<<^^v<<><<>v.vv.^>^>><^><<vv>^.<>>v>^^v>^vv>.^^v>^.vvv>><<<#',
'#><^^^>vv.<^>^<><vv<><^^v<v.>.vv><^<.^^.v<vv<v<<<^<vvv.^^v^>^v.>^v<<<^vv><<v..^<v<^>>.^^^>v<><^vv^<v<#',
'#<>^^.>><v>v>^^.v<>.^vv^>.<^<vv<<v<v<v>.<^v>.<><v><^<^^>v>>^>.^>>^><.<><^<<v^v^<>vv<<<>>>^>^<vv^v<^^<#',
'#<>v^v><<v<v<.v><vv^v>><>><^.>>^vv>^.<v^^<^><>v<v^<v>vv>^v>vv<<v^>>>^>>>><>vvvv<^>v>^^>>^>^^^..^<v^<>#',
'#>v^<^^>v^v^<^>.<vv.<^>>>v.v^^<<^^<.<^.v<<^>v.>^v<.vvv^<vv<><>.v^>>vv<<<v>vvv>^<>^<vvv><v^vv<^^v>^<^<#',
'#<v^^v><.>>vv^.>>>^^><.v><<>^^><vv<><>v^v<<v^<v><.vv><<>>^^^>vvvv.^<<>vv.<.v.v<><><>.<><^^>v>v>v.^^<<#',
'#<>v^^<v^^>^>^<<<><<<^^>v>^><^v^>.<^^.<<.<v>><..^<v^^><^<<<.<.vvv.<<^v^<<<>v^.<^><>>.^>v<>^v><.^^>^><#',
'#><<^^^vvv^^>v^v^>v<v.v^<<<v^><>v><<vvv.v<>vv<<^^^><v^vv.>^<^><^>>v>.^<^^v^<<^><<^.^>vvv>>>.<><^v^^<<#',
'#<>>vv.^^^<^^>v<<>^>>v^<v.vv<vv^.<<v><v>v^>>>^^<.><^v^vvv..><><>v.^.v<vv><>v>><><>v^<<^.^^^v<^>>^<^^>#',
'#<>>.^>>v<>>>^<v>.>^><>^^>^vv>vv^><.<<<<<^<>.^.v^vv><v<vv>vv^^<><^.^>>v^<><><^v<v.>^^^>^v^^<v^><^<..>#',
'#><..>vv<<>vv^vv^>>.^^>^v><^^v<<..<^>.>^<vv^v>>><v^.>v^<>..<^<<<^>v^v<>v><vvv^^v^<>vv^<<<v<<vv<>>v^v>#',
'#>v<^>v<>v.v<>^vv.^<>v>>^v>.^^^>^<v^^>v>^><..v>v.>vvv^.^<v><^^v.^^<^vv..v^^^.>><>vvv>^vv^v<>>v^>v^v^.#',
'#>v><<^<.<^<<v.^^v^^^>>vv<^<^^.^^^v.<<.^>^>.<vv<v<^.>.^v^^v<><><^<^<^>v<><>^^<<<<>^..>v>><>^.v^.<>^^>#',
'#>>^^^^^v.<<>^^v>^vv.^<.<v^.^.^^>v<^^v<>v<^.>v<<<^>v^vv^><>>^^.><<>.v<^v^<>>^<>^v>v>>^^.<v<>v>.>vv^<.#',
'#<<^v>^^>^>.<^<>vvv^^v>v<<>v<.><^<<v><v<.v>v^>>>^v<vv>>>>>v^>.^^^>^.<<>vv<^v<>v>v^vv>v><.v.>.v><><.><#',
'#>v.^>v^^<>>v^.>^<<>><vv><<v<^>^<>.^<>>^^>^^>.><^>vv<<<v><^<<vv>^.^<v<<>v^.<<<.<>^<^v<^^<^>v>><.^>.<<#',
'#><<<<.^.vvvv^^<v^^^...<>v<<<v^^<v<.>>>><<^^<>^vv<<<v^^><.<^><<.<>vv<><>vv^>>vvv^^.><^<<v>^^^^.<v>>>>#',
'#<^.>>^vv<v<<v>>^>v.>^.vv^.>^<^v^.^<..><<.vvv>>vv>.^v^.>^<vv^vv^<^>>^>^>><<<^vv.^.>^>><v>v^v><^<>vv^>#',
'#..v^>..>v....v<vv^<^.^>v.<.>^<<vv^^^>v^<<>v^v^>^<<>v^^^>.<^>^<<.v.v<<<^>>><^<^<<>.^^^<<<><^^^vv<vv.<#',
'####################################################################################################.#'
]


blizz=[]
for i in range(len(my_in)):
    for j in range(len(my_in[0])):
        if my_in[i][j]=='<':
            blizz.append([[0,-1],[i,j]])
        elif my_in[i][j]=='>':
            blizz.append([[0,1],[i,j]])
        elif my_in[i][j]=='^':
            blizz.append([[-1,0],[i,j]])
        elif my_in[i][j]=='v':
            blizz.append([[1,0],[i,j]])


safe = [[0,1]]
moves=0

while [len(my_in)-1,len(my_in[0])-2] not in safe:
    old_blizz = blizz[:]
    for z in range(len(blizz)):
        if blizz[z][0][0]==0:
            blizz[z][1][0]=old_blizz[z][1][0]
            if old_blizz[z][1][1]+old_blizz[z][0][1] == 0:
                blizz[z][1][1] = len(my_in[0])-2
            elif old_blizz[z][1][1]+old_blizz[z][0][1] == len(my_in[0])-1:
                blizz[z][1][1] = 1
            else:
                blizz[z][1][1]=(old_blizz[z][1][1]+old_blizz[z][0][1])
        else:
            blizz[z][1][1]=old_blizz[z][1][1]
            if old_blizz[z][1][0]+old_blizz[z][0][0] == 0:
                blizz[z][1][0]=len(my_in)-2
            elif old_blizz[z][1][0]+old_blizz[z][0][0] == len(my_in)-1:
                blizz[z][1][0]=1
            else:
                blizz[z][1][0]=(old_blizz[z][1][0]+old_blizz[z][0][0])
    potential=[]
    int_safe=[]
    for i in range(len(my_in)):
        for j in range(len(my_in[0])):
            if my_in[i][j]!='#':
                potential.append([i,j])
                
    for b in blizz:
        if b[1] in potential:
            potential.remove(b[1])
    #print(len(potential))        
    for p in potential:
        if p in safe or [p[0]-1,p[1]] in safe or [p[0]+1,p[1]] in safe or [p[0],p[1]-1] in safe or [p[0],p[1]+1] in safe:
            int_safe.append(p)
    safe = int_safe[:]
    moves+=1  
    #print(blizz[10])
    #print(moves)
    #print(safe)
    #print('')
print(moves)
""" Step 1 = 221 """

safe = [[len(my_in)-1,len(my_in[0])-2]]
moves=0

while [0,1] not in safe:
    old_blizz = blizz[:]
    for z in range(len(blizz)):
        if blizz[z][0][0]==0:
            blizz[z][1][0]=old_blizz[z][1][0]
            if old_blizz[z][1][1]+old_blizz[z][0][1] == 0:
                blizz[z][1][1] = len(my_in[0])-2
            elif old_blizz[z][1][1]+old_blizz[z][0][1] == len(my_in[0])-1:
                blizz[z][1][1] = 1
            else:
                blizz[z][1][1]=(old_blizz[z][1][1]+old_blizz[z][0][1])
        else:
            blizz[z][1][1]=old_blizz[z][1][1]
            if old_blizz[z][1][0]+old_blizz[z][0][0] == 0:
                blizz[z][1][0]=len(my_in)-2
            elif old_blizz[z][1][0]+old_blizz[z][0][0] == len(my_in)-1:
                blizz[z][1][0]=1
            else:
                blizz[z][1][0]=(old_blizz[z][1][0]+old_blizz[z][0][0])
    potential=[]
    int_safe=[]
    for i in range(len(my_in)):
        for j in range(len(my_in[0])):
            if my_in[i][j]!='#':
                potential.append([i,j])
                
    for b in blizz:
        if b[1] in potential:
            potential.remove(b[1])
    #print(len(potential))        
    for p in potential:
        if p in safe or [p[0]-1,p[1]] in safe or [p[0]+1,p[1]] in safe or [p[0],p[1]-1] in safe or [p[0],p[1]+1] in safe:
            int_safe.append(p)
    safe = int_safe[:]
    moves+=1  
    #print(blizz[10])
    #print(moves)
    #print(safe)
    #print('')
print(moves)   
""" Step 2 = """

safe = [[0,1]]
moves=0

while [len(my_in)-1,len(my_in[0])-2] not in safe:
    old_blizz = blizz[:]
    for z in range(len(blizz)):
        if blizz[z][0][0]==0:
            blizz[z][1][0]=old_blizz[z][1][0]
            if old_blizz[z][1][1]+old_blizz[z][0][1] == 0:
                blizz[z][1][1] = len(my_in[0])-2
            elif old_blizz[z][1][1]+old_blizz[z][0][1] == len(my_in[0])-1:
                blizz[z][1][1] = 1
            else:
                blizz[z][1][1]=(old_blizz[z][1][1]+old_blizz[z][0][1])
        else:
            blizz[z][1][1]=old_blizz[z][1][1]
            if old_blizz[z][1][0]+old_blizz[z][0][0] == 0:
                blizz[z][1][0]=len(my_in)-2
            elif old_blizz[z][1][0]+old_blizz[z][0][0] == len(my_in)-1:
                blizz[z][1][0]=1
            else:
                blizz[z][1][0]=(old_blizz[z][1][0]+old_blizz[z][0][0])
    potential=[]
    int_safe=[]
    for i in range(len(my_in)):
        for j in range(len(my_in[0])):
            if my_in[i][j]!='#':
                potential.append([i,j])
                
    for b in blizz:
        if b[1] in potential:
            potential.remove(b[1])
    #print(len(potential))        
    for p in potential:
        if p in safe or [p[0]-1,p[1]] in safe or [p[0]+1,p[1]] in safe or [p[0],p[1]-1] in safe or [p[0],p[1]+1] in safe:
            int_safe.append(p)
    safe = int_safe[:]
    moves+=1  
    #print(blizz[10])
    #print(moves)
    #print(safe)
    #print('')
print(moves)
""" Step 3 = """
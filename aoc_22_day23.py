# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 14:52:09 2023

@author: adam.davitt
"""
"""
my_in=['.....',
       '..##.',
       '..#..',
       '.....',
       '..##.',
       '.....']


my_in=['....#..',
       '..###.#',
       '#...#.#',
       '.#...##',
       '#.###..',
       '##.#.##',
       '.#..#..']

"""
my_in=['#.##.#....#.#.#..#.##.......#..##..#.#####.#...##.##.##.#..#..#..#####...##',
'.##..#..#.#...#...#######.#.##....###..#..#####..##....#.#.##.##.##.....###',
'#...#..#.######..#...#..#....####..######.#....#..####.....#..##.##...#.###',
'#.##.##.#....#.#.#.#.#.##...####..#..#...##..###....#.....#.#.###..####..#.',
'##.#...##..###.#.#.##..#.#.....#.#..#...#.##..#....#..#..#..##..#.#..##..#.',
'##.##.#.#.#####.#.###.###..#..#.#.##...#..##.#...#..#.##...###.##.##....#..',
'###.#..##.#.#.#.....##......#.#..#..#.###..##.#.#.#..####.#....#.##...#.###',
'.#..###..##.####...#.#.#...#..###.#.###.###.##.#.#.....#.....#..#.######.#.',
'....###.##.######.##########.#....#..###..##.#..####...##.#..###.#..#....#.',
'..#..##.#.#.....##.##..#..####.###.#...##...#..#..#....#.#...#.#..###.##.##',
'......##......####..##..#..#.#.##.###...#####.........#..##.#.....#........',
'...#....#.#.##.##.###.#.#####.#.##.####.....#....##.###..####.#.#.#..#.#.#.',
'#.#..#.##..##.##...#.##.....#..#.#..###...#.#.....#.#.####.#.###.##.......#',
'#.#.#...#####..##..#..#####....#.###.#.#...#..##..#.#..###.###....#.#####.#',
'..#....#.....#######.##...#.##...##..#.....###..##..###..#.#.#..#..#.###.##',
'####.##.##.##.#.#..#..##.##..#...#.####..##....#..#.#..#...###.##.#..######',
'#####....#.#.##.#.###....###.##..##.#.##.#.###.#.#.##......#.##.#..########',
'..##.##.#.##..#.#....#....#....######..#.......#..#..#####...#..##....#..##',
'.##.##..##..#......#.####.#....##.##.#.#..#.#.###.#..##..####...#..###.####',
'.###.###.##.##...##.##....#..##....#.#..###.#.##...#.#...##..####.#.##..#..',
'..#..#.##..##....##.##..#..#.##...#..##.#...#..##..#....##.###...#.##.#..##',
'..#...#.#...#.#...##..#####..###...###.#..#..#...#.....##.##..#.###...#..##',
'.###.##.....###.#.##..##...#...######...#####.##.##.......#...##.#..##.#...',
'#....#.#####...###.#.###..#.####........#..###.......##.###.##.#...##.##..#',
'#.####...###.#...#.##.#####......##.#####..#..##..####.##..##.#.#...#.....#',
'#...#.##.#.##...##...##.###...###..##.#####.#........###.####..####.#...##.',
'..##...####.##.#....#...#.##...##.###..####.#..###.#.###.#.##..#....#..####',
'....#..#.....###...#.#..##..#....##..####.###.##..#...#..##..#####....#.##.',
'.#.#..##..#.####.#.###.##.#.#.....#.....###..##......##..#.##.#####.#.#..#.',
'.....##.....#....#....##.#.....#....######.##....##.#.##...#..###.#.#.#....',
'...##..#...##.###.###.#.#..#.##...#..#####..#.#.#..##.####...#.#....#####.#',
'....#########..#.###.#...##..#####..##..###....#....#.#...#......########.#',
'#..##...###.###.######..#....####...####...#####.#...##...####..##.#.#.##.#',
'#..#.###.....#....#.#...####..##.#..#.###..###..##.##.###.#######.###.##.##',
'#.#......#.#.####....##.#####...##.#.##.#.##...###..#.#.#####.##.##.#..#..#',
'#.##.#..##.####.#.##..##...##...#.###.#####.#.##.##.....####.##.#####..##..',
'#..##.##...#...#..##..#..#..##...#....#..###.##...##......#...#.##.#.##.#..',
'#####..#.#.##..#.#......#.........#....#####..#.##....#..#####.......##..##',
'..#.#..##..###.....#..##.###..##.#...####......##.##.......#..######.##.#.#',
'#..#.##..#..#....##.##.#.#..#.###...######...####..##..#..#...#.#..........',
'#.#.#.##...........#...#.#...##...#.###....#..####....#....#####...#..#####',
'##...#....##..#.#.#......###..###..##..#..###.......#.#....##.##......#.###',
'###.#.#.###.######.##...#..#.##.....#########.##..##..#..#.#.........##..##',
'###..##....#.#...####..###......#.###...#...###.###.#.###.##.##.##..#.#..##',
'#.#...###.#.###....#...##...#.##.##..#.#..#..#####.#.##.#####.##.##........',
'###...##..##....##....#...#..#...#..#.##..###..##.##.##....##.####...##.##.',
'###.##..###..####.##..##......##..##.....####.######....#....##...#..##.#.#',
'.....####..##............#...#...##..#...####..#..###...#####..#####....#..',
'###..###.#.####....#.####.###.###..#.#.#########.#.#.#.....##.#..###....##.',
'#.##..#..#####...#.#...####..####....#.#.#.#...##..##.#...#...#.#.##.#.####',
'...#.#....#..#.#.#..#..#######.....#.#.####.####.#...##...##.#.####....#..#',
'#..#.##..###.###..#..##.##.##..#.#.###.###..##.#.####..#...........#..#.##.',
'..#....#.######.####.##.##..#...#..###..#.....##.##...........#######..#...',
'.#..######......##.#.#....##...#..#.#.#..##..#####.#.##...####.#.####...##.',
'...#.#.##....###.#..#.##..#####.####.###..#...#.##..##...##..#...#..##..###',
'.##..#.#...###...##.#..#####.##.##.#..#.#.#.###.#.#...#.#.##..#.####.##...#',
'##...#..#...#..#.#..##..#.#...###.#......#####.#..#.#....###.#..##.....#...',
'##.#.###.#.#.####.##......#..#.##.##..#.##..#.#.###..#..#..#...#.#.#.....##',
'#.##..###..###...##...#.#....##..##.#..#####.#.#.#......#####.##.#.#..#.###',
'#..#..#..#..##.......##.#..##..##..##..####.##.####.#.........#.#.###....##',
'##..#.##....#.#....######....#.#.#....#...####..###....##..###..##.#.#.#.##',
'..#.##.#...##...#.###.#.#####........#.#########.#..###..#...#.#.....##.###',
'..###....##.##..#...###..####.#...###.#...#....#.....##.#...##.#...###.#.#.',
'###.....##.###.....#.#.#.#..#..########.######.#...#.####.###..#..#.###...#',
'.###..##.#.#.....##.#.#....#.......#..#...#..##.######.#.##.###....######..',
'###..###..#..#.###.###..####.###.#.##.##......#.....#.#...###.###.##..#....',
'..###.##..#.##......##...##.#######...#####.####.#.##########.#....#...#.#.',
'#...#....##...###..####.#.......##..####.###.##.#.###.....###.##..###.#.###',
'...#.#..#.#.###...##....###....##.#....##..###.#..#.#....##..#....#...####.',
'...#...#...#..##.....#..#..####.##....#........##.#...#.##....#...#.###.###',
'...#.#.#.#.#.#.#...###.###...#..###..#..#.......#.#.#...#......#.#.##..####',
'#.##..#.#.######....####...##..###..#..#.#.#.##...#.###.#.#..#.#..#.#####.#',
'.#.....#.#.#####..#.###.....###..#.#.#..##......#.#.####.###............#.#',
'##..#.....#....#.#.#..#.######........####..#...##.###.#.####.#.###.#.##.##',
'#.#....######.#.....#..#.##.###.#..#.#...###.####.#.....###....#.....###.##']




""" Part 1  """
elves=[]
f=0
for i in range(len(my_in)):
    for j in range(len(my_in[0])):
        if my_in[i][j]=='#':
            elves.append([i,j])
            f+=1
mov=[]
for a in range(f):
    mov.append([0,0])

def ElfMover(my_t):
    ElfPlotter(elves)    
    for turn in range(my_t):
        for g in range(len(elves)):
            #print('t=' + str(turn) + ' elf=' + str(g))
            e=elves[g]
            x=e[0]
            y=e[1]
            nw=[x-1,y-1]
            n=[x-1,y]
            ne=[x-1,y+1]
            w=[x,y-1]
            e=[x,y+1]
            sw=[x+1,y-1]
            s=[x+1,y]
            se=[x+1,y+1]
            if ne not in elves and n not in elves and nw not in elves:
                north=True
            else:
                north=False
            if ne not in elves and e not in elves and se not in elves:
                east=True
            else:
                east=False
            if se not in elves and s not in elves and sw not in elves:
                south=True
            else:
                south=False
            if nw not in elves and w not in elves and sw not in elves:
                west=True
            else:
                west=False
            if turn in [0,4,8]:
                if north and south and east and west:
                    mov[g]=[x,y]
                elif north:
                    mov[g]=n
                elif south:
                    mov[g]=s
                elif west:
                    mov[g]=w
                elif east:
                    mov[g]=e
                else:
                    mov[g]=[x,y]
            elif turn in [1,5,9]:
                if north and south and east and west:
                    mov[g]=[x,y]
                elif south:
                    mov[g]=s
                elif west:
                    mov[g]=w
                elif east:
                    mov[g]=e
                elif north:
                    mov[g]=n
                else:
                    mov[g]=[x,y]
            elif turn in [2,6]:
                if north and south and east and west:
                    mov[g]=[x,y]
                elif west:
                    mov[g]=w
                elif east:
                    mov[g]=e
                elif north:
                    mov[g]=n
                elif south:
                    mov[g]=s
                else:
                    mov[g]=[x,y]
            elif turn in [3,7]:
                if north and south and east and west:
                    mov[g]=[x,y]
                elif east:
                    mov[g]=e
                elif north:
                    mov[g]=n
                elif south:
                    mov[g]=s
                elif west:
                    mov[g]=w
                else:
                    mov[g]=[x,y]
        for h in range(len(elves)):
            my_mov=mov[h]
            if my_mov not in mov[:h] + mov[h+1:]:
                elves[h]=my_mov
        ElfPlotter(elves)
        min_x=1000
        min_y=1000
        max_x=0
        max_y=0
        
        for i in elves:
            if i[0]<min_x:
                min_x=i[0]
            if i[0]>max_x:
                max_x=i[0]
            if i[1]<min_y:
                min_y=i[1]
            if i[1]>max_y:
                max_y=i[1]
                
        print ( (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves))
        

def ElfPlotter(elfs):
    min_x=1000
    min_y=1000
    max_x=0
    max_y=0
    for i in elfs:
        if i[0]<min_x:
            min_x=i[0]
        if i[0]>max_x:
            max_x=i[0]
        if i[1]<min_y:
            min_y=i[1]
        if i[1]>max_y:
            max_y=i[1]
    my_str=''
    ctr=0
    for a in range(min_x,max_x+1):
        for b in range(min_y,max_y+1):
            ctr+=1
            if [a,b] in elfs:
                my_str+='#'
            else:
                my_str+='.'
        my_str+='\n'
    print(my_str)
    #print(ctr)

# 5329 - too high
# 6889 - too high

elves=[]
f=0
for i in range(len(my_in)):
    for j in range(len(my_in[0])):
        if my_in[i][j]=='#':
            elves.append([i,j])
            f+=1
mov=[]
for a in range(f):
    mov.append([0,0])
#ElfPlotter(elves)
ElfMover(10) 

''' Part 2 '''

elves=[]
f=0
for i in range(len(my_in)):
    for j in range(len(my_in[0])):
        if my_in[i][j]=='#':
            elves.append([i,j])
            f+=1
mov=[]
for a in range(f):
    mov.append([0,0])
    
ct=1
turn=0
t_turn=0
#ElfPlotter(elves)    
while ct>0:
    ct=0
    for g in range(len(elves)):
        e=elves[g]
        x=e[0]
        y=e[1]
        nw=[x-1,y-1]
        n=[x-1,y]
        ne=[x-1,y+1]
        w=[x,y-1]
        e=[x,y+1]
        sw=[x+1,y-1]
        s=[x+1,y]
        se=[x+1,y+1]
        if ne not in elves and n not in elves and nw not in elves:
            north=True
        else:
            north=False
        if ne not in elves and e not in elves and se not in elves:
            east=True
        else:
            east=False
        if se not in elves and s not in elves and sw not in elves:
            south=True
        else:
            south=False
        if nw not in elves and w not in elves and sw not in elves:
            west=True
        else:
            west=False
        if turn in [0,4,8]:
            if north and south and east and west:
                mov[g]=[x,y]
            elif north:
                mov[g]=n
            elif south:
                mov[g]=s
            elif west:
                mov[g]=w
            elif east:
                mov[g]=e
            else:
                mov[g]=[x,y]
        elif turn in [1,5,9]:
            if north and south and east and west:
                mov[g]=[x,y]
            elif south:
                mov[g]=s
            elif west:
                mov[g]=w
            elif east:
                mov[g]=e
            elif north:
                mov[g]=n
            else:
                mov[g]=[x,y]
        elif turn in [2,6]:
            if north and south and east and west:
                mov[g]=[x,y]
            elif west:
                mov[g]=w
            elif east:
                mov[g]=e
            elif north:
                mov[g]=n
            elif south:
                mov[g]=s
            else:
                mov[g]=[x,y]
        elif turn in [3,7]:
            if north and south and east and west:
                mov[g]=[x,y]
            elif east:
                mov[g]=e
            elif north:
                mov[g]=n
            elif south:
                mov[g]=s
            elif west:
                mov[g]=w
            else:
                mov[g]=[x,y]
    for h in range(len(elves)):
        my_mov=mov[h]
        if my_mov not in mov[:h] + mov[h+1:] and elves[h] != my_mov:
            elves[h]=my_mov
            ct+=1
    turn = (turn+1)%4
    t_turn+=1
    print(t_turn)
 
            
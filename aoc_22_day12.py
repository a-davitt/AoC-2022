# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 08:06:11 2022

@author: adam.davitt
"""
my_in="""abaaaaacaaaacccccccccaaaaaaccccccccccccccccccccccccccccccccccaaaaaa
abaaaaacaaaaccccaaaaaaaaaacccccccccccccccccccccccccccccccccccaaaaaa
abaaacccaaaaccccaaaaaaaaaaacccaacccccccccccaacccccccccccccccccaaaaa
abaaaacccaacccccaaaaaaaaaaaaaaaaacccccccccccacccccccccccccccccccaaa
abacaacccccccccccaaaaaaaaaaaaaaaaccccccccccaacccccccccccccccccccaaa
abcccacccccccccccaaaaaaaccaaaaaaaccccccccccclllcccccacccccccccccaac
abccccccccccccccccaaaaaccccccccccccccccccclllllllcccccccccccccccccc
abaaacccccccccccccaaaaaccccccccccccccccaakklllllllcccccccccaacccccc
abaaacccccccccccacccaaaccccccccccccccccakkklpppllllccddaaacaacccccc
abaaacccaaacccccaacaaaccccccccccccccccckkkkpppppllllcddddaaaacccccc
abaacccaaaacccccaaaaaccccccccccccccccckkkkpppppppllmmddddddaaaacccc
abaaaccaaaaccccccaaaaaacaaacccccccccckkkkpppuuuppplmmmmdddddaaacccc
abaaacccaaaccccaaaaaaaacaaaaccccccckkkkkoppuuuuuppqmmmmmmdddddacccc
abcccccccccccccaaaaaaaacaaaacccccjkkkkkooppuuuuuuqqqmmmmmmmddddcccc
abccccccccccccccccaaccccaaaccccjjjjkoooooouuuxuuuqqqqqqmmmmmddecccc
abacaaccccccccccccaacccccccccccjjjjoooooouuuxxxuvvqqqqqqqmmmeeecccc
abaaaacccccccacccaccccccccccccjjjjoootuuuuuuxxxyvvvvvqqqqmmmeeecccc
abaaaaacccccaaacaaacccccccccccjjjoooottuuuuuxxyyvvvvvvvqqmnneeecccc
abaaaaaccaaaaaaaaaaccccccccaccjjjooottttxxxxxxyyyyyyvvvqqnnneeecccc
abaaaccccaaaaaaaaaacccccccaaccjjjoootttxxxxxxxyyyyyyvvqqqnnneeecccc
SbcaaccccaaaaaaaaaaccccaaaaacajjjnnntttxxxxEzzzyyyyvvvrrqnnneeccccc
abcccccccaaaaaaaaaaacccaaaaaaaajjjnnntttxxxxyyyyyvvvvrrrnnneeeccccc
abcccccccaaaaaaaaaaacccccaaaaccjjjnnnnttttxxyyyyywvvrrrnnneeecccccc
abcccccccccaaaaaaccaccccaaaaaccciiinnnnttxxyyyyyyywwrrnnnneeecccccc
abccccccccccccaaacccccccaacaaaccciiinnnttxxyywwyyywwrrnnnffeccccccc
abccccccccccccaaacccccccaccaaaccciiinnnttwwwwwwwwwwwrrrnnfffccccccc
abccccccccccccccccccccccccccccccciiinnnttwwwwsswwwwwrrrnnfffccccccc
abaaaccaaccccccccccccccccccccccccciinnnttswwwssswwwwrrroofffacccccc
abaaccaaaaaacccccccccccccccccaaacciinnntssssssssssrrrrooofffacccccc
abaccccaaaaacccccccaaacccccccaaaaciinnnssssssmmssssrrrooofffacccccc
abaacaaaaaaacccccccaaaaccccccaaaaciiinmmmssmmmmmoosroooooffaaaacccc
abaaaaaaaaaaaccccccaaaaccccccaaacciiimmmmmmmmmmmoooooooofffaaaacccc
abcaaaaaaaaaaccccccaaaaccccccccccccihhmmmmmmmhggoooooooffffaaaccccc
abcccccaaacaccccccccaaccccccccccccchhhhhhhhhhhggggggggggffaaacccccc
abaccccaacccccccccccaaaccccccccccccchhhhhhhhhhgggggggggggcaaacccccc
abaaaccccaccccccccccaaaacccaacccccccchhhhhhhaaaaaggggggcccccccccccc
abaaaccccaaacaaaccccaaaacaaaacccccccccccccccaaaacccccccccccccccaaac
abaacccccaaaaaaaccccaaaaaaaaacccccccccccccccaaacccccccccccccccccaaa
abaaaccccaaaaaaccccaaaaaaaaccccccccccccccccccaacccccccccccccccccaaa
abccccccaaaaaaaaaaaaaaaaaaacccccccccccccccccaaccccccccccccccccaaaaa
abcccccaaaaaaaaaaaaaaaaaaaaacccccccccccccccccccccccccccccccccaaaaaa"""

#Create 2 arrays of the above dimension. One with the data, on with -1
#Steps will track how many steps required to get to the end
my_arr=[]
steps=[]
for i in range(41):
    my_arr.append([])
    steps.append([])
    for j in range(67):
        my_arr[i].append(my_in[i*68+j])
        steps[i].append(-1)

# Checks if there are any -1s left in the data. This ended up being redundant
def Do_Continue(in_arr):
    for x in in_arr:
        if min(x)==-1:
            return True
    return False

#Find the end, make a note of its place and change it to z
E=[]
for i in range(41):
    for j in range(67):
        if my_arr[i][j]=="E":
            E=[i,j]
            my_arr[i][j]='z'

#It takes 0 steps to get from the end to the end
steps[E[0]][E[1]]=0

# Similar for the start
S=[]
for i in range(41):
    for j in range(67):
        if my_arr[i][j]=="S":
            S=[i,j]
            my_arr[i][j]='a'

#ctr is a counter of how many steps we have mapped out
ctr=0
#There are 2747 elements in the input so no path can be longer than this
while Do_Continue(steps) and ctr<2747:
    #Iterate through every element
    for a in range(41):
        for b in range(67):
            #If it = ctr then check if we can have come from any adjacent element
            #If we can, check we havn't already found a shorter path there
            if steps[a][b]==ctr:
                ht=ord(my_arr[a][b])
                if a>0:
                    if ord(my_arr[a-1][b])>=ht-1 and steps[a-1][b]==-1:
                        steps[a-1][b]=ctr+1
                if a<40:
                    if ord(my_arr[a+1][b])>=ht-1 and steps[a+1][b]==-1:
                        steps[a+1][b]=ctr+1
                if b>0:
                    if ord(my_arr[a][b-1])>=ht-1 and steps[a][b-1]==-1:
                        steps[a][b-1]=ctr+1
                if b<66:
                    if ord(my_arr[a][b+1])>=ht-1 and steps[a][b+1]==-1:
                        steps[a][b+1]=ctr+1
    print(ctr)
    ctr+=1


# Number of steps from S to E
print(steps[S[0]][S[1]])


"""             PART 2             """

#Iterate through all spaces. Where we have an 'a', check if we found a path
strts=[]
for i in range(41):
    for j in range(67):
        if my_arr[i][j]=='a' and steps[i][j]>0:
            strts.append(steps[i][j])
#Of all the paths, where was the shortest starting from
print(min(strts))       


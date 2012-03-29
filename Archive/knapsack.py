#! /usr/bin/python

import sys
import math

filename = sys.argv[1]

try:
    file = open(filename, "r")
except IOError:
    print "Can't open the file for reading"
    sys.exit(0)

firstline = file.readline()

n , t = map(int,firstline.split(" "))

inputline = file.readline()
inputline = inputline.strip()

x = (map(int,inputline.split(" ")))
x.insert(0,0) #first index is a dummy 0
k = [[ False for j in range(t+1)] for i in range(n+1)]

k[0][0] = True
inclMatrix = [[False for j in range(t+1)] for i in range(n+1)]

for s in range(1,t+1):
    k[0][s] = False

for i in range(1,n+1): #excludes n+!
    for s in range(0,t+1): #excludes t+1
    #for s in range(t,-1,-1): #excludes t+1
        if (x[i] <= s):
            includeIt = k[i-1][s-x[i]]
            tryPrev = k[i-1][s]
            k[i][s] = includeIt or tryPrev
            inclMatrix[i][s] = includeIt
        else: # if x[i] is too big
            k[i][s] = k[i-1][s]


#print k
#print k[n][t]

def print_solution(i,s):
    
    if(not k[n][t]):
        print "No solution"
        return

    if i == 0 or s == 0 :return

    if(inclMatrix[i][s]): 
        print x[i]
        print_solution(i-1,s-x[i])
        #print x[i]
    else:
        print_solution(i-1,s)

print_solution(n,t)
#print n,t

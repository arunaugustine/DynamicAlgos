#!/usr/bin/python

import sys
import getopt
from collections import namedtuple
import math

filename = sys.argv[1]
print "filename is:", filename, "\n" 

try:
    file = open(filename, "r");
except IOError:
    print 'Can\'t open file for reading'
    sys.exit(0)

firstline = file.readline(); # read first line

#split the line read into the variables.
n, k = map(int, firstline.split(" "))

#declare a named tuple to represent our activities

activity = namedtuple('activity', ['i', 's', 'f', 'p'])
activitylist = [] #list of activities

# iterate through n lines and read them to a namedtuple for each activity

for i in range(1,n):
    oneline = file.readline()
    i,s,f,p = map(int, oneline.split(" "))
    a = activity(i,s,f,p)
    activitylist.append(a)


for a in activitylist:
    print a.i, a.s, a.f,a.p 


def isCompatible(a,b): 
    """ isCompatible: 
    compare two activities and return true if start time
    and finish times are compatible. The activity being included is a
    and the activity being considered to be included or not is b
    """
    if(b.f <= a.s):
        return True
    else:
        return False


def isCharitable(a):
    """ isCharitable:
    returns true if the activity is a charity event
    """

    if(a.p == 0):
        return True
    else: return False

# isCharitable definition above

def max(x,y):
    """ max:
    returns maximum of the two values
    """
    if ( x > y): return x
    elif (y >= x): return y
    else: # one of them is negInf
        if (math.isnan(x)):
            if(math.isnan(y)):
                return x
            else: return y
        else: return x

for a in activitylist:
    if(isCharitable(a)):
        print a.i, a.s, a.f, a.p

        


# code for asp1 problem

asp1 = []

asp1.append(0)
#print asp1[0]

def asp1MaxProfit(asp1):
    """ asp1MaxProfit
    returns the maximum profit from the asp1 array already computed
    """
    maximum = 0
    for ap in asp1:
        maximum = max(maximum, ap)
    return maximum

for a in activitylist: #iterate through the activities in increasing order
    if (isCharitable(a)):
        maxAsp = 0
        for j in range(1,a.i):
            maxAsp = max(maxAsp, asp1[j])
        asp1.append(maxAsp) #maxAsp + 0 appended for charitable events
        
    if (not isCharitable(a)): # a is a profitable event
        maxAsp = 0
        for m in range(1,a.i):
            if (isCompatible(a, activitylist[m]) and isCharitable(activitylist[m])):
                maxAsp = max(maxAsp, asp1[m])
        asp1.append(maxAsp + a.p)


print asp1MaxProfit(asp1)
print asp1


#Activity selection 2 solution

negInf = float('nan')
print "Asp2 :-------"
print n, k
asp2 = [ [ 0 for j in range(k+1)] for i in range(n+1)] # base case when i = 0, j = 0
print asp2

for j in range(1,k+1):   # base case when i = 0 and j > 0
    asp2[0][j] = negInf


for i in range(1,n+1):
    for j in range(1,k+1):

        if (isCharitable(activitylist[i])):
            q = asp2[i-1][j] # don't include current activity. prev act gives best sol
            for m in range(i-1,0,-1): # count downward till 1 decrement by one
                if (isCompatible(activitylist[i],activitylist[m])): # if a_k is compatible with a_i
                    q = max(q, asp2[m][j-1])
                    break
            print i 
            print j
            asp2[i][j] = q

        if (not isCharitable(activitylist[i])): # if it's a for_profit activity
            q = asp2[i-1][j]
            for m in range(i-1,0,-1):
                if (isCompatible(activitylist[i],activitylist[m])):
                    q = max(q,asp2[m][j-1] + activitylist[i].p)
                    break
            
            asp2[i][j] = q


print asp2[n][k]
print asp2


#todo add when 0 charitable event needs to be scheduled

#Greedy algorithm: select the optimum structure/schedule of activities that do not conflict the start time and finish time
#You have a list of activities, each of them have 2D: the start and finish time
#How to select your schedule of activities in a optimum way

#The idea is to keep choosing the activities with the smallest finish time
import numpy as np
def greedy_algo(l):
    #l is a list with elements indicating start and finish time
    import numpy as np
    sched = []
    l = l[l[:,1].argsort()]
    sched.append(l[0])
    for i in range(1,len(l)):

        if l[i][0] > sched[-1][1]:
            sched.append(l[i])
    return sched

#Testing the algorithm
l = np. array([[0,1],[2,3],[15,20],[4,7],[3,8],[2,8],[6,10],[10,13],[15,17]])
greedy_algo(l)




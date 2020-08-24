#!/bin/python3


"""
Input:
9 5
2 3 4 2 3 6 8 4 5
Output:
2

Input:
5 4
1 2 3 4 4
Output:
0

Input:
5 3
10 20 30 40 50
Output:
1

Algorithms
Sorting
Counting Sort
Dictionary

"""

import math
 

def activityNotifications(expenditure, d):    
    
    result = 0
    count = {}   
    
    SortedtrailingSpent = expenditure[0:d]
    for a in SortedtrailingSpent:        
        if a in count:
            count[a] += 1
        else:
            count[a] = 1             

    i = 0 # sorting SortedtrailingSpent
    for a in count:            
        for c in range(count[a]):  
            SortedtrailingSpent[i] = a
            i += 1
    
    for daySpent in range(d, len(expenditure)):        
    
        if d == 1:
            calcMedian = SortedtrailingSpent[0]
        elif d % 2 == 0:        
            calcMedian =  (SortedtrailingSpent[int(d/2-1)] + SortedtrailingSpent[int(d/2)])/2
        else:
            calcMedian =  SortedtrailingSpent[math.floor(d/2)]
            
        if expenditure[daySpent] >= 2*calcMedian:
            result += 1
        
        if expenditure[daySpent] in count:
            count[expenditure[daySpent]] += 1
        else:
            count[expenditure[daySpent]] = 1
        
        count[expenditure[daySpent-d]] -= 1
        if count[expenditure[daySpent-d]] == 0:
            del count[expenditure[daySpent-d]]
        
        i = 0 # sorting SortedtrailingSpent
        for a in count:
            for c in range(count[a]):  
                SortedtrailingSpent[i] = a
                i += 1
    
    return result


if __name__ == '__main__':
            
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')

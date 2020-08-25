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
5 4
1 2 3 4 5
Output:
1

Input:
5 3
10 20 30 40 50
Output:
1

Input:
16 10
10 9 8 7 6 5 4 3 2 1 1 1 7 1 1 6
Output:
2


Algorithms
Sorting
Counting Sort
Dictionary

"""

import math
 
def activityNotifications(expenditure, d):    
    
    result = 0
    calcMedian = 0
    max_e = max(expenditure)
    
    count = dict(enumerate([0]*(max_e+1)))    
    for e in expenditure[0:d]:        
        count[e] += 1
    
    if d % 2 == 0:
        half_d = int(d/2)
        even = True
    else:
        half_d = math.ceil(d/2)
        even = False
    
    for daySpent in range(d, len(expenditure)):                    
        e = 0
        for i in range(max_e+1):
            e += count[i]
            if e >= half_d:
                break
        calcMedian = i            
        if (e == half_d) and even:
            for i in range(i+1, max_e+1):
                e += count[i]
                if e >= half_d + 1:
                    break
            calcMedian = (calcMedian+i)/2
        
        if expenditure[daySpent] >= int(2*calcMedian):
            result += 1
        
        count[expenditure[daySpent]] += 1
        count[expenditure[daySpent-d]] -= 1
                            
    return result


if __name__ == '__main__':
            
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')

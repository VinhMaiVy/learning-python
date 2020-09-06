#!/bin/python3

"""
Python

Input:
3
10
30
0
40

Output:
2

Input:
4
3
5
4
3
3

Output:
0


"""


import math
import os
import random
import re
import sys



#
# Complete the 'filledOrders' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. INTEGER k
#
def filledOrders(order, k):
    su_order = 0
    nb_order = 0
    s_order = sorted(order)
    
    for odr in s_order:        
        su_order += odr
        if (su_order <= k):            
            nb_order +=1
        else:
            break        
    return nb_order

if __name__ == '__main__':
    
    order_count = int(input().strip())

    order = []

    for _ in range(order_count):
        order_item = int(input().strip())
        order.append(order_item)

    k = int(input().strip())
    
    result = filledOrders(order, k)

    print(str(result) + '\n')
    

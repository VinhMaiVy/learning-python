#!/bin/python3

"""
Python

Input:
10
7 8 3 2 1 4 8 9 4 5
Output:
[1, 2, 3, 4, 4, 5, 7, 8, 8, 9]

Input:
5
4 5 2 1 3

Output:
[1, 2, 3, 4, 5]

"""

def bubble_sort(a):
        
    #for ( i = 1 ; i < n ; i++ )
    #    for ( j = n-1 ; j >= i ; j-- )
    #        if ( a[j] < a[j-1] )
    #            swap a[j] and a[j-1]
    
    n = len(a)
    for i in range(1, n): # from 1 to n
        for j in range(n-1, i-1, -1): # from n-1 to i
            print(j, j-1)
            if (a[j] < a[j-1]):        
                a[j], a[j-1] = a[j-1], a[j]
                print('   swap: a[', j, ']=', a[j] , 'with a[', j-1, ']=', a[j-1])
                print(a)
            
    return(a)

if __name__ == '__main__':
    
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    
    print(a)
    print(bubble_sort(a))

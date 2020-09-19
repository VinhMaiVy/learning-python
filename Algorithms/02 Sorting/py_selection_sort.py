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

def selection_sort(a):
        
    #for ( i = 0 ; i < n-1 ; i++ ) {
    #    k = i
    #    for ( j = i+1 ; j < n ; j++ )
    #        if ( a[j] < a[k] )
    #            k = j
    #    swap a[i] and a[k]
    #}
    
    n = len(a)
    for i in range(n): # from 0 to n-1
        k = i
        for j in range(i+1, n): # from i+1 to n-1            
            if (a[j] < a[k]):
                k = j
            # print(j, k)        
        a[i], a[k] = a[k], a[i]
        #print('   swap: a[', i, ']=', a[i] , 'with a[', k, ']=', a[k])
        #print(a)
            
    return(a)

if __name__ == '__main__':
    
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    
    print(a)
    print(selection_sort(a))

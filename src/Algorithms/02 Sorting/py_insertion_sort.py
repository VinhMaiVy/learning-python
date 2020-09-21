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

def insertion_sort(a):
        
        
    #for ( i = 1 ; i < n ; i++ ) {
    #    for( j = i ; j > 0 ; j-- )
    #        if ( a[j] < a[j-1] )
    #            swap a[j] and a[j-1]
    #        else break
    #}
    
    n = len(a)
    for i in range(1, n): # from 1 to n-1
        for j in range(i, 0, -1): # from i to 1
            #print(j, j-1)
            if (a[j] < a[j-1]):        
                a[j], a[j-1] = a[j-1], a[j]
                #print('   swap: a[', j, ']=', a[j] , 'with a[', j-1, ']=', a[j-1])
                #print(a)
            else:
                break    
    return(a)



def insertion_sort2(a):

    #for ( i = 1 ; i < n ; i++ ) {
    #    j = i
    #    t = a[j]
    #    while ( j > 0 && t < a[j-1] ) {
    #        a[j] = a[j-1]
    #        j--
    #    }
    #    a[j] = t
    #}
    
    n = len(a)
    for i in range(1, n): # from 1 to n
        j = i
        
        t = a[j]
        
        while j>0 and t<a[j-1]:
            a[j] = a[j-1]
            j -= 1
        a[j] = t
    
    return(a)


if __name__ == '__main__':
    
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    
    print(a)
    print(insertion_sort2(a))

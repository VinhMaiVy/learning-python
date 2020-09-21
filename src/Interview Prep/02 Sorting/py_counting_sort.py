#! /bin/python3

"""

Counting Sort

"""

def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m                
        
    for a in array1:        
        count[a] += 1 # count occurences             
        
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            array1[i] = a
            i += 1
    return array1


if __name__ == '__main__':
    
    array1 = [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1]
    max_val = max(array1)
    
    print(array1)
    print(counting_sort( array1, max_val ))
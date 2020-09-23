#!/bin/python3

"""
Python
    Dictionary
    
Input:
10
1 97
2 97
1 20
2 20
1 26
1 20
2 26
3
1 
3

Output:
26
91

Input:
5  
1 4  
1 9  
3  
2 4  
3

Output:
4
9

"""


class HeapMin:

    def __init__(self): 
        self.heap = {}
        self.min = float('inf')
        
    def add(self, val):
        self.heap[val] = self.min
        if val < self.min:
            self.min = val
    
    def delete(self, val):                
        del self.heap[val]
        if val == self.min:
            if self.heap:
                self.min = min(self.heap)
            else:
                self.min = float('inf')
    
    def min(self):
        return self.min

    def __str__(self):
        return str(self.min) 


if __name__ == '__main__':
    
    
    heap = HeapMin()
        
    n = int(input())
    for _ in range(n):
                
        c, *a = list(map(int, input().split()))
        
        if c == 1:     # Add an element  to the heap.
            heap.add(a[0])
                            
        elif c == 2:   # Delete the element  from the heap.           
            heap.delete(a[0])
                    
        elif c == 3:   # Print the minimum of all the elements in the heap.
            print(heap)


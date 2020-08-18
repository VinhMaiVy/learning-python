#!/bin/python3

"""

3
5 2
8 5
2 2

9
955 236
132 107
178 104
394 378
773 29
159 117
928 443
250 146
730 468


"""

import math

# function to find the position  
# of rightmost set bit 
def getPosOfRightmostSetBit(n): 
  
    return int(math.log2(n&-n)+1) 
  
   
def setRightmostUnsetBit(n): 
  
    # if n = 0, return 1 
    if (n == 0): 
        return 1
       
    # if all bits of 'n' are set 
    if ((n & (n + 1)) == 0):     
        return n 
       
    # position of rightmost un-set bit in 'n' 
    # passing ~n as argument 
    pos = getPosOfRightmostSetBit(~n)     
       
    # set the bit at position 'pos' 
    return ((1 << (pos - 1)) | n)

if __name__ == '__main__':
    
    t = int(input())

    list_nk = []    
    
    for t_itr in range(t):
        nk = input().split()
        list_nk.append((int(nk[0]), int(nk[1])))        
                
    for nk in list_nk:
        n = nk[0]
        k = nk[1]
        if (k & 1):
            print(k-1)            
        else:
            m = math.log2(k)
            if math.ceil(m) ==  math.floor(m):                
                if (2**(m+1))-1 <= n:
                    print(k-1)
                else:
                    print(k-2)
            else:                
                if setRightmostUnsetBit(k-1) <= n:
                    print(k-1)
                else:
                    print(k-2)
            
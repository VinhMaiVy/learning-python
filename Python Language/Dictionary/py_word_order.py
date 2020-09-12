#!/bin/python3

"""
Python

Input:
4
bcdef
abcdefg
bcde
bcdef

Output:
3
2 1 1

"""



if __name__ == '__main__':
    
    n = int(input())
    
    dict = {}
    
    for _ in range(n):
        i = input()
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    print(len(dict))
    
    print(*dict.values())
    

    

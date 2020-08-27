#!/bin/python3

"""
Input:
10
161 182 161 154 176 170 167 171 170 174

Output:
169.375

"""

def average(array):
    result = 0
    set_array = set(array)
    result = sum(set_array)/len(set_array)
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
#!/bin/python3

def pairs(k, arr):
    result = 0
    set_arr = set(arr)
    while len(set_arr) > 1:
        n = set_arr.pop()
        if n+k in set_arr:
            result += 1
        if n-k in set_arr:
            result += 1
    return result

def pairs2(k, arr):
    result = 0
    sorted_arr = tuple(sorted(arr))
    len_arr = len(sorted_arr)
    for n in range(len_arr-1):
        m = n+1
        while (sorted_arr[m] - sorted_arr[n]) <= k:
            if (sorted_arr[m] - sorted_arr[n]) == k:
                result += 1
                break
            if  (m < len_arr-1):
                m += 1
            else:
                break
    return result

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    print(result)

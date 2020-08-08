#!/bin/python3

if __name__ == '__main__':

    ds = {}
    s = input()
    for c in s:
        if c in ds:
           ds[c] -= 1
        else:
            ds[c] = -1

    ds_sorted = sorted(ds.items(), key=lambda x: (x[1],x[0]))
    for i in range(min(3, len(ds_sorted))):
        print(ds_sorted[i][0], ds_sorted[i][1]*-1)
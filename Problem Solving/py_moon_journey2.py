#!/bin/python3

from itertools import combinations as combo

def journeyToMoon(n, astronaut):                   # Uses set-arithmetic & counting

    C = []                                          # partition (as array) of sets of astronauts by country

    for a,b in astronaut:
        p, m = {a,b}, len(C)                        # p is doubleton set, m is #countries

        i = next( (k for k in range(m) if p & C[k]), -1 )
        if i == -1:
            C.append( p )
            continue                                # form a new country

        j = next( (k for k in range(i+1,m) if p & C[k]), -1 )
        if j == -1:
            C[i] |= p                               # chain annexation of pair p
        else:
            C[i] |= C[j]
            del C[j]                                # merge countries along p

    nC = list(map( len, C ))
    s = n - sum( nC )                               # find subtotals

    return s*(s-1)//2 + s*(n-s) + sum( x*y for x,y in combo(nC,2))


if __name__ == '__main__':

    np = input().split()
    n = int(np[0]) # Number of astronauts
    p = int(np[1]) # Number of pairs

    astronaut = []
    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))
    #
    result = journeyToMoon(n, astronaut)
    print(result)
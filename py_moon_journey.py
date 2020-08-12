#!/bin/python3

"""
10 7
0 2
1 8
1 4
2 8
2 6
3 5
6 9
-> 23

5 3
0 1
2 3
0 4
-> 6

4 2
1 2
2 3
-> 3

10000 2
1 2
3 4
-> 49994998

"""

from itertools import combinations as combo

def journeyToMoon2(n, astronaut):
    C = []                                          # partition (as array) of sets of astronauts by country
    for a,b in astronaut :
        p, m = {a,b}, len(C)                        # p is doubleton set, m is #countries
        i = next( (k for k in range(m) if p & C[k]), -1 )
        if i == -1 : C.append( p ) ; continue       # form a new country
        j = next( (k for k in range(i+1,m) if p & C[k]), -1 )
        if j == -1 : C[i] |= p                      # chain annexation of pair p
        else : C[i] |= C[j] ; del C[j]              # merge countries along p
    nC = list(map( len, C )) ; s = n - sum( nC )    # find subtotals
    return s*(s-1)//2 + s*(n-s) + sum( x*y for x,y in combo(nC,2))

def journeyToMoon(n, astronaut):
    astronaut_country = {}
    for a in range(n):
        astronaut_country[a] = a

    for p in astronaut:
        for a in range(n):
            if astronaut_country[a] == astronaut_country[p[1]]:
                astronaut_country[a] = astronaut_country[p[0]]
        astronaut_country[p[1]] = astronaut_country[p[0]]

    country_astronauts = {}
    for a in astronaut_country.values():
        if a not in country_astronauts:
            country_astronauts[a] = 1
        else:
            country_astronauts[a] += 1

    result = 0
    sum = 0
    for s in country_astronauts.values():
        result += sum*s
        sum += s

    return result

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
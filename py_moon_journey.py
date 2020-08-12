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
14

0 2 1 8 4 6 9
3 5
7

5 3
0 1
2 3
0 4

4 2
1 2
2 3

"""


def journeyToMoon(n, astronaut):
    result = 0
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

    while country_astronauts.keys():
        astronaut_for_country = country_astronauts.popitem()
        for a in country_astronauts:
            result += astronaut_for_country[1]*country_astronauts[a]

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
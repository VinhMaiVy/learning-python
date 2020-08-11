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
"""


def journeyToMoon(n, astronaut):
    result = 0

    p = astronaut.pop()
    countries_id = 0
    countries = {}
    countries[countries_id] = p

    for p in astronaut:
        t_countries = dict(countries)
        notfound = True
        for t in t_countries:
            current_countries = countries.get(t)
            if p[0] in current_countries:
                current_countries.append(p[1])
                countries[t] = current_countries
                notfound = False
            if p[1] in current_countries:
                current_countries.append(p[0])
                countries[t] = current_countries
                notfound = False
                break
        if notfound:
            countries_id += 1
            countries[countries_id] = p

    return countries

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
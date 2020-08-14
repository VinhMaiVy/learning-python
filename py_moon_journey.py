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


def journeyToMoon(n, astronaut):
    country_astronauts = {}
    for a in range(n):
        country_astronauts[a] = {a}

    for p in astronaut:
        for p0 in country_astronauts:  # Find if the country astronaut 1 is in
            if p[0] in country_astronauts[p0]:
                break
        for p1 in country_astronauts:  # Find if the country astronaut 2 is in
            if p[1] in country_astronauts[p1]:
                break
        if p0 != p1:  # If different country, then we merge
            country_astronauts[p0].update(country_astronauts[p1])
            del country_astronauts[p1]

    result = 0
    sum = 0
    for c in country_astronauts:
        s = len(country_astronauts[c])
        result += sum * s
        sum += s

    return result


if __name__ == '__main__':

    np = input().split()
    n = int(np[0])  # Number of astronauts
    p = int(np[1])  # Number of pairs

    astronaut = []
    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))
    #
    result = journeyToMoon(n, astronaut)
    print(result)

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

    countries = {}
    for a in range(n):
        countries[a] = {a}

    for p in astronaut:
        if p[0] in countries:
            p0 = p[0]
        else:
            for p0 in countries:  # Find country of astronaut 1
                if p[0] in countries[p0]:
                    break

        if p[1] in countries:
            p1 = p[1]
        else:
            for p1 in countries:  # Find country of astronaut 2
                if p[1] in countries[p1]:
                    break

        if p0 != p1:  # If different countries, then we merge the 2 sets
            countries[p0].update(countries[p1])
            del countries[p1] # delete the orphan set

    result = 0
    sum = 0
    for c in countries:
        astronauts = len(countries[c])
        result += sum * astronauts
        sum += astronauts

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

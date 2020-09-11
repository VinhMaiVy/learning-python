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
    for pair in astronaut:
        c = -1
        for c1 in countries:  # Find country of astronaut 1
            if pair[0] in countries[c1]:
                c = c1
                break
        if c == -1:
            c1 = pair[0]
            countries[c1] = {c1}

        c = -1
        for c2 in countries:  # Find country of astronaut 2
            if pair[1] in countries[c2]:
                c = c2
                break
        if c == -1:
            c2 = pair[1]
            countries[c2] = {c2}

        if c1 != c2:  # If different countries, then we merge the 2 sets
            countries[c1].update(countries[c2])
            del countries[c2]  # delete the orphan set

    all = {-1}
    for cc in countries:
        all.update(countries[cc])

    for a in range(n):
        if not a in all:
            countries[a] = {a}

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

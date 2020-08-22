#!/bin/python3

"""
Input:
4 4 3
2 2 3
3 1 4
4 4 4
Output:
9

Input:
4 4 4
1 1 4
2 2 4
3 1 2
4 2 3
Output:
5

Input:
1 5 3
1 1 2
1 2 4
1 3 5
Output:
0

Input:
1 7 3
1 1 2
1 2 4
1 3 5
Output:
2

Input:
2 9 3
2 1 5
2 2 4
2 8 8
Output:
12

Input:
1 10 4
1 3 4
1 1 5
1 7 8
1 10 10
Output:
2

Merge Overlapping Intervals

Dictionary

"""

def gridlandMetro(n, m, k, track):
    # print(n, m, k)
    # print(track)
    
    tracks = {} # dictionary of all tracks
    for t in track:
        r, c1, c2 = t[0]-1, t[1], t[2]        
        # print(r, c1, c2)
        if r in tracks:
            # tracks[r] = tracks[r] + [[c1,c2]]
            merged = False
            for t in range(len(tracks[r])):
                C1 = tracks[r][t][0]
                C2 = tracks[r][t][1]
                if C1 <= c1 <= C2:
                    tracks[r][t][1] = max(c2,C2)
                    merged = True
                    break
                elif (c1 <= C1) and (c2 >= C1):
                    tracks[r][t][0] = c1
                    tracks[r][t][1] = max(c2,C2)
                    merged = True
                    break
            if not merged:
                tracks[r] = tracks[r] + [[c1,c2]]
        else:
            tracks[r] = [[c1,c2]]
    
    len_t = len(tracks)
    result = (n - len_t)*m
    
    for l in tracks:
        result += m
        for t in range(len(tracks[l])):
            result -= tracks[l][t][1] - tracks[l][t][0] + 1
        
    return result


        
if __name__ == '__main__':
        
    nmk = input().split()
    n = int(nmk[0])
    m = int(nmk[1])
    k = int(nmk[2])

    track = []
    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    print(str(result) + '\n')

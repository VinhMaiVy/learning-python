#!/bin/python3

"""

7
100 100 50 40 40 20 10
4
5 25 50 120

6
4
2
1

"""

def climbingLeaderboard(scores, alice):
    currentrank = len(set(scores))
    score_index = 0
    highscore_index = len(scores)-1
    while score_index!=len(alice):
        while alice[score_index] > scores[highscore_index] and highscore_index>-1:
            highscore_index-=1
            if scores[highscore_index]!=scores[highscore_index+1]:
                currentrank-=1
        if alice[score_index] == scores[highscore_index]:
            yield currentrank 
        else:
            yield currentrank+1
        score_index+=1

if __name__ == '__main__':
    
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)
    print('\n'.join(map(str, result)))
    

    
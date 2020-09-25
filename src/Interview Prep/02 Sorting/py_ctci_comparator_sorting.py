#!/bin/python3

"""
Sort
    cmp_to_key

Input:
5
amy 100
david 100
heraldo 50
aakansha 75
aleksa 150

Output:
aleksa 150
amy 100
david 100
aakansha 75
heraldo 50

"""


from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return { 'name':self.name, 'score':self.score }
        
    def comparator(a, b):
        if a.score != b.score:
            return b.score - a.score
        else:
            if a.name == b.name:
                return 0
            else:
                return 1 if a.name > b.name else -1 

if __name__ == '__main__':
    n = int(input())
    data = []
    for i in range(n):
        name, score = input().split()
        score = int(score)
        player = Player(name, score)
        data.append(player)
        
    data = sorted(data, key=cmp_to_key(Player.comparator))
    for i in data:
        print(i.name, i.score)

#!/bin/python3


"""
Input
5
129300455 
5559948277
012334556 
56789
123456879

Output
5

"""

def winningLotteryTicket(tickets):
    pass


if __name__ == '__main__':
    
    n = int(input())

    tickets = []
    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    print(result + '\n')
    

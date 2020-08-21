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

set & combination
bit manipulation

"""

def winningLotteryTicket(tickets):
    tickets_d = []
    tickets_f = 0
    for t in range(len(tickets)):
        tb = ''        
        for n in range(10):
            if str(n) in tickets[t]:
                tb += '1'
            else:
                tb += '0'
        tb = int(tb,2)
        if tb == 1023:
            tickets_f +=1
        else:
            tickets_d.append(tb)
                
    # Combination n*(n-1)/2
    result += int(len(tickets_d)*tickets_f + tickets_f*(tickets_f-1)/2)
    
    while len(tickets_d):
        t1 = tickets_d.pop()
        for t2 in tickets_d:
            if t1 | t2 == 1023:
                result += 1 
    return result


if __name__ == '__main__':
    
    n = int(input())

    tickets = []
    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    print(result)
    

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

dictionary
list comprehension
set & combination
bit manipulation

"""

def winningLotteryTicket(tickets):
            
    tickets_other = 0    
    tickets_d = {}
    _3FF = int('1111111111',2)
    
    for t in range(_3FF+1):
        tickets_d[t] = 0 # Set counter for each dictionary entry
            
    for t in range(len(tickets)):
        tb = int("".join(['1' if str(n) in tickets[t] else '0' for n in range(10)]),2)
        tickets_d[tb] += 1 # Increase counter for dictionary entry
        if tb < _3FF:
            tickets_other += 1        
                            
    # Combination n*(n-1)/2
    tickets_3ff = tickets_d[_3FF]
    tickets_d.pop(_3FF)    
    result = int(tickets_other*tickets_3ff + tickets_3ff*(tickets_3ff-1)/2)

    for t in range(_3FF):
        if tickets_d[t] != 0:
            for u in range(t+1,_3FF):
                if (t | u) == _3FF:
                    result +=  tickets_d[t]*tickets_d[u] 
               
    return result


if __name__ == '__main__':
    
    n = int(input())

    tickets = []
    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    print(result)
    

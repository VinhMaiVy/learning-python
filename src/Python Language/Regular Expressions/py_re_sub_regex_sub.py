#!/bin/python3

"""
Python

Input:
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.

Output:
a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.  

Input:
20
x| ||&|& | & | &&  &&x
x& & |&||  || &&& & &x
x| &&||&& |  & |  |||x
x|&&& |&||  &|& |&|| x
x&& |   | ||&| |&|| &x
x|& &||& && &&&  &&| x
x|& &| | |&|& &  &| |x
x &&& |& & &||&|&&||&x
x  & &&| && ||  ||  |x
x&&& &&&  &|  || | ||x
x|&|& &&  |&   &|||&|x
x    &&&|&&| ||&&& &&x
x  & || |&&&&&|&&&&| x
x|&|&&&|&| || | &||& x
x&& |&|   |& &&&| && x
x &    &&&&& &|& &| |x
x|& & |   & |&  | |&|x
x&|&|&||||| &|&& || |x
x&|&  &&  |&|  &&&||&x
x || & | &&  &|&| |&|x

Output:
x| ||&|& | & | and  &&x
x& & |&||  or &&& & &x
x| &&||&& |  & |  |||x
x|&&& |&||  &|& |&|| x
x&& |   | ||&| |&|| &x
x|& &||& and &&&  &&| x
x|& &| | |&|& &  &| |x
x &&& |& & &||&|&&||&x
x  & &&| and or  or  |x
x&&& &&&  &|  or | ||x
x|&|& and  |&   &|||&|x
x    &&&|&&| ||&&& &&x
x  & or |&&&&&|&&&&| x
x|&|&&&|&| or | &||& x
x&& |&|   |& &&&| and x
x &    &&&&& &|& &| |x
x|& & |   & |&  | |&|x
x&|&|&||||| &|&& or |x
x&|&  and  |&|  &&&||&x
x or & | and  &|&| |&|x
"""
import re

def sub_and_or(match):
    if match.group(0) == ' && ':
        return(' and ')
    else:
        return(' or ')
        
if __name__ == '__main__':
    
    n = int(input())
    for _ in range(n):
        # print(re.sub(r'(?<= )(&&|\|\|)(?= )', sub_and_or, input()))
        print(re.sub(r'( && )|( \|\| )', sub_and_or, input()))
    
#!/bin/python

"""

Given an integer, n, and n-space-separated integers as input, create a tuple,t, of those n integers.
Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format
The first line contains an integer,n , denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple .

Output Format
Print the result of hash(t).

Sample Input
2
1 2
Sample Output
3713081631934410656

"""

def main():
    n = int(input())
    integer_list = map(int, input().split())
    integer_tuple = tuple(integer_list)
    print(hash(integer_tuple))

if __name__ == '__main__':
    main()
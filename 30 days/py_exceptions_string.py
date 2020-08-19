#!/bin/python3

if __name__ == '__main__':
    S = input().strip()
    try:
        n = int(S)
    except:
        print("Bad String")
    else:
        print(n)
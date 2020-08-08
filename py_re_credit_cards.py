#!/bin/python3

import re

def validate_cc(c):
    if re.search('^[456]\\d{3}\\d{4}\\d{4}\\d{4}$|^[456]\\d{3}[-]\\d{4}[-]\\d{4}[-]\\d{4}$', c):
        return (not re.search(r'(\d)\1{3}', re.sub("-", "", c)))

if __name__ == '__main__':
    N = int(input())
    cc = []

    for n in range(N):
        cc.append(str(input()))

    for c in cc:
        if validate_cc(c):
            print('Valid')
        else:
            print('Invalid')
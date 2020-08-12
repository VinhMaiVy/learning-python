#!/bin/python3

import re

if __name__ == '__main__':

    N = int(input())

    N_list = []
    for N_itr in range(N):
        N_list.append(input().split())

    firstName_pattern = re.compile("^[a-z]{1,20}$")
    emailID_pattern = re.compile("^[a-z\\.]{1,40}@gmail\\.com$")

    firstName = ''
    emailID = ''
    firstName_list = []
    for N_itr in N_list:
        firstName = N_itr[0]
        emailID = N_itr[1]
        if firstName_pattern.match(firstName) and emailID_pattern.match(emailID):
            firstName_list.append(firstName)

    for N_itr in sorted(firstName_list):
        print(N_itr)
#!/bin/python

"""



"""

import math
import os
import random
import re
import sys

def main():
    print(list(students))
    students.sort(key = lambda x: x[1])
    best_score = students[len(students)-1][1]
    runner_up_list = list([student for student in students if students[1] < best_score])
    runner_up_score = runner_up_list[len(students)-1][1]
    runner_up_list = list([student for student in students if students[1] >= runner_up_score])
    for student in runner_up_list: print(*student[0])

if __name__ == '__main__':
    students = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    main()
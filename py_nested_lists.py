#!/bin/python

"""



"""

import math
import os
import random
import re
import sys

students = []

def main():
    print(list(students))
    students.sort(key = lambda x: x[1])
    best_score = students[len(students)-1][1]
    runner_up_list = list([student for student in students if students[1] < best_score])
    runner_up_score = runner_up_list[len(students)-1][1]
    runner_up_list = list([student for student in students if students[1] >= runner_up_score])
    for student in runner_up_list: print(*student[0])

if __name__ == '__main__':
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

if __name__ == "__main__":
    # execute only if run as a script
    main()
#!/bin/python

"""

Given the names and grades for each student in a class of N students, store them in a nested list and print
the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print
 each name on a new line.

Example:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Output:
Berry
Harry

List Comprehension

"""

import math
import os
import random
import re
import sys

def main():
    students.sort(key = lambda x: x[1])
    lowest_score = students[0][1]
    runner_down_list = list([student for student in students if student[1] > lowest_score])
    runner_down_score = runner_down_list[0][1]
    runner_up_list = list([student for student in runner_down_list if student[1] == runner_down_score])
    runner_up_list.sort(key = lambda x: x[0])
    for student in runner_up_list: print(*student[0],sep = "")

if __name__ == '__main__':
    students = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    main()
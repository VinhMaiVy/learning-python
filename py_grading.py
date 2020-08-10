#!/bin/python3

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for n in range(len(grades)):
        if (grades[n] >= 38) and (((grades[n] // 5) +1)*5 - grades[n]) < 3:
            grades[n] = ((grades[n] // 5) +1)*5
        print(grades[n])
    return grades

if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
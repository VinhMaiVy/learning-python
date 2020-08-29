#!/bin/python3

"""
Calendar

https://docs.python.org/3/library/calendar.html

Input:
08 05 2015

Output:
WEDNESDAY

"""

import calendar

if __name__ == '__main__':
    
    WEEKDAYS = ('MONDAY','TUESDAY', 'WEDNESDAY', 'THURSDAY', 
                'FRIDAY', 'SATURDAY', 'SUNDAY')
    
    month, day, year = list(map(int, input().rstrip().split()))
    weekday = calendar.weekday(year, month, day)
    print(WEEKDAYS[weekday])

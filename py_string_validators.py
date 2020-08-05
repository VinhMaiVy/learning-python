#! /bin/python

"""

Task

You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters,
digits, lowercase and uppercase characters.

Input Format

A single line containing a string S.

Constraints len(S) < 1000


Output Format

In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

Sample Input
qA2

Sample Output
True
True
True
True
True

"""

import re

if __name__ == '__main__':
    s = input()
    print(bool(re.search("[a-zA-Z0-9]", s)))
    print(bool(re.search("[a-zA-Z]", s)))
    print(bool(re.search("[0-9]", s)))
    print(bool(re.search("[a-z]", s)))
    print(bool(re.search("[A-Z]", s)))

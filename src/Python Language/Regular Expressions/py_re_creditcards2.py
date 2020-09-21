#!/bin/python3

"""
► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.

Examples:

Valid Credit Card Numbers

4253625879615786
4424424424442444
5122-2368-7954-3214

Invalid Credit Card Numbers
42536258796157867       #17 digits in card number → Invalid
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid

Sample Input
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

Sample Output
Valid
Valid
Invalid
Valid
Invalid
Invalid

"""

import re

if __name__ == '__main__':
    TESTER = re.compile(
        r"^"
        r"(?!.*(\d)(-?\1){3})"
        r"[456]"
        r"\d{3}"
        r"(?:-?\d{4}){3}"
        r"$")

    for _ in range(int(input().strip())):
        print("Valid" if TESTER.search(input().strip()) else "Invalid")

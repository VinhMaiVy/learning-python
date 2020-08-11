#! /bin/python3

import re

if __name__ == '__main__':

    regex_integer_in_range = r"[1-9][0-9][0-9][0-9][0-9][0-9]"  # Do not delete 'r'.
    regex_alternating_repetitive_digit_pair = r"_________"  # Do not delete 'r'.

    P = input()

    print(bool(re.match(regex_integer_in_range, P))
          and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
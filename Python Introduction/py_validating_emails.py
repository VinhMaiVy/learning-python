#!/bin/python

"""

You are given an integer  followed by  email addresses. Your task is to print a list containing only valid
email addresses in lexicographical order.

Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.
The maximum length of the extension is .

Sample Input
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Sample Output
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

Regular Expressions

    return True if s is a valid email, else return False

    \w              => matches alphabets and numbers including underscore - => matches -
    [\w-]           => will match either of them
    [\w-]+          => means once or more than once

    @               => match @
    [0-9|a-z|A-Z]+  => match the given range of alphabets and numbers one or more than once
    \.              => will match character .
    [a-z]{1,3}     => will match any string that has lowercase and
    length one, two or three

"""

import re

def fun(s):
    pattern = re.compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$")
    return pattern.match(s)

def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)

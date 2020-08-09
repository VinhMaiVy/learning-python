#! /bin/python3

# Complete the solve function below.

def solve(s):
    return ' '.join((word.capitalize() for word in s.split(' ')))

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
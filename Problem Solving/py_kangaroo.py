#!/bin/python3

"""

0 2 5 3
NO

0 3 4 2
YES

43 2 70 2
NO

"""

def kangaroo(x1, v1, x2, v2):
    result = 'NO' 
    if (v1 != v2):
        jumps = (x2-x1)/(v1-v2) 
        if jumps > 0 and jumps % 1 == 0:
            result = 'YES'
    return result


if __name__ == '__main__':
    
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result + '\n')

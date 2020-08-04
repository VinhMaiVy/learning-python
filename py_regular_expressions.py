"""

"""

import sys
import re


def main(arg1):
    print(re.sub("\s", "-", arg1))

if __name__ == '__main__':
    arg1 = str(sys.argv[1])
    main(arg1)

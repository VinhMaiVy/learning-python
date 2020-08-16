#! /bin/python

"""

Consider a list (list = []). You can perform the following commands:
    insert i e: Insert integer  at position .
    print: Print the list.
    remove e: Delete the first occurrence of integer .
    append e: Insert integer  at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7
 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example
4
append 1
append 2
insert 3 1
print

append 1: Append 1 to the list, arr = [1].
append 2: Append 2 to the list,  arr = [1,2].
inser 3 1: Insert 3 at index ,  arr = [1,3,2].
: Print the array.
Output:
[1, 3, 2]

"""

def main():
    N = int(input())
    list_ = []
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd != "print":
            cmd += "(" + ",".join(args) + ")"
            eval("list_." + cmd)
        else:
            print(list_)

if __name__ == '__main__':
    main()

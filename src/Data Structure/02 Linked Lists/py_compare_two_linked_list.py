#!/bin/python3

"""
Singly Linked List

Input:
2
2
1
2
1
1
2
1
2
2
1
2

Output:
0
1

"""


import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node):
    while node:
        print(str(node.data))
        node = node.next


# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):

    while True:
        if (not llist1) and (not llist2):
            return 1
        elif (not llist1) or (not llist2):
            return 0
        if llist1.data != llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next


if __name__ == '__main__':
    
    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        print(str(int(result)) + '\n')

    
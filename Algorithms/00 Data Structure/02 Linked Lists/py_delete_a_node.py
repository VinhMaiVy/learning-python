#!/bin/python3

"""
Delete Node from Linked List

Input:
8
20
6
2
19
7
4
15
9
3
Output:
20 6 2 7 4 15 9

"""


import math
import os
import random
import re
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

# Complete the deleteNode function below.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
      
    if head and position > 0:
        node = head
        previous = 0
        while node.next and previous != position-1:
            node = node.next
            previous += 1
        if node.next:
            if node.next.next:
                node_delete = node.next
                node.next = node.next.next
                del node_delete
            else:
                node.next = None
    elif position == 0:
        node_delete = head        
        if head.next:
            head = head.next
        del node_delete
    else:
        head = None
    
    return(head)


if __name__ == '__main__':
    
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1)
    print('\n')

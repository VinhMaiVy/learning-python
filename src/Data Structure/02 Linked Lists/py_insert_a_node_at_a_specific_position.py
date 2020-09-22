#!/bin/python3

"""
Linked List

Input:
3
16
13
7
1
0

Output:
16 13 1 7

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

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
        
    new_node = SinglyLinkedListNode(data)

    if head and position:
        node = head
        current = 1
        while node.next and current != position:
            node = node.next
            current += 1
        new_node.next = node.next        
        node.next = new_node        
    elif not position:
        new_node.next = head
        head = new_node
    else:
        head = new_node
    
    return(head)


if __name__ == '__main__':
    
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head)
    print('\n')

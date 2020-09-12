#!/bin/python3

"""
Linked List

Input:
5
383
484
392
975
321

Output:
321
975
392
484
383

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

def print_singly_linked_list(node):
    while node:
        print(str(node.data))
        node = node.next

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
        
    node = SinglyLinkedListNode(data)

    if llist:            
        node.next = llist
            
    return(node)


if __name__ == '__main__':
    

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    
    print_singly_linked_list(llist.head)
    print('\n')
        

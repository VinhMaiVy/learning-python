#!/bin/python3

"""
Recursion

Input:
1
4
2
3
4
10
11

Output:
1 3 4 5 10

"""


import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node):
    while node:
        print(str(node.data))
        node = node.next

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    
    new_node = DoublyLinkedListNode(data)
    
    current_node = head
    
    while True:
        if not current_node or current_node.data > data:
            break
        previous_node = current_node
        current_node = current_node.next
    
    if not current_node:
        new_node.previous = previous_node
        previous_node.next = new_node
    elif current_node.prev:
        current_node.prev.next = new_node
        new_node.previous = current_node.prev
    else:
        head = new_node
        
    new_node.next = current_node
    
    return head

def sortedInsert2(head, data):
    node = DoublyLinkedListNode(data)
    
    if not head:
        return node
    elif (data < head.data):
        node.next = head
        head.prev = node
        return node
    else:
        node = sortedInsert2(head.next, data)
        head.next = node 
        node.prev = head
        return head

if __name__ == '__main__':
    
    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert2(llist.head, data)

        print_doubly_linked_list(llist1)
        print('\n')

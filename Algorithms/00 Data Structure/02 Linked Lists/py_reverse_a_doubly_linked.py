#!/bin/python3

"""
Doubly Linked List
Recursion

Input:
1
6
1
2
1
3
5
4

Output:
5 4 3 2 1 1

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

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    
    last = head
    while last.next:
        last = last.next
    
    tail = DoublyLinkedList()
        
    while last:        
        tail.insert_node(last.data)
        last = last.prev
    
    return tail.head
    

def reverse2(head):
    if not head:
        return head
    head.next, head.prev = head.prev, head.next
    if not head.prev:
        return head
    return reverse2(head.prev)


def reverse3 (head):
    temp = head
    newHead = head
    while temp:
        prev = temp.prev
        temp.prev = temp.next
        temp.next = prev
        newHead = temp
        temp = temp.prev        
    return newHead

    
if __name__ == '__main__':
    
    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse3(llist.head)

        print_doubly_linked_list(llist1)
        print('\n')


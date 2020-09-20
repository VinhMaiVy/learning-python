#!/bin/python3

import math
import os
import random
import re
import sys

"""
Singly Linked List

Input:
1
2
5
1
2
3
4
5
3
8
9
10

Output:


"""


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
        fptr.write(str(node.data))
        node = node.next



# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findLength(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def advance(head, steps):
    for _ in range(steps):
        head = head.next
    return head

def findMergeNode(headA, headB):
    lenA = findLength(headA)
    lenB = findLength(headB)
    
    if lenA > lenB:
        headA = advance(headA, lenA - lenB)
    elif lenA < lenB:
        headB = advance(headB, lenB - lenA)
    
    while headA != headB:
        headA = headA.next
        headB = headB.next
    return headA.data
       
if __name__ == '__main__':
    
    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

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
            
        ptr1 = llist1.head;
        ptr2 = llist2.head;

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        print(str(result) + '\n')
    
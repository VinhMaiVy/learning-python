#!/bin/python3

"""
Merge two sorted lists
Recursion

Input:
1
3
1
5
5
3
2
2
2

Output:
1 2 3 4 5 6

Input:
1
3
4
5
6
3
1
2
10

Output:
1 2 4 5 6 10 

1
3
4 1
5 2
6 3

3
1 1
2 2
10 3

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

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists2(head1, head2):
        
    current1 = head1
    current2 = head2
    previous1 = None
    
    while current2:
        if current1.data == current2.data:            
            temp1 = current1.next
            temp2 = current2.next
            current1.next = current2
            current2.next = temp1
            previous1 = current2
            current1 = current2                        
            current2 = temp2                        
        elif current1.data < current2.data:
            previous1 = current1
            if current1.next:
                current1 = current1.next
            else:
                current1.next = current2
                break
        else: # current1.data > current2.data            
            temp2 = current2.next
            if previous1:
                previous1.next = current2
                previous1 = current2
            else:                
                previous1 = current2
                head1 = current2
            current2.next = current1 
            current2 = temp2
                        
    return(head1)


def mergeLists(head1, head2):
  if head1 is None and head2 is None:
    return None
  
  if head1 is None:
    return head2

  if head2 is None:
    return head1
  
  if head1.data < head2.data:
    smallerNode = head1
    smallerNode.next = mergeLists(head1.next, head2)
  else:
    smallerNode = head2
    smallerNode.next = mergeLists(head1, head2.next)
  
  return smallerNode


             
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

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3)
        print('\n')

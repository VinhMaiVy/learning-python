#!/bin/python3

"""

6
1
2
2
3
3
4

"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        start = head
        while(head.next!=None):
            if head.data == head.next.data:
                #delete start.next
                if (head.next.next!=None):
                    p = head.next
                    head.next = head.next.next
                    del p
                else:
                    p = head.next
                    head.next = None
                    del p
            else:
                head = head.next    
        return start


if __name__ == '__main__':
    mylist= Solution()
    T=int(input())

    head=None
    for i in range(T):
        data=int(input())
        head=mylist.insert(head,data)    
    head=mylist.removeDuplicates(head)
    mylist.display(head); 
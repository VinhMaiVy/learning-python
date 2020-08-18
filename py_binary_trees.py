#!/bin/python3

"""

8
3
5
2
1
4
6
7
8

6
3
5
4
7
2
1

"""


import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root    

    def levelOrder(self,root):
        queue = [root]
        list = []
        while len(queue)>0:
            current = queue.pop(0) 
            list.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print(" ".join(map(str,list)))    
                            
                                    
if __name__ == '__main__':
    T=int(input())
    myTree=Solution()
    root=None
    for i in range(T):
        data=int(input())
        root=myTree.insert(root,data)
    myTree.levelOrder(root)

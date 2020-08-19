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

"""

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

    def getHeight(self,root):
        if root.right:
            hr = self.getHeight(root.right) + 1
        else:
            hr = 0
        if root.left:
            hl = self.getHeight(root.left) + 1
        else:
            hl = 0
        return max(hr,hl) 

if __name__ == '__main__':
    T=int(input())
    myTree=Solution()
    root=None
    for i in range(T):
        data=int(input())
        root=myTree.insert(root,data)
    height=myTree.getHeight(root)
    print(height)
#!/bin/python3

"""
Binary Search Tree
Recursion

Input:
6
4 2 3 1 7 6
1 6

Output:
7

Input:
8
8 4 9 1 2 3 6 5
1 2

Output:
1
"""


class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def findpath(root, v):
    if root:
        if v == root.info: # v == root.info
            return [root]
        elif v < root.info:            
            match = findpath(root.left, v)
            if match:
                return match + [root]
            else:
                return []
        elif v > root.info:                
            match = findpath(root.right, v)
            if match:
                return match + [root]
            else:
                return []   
    else:
        return []
        
def lca2(root, v1, v2):
    findpath_v1 = findpath(root, v1)
    findpath_v2 = findpath(root, v2)
    i = 0
    for i in range(-1, -min(len(findpath_v1), len(findpath_v2))-1, -1):
        if findpath_v1[i].info != findpath_v2[i].info:
            return findpath_v1[i+1]
    #print(findpath_v1[i].info)
    return findpath_v1[i]


def lca(root, v1, v2):
    # The value of a common ancestor has to always be between the two values in question.    
    if root.info < v1 and root.info < v2:
        return lca(root.right, v1, v2)
    elif root.info > v1 and root.info > v2:
        return lca(root.left, v1, v2)
    else:
        return root

if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())
    
    arr = list(map(int, input().split()))
    
    for i in range(t):
        tree.create(arr[i])
    
    v = list(map(int, input().split()))
    
    #print(findpath(tree.root, v[0]))
    #print(findpath(tree.root, v[1]))
    ans = lca(tree.root, v[0], v[1])    
    print (ans.info)

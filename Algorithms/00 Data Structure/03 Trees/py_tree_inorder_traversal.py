#!/bin/python3

"""
Trees
Recursion

Input:
6
1 2 5 3 4 6

Output:
1 2 3 4 5 6


Input:
7
5 2 1 7 3 4 6

Output:
1 2 3 4 5 6 7


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

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder2(root):

    # Set current to root of binary tree 
    current = root  
    stack = [] # initialize stack 
    l_info = []
    done = 0 
      
    while True: 
          
        # Reach the left most Node of the current Node 
        if current: 
              
            # Place pointer to a tree node on the stack  
            # before traversing the node's left subtree 
            stack.append(current) 
          
            current = current.left  
  
        # BackTrack from the empty subtree and visit the Node 
        # at the top of the stack; however, if the stack is  
        # empty you are done 
        elif stack: 
            current = stack.pop() 
            l_info.append(current.info) 
          
            # We have visited the node and its left  
            # subtree. Now, it's right subtree's turn 
            current = current.right  
  
        else: 
            break
        
    print(' '.join([str(i) for i in l_info]))

def inOrder(root):
    if root:        
        inOrder(root.left)        
        inOrder(root.right)
        print(root.info, end=" ")
        

            
if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())
    
    arr = list(map(int, input().split()))
    
    for i in range(t):
        tree.create(arr[i])
    
    inOrder2(tree.root)
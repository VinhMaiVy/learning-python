#!/bin/python3

"""
Trees

Input:
7
4 3 1 5 2 8 6

Output:
True

Input:
7
4 3 1 5 2 8 4

Output:
False
"""


class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val <= current.data:
                #if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                #elif val > current.data:
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
self.data (the value of the node)
"""
def check_binary_search_tree_2(root): # ---- WRONG -----
                
    if root.left:
        if root.left.data < root.data:
            left = check_binary_search_tree_(root.left)
        else:
            left = False
    else:
        left = True
    
    if root.right:
        if root.right.data > root.data:
            right = check_binary_search_tree_(root.right)
        else:
            right = False
    else:
        right = True
        
    return left and right


def check(root, nodes_list):
    if root:
        if not check(root.left, nodes_list):
            return False

        if nodes_list and (root.data in nodes_list or root.data < nodes_list[-1]):
            return False

        nodes_list.append(root.data)

        if not check(root.right, nodes_list):
            return False
        
        return True
    
    else:
        return True

def check_binary_search_tree_(root):
    nodes_list = []
    return check(root, nodes_list)

        
if __name__ == '__main__':
    tree = BinarySearchTree()
    
    t = int(input())    
    arr = list(map(int, input().split()))
    
    for i in range(t):
        tree.create(arr[i])
    
    print(check_binary_search_tree_(tree.root))
    
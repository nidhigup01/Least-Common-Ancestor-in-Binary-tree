# -*- coding: utf-8 -*-
"""
Created on Thu May 31 13:27:37 2018
Question 4
Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node 
from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree,
but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. 
You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. 
The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, 
where the index of the list is equal to the integer stored in that node and a 1 represents a child node, 
r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes 
in no particular order. For example, one test case might be
question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.


"""
# This function assumes that n1 and n2 are present in
# Binary Tree
class Node_root:
     
    # Constructor to create a new tree node
    def __init__(self, key):
        self.key = key 
        self.left = None
        self.right = None
     
# This function returns pointer to LCA of two given
# values n1 and n2
# This function assumes that n1 and n2 are present in
# Binary Tree
def findLCA(T, key, n1, n2):
    
    root = Node_root(key)
    print ('root.key', root.key)
    # Base Case
    if root is None or T == None or T == [[]]:
        return None
    num_rows = len(T)
    print ('num_rows', num_rows)
    num_columns = len(T[0])
    print ('num_columns', num_columns)
   
    parent = key
    print ('parent', parent)
    for child in range(0, num_columns):
        if T[parent][child] == 1 and  child <= parent:
            root.left = child
            print ('root.left', root.left )
            
        elif T[parent][child] == 0:
                root.left = None
        elif T[parent][child] == 1 and  child > parent:
            root.right = child
            print ('root.right', root.right )
    
    # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
    if root.key == n1 or root.key == n2:
        return root 
 
    # Look for keys in left and right subtrees
    left_lca = findLCA(T, root.left, n1, n2) 
    right_lca = findLCA(T, root.right, n1, n2)
 
    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root 
 
    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca
 
 
# Driver program to test above function
 
# Let us create a binary tree given in the above example
print ("LCA(4,5) = ", findLCA([[0, 1, 0, 0, 0],[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]], key = 3, n1 = 1, n2 = 4))

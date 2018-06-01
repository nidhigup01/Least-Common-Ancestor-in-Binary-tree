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
class Node():
    # Constructor to create a new tree node
    def __init__(self, root = None, T = [[]]):
        self.root = root
        self.left = None
        self.right = None
        self.T = T
    
    def left_child(self):
        num_rows = len(self.T)
        print ('num_rows', num_rows)
        num_columns = len(self.T[0])
        print ('num_columns', num_columns)
        parent = self.root
        print ('parent', parent)
        print('T[3][0]', self.T[3][0])
        print('T[3][1]', self.T[3][1])
        print('T[3][2]', self.T[3][2])
        print('T[3][3]', self.T[3][3])
        print('T[3][4]', self.T[3][4])
        for child in range(0, num_columns):
            if self.T[parent][child] == 1 and  child <= parent:
                node_root.left = child
                print ('node_root.left', node_root.left )
                return node_root.left
            
    def right_child(self):
        num_rows = len(self.T)
        print ('num_rows', num_rows)
        num_columns = len(self.T[0])
        print ('num_columns', num_columns)
        parent = self.root
        print ('parent', parent)
        for child in range(0, num_columns):   
            if self.T[parent][child] == 1 and  child > parent:
                node_root.right == child
                print ('node_root.right', node_root.right )
                return node_root.right
            
    def LCA_binary_tree(self, r, n1, n2):
        T= self.T
        root = r
     # Base Case
        if root is None or T == None or T == [[]]:
            print ('none')
            return None
    
        node_root.data = root
        print ('node_root.data', node_root.data )
    
    
     # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
        if node_root.data == n1 or node_root.data == n2:
            return node_root.data 
    # Look for keys in left and right subtrees
        left_lca = node_root.LCA_binary_tree(node_root.left_child(), n1, n2) 
        print('left_lca', left_lca)
        right_lca = node_root.LCA_binary_tree(node_root.right_child(), n1, n2)
        print('right_lca', right_lca)
    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA. 
        if left_lca and right_lca:
            return node_root.data 
    
    # Otherwise check if left subtree or right subtree is LCA
        return left_lca if left_lca is not None else right_lca
 
      

# Test cases
    
 
# Let us create a binary tree given in the above example
node_root = Node(3, [[0, 1, 0, 0, 0],[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]])

node_root.LCA_binary_tree(r = 3, n1 = 1,n2 = 4)

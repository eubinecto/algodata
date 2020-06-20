# Chapter 8.64/65 (Project Question)
page 359 of 'Data Structures and Algorithms in Python by Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser (z-lib.org)'.

## Q.64
Implement the binary tree ADT using the array-based representation described in Section 8.3.2

## Q.65
Implement the tree ADT using a linked structure as described in Section 8.3.3. <br/> 
Provide a reasonable set of update methods for your tree.

## Tree (ADT)
~~~
Tree
 |
(BinaryTree / LinkedTree)
    |
(ArrayBinaryTree / LinktedBinaryTree)
~~~

## Cases
### Base case
n(Tree) = 0  means the tree is empty
### Step case
parent T has t and t' children. Then T = tree(t, t') 

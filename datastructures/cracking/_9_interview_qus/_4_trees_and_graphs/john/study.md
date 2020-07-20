# Trees

## 16/07/20

### 4.2 Minimal Trees

#### Minimal Tree: 
> Given a sorted (increasing order) array with unique integer elements, write an algo­rithm to create a binary search tree with minimal height. <br/>
> Hints:#19,#73,#116


"Binary Search Tree":
왼쪽 자녀는 부모보다 작고, 오른쪽은 크거나 같다. 


> Hint #19: 
> A minimal binary tree has about the same number of nodes on the left of each node as on the right. Let's focus on just the root for now. How would you ensure that about the same number of nodes are on the left of the root as on the right?

> Hint #73: 
> You could implement this by finding the "ideal" next element to add and repeatedly calling insertValue. This will be a bit inefficient, as you would have to repeatedly traverse the tree. Try recursion instead. Can you divide this problem into subproblems?

> Hint #116: 
> Imagine we had a createMinimalTree method that returns a minimal tree for a given array (but for some strange reason doesn't operate on the root of the tree). Could you use this to operate on the root of the tree? Could you write the base case for the function? Great! Then that's basically the entire function.

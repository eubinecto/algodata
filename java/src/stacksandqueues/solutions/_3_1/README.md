# Question

> Describe how you could use a single array to implement three stacks. (pg 98, chapter 3)

hints: #2, #12, #38, #58

## attempt1

Some initial thoughts.

There could be two ways of approaching this problem; The first one being the simpler one (yet inefficient) 
the other one being a more complex one (yet more efficient).

### the simple approach
Break the array into three sections, each of which is allocated to each linkedListStack.

When some element is pushed into each linkedListStack, you store the element in the section allocated.

If any of each section runs out of space, you resize the array. (make a larger one and copy & paste)

Drawbacks of this approach
1. simple, but potential waste of space.
  - resizing could happen just because linkedListStack A has run out of space, when linkedListStack B and C are still empty.
  
  
 ### the complex approach
 Adopt the concept of virtual address.
 
 That is, the starting index at which to store elements is 0 for all three stacks, which will be a
 "virtual address" of each linkedListStack. 
 
 Given a virutal address of a linkedListStack, we get the real address, the logical address, from a page table.
 
But what would the algorithm for the page table? - that, I can't come up with a solution right off the bat.

wait, but the page table approach is exactly the same as the "sections' approach...
- swapping?
- context switching?
- dirty location?


##  hints
### 2
A linkedListStack is simply a data structure in which the most recently added elements are
removed first. Can you simulate a single linkedListStack using an array? Remember that there are
many possible solutions, and there are tradeoffs of each.


 
      


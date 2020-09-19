# Question

> Describe how you could use a single array to implement three stacks. (pg 98, chapter 3)

- hints: #2, #12, #38, #58

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

No, this is not what you want..



##  hints
### 2
> A linkedListStack is simply a data structure in which the most recently added elements are
removed first. Can you simulate a single linkedListStack using an array? Remember that there are
many possible solutions, and there are tradeoffs of each.


What are the trade-offs?


stack | last inserted element | required space
--- | --- | ---
`LinkedListStack` | Slow; O(N) but can be O(1) if maintains `lastNode` pointer  | just N 
`ArrayStack` | Fast; O(1) | N + more



time complexities of the implementations:

operation | LinkedListStack | ArrayStack
--- | --- | ---
push | O(1), amortised | O(1)
pop | O(1) | O(1)
peek | O(1) | O(1)
isEmpty | O(1) | O(1)
 
the  time complexities are the same, except that `push` in ArrayStack runs in **amortised** O(1).

and array stack requires more space than LinkedListStack, as the capacity of the array will always be larger than the
size of the stack.

### 12
> We could simulate three stacks in an array by just allocating the first third of the array to
  the first stack, the second third to the second stack, and the final third to the third stack.
  One might actually be much bigger than the others, though. Can we be more flexible
  with the divisions?
      
      
Yup, this is what immediately came to mind. (the simple approach).


### 38

> If you want to allow for flexible divisions, you can shift stacks around. Can you ensure
that all available capacity is used?


what does it mean by  "shift stacks around"?

### 58
> Try thinking about the array as circular, such that the end of the array "wraps around"to
the start of the array.


Ha...? something like collision resolution? But that way we have to search through the array..
Which is not the most efficient way of doing this.


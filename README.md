# Data Structures
This file holds sample code for a number of classic data structures impemented in python.

**Authors:** Kavdi Hodgson and Megan Flood

## Linked-List

List of values stored in nodes linked to each other in one direction.

A single linked list is beneficial when creating a to do list. You can remove the items when they are completed whithout having to alter the entire list. And there is no need to iterate through it from both directions. 

### Constructor:
```python
l = LinkedList(iterable='list, tuple, or str')
```
### Implements the following methods:
- **push(val):** Add another value to the front of the list.
    - Time complexity: O(1)
- **pop():** Remove the first node and return it's value. Raises an IndexError if there are no values to return.
    - Time complexity: O(1)
- **size():** Get the size of the LinkedList.
    - Time complexity: O(1)
- **search(val):** Find the node that has the given value if present, else None.
    - Time complexity: O(n)
- **remove(node):** Remove the given node from the LinkedList. Raises a ValueError if the node is not in the list.
    - Time complexity: O(n)
- **display():** Display LinkedList as if it were a tuple literal. Ex: “(12, ‘sam’, 37, ‘tango’)”
    - Time complexity: O(n)


## Stack

Structure for values in a stack where first item in is last out.

### Constructor:
```python
s = Stack(iterable='list, tuple, or str')
```
### Implements the following methods:
- **push(val):** Add another value to the top of the stack.
    - Time complexity: O(1)
- **pop():** Remove the top node and return it's value. Raises an IndexError if there are no values to return.
    - Time complexity: O(1)


## Doubly-Linked-List


List of values stored in nodes linked in two directions.


A doubly linked list is better for keeping a log of information, such as history, this way you can access information from both directions.

### Constructor:
```python
l = DLL(iterable='list, tuple, or str')
```
### Implements the following methods:
- **push(val):** Add another value to the front of the list.
    - Time complexity: O(1)
- **pop():** Remove the first node and return it's value. Raises an IndexError if there are no values to return.
    - Time complexity: O(1)
- **remove(val):** Remove the given value from the doubly-linked list. Raises a ValueError if the value is not in the list.
    - Time complexity: O(n)
- **append(val):** Append the value at the tail of the list.
    - Time complexity: O(1)
- **shift():** Remove the last value from the tail of the list and return it. Raises an IndexError if there are no values to return
    - Time complexity: O(1)

## Queue

Structure for values in a queue where first item in is first out.

### Constructor:
```python
q = Queue(iterable='list, tuple, or str')
```
### Implements the following methods:
- **enqueue(value):** Add a value to the end of the queue.
    - Time complexity: O(1)
- **dequeue():** Remove the value from the front of the queue and return it. Raises an IndexError if there are no values to return.
    - Time complexity: O(1)
- **peek():** Get the value from the front of the queue without removing it.
    - Time complexity: O(1)
- **size():** Get the size of the queue.
    - Time complexity: O(1)

## Deque

Structure for values in a deque, double-ended queue.

### Constructor:
```python
d = Deque(iterable='list, tuple, or str')
```
### Implements the following methods:
- **append(value):** Add a value to the end of the deque.
    - Time complexity: O(1)
- **appendleft(value):** Add a value to the front of the deque.
    - Time complexity: O(1)
- **pop():** Remove the value from the end of the deque and return it. Raises an IndexError if there are no values to return.
    - Time complexity: O(1)
- **popleft():** Remove the value from the front of the deque and return it. Raises an IndexError if there are no values to return.
    - Time complexity: O(1)
- **peek():** Get the value from the end of the deque without removing it.
    - Time complexity: O(1)
- **peekleft():** Get the value from the front of the deque without removing it.
    - Time complexity: O(1)
- **size():** Get the size of the deque.
    - Time complexity: O(1)

## Binary Heap

Structure for values in a Binary Heap. A max binary heap is a complete binary tree where each level of the tree is greater than the level below it. A min heap has the lowest values at the top.

### Constructor:
```python
h = BinHeap(iterable='list, tuple, or str', is_max_heap=True)
```
### Implements the following methods:
- **push(val):** Put a new value into the binary heap.
    - Time coplexity: O(log(n))
- **pop():** Remove the value from the end of the heap and return it. Raises an IndexError if there are no values to return.
    - Time complexity: O(log(n))

## Resources

- **Wikipedia:** https://en.wikipedia.org/wiki/Binary_heap

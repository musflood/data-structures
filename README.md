# Data Structures
This file holds sample code for a number of classic data structures impemented in python.

**Authors:** Kavdi Hodgson and Megan Flood

## Linked-List
Constructor:
```python
l = LinkedList(iterable='list, tuple, or str')
```
Implements the following methods:
- push(val): Add another value to the front of the list.
    - Time complexity: O(1)
- pop(): Remove the first node and return it's value. Raises a IndexError if there are no values to return.
    - Time complexity: O(1)
- size(): Get the size of the LinkedList.
    - Time complexity: O(1)
- search(val): Find the node that has the given value if present, else None.
    - Time complexity: O(n)
- remove(node): Remove the given node from the LinkedList. Raises a ValueError if the node is not in the list.
    - Time complexity: O(n)
- display(): Display LinkedList as if it were a tuple literal. Ex: “(12, ‘sam’, 37, ‘tango’)”
    - Time complexity: O(n)

## Resources



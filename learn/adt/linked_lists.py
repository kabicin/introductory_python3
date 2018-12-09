from typing import Union
"""
SINGLY LINKED LISTS


Memory created in a regular list is often stored contiguously (each element appears in memory one after another).
To counteract the problem of not finding enough "free space" to allocate, we can use a linked list.

A linked list is a collection of Nodes that are connected by a "next" attribute, where each node may be stored separately
in memory.

This next attribute is either another Node OR a None (null) value

By construction, the nodes in this linked list will only be able to access a NEXT value, therefore you must traverse the list again
if you would like to obtain any value towards the "front" of the linked list, relative to the current node. As a result,
we may only traverse towards the "back" of the linked list.

This is problem is solved in doubly linked lists, in which a "prev" attribute is also stored for every node, allowing you
to traverse in both towards the "back" or "front" of the linked list.
"""


class Node:
    """
    Represents a node object
    """
    value: object
    nxt: Union['Node', None]

    def __init__(self, value, nxt=None):
        """
        Initialize a node with value, value and nxt node, nxt.
        """
        self.value = value
        self.nxt = nxt

    def __str__(self):
        s = ""
        curr = self
        while curr is not None:
            s += str(curr.value)
            if curr.nxt is not None:
                s = s + " -> "
            curr = curr.nxt
        return s


class LinkedList:
    """
    Represents a (single) linked list
    """
    front: Union['Node', None]
    back: Union['Node', None]
    size: int

    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def append(self, val):
        n = Node(val)
        if self.back is None:
            self.front = n
            self.back = n
        else:
            self.back.nxt = n
            self.back = n
        self.size += 1

    def prepend(self, val):
        n = Node(val)
        if self.front is None:
            self.front = n
            self.back = n
        else:
            n.nxt = self.front
            self.front = n
        self.size += 1

    def insert(self, index, val):
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.prepend(val)
        elif index == self.size:
            self.append(val)
        else:
            i = 0
            curr = self.front
            n = Node(val)
            while i < index - 1 and curr is not None:
                i += 1
                curr = curr.nxt
            n.nxt = curr.nxt
            curr.nxt = n
        self.size += 1


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.insert(1, 15)
    ll.insert(0, 203)
    ll.insert(2, 12)
    ll.insert(6, 100)
    print(ll.front)


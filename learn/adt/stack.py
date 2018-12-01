
"""
Stack Class

The stack is LIFO - Last-in First-out
The three main methods used for a stack are push, pop, and is_empty
The stack below is implemented using a Python list
"""


class Stack:
    """
    Represents a stack object
    """
    storage: list

    def __init__(self):
        self.storage = []

    def __str__(self):
        strx = "----TOP OF STACK ----\n"
        for x in self.storage[::-1]:
            strx += str(x) + "\n"
        strx += "----BOTTOM Of STACK ----"
        return strx

    def push(self, item: object):
        self.storage.append(item)

    def pop(self):
        if not self.is_empty():
            return self.storage.pop()

    def is_empty(self):
        return len(self.storage) == 0


if __name__ == "__main__":
    s = Stack()
    s.push("chicken")
    s.push("cheese")
    s.push("pizza")
    s.pop()
    s.pop()
    print(s)

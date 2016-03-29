class Stack(object):
    """Create a stack class using a list"""

    def __init__(self):
        self._stack = []

    def push(self, item):
        """Add an item to the top"""

        self._stack.append(item)

    def pop(self):
        """Remove the top item"""

        self._stack.pop()

    def peek(self):
        """Return the top item of the stack"""

        return self._stack[-1]

    def is_empty(self):
        """Check if the stack is empty"""

        return not self._stack


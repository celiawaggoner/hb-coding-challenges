class Node(object):
    """Node in a tree."""

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def count_employees(self):
    """Return a count of how many employees this person manages.

    Return a count of how many people that manager manages. This should
    include *everyone* under them, not just people who directly report to
    them.
    """
        #start count of employees to zero
        count = 0

        #iterate over children of self and increment count
        #then call recursive function on that child
        for child in self.children:
            count += 1 + child.count_employees()

        return count
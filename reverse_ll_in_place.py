class Node(Object):
    """Node class in linked list"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList(Object):
    """Linked list class"""

    def __init__(self, head=None):
        self.head = head

def reverse_ll_in_place(lst):
    """Reverse a linked list in place"""

    prev = None
    curr = lst.head

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    lst.head = prev

class Node(Object):
    """Node class in a linked list"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reverse_linked_list(head):
    """Given a linked list head node, reverse the list and return the new head node"""

    output_head = None
    curr = head

    while curr:
        output_head = Node(curr.data, curr.next)
        curr = curr.next

    return output_head
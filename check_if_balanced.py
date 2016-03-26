class BinaryNode(object):
    """Class for a node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_balanced(self):
        """Check if the tree is balanced at this node"""

        def _num_descendants(node):
            """Returns the number of descendants or None if already imbalanced."""

            #establish base case to be when we are not at node
            if not node:
                return 0

            # Get descendants on left; if "None", already imbalanced
            left = _num_descendants(node.left)

            if left is None:
                return None

            # Get descendants on right; if "None", already imbalanced
            right = _num_descendants(node.right)

            if right is None:
                return None

            #check if absolute value between left and right is greater than 1
            #if greater than 1, tree os imbalanced 
            if abs(left - right) > 1:
                return None

            # Height of this node is height of our deepest descendant + ourselves
            return max(left, right) + 1

        return _num_descendants(self) is not None
class PersonNode(object):
    """A node in a graph representing a person.

    This is created with a name and, optionally, a list of adjacent nodes.
    """

    def __init__(self, name, adjacent=[]):
        self.name = name
        self.adjacent = set(adjacent)

    def __repr__(self):
        return "<PersonNode %s>" % self.name


class FriendGraph(object):
    """Graph to keep track of social connections."""

    def __init__(self):
        """Create an empty graph.

        We keep a dictionary to map people's names -> nodes.
        """

        self.nodes = {}

    def add_person(self, name):
        """Add a person to our graph."""

        if name not in self.nodes:
            # Be careful not to just add them a second time -- otherwise,
            # if we accidentally added someone twice, we'd clear our their list
            # of friends!
            self.nodes[name] = PersonNode(name)

    def set_friends(self, name, friend_names):
        """Set two people as friends.

        This is reciprocal: so if Romeo is friends with Juliet, she's
        friends with Romeo (our graph is "undirected").

        """

        person = self.nodes[name]

        for friend_name in friend_names:
            friend = self.nodes[friend_name]

            # Since adjacent is a set, we don't care if we're adding duplicates --
            # it will only keep track of each relationship once. We do want to
            # make sure that we're adding both directions for the relationship.
            person.adjacent.add(friend)
            friend.adjacent.add(person)

    def are_connected(self, name1, name2):
        """Is this name1 friends with name2?"""

        def _are_connected(name1, name2, seen):
            """Recursive function to check if a node connects with a person name.
                Seen is a set that saves all nodes that have been visited"""

            # Use a depth-first search to see if the nodes are connected.
            # Recurse for each node adjacent to the node that is passed in
            # Add each visited node to the set

            
            if node.name == name2:
                return True

            # Keep track of the fact that we've visited here
            seen.add(node)

            # Recursively check all friends of node
            for n in node.adjacent:

                # If this node has already been checked, we can continue  
                if n in seen:
                    continue

                # If the node hasn't been checked, call the function on that node
                if _are_connected(n, name2, seen):
                    return True

            # Return false if no match is found
            return False

        # Call the recursive function, passing in the node of name1,
        # name2, and an empty set
        return _are_connected(self.nodes[name1], name2, set())

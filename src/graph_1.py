"""Implement a graph."""


class Graph(object):
    """Structure for values in a graph."""

    def __init__(self):
        """Create a graph with no values."""
        self.node_set = set()
        self.edge_set = set()

    def nodes(self):
        """Get all nodes in the graph to display in list form."""
        return list(self.node_set)

    def edges(self):
        """Get all edges in graph to display in list of tuples."""
        return list(self.edge_set)

    def add_node(self, val):
        """Add a node with a value to the graph."""
        self.node_set.add(val)

    def add_edge(self, val1, val2):
        """Add an edge with two values to the graph that does not exist."""
        self.edge_set.add((val1, val2))

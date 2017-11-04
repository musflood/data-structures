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
        self.add_node(val1)
        self.add_node(val2)
        self.edge_set.add((val1, val2))

    def del_node(self, val):
        """Remove the node with the given value from the graph.

        Also removes all edges connected to the node.
        """
        try:
            self.node_set.remove(val)
        except KeyError:
            raise ValueError('Value is not in the graph.')

        for edge in self.edge_set:
            if val in edge:
                self.edge_set.remove(edge)

    def del_edge(self, val1, val2):
        """Remove the edge connecting node of val1 to node of val2."""
        try:
            self.edge_set.remove((val1, val2))
        except KeyError:
            raise ValueError('Edge is not in the graph.')

    def has_node(self, val):
        """Check if the given value is in the graph."""
        return val in self.node_set

    def neighbors(self, val):
        """Get a list of all nodes connected to the node of the given value."""
        if val not in self.node_set:
            raise ValueError('Value is not in the graph.')

        neighbor_set = set()

        for edge in self.edge_set:
            start, end = edge
            if start == val:
                neighbor_set.add(end)
            elif end == val:
                neighbor_set.add(start)

        return neighbor_set

    def adjacent(self, val1, val2):
        """Check if there is an edge connecting the nodes with given values."""
        if val1 not in self.node_set or val2 not in self.node_set:
            raise ValueError('Value is not in the graph.')

        return (val1, val2) in self.edge_set

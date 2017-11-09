"""Implement a graph."""


class Graph(object):
    """Structure for values in a graph."""

    def __init__(self):
        """Create a graph with no values."""
        self.graph = {}

    def nodes(self):
        """Get all nodes in the graph to display in list form."""
        return list(self.graph)

    def edges(self):
        """Get all edges in graph to display in list of tuples with weights."""
        edge_list = []
        for start in self.graph:
            for end in self.graph[start]:
                edge_list.append((start, end, self.graph[start][end]))
        return edge_list

    def add_node(self, val):
        """Add a node with a value to the graph."""
        self.graph.setdefault(val, {})

    def add_edge(self, val1, val2, weight):
        """Add an edge from val1 to val2 with the given weight.

        If the node for either value does not exist, it is added to the graph.
        """
        if val1 == val2:
            raise ValueError('Edge needs two different values.')

        self.add_node(val1)
        self.add_node(val2)
        self.graph[val1][val2] = weight

    def del_node(self, val):
        """Remove the node with the given value from the graph.

        Also removes all edges connected to the node.
        """
        if val not in self.graph:
            raise ValueError('Value is not in the graph.')

        del self.graph[val]
        for node in self.graph:
            if val in self.graph[node]:
                del self.graph[node][val]

    def del_edge(self, val1, val2):
        """Remove the edge connecting node of val1 to node of val2."""
        try:
            del self.graph[val1][val2]
        except KeyError:
            raise ValueError('Edge is not in the graph.')

    def has_node(self, val):
        """Check if the given value is in the graph."""
        return val in self.graph

    def neighbors(self, val):
        """List all nodes the node of the given value connects to."""
        pass

    def adjacent(self, val1, val2):
        """Check if there is an edge connecting the nodes with given values."""
        pass

    def breadth_first_traversal(self, start_val):
        """Get the full visited path of a breadth first traversal."""
        pass

    def depth_first_traversal(self, start_val):
        """Get the full visited path of a depth first traversal."""
        pass

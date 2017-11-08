"""Tests for the weight_graph module."""

import pytest


def test_empty_constructor_constructs_empty_weight_graph():
    """Test that a new graph is empty."""
    from weight_graph import Graph
    g = Graph()
    assert len(g.graph) == 0


def test_nodes_of_empty_weight_graph_is_empty(empty_weight_graph):
    """Test that the list of nodes for an empty graph is empty."""
    assert empty_weight_graph.nodes() == []


def test_edges_of_empty_weight_graph_is_empty(empty_weight_graph):
    """Test that the list of edges for an empty graph is empty."""
    assert empty_weight_graph.edges() == []

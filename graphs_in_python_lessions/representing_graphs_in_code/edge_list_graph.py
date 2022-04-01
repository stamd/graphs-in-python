from base_classes.node import Node
from base_classes.graph import Graph

class EdgeListGraph(Graph):
    
    ###################################
    # Constructor
    ###################################
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = []

        # Define the type of a graph
        self.m_directed = directed

        # A representation of a graph
        # i.e. list of edges
        self.m_graph = []

        # For Bovurka's algorithm
        self.m_components = {}

    ###################################
    # Add edge to a graph
    ###################################
    def add_edge(self, node1_name, node2_name, weight=1):
        node1 = Node(node1_name)
        node2 = Node(node2_name)       
        if (node1 not in self.m_nodes):
            node1_id = len(self.m_nodes)
            node1.set_id(node1_id)
            self.m_nodes.append(node1)
        else:
            node1 = self.get_node_by_name(node1_name)
        
        if (node2 not in self.m_nodes):
            node2_id = len(self.m_nodes)
            node2.set_id(node2_id)
            self.m_nodes.append(node2)
        else:
            node2 = self.get_node_by_name(node2_name)

        # Add the edge from node1 to node2
        self.m_graph.append([node1, node2, weight])
        
        # If a graph is undirected, add the same edge,
        # but also in the opposite direction
        if not self.m_directed:
            self.m_graph.append([node1, node2, weight])

    ###################################
    # Load a graph from a list of edges
    # For example:
    # edge_list = [
    #   [0, 0, 25],
    #   [0, 1, 5],
    #   [0, 2, 3],
    #   [1, 3, 1],
    #   [1, 4, 15],
    #   [4, 2, 7],
    #   [4, 3, 11]
    # ]
    ###################################
    def load_from_edge_list(self, edge_list):
        num_of_edges = len(edge_list)
        for i in range(num_of_edges):
            node1 = edge_list[i][0]
            node2 = edge_list[i][1]
            weight = edge_list[i][2]
            self.add_edge(node1, node2, weight)
    
    ###################################
    # Print a graph representation
    ###################################
    def __str__(self):
        out = ""
        num_of_edges = len(self.m_graph)
        for i in range(num_of_edges):
            out += "edge " + str(i+1) + ": " + str(self.m_graph[i]) + "\n"
        return out
    
    ###################################
    # Find node in a graph using its name
    ###################################
    def get_node_by_name(self, name):
        search_node = Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node 
        return None
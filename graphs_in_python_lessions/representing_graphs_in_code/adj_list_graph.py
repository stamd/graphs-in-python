from base_classes.node import Node
from base_classes.graph import Graph

class AdjListGraph(Graph):
    
    ###################################
    # Constructor
    ###################################
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = []

        self.m_directed = directed

        self.m_graph = {}    

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
            self.m_graph[node1_name] = set()
        else:
            node1 = self.get_node_by_name(node1_name)
        
        if (node2 not in self.m_nodes):
            node2_id = len(self.m_nodes)
            node2.set_id(node2_id)
            self.m_nodes.append(node2)
            self.m_graph[node2_name] = set()
        else:
            node2= self.get_node_by_name(node2_name)

        self.m_graph[node1_name].add((node2, weight))

        if not self.m_directed:
            self.m_graph[node2_name].add((node1, weight))

    ###################################
    # Find node in a graph using its name
    ###################################
    def get_node_by_name(self, name):
        search_node = Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node 
        return None

    ###################################
    # Load a graph from a dictionary
    # definig an adjacency list
    # For exaple:
    # adjacency_list = {
    # 'A': [('B', 1), ('C', 3), ('D', 7)],
    # 'B': [('D', 5)],
    # 'C': [('D', 12)]
    # }
    ###################################
    def load_from_dict(self, dict):
        if len(dict) > self.m_num_of_nodes:
            raise ValueError("Number of nodes in the dictionary must be " + str(self.m_num_of_nodes))
        for node1 in dict.keys():
            for (node2, weight) in dict[node1]:
                self.add_edge(node1, node2, weight)
    
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
        for key in self.m_graph.keys():
            out += "node " + str(key) + ": " +  str(self.m_graph[key]) + "\n"
        return out

    ###################################
    # Get all nodes from a graph
    ####################################
    def get_nodes(self):
        return self.m_nodes
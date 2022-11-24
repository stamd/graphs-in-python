from base_classes.graph import Graph

class AdjMatrixGraph(Graph):

    ###################################
    # Constructor
    ###################################
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed

        # A representation of a graph
        # i.e. adjacency matrix
        self.m_graph = [[0 for column in range(num_of_nodes)]
                            for row in range(num_of_nodes)]

    ###################################
    # Assert node names
    ###################################
    def check_node_names(self, name1, name2):
        num_of_nodes = self.m_num_of_nodes
        node1_name = str(name1)
        node2_name = str(name2)
        if (not (node1_name.isdigit() and node2_name.isdigit())):
            raise TypeError("Node names must be integer values")
        if (name1<0 or name1>=num_of_nodes or name2<0 or name2>=num_of_nodes):
            raise ValueError("Node names must be from 0 to " + str(num_of_nodes-1))

    ###################################
    # Add edge to a graph
    ###################################
    def add_edge(self, node1, node2, weight=1):
        self.check_node_names(node1, node2)
        self.m_graph[node1][node2] = weight

        if not self.m_directed:
            self.m_graph[node2][node1] = weight

    ###################################
    # Print a graph representation
    ###################################
    def __str__(self):
        out = ""
        for i in range(self.m_num_of_nodes):
           out += str(self.m_graph[i]) + "\n"
        return out
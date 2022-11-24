class Graph:
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed

        # Initialize the adjacency matrix
        # Create a matrix with `num_of_nodes` rows and columns
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)]
                            for row in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight=1):
        self.m_adj_matrix[node1][node2] = weight

        if not self.m_directed:
            self.m_adj_matrix[node2][node1] = weight

    def print_adj_matrix(self):
        for i in range(self.m_num_of_nodes):
            print(self.m_adj_matrix[i])

def main():
    graph = Graph(5)

    graph.add_edge(0, 0, 25)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 3, 1)
    graph.add_edge(1, 4, 15)
    graph.add_edge(4, 2, 7)
    graph.add_edge(4, 3, 11)

    graph.print_adj_matrix()

if __name__=="__main__":
    main()
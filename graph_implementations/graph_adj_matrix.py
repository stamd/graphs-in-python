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

    ###################################
    # Prims's MST Algorithm
    ###################################
    def prims_mst(self):
        # Defining a really big number:
        postitive_inf = float('inf')

        # This is a list showing which nodes are already selected
        # so we don't pick the same node twice and we can actually know when stop looking
        selected_nodes = [False for vertex in range(self.m_num_of_nodes)]

        # Matrix of the resulting MST
        result = [[0 for column in range(self.m_num_of_nodes)]
                    for row in range(self.m_num_of_nodes)]

        indx = 0
        for i in range(self.m_num_of_nodes):
            print(self.m_graph[i])

        print(selected_nodes)

        # While there are nodes that are not included in the MST, keep looking:
        while(False in selected_nodes):
            # We use the big number we created before as the possible minimum weight
            minimum = postitive_inf

            # The starting node
            start = 0

            # The ending node
            end = 0

            for i in range(self.m_num_of_nodes):
                # If the node is part of the MST, look its relationships
                if selected_nodes[i]:
                    for j in range(self.m_num_of_nodes):
                        # If the analyzed node have a path to the ending node AND its not included in the MST (to avoid cycles)
                        if (not selected_nodes[j] and self.m_graph[i][j]>0):
                            # If the weight path analized is less than the minimum of the MST
                            if self.m_graph[i][j] < minimum:
                                # Defines the new minimum weight, the starting vertex and the ending vertex
                                minimum = self.m_graph[i][j]
                                start, end = i, j

            # Since we added the ending vertex to the MST, it's already selected:
            selected_nodes[end] = True


            # Filling the MST Adjacency Matrix fields:
            result[start][end] = minimum

            if minimum == postitive_inf:
                result[start][end] = 0

            print("(%d.) %d - %d: %d" % (indx, start, end, result[start][end]))
            indx += 1

            result[end][start] = result[start][end]

        # Print the resulting MST
        # for node1, node2, weight in result:
        for i in range(len(result)):
            for j in range(0+i, len(result)):
                if result[i][j] != 0:
                    print("%d - %d: %d" % (i, j, result[i][j]))


graph = Graph(5)

graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

print(graph)
graph.prims_mst()



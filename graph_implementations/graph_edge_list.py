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
            self.m_graph.append([node2, node1, weight])

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

    ###################################
    # Kruskal's MST Algorithm
    ###################################
    # Finds the root node of a subtree containing node `node`
    def find_subtree(self, parent, node):
        if parent[node.get_id()] == node:
            return node
        return self.find_subtree(parent, parent[node.get_id()])

    # Connects subtrees containing nodes `node1` and `node2`
    def connect_subtrees(self, parent, subtree_sizes, node1, node2):
        node1_root = self.find_subtree(parent, node1)
        node1_root_id = node1_root.get_id()
        node2_root = self.find_subtree(parent, node2)
        node2_root_id = node2_root.get_id()

        if subtree_sizes[node1_root_id] < subtree_sizes[node2_root_id]:
            parent[node1_root_id] = node2_root
        elif subtree_sizes[node1_root_id] > subtree_sizes[node2_root_id]:
            parent[node2_root_id] = node1_root
        else:
            parent[node2_root_id] = node1_root
            subtree_sizes[node1_root_id] += 1

    #  Applying Kruskal algorithm
    def kruskals_mst(self):
        result = []
        i, e = 0, 0

        parent = [-1 for i in range(self.m_num_of_nodes)]
        subtree_sizes = [0 for i in range(self.m_num_of_nodes)]

        # `node` is the number form 0 to num_of_nodes -> {0, 1, ..., num_of_nodes-1}
        # Add that number to the `parent` array
        # Add zero to the `subtree_sizes` array
        # => initialize `parent` and `subtree_sizes`
        for node in self.m_nodes:
            parent[node.get_id()] = node

        # Sort edges by weight
        sorted_graph = sorted(self.m_graph, key=lambda item: item[2])

        # Important property of any MST
        # the number of edges is equal to the number of nodes minus 1
        while e < (self.m_num_of_nodes - 1):
            # Pick an edge with the minimum weight at the moment
            node1, node2, weight = sorted_graph[i]
            i = i + 1
            x = self.find_subtree(parent, node1)
            y = self.find_subtree(parent, node2)
            if x != y:
                e = e + 1
                result.append([node1, node2, weight])
                self.connect_subtrees(parent, subtree_sizes, x, y)

        print("Kruskal's MST:")
        for node1, node2, weight in result:
            print("%s - %s: %d" % (node1, node2, weight))

    ###################################
    # Borůvka's MST Algorithm
    ###################################
    def find_component(self, node):
        if self.m_components[node] == node:
            return node
        return self.find_component(self.m_components[node])

    def set_component(self, node):
        if self.m_components[node] == node:
            return
        else:
            for k in self.m_components.keys():
                self.m_components[k] = self.find_component(k)

    def union(self, component_size, node1, node2):
        if component_size[node1] <= component_size[node2]:
            self.m_components[node1] = node2
            component_size[node2] += component_size[node1]

        elif component_size[node1] >= component_size[node2]:
            self.m_components[node2] = self.find_component(node1)
            component_size[node1] += component_size[node2]

        print(self.m_components)

    def boruvkas_mst(self):
        component_size = []
        cheapest_edge = []

        mst_weight = 0

        cheapest_edge = [-1] * self.m_num_of_nodes

        for node in self.m_nodes:
            self.m_components.update({node.get_name() : vertex})
            component_size.append(1)

        num_of_components = self.m_num_of_nodes
        while num_of_components > 1:
            for i in range(len(self.m_graph)):

                node1 = self.m_graph[i][0]
                node2 = self.m_graph[i][1]
                weight = self.m_graph[i][2]

                self.set_component(node1)
                self.set_component(node2)

                node1_component = self.m_components[node1]
                node2_component = self.m_components[node2]

                if node1_component != node2_component:
                    if cheapest_edge[node1_component] == -1 or cheapest_edge[node1_component][2] > weight:
                        cheapest_edge[node1_component] = [node1, node2, weight]
                    if cheapest_edge[node2_component] == -1 or cheapest_edge[node2_component][2] > weight:
                        cheapest_edge[node2_component] = [node1, node2, weight]

            for vertex in range(self.m_num_of_nodes):
                if cheapest_edge[vertex] != -1:
                    node1 = cheapest_edge[vertex][0]
                    node2 = cheapest_edge[vertex][1]
                    weight = cheapest_edge[vertex][2]

                    self.set_component(node1)
                    self.set_component(node2)

                    node1_component = self.m_components[node1]
                    node2_component = self.m_components[node2]

                    if node1_component != node2_component:
                        mst_weight += weight
                        self.union(component_size, node1_component, node2_component)
                        print("Edge " + str(node1) + " - " + str(node2) + " with weight " + str(weight) + " is included in MST.")

                        num_of_components -= 1

            cheapest_edge = [-1] * self.m_num_of_nodes

        print("The weight of MST is " + str(mst_weight))


# graph = Graph(5)

# graph.add_edge('A', 'A', 25)
# graph.add_edge('A', 'B', 5)
# graph.add_edge('A', 'C', 3)
# graph.add_edge('B', 'D', 1)
# graph.add_edge('B', 'E', 15)
# graph.add_edge('E', 'C', 7)
# graph.add_edge('E', 'D', 11)

# graph.add_edge(0, 0, 25)
# graph.add_edge(0, 1, 5)
# graph.add_edge(0, 2, 3)
# graph.add_edge(1, 3, 1)
# graph.add_edge(1, 4, 15)
# graph.add_edge(4, 2, 7)
# graph.add_edge(4, 3, 11)

###################################
# Kruskal qith letter nodes
#
# graph = EdgeListGraph(9)
#
# graph.add_edge("A", "B", 4)
# graph.add_edge("A", "C", 7)
# graph.add_edge("B", "C", 11)
# graph.add_edge("B", "D", 9)
# graph.add_edge("B", "F", 20)
# graph.add_edge("C", "F", 1)
# graph.add_edge("D", "G", 6)
# graph.add_edge("D", "E", 2)
# graph.add_edge("E", "G", 10)
# graph.add_edge("E", "I", 15)
# graph.add_edge("E", "H", 5)
# graph.add_edge("E", "F", 1)
# graph.add_edge("F", "H", 3)
# graph.add_edge("G", "I", 5)
# graph.add_edge("H", "I", 12)
#
# graph.kruskals_mst()
###################################

###################################
# Kruskal qith letter nodes
#
# graph = EdgeListGraph(9)

# graph.add_edge(0, 1, 4)
# graph.add_edge(0, 2, 7)
# graph.add_edge(1, 2, 11)
# graph.add_edge(1, 3, 9)
# graph.add_edge(1, 5, 20)
# graph.add_edge(2, 5, 1)
# graph.add_edge(3, 6, 6)
# graph.add_edge(3, 4, 2)
# graph.add_edge(4, 6, 10)
# graph.add_edge(4, 8, 15)
# graph.add_edge(4, 7, 5)
# graph.add_edge(4, 5, 1)
# graph.add_edge(5, 7, 3)
# graph.add_edge(6, 8, 5)
# graph.add_edge(7, 8, 12)
#
# graph.kruskals_mst()
###################################

g = EdgeListGraph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 6, 7)
g.add_edge(1, 6, 11)
g.add_edge(1, 7, 20)
g.add_edge(1, 2, 9)
g.add_edge(2, 3, 6)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 10)
g.add_edge(3, 5, 5)
g.add_edge(4, 5, 15)
g.add_edge(4, 7, 1)
g.add_edge(4, 8, 5)
g.add_edge(5, 8, 12)

g.boruvkas_mst()

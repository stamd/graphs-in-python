class Graph:
    ###################################
    # Constructor
    ###################################
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes

        # Define the type of a graph
        self.m_directed = directed

        # Different representations of a graph
        # i.e. list of edges
        self.m_graph = []

        # For Bovurkas
        self.m_components = {}

    ###################################
    # Add edge to a graph
    ###################################
    def add_edge(self, node1, node2, weight=1):        
        # Add the edge from node1 to node2
        self.m_graph.append([node1, node2, weight])
        
        # If a graph is undirected, add the same edge,
        # but also in the opposite direction
        if not self.m_directed:
            self.m_graph.append([node1, node2, weight])
    
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
    # Kruskal's MST Algorithm
    #### za sada radi samo sa numbered nodes
    ###################################
    # Finds the root node of a subtree containing node `i`
    def find_subtree(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_subtree(parent, parent[i])

    # Connects subtrees containing nodes `x` and `y`
    def connect_subtrees(self, parent, subtree_sizes, x, y):
        x_root = self.find_subtree(parent, x)
        y_root = self.find_subtree(parent, y)
        if subtree_sizes[x_root] < subtree_sizes[y_root]:
            parent[x_root] = y_root
        elif subtree_sizes[x_root] > subtree_sizes[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            subtree_sizes[x_root] += 1

    #  Applying Kruskal algorithm
    def kruskals_mst(self):
        result = []
        i, e = 0, 0

        # Sort edges by weight
        sorted_graph = sorted(self.m_graph, key=lambda item: item[2])
        parent = []
        subtree_sizes = []

        # `node` je broj od 0 do numOfNodes -> {0, 1, ..., numOfNodes-1}
        # dodajemo tu vrednost na `parent` niz
        # dodajemo nulu na `subtree_sizes`
        # => inicijalizujemo `parent` i `subtree_sizes`
        for node in range(self.m_num_of_nodes):
            parent.append(node)
            subtree_sizes.append(0)
        # parent = [0, 1, 2, ... , numOfNodes-1]


        # broj grana je jednak broju cvorova -1
        # vazno svojstvo msta
        while e < (self.m_num_of_nodes - 1):
            # Uzimamo granu sa trenutno najmanjom tezinom
            node1, node2, weight = sorted_graph[i]
            i = i + 1

            x = self.find_subtree(parent, node1)
            y = self.find_subtree(parent, node2)
            if x != y:
                e = e + 1
                result.append([node, node2, weight])
                self.connect_subtrees(parent, subtree_sizes, x, y)

        print("Kruskal's MST:")
        for node1, node2, weight in result:
            print("%d - %d: %d" % (node1, node2, weight)) 
    
    ################################### 
    # Borůvka's MST Algorithm
    ###################################
    def find_component(self, u):
        if self.m_components[u] == u:
            return u
        return self.find_component(self.m_components[u])

    def set_component(self, u):
        if self.m_components[u] == u:
            return
        else:
            for k in self.m_components.keys():
                self.m_components[k] = self.find_component(k)



    def union(self, component_size, u, v):
        if component_size[u] <= component_size[v]:
            self.m_components[u] = v
            component_size[v] += component_size[u]

        elif component_size[u] >= component_size[v]:
            self.m_components[v] = self.find_component(u)
            component_size[u] += component_size[v]

        print(self.m_components)

    def boruvkas_mst(self):
        component_size = []
        cheapest_edge = []

        mst_weight = 0

        cheapest_edge = [-1] * self.m_num_of_nodes

        for vertex in range(self.m_num_of_nodes):
            self.m_components.update({vertex : vertex})
            component_size.append(1)

        num_of_components = self.m_num_of_nodes
        while num_of_components > 1:
            for i in range(len(self.m_graph)):

                u = self.m_graph[i][0]
                v = self.m_graph[i][1]
                w = self.m_graph[i][2]

                self.set_component(u)
                self.set_component(v)

                u_component = self.m_components[u]
                v_component = self.m_components[v]

                if u_component != v_component:
                    if cheapest_edge[u_component] == -1 or cheapest_edge[u_component][2] > w:
                        cheapest_edge[u_component] = [u, v, w]
                    if cheapest_edge[v_component] == -1 or cheapest_edge[v_component][2] > w:
                        cheapest_edge[v_component] = [u, v, w]

            for vertex in range(self.m_num_of_nodes):
                if cheapest_edge[vertex] != -1:
                    u = cheapest_edge[vertex][0]
                    v = cheapest_edge[vertex][1]
                    w = cheapest_edge[vertex][2]

                    self.set_component(u)
                    self.set_component(v)

                    u_component = self.m_components[u]
                    v_component = self.m_components[v]

                    if u_component != v_component:
                        mst_weight += w
                        self.union(component_size, u_component, v_component)
                        print("Edge " + str(u) + " - " + str(v) + " with weight " + str(w) + " is included in MST.")

                        num_of_components -= 1

            cheapest_edge = [-1] * self.m_num_of_nodes

        print("The weight of MST is " + str(mst_weight))


    
    



graph = Graph(5)

# graph.add_edge('1', 'A', 25)
# graph.add_edge('A', 'B', 5)
# graph.add_edge('A', 'C', 3)
# graph.add_edge('B', 'D', 1)
# graph.add_edge('B', 'E', 15)
# graph.add_edge('E', 'C', 7)
# graph.add_edge('E', 'D', 11)
graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

print(graph)

graph.boruvkas_mst()



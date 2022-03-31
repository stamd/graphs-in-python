from node import Node
from graph import Graph
from queue import Queue

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
            self.m_nodes.add(node1)
            self.m_graph[node1_name] = set()
        else:
            node1 = self.get_node_by_name(node1_name)
        
        if (node2 not in self.m_nodes):
            node2_id = len(self.m_nodes)
            node2.set_id(node2_id)
            self.m_nodes.add(node2)
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

    def get_nodes(self):
        return self.m_nodes
    
    ###################################
    # DFS Search
    ###################################
    def dfs(self, start, target, path = [], visited = set()):
        path.append(start)
        visited.add(start)
        if start == target:
            return path
        for (neighbour, weight) in self.m_graph[start]:
            if neighbour not in visited:
                result = self.dfs(neighbour, target, path, visited)
                if result is not None:
                    return result
        path.pop()
        return None  

    ###################################
    # BFS Search
    ###################################
    def bfs(self, start_node, target_node):
        # Set of visited nodes to prevent loops
        visited = set()
        queue = Queue()

        # Add the start_node to the queue and visited list
        queue.put(start_node)
        visited.add(start_node)
        
        # start_node has not parents
        parent = dict()
        parent[start_node] = None

        # Perform step 3
        path_found = False
        while not queue.empty():
            current_node = queue.get()
            if current_node == target_node:
                path_found = True
                break

            for (next_node, weight) in self.m_graph[current_node]:
                if next_node not in visited:
                    queue.put(next_node)
                    parent[next_node] = current_node
                    visited.add(next_node)
                    
        # Path reconstruction
        path = []
        if path_found:
            path.append(target_node)
            while parent[target_node] is not None:
                path.append(parent[target_node]) 
                target_node = parent[target_node]
            path.reverse()
        return path    
    
    ###################################
    # BFS Traversal
    ###################################
    def bfs_traversal(self, start_node):
        visited = set()
        queue = Queue()
        queue.put(start_node)
        visited.add(start_node)

        while not queue.empty():
            current_node = queue.get()
            if current_node:
                print(current_node, end = " ")
            for (next_node, weight) in self.m_graph[current_node]:
                if next_node not in visited:
                    queue.put(next_node)
                    visited.add(next_node)  

g = AdjListGraph(5)
adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}
edge_list = [
  [0, 0, 25],
  [0, 1, 5],
  [0, 2, 3],
  [1, 3, 1],
  [1, 4, 15],
  [4, 2, 7],
  [4, 3, 11]
]
# g.load_from_dict(adjacency_list)
g.load_from_edge_list(edge_list)
for node in g.get_nodes():
    print(node)
print(g)


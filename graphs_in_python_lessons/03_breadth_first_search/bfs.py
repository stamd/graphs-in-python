from queue import Queue

class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)

        # Directed or Undirected
        self.m_directed = directed

        # Graph representation - Adjacency list
        # We use a dictionary to implement an adjacency list
        self.m_adj_list = {node: set() for node in self.m_nodes}

    # Add edge to the graph
    def add_edge(self, node1, node2, weight=1):
        self.m_adj_list[node1].add((node2, weight))

        if not self.m_directed:
            self.m_adj_list[node2].add((node1, weight))

    # Print the graph representation
    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("node", key, ": ", self.m_adj_list[key])

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

            for (next_node, weight) in self.m_adj_list[current_node]:
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

    def bfs_traversal(self, start_node):
        visited = set()
        queue = Queue()
        queue.put(start_node)
        visited.add(start_node)

        while not queue.empty():
            current_node = queue.get()
            print(current_node, end = " ")
            for (next_node, weight) in self.m_adj_list[current_node]:
                if next_node not in visited:
                    queue.put(next_node)
                    visited.add(next_node)

def main():
    # Testing the `bfs()` method
    graph1 = Graph(6, directed=False)

    graph1.add_edge(0, 1)
    graph1.add_edge(0, 2)
    graph1.add_edge(0, 3)
    graph1.add_edge(0, 4)
    graph1.add_edge(1, 2)
    graph1.add_edge(2, 3)
    graph1.add_edge(2, 5)
    graph1.add_edge(3, 4)
    graph1.add_edge(3, 5)
    graph1.add_edge(4, 5)

    graph1.print_adj_list()

    path = []
    path = graph1.bfs(0, 5)
    print(path)

    # Testing the `bfs_traversal()` method
    graph2 = Graph(5, directed=False)

    graph2.add_edge(0, 1)
    graph2.add_edge(0, 2)
    graph2.add_edge(1, 2)
    graph2.add_edge(1, 4)
    graph2.add_edge(2, 3)

    graph2.bfs_traversal(0)

if __name__=="__main__":
    main()
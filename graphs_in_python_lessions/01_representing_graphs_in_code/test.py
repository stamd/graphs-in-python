from edge_list_graph import EdgeListGraph
from adj_matrix_graph import AdjMatrixGraph
from adj_list_graph import AdjListGraph

def test_edge_list_graph():
    print("***** Testing Edge List Graph *****")

    edge_list = [
      [0, 0, 25],
      [0, 1, 5],
      [0, 2, 3],
      [1, 3, 1],
      [1, 4, 15],
      [4, 2, 7],
      [4, 3, 11]
    ]
    graph = EdgeListGraph(5)
    graph.load_from_edge_list(edge_list)
    
    print("> Graph loaded from list of edges:")
    print(graph)

    graph2 = EdgeListGraph(5)
    graph2.add_edge(0, 0, 25)
    graph2.add_edge(0, 1, 5)
    graph2.add_edge(0, 2, 3)
    graph2.add_edge(1, 3, 1)
    graph2.add_edge(1, 4, 15)
    graph2.add_edge(4, 2, 7)
    graph2.add_edge(4, 3, 11)
    
    print("> The same graph created with `add_edge` method:")
    print(graph)

    print("********************")

def test_adj_matrix_graph():
    print("***** Testing Adjacency Matrix Graph *****")

    graph = AdjMatrixGraph(5)

    graph.add_edge(0, 0, 25)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 3, 1)
    graph.add_edge(1, 4, 15)
    graph.add_edge(4, 2, 7)
    graph.add_edge(4, 3, 11)

    print("> Adjacency matrix graph:")
    print(graph)

    print("********************")

def test_adj_list_graph():
    print("***** Testing Adjacency Matrix Graph *****")
    graph = AdjListGraph(5)

    graph.add_edge(0, 0, 25)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 3, 1)
    graph.add_edge(1, 4, 15)
    graph.add_edge(4, 2, 7)
    graph.add_edge(4, 3, 11)

    print("> Adjacency list graph created with `add_edge` method:")
    print(graph)

    print("> A graph created with `load_from_dict` method and with letter labeled nodes:")
    graph2 = AdjListGraph(4)
    adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
    }
    graph2.load_from_dict(adjacency_list)
    print(graph2)

    print("> The same graph created with `load_from_edge_list` method:")
    graph3 = AdjListGraph(5)
    edge_list = [
      [0, 0, 25],
      [0, 1, 5],
      [0, 2, 3],
      [1, 3, 1],
      [1, 4, 15],
      [4, 2, 7],
      [4, 3, 11]
    ]
    graph3.load_from_edge_list(edge_list)
    print(graph3)

    print("********************")

def main():
    test_edge_list_graph()
    test_adj_matrix_graph()
    test_adj_list_graph()

if __name__ == "__main__":
    main()

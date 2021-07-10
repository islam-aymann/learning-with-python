import itertools


def dijkstra(nodes: list, edges: dict, source_index: int = 0):
    """

    :param nodes: the set of nodes
    :param edges: the set of edges. e.g. {(node, node): distance}
    :param source_index: the index of the source node
    :return: the shortest distances from the source node
    """
    path_lengths = {v: float('inf') for v in nodes}
    path_lengths[nodes[source_index]] = 0

    adjacent_nodes = {v: {} for v in nodes}
    for (u, v), w_uv in edges.items():
        adjacent_nodes[u][v] = w_uv
        adjacent_nodes[v][u] = w_uv

    temporary_nodes = [v for v in nodes]
    while len(temporary_nodes) > 0:
        upper_bounds = {v: path_lengths[v] for v in temporary_nodes}
        u = min(upper_bounds, key=upper_bounds.get)
        print(u)
        temporary_nodes.remove(u)
        for v, w_uv in adjacent_nodes[u].items():
            print(v)
            path_lengths[v] = min(path_lengths[v], path_lengths[u] + w_uv)

    return path_lengths


def shortest_path(nodes, edges, frm, to):
    return dijkstra(nodes, edges, frm)[to]


def shortest_path2(arr):
    arr = arr.split(', ')
    nodes_count = int(arr[0])
    nodes = arr[1: nodes_count + 1]

    edges_list = arr[nodes_count + 1:]

    edges = dict()

    for edge_list in edges_list:
        s = edge_list.split('-')[0]
        d = edge_list.split('-')[1]
        edges[(s, d)] = 1.0

    return dijkstra(nodes, edges)[nodes[-1]]


def shortest_path3(arr):
    nodes_count = int(arr[0])
    nodes = arr[1: nodes_count + 1]

    edges_list = arr[nodes_count + 1:]

    edges = dict()

    for edge_list in edges_list:
        s = edge_list.split('-')[0]
        d = edge_list.split('-')[1]
        edges[(s, d)] = 1.0

    return dijkstra(nodes, edges)[nodes[-1]]


if __name__ == '__main__':
    # nodes = [0, 1, 2, 3, 4, 5]
    # edges = {
    #     (0, 1): 1.0,
    #     (0, 2): 1.5,
    #     (0, 3): 2.0,
    #     (1, 3): 0.5,
    #     (1, 4): 2.5,
    #     (2, 3): 1.5,
    #     (3, 5): 1.0,
    # }
    #
    # # print(shortest_path(nodes, edges, 0, 5))
    # #
    # # inp = "4, A, B, C, D, A-B, B-D, B-C, C-D"
    # # print(shortest_path2(inp))
    #
    # inp = ["4", "A", "B", "C", "D", "A-B", "B-D", "B-C", "C-D"]
    # print(shortest_path3(inp))

    l = 'A B C D'.split(' ')
    x = itertools.permutations(l, 3)
    m = [d for d in x if d[0] == l[0] and d[-1] == l[-1]]
    print(m)

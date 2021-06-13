grafo = {
    0: [(0, "a"), (0, "b"), (1, "a")],
    1: [(2, "b")],
    2: [(3, "b")],
    3: []
}

grafo2 = {
    0: [(1, "a"), (2, "a")],
    1: [(3, "b")],
    2: [(5, "b")],
    3: [(4, "a")],
    4: [(1, "b")],
    5: [(2, "a")]
}


def bfs(start):

    queue = [(start, "")]
    visited = []

    while len(queue) > 0:

        estado = queue.pop(0)
        neighbours = grafo.get(estado[0])
        print("estado ", estado, "vecinos: ", neighbours)

        for edge in neighbours:

            if edge not in visited:
                visited.append(edge)
                queue.append(edge)
                print(edge)


bfs(0)



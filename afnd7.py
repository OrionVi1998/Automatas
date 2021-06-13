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

estados_finales = [0]


def bfs(start, palabra):

    queue = [(start, "")]
    visited = []

    while len(queue) > 0:

        print("cola:", queue)
        estado_actual = queue.pop(0)
        if not palabra and estado_actual not in estados_finales:
            return "rechazada"
        char = palabra[0]

        neighbours = grafo.get(estado_actual[0])
        print("estado ", estado_actual, "vecinos: ", neighbours)

        for edge in neighbours:

            if edge not in visited and char == edge[1] and edge not in visited:
                print("char actual:", char)
                visited.append(edge)
                queue.append(edge)
                print("visitados:", visited, "edge:", edge)

        palabra = palabra[1:]
        print("palabra:", palabra)


    print(f"\nV :{visited}")

            # if edge not in visited:


print(bfs(0, "abb"))
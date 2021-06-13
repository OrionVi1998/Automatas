grafo = {
    0: [(0, "a"), (0, "b"), (1, "a")],
    1: [(2, "b")],
    2: [(3, "b")],
    3: []
}

grafo = {
    0: [(1, "a"), (2, "a")],
    1: [(3, "b")],
    2: [(5, "b")],
    3: [(4, "a")],
    4: [(1, "b")],
    5: [(2, "a")]
}

# (0, "a"), (0, "b"),
ss = 0
accepting_states = {3}

accept = ""
suc = []

def nfa(string, starting_state):
    visited = []
    queue = [(starting_state, "")]
    neighbors = 1
    test_string = string
    cur = None

    while len(queue) > 0 and neighbors and test_string:

        cur = queue.pop(0)
        neighbors = grafo.get(cur[0])
        char = test_string[0]
        test_string = test_string[1:]

        print(cur, "-", neighbors, "-", char, "-", test_string, suc)

        for edge in neighbors:

            if char == edge[1] and edge[0] != cur[0]:
                visited.append(edge)
                queue.append(edge)
                suc.append(char)

            # if edge not in visited:
            #         visited.append(edge)
            #         queue.append(edge)

        test_string = test_string[1:]

        # print(cur, ":", queue, "-", visited)



nfa("aba", 0)

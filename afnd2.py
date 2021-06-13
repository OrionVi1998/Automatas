grafo = {
    "-e0": [("a", "-e0"), ("b", "-e0"), ("a", "e1")],
    "e1": [("b", "e2")],
    "e2": [("b", "*e3")],
    "*e3": []
}

palabra = "aabb"
aceptada = False
nodoActual = "-e0"

visitado = []
queue = []

queue.append(nodoActual)
visitado.append(nodoActual)

lacceptado = []

while queue:
    m = queue.pop(0)
    # simbolo = palabra[0]

    print(m)

    loops = []
    avanzar = []

    for trans in grafo[m]:
        if trans[1] not in visitado:
            visitado.append(trans[1])
            queue.append(trans[1])
            if loops:
                avanzar.append(trans[0])
            else:
                avanzar.append(trans[0])

            # palabra = palabra[1:]

        elif trans[1] == m and [t[1] for t in grafo[m]].count(m) > 1:
            loops.append(f"{trans[0]}*")

        elif trans[1] == m and [t[1] for t in grafo[m]].count(m) == 1:
            lacceptado.append(f"{trans[0]}*")

    if len(loops) != 0:
        lacceptado.append("|".join(loops))

    [lacceptado.append(t) for t in avanzar]

print(lacceptado)

transitions = [
    {"a": {1}},
    {"b": {0, 2}},
    {"c": {0}}
]

starting_state = 0
accepting_states = {0}


def nfa(w):
    cur_states = {starting_state}
    for c in w:
        if not cur_states: return "reject"
        cur_states = set.union(*
                               (transitions[s].get(c, set()) for s in cur_states))
    return "accept" if cur_states & accepting_states else "reject"

grafo = {
    "-e0": [("a", "-e0"), ("a", "-e0"), ("b", "e1")],
    "e1": [("b", "e2")],
    "e2": [("b", "*e3")],
    "*e3": []
}

palabra = "aabb"
aceptada = False
nodoActual = "-e0"


bifurcaciones = []

# (mientras la palabra no sea vacia) y (podemos seguir avanzando por las transiciones del nodoActual por el simbolo)
while len(palabra) > 0 and any([t[0] == palabra[0] for t in grafo[nodoActual]]):

    simbolo = palabra[0]

    if [t[0] for t in grafo[nodoActual]].count(simbolo) > 1:
        bifurcaciones.append([t for t in grafo[nodoActual] if t[0] == simbolo])

    for trans in grafo[nodoActual]:
        if simbolo == trans[0]:
            nodoActual = trans[1]
            palabra = palabra[1:]
            print(palabra, nodoActual, trans, "bifurcaciones:", bifurcaciones)


if nodoActual[0] == "*":
    aceptada = True
    print(aceptada, ", palabra aceptada.")
else:
    print(aceptada, ", palabra no aceptada.")


####


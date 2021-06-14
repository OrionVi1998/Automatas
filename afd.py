def afd(grafo, nodo_inicial, estados_finales, palabra):

    estado_actual = nodo_inicial
    aceptada = False

    # Mientras la palabra no sea vacia y podemos seguir avanzando por las transiciones del nodoActual por el simbolo
    while len(palabra) > 0 and any([t[1] == palabra[0] for t in grafo[estado_actual]]):

        simbolo = palabra[0]

        for trans in grafo[estado_actual]:
            if simbolo == trans[1]:
                estado_actual = trans[0]
                palabra = palabra[1:]
                print(palabra, estado_actual, trans)

    if estado_actual in estados_finales:
        aceptada = True
        print(aceptada, ", palabra aceptada.")
    else:
        print(aceptada, ", palabra no aceptada.")


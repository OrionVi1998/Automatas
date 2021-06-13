
import sys


def LINE():
    return sys._getframe(1).f_lineno


# grafo = {
#     0: [(0, "a"), (0, "b"), (1, "a")],
#     1: [(2, "b")],
#     2: [(3, "b")],
#     3: []
# }

grafo = {
    0: [(1, "a"), (2, "a")],
    1: [(3, "b")],
    2: [(5, "b")],
    3: [(4, "a")],
    4: [(1, "b")],
    5: [(2, "a")]
}



estado_inicial = 0
estados_finales = [1, 2]
ramificaciones = []

print("<-- INICIO ALGORTIMO -->\n")
def afnd(estado_inicial, palabra):

    cola = [estado_inicial]
    visitados = []
    bifurcaciones = []

    while len(cola) > 0:
        # print("cola:", cola)
        # print("visitados:", visitados)
        estado_actual = cola.pop(0)
        # print("estado actual:", estado_actual)

        if palabra:
            char = palabra[0]
        elif not palabra:
            break

        print("estado actual:", estado_actual, "y char:", char)
        # print("caracter:", char)

        vecinos = [tupla[0] for tupla in grafo.get(estado_actual) if tupla[1] == char]
        # si no hay vecinos
        if not vecinos:
            return

        if len(vecinos) > 1:
            # metodo rapido para insertar todos los vecinos en bifurcaciones
            for e in vecinos:
                bifurcaciones.append(e)

            print("bifurcaciones por", char, "-->", bifurcaciones)
            for estado in bifurcaciones:
                print("INICIO RAMIFICACION POR ESTADO:", estado)
                ramificacion = afnd(estado, palabra[1:])
                ramificaciones.append(ramificacion)
                print("ramificacion:", ramificacion)
                print("FIN RAMIFICACION")


        else:
            # print("vecinos:", vecinos)

            for estado in vecinos:
                # print("linea:", LINE(), "cola:", cola, "visitados:", visitados)
                if estado not in visitados and palabra:
                    visitados.append(estado)
                    cola.append(estado)
                if estado in visitados and palabra:
                    return afnd(estado, palabra[1:])

            palabra = palabra[1:]

    if (not palabra and estado_actual not in estados_finales) or palabra:
        return False

    elif not palabra and estado_actual in estados_finales:
        return True


afnd(estado_inicial, "aba")
print("<-- FIN ALGORITMO -->\n")
if any(ramificaciones):
    print("Resultado: cadena aceptada")
else:
    print("Resultado: cadena rechazada")




import sys

def LINE():
    return sys._getframe(1).f_lineno

def afnd(grafo, estado_inicial, estados_finales, palabra, visitados, bifurcaciones, ramificaciones):

    cola = [estado_inicial]

    while len(cola) > 0:
        estado_actual = cola.pop(0)

        if palabra:
            char = palabra[0]
        elif not palabra:
            break

        vecinos = [tupla[0] for tupla in grafo.get(estado_actual) if tupla[1] == char]
        # Si no hay vecinos
        if not vecinos:
            return

        if len(vecinos) > 1:
            # Metodo rapido para insertar todos los vecinos en bifurcaciones
            for e in vecinos:
                if e not in bifurcaciones:
                    bifurcaciones.append(e)

            for estado in bifurcaciones:
                print("INICIO RAMIFICACION POR ESTADO:", estado)
                ramificacion = afnd(grafo, estado, estados_finales, palabra[1:], visitados, bifurcaciones, ramificaciones)
                ramificaciones.append(ramificacion)
                print("FIN RAMIFICACION")

        else:
            for estado in vecinos:
                if estado not in visitados and palabra:
                    visitados.append(estado)
                    cola.append(estado)
                if estado in visitados and palabra:
                    return afnd(grafo, estado, estados_finales, palabra[1:], visitados, bifurcaciones, ramificaciones)

            palabra = palabra[1:]

    if not palabra and estado_actual in estados_finales:
        return True

    else:
        return False

    else:
        return False



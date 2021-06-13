"""
Consigna: Hacer un programa que acepte los datos de un autómata de
terminista y no determinista y, lo haga funcionar como un autómata.
"""

# PREGUNTAR AL USUARIO
import sys

class bcolors:
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


grafo = {}
estados_iniciales = None
estados_finales = []

# PREGUNTAR AL USUARIO
print("¿Su automata es de que tipo? \n"
             + "0. AFD\n"
             + "1. AFND\n"
             + "2. Salir\n")
opcion_elegida = int(input())

def menu_afd():

    print("¿Cuáles son sus estados? (separelos con espacios. Por ejemplo: 0 1 2 ...)\n")
    estados_keys = sorted([input().split(" ")])
    print("Cuales son sus estados iniciales? (separelos con espacios)\n")
    estados_inis = sorted([input().split(" ")])
    print("Cuales son sus estados finales? (separelos con espacios)\n")
    estados_fin = sorted([input().split(" ")])
    for estado in estados_keys:
        print("Defina las transiciones para el estado", estado, "de la siguiente forma: estado_al_que_voy caracter" +
              ", estado_al_que_voy caracter)=\n")
        # resultante:
        # 0: [(1, "a"), (2, "a")],
        inp_str = input().split(",")
        transiciones = [(inp_str[0], inp_str[1])]
        grafo[estado] = transiciones

    print(grafo)

# def menu_afnd():




#AFD: Comienzo

grafo = {
    "-e1": [("0", "e2"), ("1", "e3")],
    "e2": [("1", "*e4")],
    "e3": [("0", "*e4")],
    "*e4": [("1", "e2"), ("0", "-e1")]
}

palabra = "1010"
aceptada = False
nodoActual = "-e1"

# (mientras la palabra no sea vacia) y (podemos seguir avanzando por las transiciones del nodoActual por el simbolo)
while len(palabra) > 0 and any([t[0] == palabra[0] for t in grafo[nodoActual]]):

    simbolo = palabra[0]

    for trans in grafo[nodoActual]:
        if simbolo == trans[0]:
            nodoActual = trans[1]
            palabra = palabra[1:]
            print(palabra, nodoActual, trans)


if nodoActual[0] == "*":
    aceptada = True
    print(aceptada, ", palabra aceptada.")
else:
    print(aceptada, ", palabra no aceptada.")

#AFD: Fin


#AFND: Comienzo

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



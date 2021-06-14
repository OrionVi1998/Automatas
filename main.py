"""
Consigna: Hacer un programa que acepte los datos de un autómata de
terminista y no determinista y, lo haga funcionar como un autómata.
"""

import sys

class bcolors:
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR




# PREGUNTAR AL USUARIO
print("¿Su automata es de que tipo? \n"
             + "0. AFD\n"
             + "1. AFND\n"
             + "2. Salir\n")
opcion_elegida = int(input())


def menu_automata(estado_inicl, estados_fin, g):

    print("¿Cuáles son sus estados? (Separelos con espacios: 0 1 2...)\n")
    estados_keys = sorted(input().split(" "))
    # metodo para convertir los estados que ingreso el usuario a int
    for index, estado in enumerate(estados_keys):
        estados_keys[index] = int(estado)
    # print(estados_keys)

    print("¿Cuál es su estado inicial? \n")
    estado_inicl = int(input())
    print("¿Cuáles son sus estados finales? (separelos con espacios: 0 1 2...)\n")
    estados_fin = sorted([input().split(" ")])
    for index, estado in enumerate(estados_keys):
        print("Defina las transiciones para el estado", estado, "de la siguiente forma: estado_al_que_voy,caracter" +
              "__espacio__ estado_al_que_voy,caracter: \n")
        # resultante:
        # 0: [(1, "a"), (2, "a")],
        inp_str = input().split(" ")
        # print(inp_str)
        transiciones = []
        for tupla in inp_str:
            if (len(inp_str) > 0):
                # print("antes de append:", tupla)
                tupla = tupla.split(",")
                # quiero convertir el primer elemento a INT
                tupla[0] = int(tupla[0])
                # quiero convertir el segundo elemento a STR
                tupla[1] = str(tupla[1])
                transiciones.append(tuple(tupla))
            else:
                pass

        # print(transiciones)
        g[index] = transiciones

    print("grafo:")
    for element in g:
        print(element, g[element])


grafo = {}
estado_inicial = None
estados_finales = []

if opcion_elegida == 0:
    menu_automata(estado_inicial, estados_finales, grafo)
    print(estado_inicial)
    # afd(estado_inicial, )
elif opcion_elegida == 1:
    menu_automata(estado_inicial, estados_finales, grafo)
    # afnd()
elif opcion_elegida == 2:
    sys.exit()
else:
    print(f"{bcolors.FAIL}ERROR: Seleccione una opción valida.{bcolors.RESET}")


# AFD: Comienzo




# AFD: Fin


# AFND: Comienzo




# AFND: Fin



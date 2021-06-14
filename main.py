"""
Consigna: Hacer un programa que acepte los datos de un autómata de
terminista y no determinista y, lo haga funcionar como un autómata.
"""

import sys
from afd import afd
from afnd import afnd


class bcolors:
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


grafo = {}
estado_inicial = None
estados_finales = []
palabra = ""

# PREGUNTAR AL USUARIO
print("¿Su automata es de que tipo? \n"
             + "0. AFD\n"
             + "1. AFND\n"
             + "2. Salir\n")
opcion_elegida = int(input())


def menu_automata():
    global estados_finales
    global estado_inicial
    global grafo
    global palabra

    print("¿Cuáles son sus estados? (Separelos con espacios: 0 1 2...)\n")
    estados_keys = sorted(input().split(" "))
    # metodo para convertir los estados que ingreso el usuario a int
    for index, estado in enumerate(estados_keys):
        estados_keys[index] = int(estado)

    print("¿Cuál es su estado inicial? \n")
    estado_inicial = input()
    while len(estado_inicial) == 0:
        estado_inicial = input(f"{bcolors.FAIL}No es posible no tener un estado inicial. Por favor ingrese uno: {bcolors.RESET}")
    estado_inicial = int(estado_inicial)

    print("¿Cuáles son sus estados finales? (separelos con espacios: 0 1 2...)\n")
    # como input() es tomado como string, necesitamos convertir los estados a int
    finales = input()
    while len(finales) == 0:
        finales = input(f"{bcolors.FAIL}No es posible no tener estados finales. Por favor ingrese (al menos) uno: {bcolors.RESET}")

    for estado_final in finales.split(" "):
        estado_final = int(estado_final)
        estados_finales.append(estado_final)

    for index, estado in enumerate(estados_keys):
        print("Defina las transiciones para el estado", estado, "de la siguiente forma: estado_al_que_voy,caracter " +
              "__espacio__ estado_al_que_voy,caracter: \n")
        # resultante:
        # 0: [(1, "a"), (2, "a")],
        inp_str = input()
        # print(inp_str)
        transiciones = []
        for tupla in inp_str.split(" "):
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
        grafo[index] = transiciones

    print("\ngrafo:")
    for element in grafo:
        print(element, grafo[element])


while opcion_elegida != 2:

    if opcion_elegida == 0:
        menu_automata()
        salir = False
        while not salir:
            palabra = input("Ingrese la palabra a evaluar: ")
            afd(grafo, estado_inicial, estados_finales, palabra)

            respuesta = input(f"{bcolors.FAIL}¿Quieres volver a correr el programa? (Si/No): {bcolors.RESET}")
            if respuesta.lower("no"):
                salir = True

    elif opcion_elegida == 1:
        menu_automata()
        salir = False
        while not salir:
            palabra = input("Ingrese la palabra a evaluar:")
            # variables que necesitamos para el algoritmo del afnd
            ramificaciones = []
            visitados = []
            bifurcaciones = []

            print("<-- INICIO ALGORTIMO -->\n")
            afnd(grafo, estado_inicial, estados_finales, palabra, visitados, bifurcaciones, ramificaciones)
            print("<-- FIN ALGORITMO -->\n")
            if any(ramificaciones):
                print("Resultado: cadena aceptada\n")
            else:
                print("Resultado: cadena rechazada\n")

            respuesta = input(f"{bcolors.FAIL}¿Quieres volver a correr el programa? (Si/No): {bcolors.RESET}")
            if respuesta.lower("no"):
                salir = True

    else:
        print(f"{bcolors.FAIL}ERROR: Seleccione una opción valida.{bcolors.RESET}")

    print("\n")


try:
    import win32api, win32con
    respuesta = win32api.MessageBox(0, "¿Está seguro de que desea salir del programa?", "Salir",
                                    win32con.MB_YESNO | win32con.MB_ICONQUESTION)
    if respuesta == win32con.IDYES:
        quit()
    else:
        print(f"{bcolors.FAIL}Aguarde...{bcolors.RESET}\n")

except:
    print("Esta computadora no cuenta con Windows.")
    sys.exit()


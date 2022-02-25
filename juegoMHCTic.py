'''
Desarrollo de Juego de Totito con dos niveles, una a la defensiva y otro a la ofensiva

Marvin Estuardo Huitz Cuc

Curso: Inteligencia Artificial

'''
'''Librerias'''
import random # Libreria que Ofrece generadores de números pseudo-aleatorios para varias distribuciones
import time 
import os #permite acceder a funcionalidades dependientes del Sistema Operativo

def dise_tablero(tablero):
    '''En esta seccion esta el tablero que aparecera en pantalla al jugador'''
    '''Por eso se definio la siguiente funcion'''

    print()
    print("+++++++++++++++Totito++++++++++")
    print()
    print("      1         |2        |3")
    print("           {}    |    {}    |    {}".format(tablero[0], tablero[1],tablero[2]))
    print("                |         |")
    print("      ----------+---------+---------")
    print("      4         |5        |6")
    print("           {}    |    {}    |    {}".format(tablero[3], tablero[4],tablero[5]))
    print("                |         |")
    print("      ----------+---------+---------")
    print("      7         |8        |9")
    print("           {}    |    {}    |    {}".format(tablero[6], tablero[7],tablero[8]))
    print("                |         |")
    print()

'''----------------------------------------------------------------------------------------------'''
def menu_principal():
    '''Menu principal que se muestra al usuario'''
    print()
    print("==========Bienvenido(a)======")
    print()
    print("              Totito")
    print()
    print(" ------Escoge una opcion:")
    print()
    print("             1. A la Defensiva")
    print("             2. A la Ofensiva")
    print()
    print()

    nivel = ""
    while nivel != "1" and nivel != "2":
        nivel = input("             ---->")

    return int(nivel)
'''----------------------------------------------------------------------------------------------'''
def escoger_ficha():

    '''En esta funcion se da a escoger al usuario que ficha toma para el juego'''

    print()
    print("--------------------Totito----------------")
    print()
    print()
    print("------------>La ficha O inicia la partida")
    print()
    print("             Elige la ficha que quieres utilizar:")
    print("             O / X")
    print()
    print()

    ficha = ""
    while ficha != "O" and ficha != "X":
        ficha = input("           -->").upper()

    if ficha == "O":
        humano = "O"
        ordenador = "X"
    else:
        humano = "X"
        ordenador = "O"

    return humano, ordenador
'''----------------------------------------------------------------------------------------------'''

def movimiento_jugador(tablero):
    '''Esta funcion devuelve la casilla que escoga el usuario humano'''

    posiciones = ["1","2","3","4","5","6","7","8","9"]
    posicion = None
    while True:
        if posicion not in posiciones:
            posicion = input("     Te toca (1-9)")
        else:
            posicion = int(posicion)
            if not casilla_libre(tablero, posicion-1):
                print("    Esta posicion esta ocupada")

            else:
                return posicion-1
'''----------------------------------------------------------------------------------------------'''
def otra_partida():
    '''Esta permite que se pueda seguir jugando otra partida sin necesidad de salir del juego'''
    
    print("----------> Deseas jugar otra partida ")
    print()
    respuesta = input("------> Ingresa S o Si").lower()
    if respuesta == "s" or respuesta == "si":
        return True
    else:
        return False

'''----------------------------------------------------------------------------------------------'''
def has_ganado(tablero, jugador):

    '''Evalua si en el tablero: Se Tiene tres fichas en raya para determinar ganador'''

    if  tablero[0] == tablero[1] ==tablero[2] == jugador or \
        tablero[3] == tablero[4] ==tablero[5] == jugador or \
        tablero[6] == tablero[7] ==tablero[8] == jugador or \
        tablero[0] == tablero[3] ==tablero[6] == jugador or \
        tablero[1] == tablero[4] ==tablero[7] == jugador or \
        tablero[2] == tablero[5] ==tablero[8] == jugador or \
        tablero[0] == tablero[4] ==tablero[8] == jugador or \
        tablero[2] == tablero[4] ==tablero[6] == jugador:
        return True
    else:
        return False
'''----------------------------------------------------------------------------------------------'''
def tablero_lleno(tablero):
    '''Devuelve True si el tablero esta lleno y False si hay casillas vacias'''
    for i in tablero:
        if i == " ":
            return False
    else:
        return True
'''----------------------------------------------------------------------------------------------'''
def casilla_libre(tablero, casilla):

    '''Devuelve True si una casilla esta vacia y False si esta llena'''

    return tablero[casilla] == " "

'''----------------------------------------------------------------------------------------------'''

def IA_trata_ganar(tablero, jugador):

   
    for i in range(9):
        copia = list(tablero)
        if casilla_libre(copia, i):
            if has_ganado(copia, jugador):
                return i

    while True:
        casilla = random.randint(0,8)
        if not casilla_libre(tablero, casilla):
            casilla = random.randint(0,8)

        else:
            return casilla

'''----------------------------------------------------------------------------------------------'''
def IA_trata_noperder(tablero, jugador):
###  '''Esta inteligencia trata a la defensiva para no perder en la siguiente jugada'''###

    if tablero[0] == tablero[1] == jugador and tablero[2] == " ":
        casilla = 2
    elif tablero[0] == tablero[2] == jugador and tablero[1] == " ":
        casilla = 1
    elif tablero[1] == tablero[2] == jugador and tablero[0] == " ":
        casilla = 0
    
    elif tablero[3] == tablero[4] == jugador and tablero[5] == " ":
        casilla = 5
    elif tablero[3] == tablero[5] == jugador and tablero[4] == " ":
        casilla = 4
    elif tablero[4] == tablero[5] == jugador and tablero[3] == " ":
        casilla = 3

    elif tablero[6] == tablero[7] == jugador and tablero[8] == " ":
        casilla = 8
    elif tablero[6] == tablero[8] == jugador and tablero[7] == " ":
        casilla = 7
    elif tablero[7] == tablero[8] == jugador and tablero[6] == " ":
        casilla = 6
    
    elif tablero[0] == tablero[3] == jugador and tablero[6] == " ":
        casilla = 6
    elif tablero[0] == tablero[6] == jugador and tablero[3] == " ":
        casilla = 3
    elif tablero[3] == tablero[6] == jugador and tablero[0] == " ":
        casilla = 0

    elif tablero[1] == tablero[4] == jugador and tablero[7] == " ":
        casilla = 7
    elif tablero[1] == tablero[7] == jugador and tablero[4] == " ":
        casilla = 4
    elif tablero[4] == tablero[7] == jugador and tablero[1] == " ":
        casilla = 1

    elif tablero[2] == tablero[5] == jugador and tablero[8] == " ":
        casilla = 8
    elif tablero[2] == tablero[8] == jugador and tablero[5] == " ":
        casilla = 5
    elif tablero[5] == tablero[8] == jugador and tablero[2] == " ":
        casilla = 2

    elif tablero[0] == tablero[4] == jugador and tablero[8] == " ":
        casilla = 8
    elif tablero[0] == tablero[8] == jugador and tablero[4] == " ":
        casilla = 4
    elif tablero[4] == tablero[8] == jugador and tablero[0] == " ":
        casilla = 0

    elif tablero[2] == tablero[4] == jugador and tablero[6] == " ":
        casilla = 6
    elif tablero[2] == tablero[6] == jugador and tablero[4] == " ":
        casilla = 4
    elif tablero[6] == tablero[4] == jugador and tablero[2] == " ":
        casilla = 2

    else:
        while True:
            casilla = random.randint(0,8)
            if tablero[casilla] == " ":
                break

    return casilla
'''----------------------------------------------------------------------------------------------'''

'''-------------------------------------Programa Principal--------------------------------------'''
jugando = True

while jugando:

    tablero = [" "] * 9

    os.system("cls")

    nivel = menu_principal()

    os.system("cls")

    humano, ordenador = escoger_ficha()

    os.system("cls")

    dise_tablero(tablero)

    if humano == "O":
        turno = "Humano"
    else:
        turno = "Ordenador"

    partida = True

    while partida:

        if tablero_lleno(tablero):
            print("      Empate")
            partida = False
        
        elif turno == "Humano":
            casilla = movimiento_jugador(tablero)
            tablero[casilla] = humano
            turno = "Ordenador"
            os.system("cls")
            dise_tablero(tablero)
            if has_ganado(tablero, humano):
                print("      Has Ganado")
                partida = False

        elif turno == "Ordenador":
            print("      Analizando mi movimiento.......")
            time.sleep(2)
            if nivel == 1:
                casilla = IA_trata_noperder(tablero, humano)
            elif nivel == 2:
                casilla = IA_trata_ganar(tablero, humano)
            tablero[casilla] = ordenador
            turno = "Humano"
            os.system("cls")
            dise_tablero(tablero)
            if has_ganado(tablero, ordenador):
                print("   Partida Perdida")
                partida = False

    jugando = otra_partida()
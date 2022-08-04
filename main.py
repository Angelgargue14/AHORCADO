import os
import random
import time

def jugar():
    eleccion = 0
    while eleccion != 3:
        eleccion = eleccion_de_menu()

        if(eleccion == 1):
            agrega_palabras()
        elif (eleccion == 2):
            empieza_el_juego()
        elif (eleccion == 3):
            print("Hasta la próxima amigo! =D")

def eleccion_de_menu():
    print("Bienvenido al ahorcado, elige una opción del menú:")
    print("    1. Agregar palabras")
    print("    2. Jugar al ahorcado")
    print("    3. Salir")
    opcion = int(input("--> "))
    return opcion

def comprueba_diccionario():
    if os.path.isfile('diccionario.txt') == False:
        diccionario = open ('diccionario.txt','w')
        diccionario.close()

def agrega_palabras():
    comprueba_diccionario()

    cuantas_palabras = int(input("¿Cuantas palabras vas a introducir? --> "))
    contador = 0

    while contador < cuantas_palabras:
        nuevaPalabra = input("Dame la nueva palabra --> ")
        diccionario = open('diccionario.txt','a')
        diccionario.write(nuevaPalabra+',')
        diccionario.close()
        contador += 1

def genera_aleatorio(maximo):
    numero = random.randint(0, maximo)
    return numero

def seleccionar_palabra():  
    fichero = open('diccionario.txt','r')
    fichero = fichero.read()
    diccionario = fichero.split(',')
    maximo = len(diccionario)
    maximo = maximo - 2
    num_palabra = genera_aleatorio(maximo)
    
    palabra = diccionario[num_palabra].upper()
    return palabra
    
def pinta_tablero():
    palabra = seleccionar_palabra()
    longitud = len(palabra)
    print(f"\n\nBienvenido al gran juego del ahorcado \n\nA continuación te muestro la longitud de la palabra que tienes que adivinar:")
    print (f"La longitud es de: {longitud}\n")
    print("\n")
    return palabra
  
def empieza_el_juego():
    palabra = pinta_tablero()
    tupalabra = ''
    vidas = 6
    pinta_ahorcado(vidas)
    
    while vidas >0:
        fallas = 0
        for letra in palabra:
            if letra in tupalabra:
                print (letra,end="")
            else:
                print(" _",end="")
                fallas+=1
        
        if fallas == 0:
            print("\n\nFelicidades, ¡¡Has ganado!!\n\n")
            time.sleep(4)
            break
        
        tuletra=input("\n\nintroduce una letra -->")
        tuletra = tuletra.upper()
        tupalabra+=tuletra
        
        if tuletra not in palabra:
            vidas-=1
            print("\nVaya te equivocaste")
            pinta_ahorcado(vidas)
        if vidas == 0:
            print("Perdiste wei!")
            print("La palabra era--> ",palabra)
    else:
        print("Gracias por participar\n\n\n")
        time.sleep(4)
                
def pinta_ahorcado(vidas):
    
    if vidas == 6:
    
        print('''
    +---+
    |   |
        |
        |
        |
        |
========='''
        )
    elif vidas ==5:
        print('''
    +---+
    |   |
    O   |
        |
        |
        |
  =========
        ''')
    elif vidas==4:
        print('''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========   
        ''')  
    elif vidas==3:
        print('''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========   
        ''')    
    elif vidas ==2:
        print('''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========
        ''')      
    elif vidas == 1:
        print('''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========        
        ''')  
    elif vidas == 0:
        print('''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========       
        ''')    

jugar()

from random import *
from os import system
system("cls")

# VARIABLES GLOBALES
palos = ('♠', '🖤', '🍀', '💎')
numeros = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A')
contManos = 0
porc_victoria = 0
racha_usuario = 0
contBlackjackNatural = 0 # va a ser usado en punto 3 y tiene la cantidad blackjack natural
#Punto 3
montoMaximo = 0
monto_promedio = 0
perdida_max = 0
nombreUsuario = input("Ingrese su nombre: ").upper()
pozoUsuario = -1



while 100000 <= pozoUsuario or pozoUsuario <= 0:
    pozoUsuario = int(input("Ingrese el monto del pozo (entre 0 y 100000):\n"))
    if 100000 <= pozoUsuario or pozoUsuario <= 0:
        system("cls")
        print((" ERROR: Pozo inválido ").center(50, "~"))
        

while True:
    
    # Menu de opciones
    print((" MENU DE OPCIONES ").center(50, "*"))
    print(f'Bienvenido {nombreUsuario}')
    print(" {1} Apostar\n {2} Jugar una mano\n {3} Salir\n ")         
    opcion = int(input('Ingrese su opcion: \n'))
    #Opcion Apostar
    if opcion == 1:
        #imprimir el pozo previo a la apuesta
        print("Pozo previo apuesta: ", pozoUsuario, "\n")
        sobrePozo = int(input('Ingrese el dinero que quiere sumar al pozo: \n'))
        if sobrePozo > 0:
            pozoUsuario += sobrePozo 
            # print('El monto de la apuesta es de', apuesta, 'pesos')
            print('El monto del pozo actualizado es de', pozoUsuario, 'pesos')
        else:
            print('ERROR...La apuesta no puede ser negativa, ni cero')
            continue
    # Opcion Jugar una mano
    elif opcion == 2:
        print('El monto de la apuesta es de', pozoUsuario, 'pesos')
        apuesta = int(input(f'{nombreUsuario}, ingresá el dinero que vas a apostar: \n'))
        # Validacion: Si la apuesta es mayor al pozo o no es multiplo de 5 (ir al menu)
        if apuesta > pozoUsuario or apuesta % 5 != 0:
            
            print((f' ERROR: El valor de la apuesta debe ser menor o igual a {pozoUsuario}').center(50,"*"))
            continue
        else:
            
            for i in range(3):
                # Seleccion automatica de la carta
                carta = choice(palos), choice(numeros)
                # Calculo del puntaje de la carta
                #
                #
                #
                puntaje = #puntaje de la carta
                if i < 1:
                    #suma del Jugador (pasa dos veces)
                    print('Carta Jugador: ',carta)
                    suma_cartas_usuario += puntaje
                else:
                    #suma del Crupier (pasa 1 vez)
                    print('Carta Crupier: ',carta)
                    suma_cartas_crupier += puntaje
                    
                
                
            system("cls")
            print((" Comienza el juego").center(50,"*"))
            contManos += 1
            print("cantidad de manos: ",contManos)
            # Jugador recibe 2 cartas
            carta1_usuario = choice(palos), choice(numeros)
            carta2_usuario = choice(palos), choice(numeros)
            # suma de cartas usuario 
            suma_cartas_usuario = carta1_usuario[1] + carta2_usuario[1]
            # Crupier recibe 1 carta
            carta1_crupier = choice(palos), choice(numeros)
            # Jugador : Opción de más cartas
            flagJugadorContinuar = True
            while flagJugadorContinuar:
                print((" Opción de jugador: ").center(50,"*"))
                jugadorContinua = input(int("{0} Pedir otra carta\n{1} Pedir otra carta\n"))
                if jugadorContinua == 0:
                   #directmaente hacer la cuenta de puntos, cuenta de cantidad de cartas y listo. (debe salir de aca el puntaje del jugador)
                   sumador_cartas_usuario += choice(numeros)
                   break
                else:
                    continue
            # Jugador : Fin mano
            
            # Crupier: Debe pedir cartas mientras tenga 16 o menos de puntaje y plantarse con 17 o más
            
            # Comprobación black jack : El blackjack natural le gana a un blackjack conseguido con 3 cartas o más.

                  

    elif opcion == 3: 
        break
        
    else:
        system("cls")
        print((" ERROR: Opcion inválida").center(50,"*"))
        continue


    
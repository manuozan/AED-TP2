from random import *
from os import system
from turtle import clear
system("cls")

# VARIABLES GLOBALES
palos = ('♠', '🖤', '🍀', '💎')
numeros = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A')
contManos = 0
contCartasManoJugador = contCartasManoCroupier = 0
sumaUsuario = sumaCrupier = 0
porc_victoria = 0 
racha_usuario = 0
contBlackjackNatural = 0 # va a ser usado en punto 3 y tiene la cantidad blackjack natural
#Punto 3
montoMaximo = 0
monto_promedio = 0
perdida_max = 0
nombreUsuario = input("Ingrese su nombre: ").upper()
pozoUsuario = -1

# Validar que el pozo sea válido
while 100000 <= pozoUsuario or pozoUsuario <= 0:
    pozoUsuario = int(input("Ingrese el monto del pozo (entre 0 y 100000):\n"))
    if 100000 <= pozoUsuario or pozoUsuario <= 0:
        system("cls")
        print((" ERROR: Pozo inválido ").center(50, "~"))
        
print((f'- BIENVENIDO {nombreUsuario} -').center(50," "))
while True:
     
    # Menu de opciones
    print((" MENU DE OPCIONES ").center(50, "*"))
    # print(" {1} Agregar al pozo\n {2} Jugar una mano\n {3} Salir")  
    # Selección de opción menu       
    opcion = input('{1} Agregar al pozo\n{2} Jugar una mano\n{3} Salir\nIngrese su opcion:\n')
    #Opcion Apostar
    if opcion == "1":
        print((" AGREGAR AL POZO ").center(50, "*"))
        #Pozo previo a la apuesta
        print("Pozo previo: ", pozoUsuario, "\n")
        #Aumento del pozo
        addPozo = int(input('Ingrese el dinero que quiere agregar al pozo: \n'))
        if addPozo > 0:
            pozoUsuario += addPozo 
            print('El monto actualizado del pozo es de:', pozoUsuario, 'pesos')
        #VALIDACION: Aumento del pozo, si no es correcto (ir a menu)
        else:
            print(('ERROR... El monto de aumento del pozo es inválido').center(50,"*"))
            continue
    # Opcion Jugar una mano
    elif opcion == "2":
        contManos += 1
        sumaJugador = 0
        sumaUsuario = 0
        sumaCrupier = 0
        
        # Realizar apuesta
        apuesta = int(input(f'{nombreUsuario}, el pozo es de ${str(pozoUsuario)}.\
                            \nIngrese el dinero del pozo a apostar: \n'))
        # Validacion: Si la apuesta es mayor al pozo o no es multiplo de 5 (ir al menu)
        if apuesta > pozoUsuario or apuesta % 5 != 0:
            print((f' ERROR: El valor de la apuesta debe ser menor o igual a {pozoUsuario} y múltiplo de 5').center(50,"*"))
            continue
        else:
            contCartasManoJugador = contCartasManoCroupier = 0
            sumaJugador = 0 # Suma de quien esté jugando (Usuario o Croupier)          
            flagJuegaUsuario = True
            flagJuegaCroupier = False
            flagSacarCarta = True
            while flagJuegaUsuario or flagJuegaCroupier:
                if flagSacarCarta:
                    # Sacar carta
                    carta = choice(palos), choice(numeros)
                    # Calculo del valor de la carta
                    cartaValor = carta[1]
                    # Si es J/Q/K valor será 10
                    if cartaValor == "J" or \
                        cartaValor == "K" or \
                        cartaValor == "Q":
                        cartaValor = 10
                    # Si es A el valor será 11
                    elif cartaValor == "A":
                        if sumaJugador < 11:
                            cartaValor = 11
                        else:
                            cartaValor = 1
                # Turno del usuario
                if flagJuegaUsuario:
                    # Jugador (primera ronda = 2 cartas)
                    if contCartasManoJugador < 2:
                        print(f'{nombreUsuario} saca carta: {carta}')
                        contCartasManoJugador += 1
                        sumaUsuario += cartaValor
                        sumaJugador = sumaUsuario
                        # Luego de jugar dos cartas le toca jugar al croupier
                        if contCartasManoJugador == 2:
                            flagJuegaCroupier = True      
                            flagJuegaUsuario = False     
                        continue
                    # Jugador: (Cuando tiene ya dos cartas o mas)
                    elif contCartasManoJugador >= 2:
                        # Si sacó una carta del maso
                        if flagSacarCarta:
                            print(f'{nombreUsuario} saca carta: {carta}')
                            contCartasManoJugador += 1
                            sumaUsuario += cartaValor
                            
                        # Opción para seleccionar más cartas usuario (SIEMPRE QUE NO SUPERE LOS 21)
                        if sumaUsuario < 21:
                            otraCarta = int(input(f'{nombreUsuario}: Desea otra carta?\n{1}->SI\n{2}->NO\n'))
                        else:
                            otraCarta = 0
                        # Si desea sacar otra carta   
                        if otraCarta == 1:
                            flagSacarCarta = True
                            sumaJugador = sumaUsuario
                            continue
                        # Si no desea o puede tomar más cartas es el turno del croupier
                        elif otraCarta == 2:
                            flagJuegaUsuario = False
                            flagJuegaCroupier = True
                            flagSacarCarta = True
                            sumaJugador = sumaCrupier
                            print((f' FIN MANO {nombreUsuario}').center(50,"*"))
                        else:
                            flagSacarCarta = False
                            print((f' ERROR: Seleccione una opción válida.').center(50,"*"))
                            break
                # Turno del Croupier
                elif flagJuegaCroupier:
                    if flagSacarCarta and sumaCrupier < 17:
                        print(f'Croupier saca carta: {carta}')
                        contCartasManoCroupier += 1
                        sumaCrupier += cartaValor
                        sumaJugador = sumaCrupier
                        # Luego de la primer ronda dar opción al usuario de sacar más cartas
                        if contCartasManoCroupier == 1: 
                            flagJuegaCroupier = False      
                            flagJuegaUsuario = True  
                            flagSacarCarta = False
                            sumaJugador = sumaJugador
                    else:
                        print((f' FIN MANO CROUPIER').center(50,"*"))
                        flagJuegaCroupier = False
                        flagSacarCarta = False
                        
            # Determinación de ganador          
            if (sumaCrupier < sumaUsuario <= 21) or (sumaCrupier > 21 >= sumaUsuario):
                resultado = f"{nombreUsuario} gana"
                # Si el usuario gana recibe el doble de la apuesta
                pozoUsuario += apuesta*2 - apuesta
                
            elif (sumaUsuario < sumaCrupier <= 21) or (sumaUsuario > 21 >= sumaCrupier):
                resultado = "La casa gana"
                # Si la casa gana se resta apuesta del pozo
                pozoUsuario -= apuesta
            elif sumaUsuario == sumaCrupier and sumaUsuario <= 21:
                resultado = "Hay empate"
                # Si hay empate el pozo queda tal cual
            else:
                resultado = "Ambos pierden"
                # Si ambos pierden
                pozoUsuario -= apuesta
            #Reiniciamos el valor de la apuesta
            apuesta = 0 
          
            
            print((f' RESULTADOS FINALES ').center(50,"*"))
            print()
            print('Monto de la apuesta: ',apuesta) 
            print(f'Puntaje {nombreUsuario}: ',sumaUsuario) 
            print('Puntaje Croupier: ',sumaCrupier) 
            print(f'El resultado es: {resultado}')
            print(f'El total restante en el pozo es de: $ {pozoUsuario}')
                        
   
    
    elif opcion == "3": 
        sumaUsuario = 0
        break
        
    else:
        system("cls")
        print((" ERROR: Opcion inválida ").center(50,"*"))
        continue

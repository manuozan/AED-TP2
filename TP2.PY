from random import *
from os import system
system("clear")


def sacarUnaCarta(sumaJugador: int):
    """Saca una carta,  devuelve su valor. Si el jugador saca un as, 
    su valor dependera del puntaje acumulado (sumaJugador)"""
    palos = ('♠', '♥', '♣', '♦')
    numeros = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A')
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
    print(f'Carta del maso: {carta[0]} {carta[1]}')
    return cartaValor


########################### INICIALIZAMOS VARIABLES ###########################

contManos = 0
contCartasManoJugador = contCartasManoCroupier = 0
sumaUsuario = sumaCoupier = 0
rachaUsuario = rachaCoupier = 0
porc_victoria = 0
contBlackjackNatural = 0
acumuladorPozo = 0
pozoMax = 0
montoPromedio = 0
perdidaMax = 0
nombreUsuario = input("Ingrese su nombre: ").upper()
pozoUsuario = -1

# Validar que el pozo sea válido
while 100000 < pozoUsuario or pozoUsuario <= 0:
    pozoInicial = int(input("Ingrese el monto del pozo (entre 0 y 100000):\n"))
    pozoUsuario = pozoInicial
    acumuladorPozo = pozoUsuario
    if 100000 < pozoUsuario or pozoUsuario <= 0:
        system("clear")
        print((" ERROR: Pozo inválido ").center(50, "~"))

print((f'=').center(50, "="))
print((f'- BIENVENIDO {nombreUsuario} -').center(50, " "))
print((f'=').center(50, "="))

while True:
    # Menu de opciones
    print((" MENU DE OPCIONES ").center(50, "*"))

    # Selección de opción menu
    opcion = input(
        '{1} Agregar al pozo\n{2} Jugar una mano\n{3} Salir\nIngrese su opción:\n')

    ########################### PUNTO 1 - APOSTAR ###########################
    if opcion == "1":
        print((" AGREGAR AL POZO ").center(50, "*"))
        # Pozo previo a la apuesta
        print("Pozo previo: ", pozoUsuario, "\n")
        # Aumento del pozo
        addPozo = int(
            input('Ingrese el dinero que quiere agregar al pozo: \n'))
        if addPozo > 0 and (pozoUsuario + addPozo) <= 100000:
            pozoUsuario += addPozo
            if contManos == 0:
                acumuladorPozo = pozoUsuario

            print('El monto actualizado del pozo es de:', pozoUsuario, 'pesos')
        # VALIDACION: Aumento del pozo, si no es correcto (ir a menu)
        else:
            print(('ERROR... El monto de aumento del pozo es inválido').center(50, "*"))

    ########################### PUNTO 2 - JUGAR UNA MANO ###########################

    elif opcion == "2":
        if pozoUsuario == 0:
            print((" ERROR NO TIENE DINERO DISPONIBLE ").center(50, "-"))
            continue
        print((" COMIENZA EL JUEGO ").center(50, "*"))
        contManos += 1
        sumaUsuario = 0
        sumaCoupier = 0

        # Realizar apuesta
        apuesta = int(input(f'{nombreUsuario}, el pozo es de ${str(pozoUsuario)}.\
                            \nIngrese el dinero del pozo a apostar: \n'))
        # Validacion: Si la apuesta es mayor al pozo o no es multiplo de 5 (ir al menu)
        print((f' TURNO {nombreUsuario} ').center(50,"*"))
        if apuesta > pozoUsuario or apuesta % 5 != 0:
            print((f' ERROR: El valor de la apuesta debe ser menor o igual a {pozoUsuario} y múltiplo de 5').center(
                50, "*"))
            continue
        else:
            contCartasManoJugador = contCartasManoCroupier = 0
            flagJuegaUsuario = True
            flagJuegaCroupier = False
            # flagSacarCarta = True

            while flagJuegaUsuario or flagJuegaCroupier:
                # Definimos quien van a jugar
                if contCartasManoJugador < 2:
                    flagJuegaUsuario = True
                    flagJuegaCroupier = False
                elif contCartasManoJugador == 2 and contCartasManoCroupier == 0:
                    flagJuegaUsuario = False
                    flagJuegaCroupier = True

                elif contCartasManoJugador >= 2 and flagJuegaUsuario:
                    # por default consideramos proxima mano juega croupier
                    flagJuegaUsuario = False
                    flagJuegaCroupier = True
                    if sumaUsuario < 21:
                        print((f' TURNO {nombreUsuario} ').center(50, "*"))
                        otraCarta = int(
                            input(f'{nombreUsuario}: Desea otra carta?\n(1)->SI\n(otra tecla)->NO\n'))
                        # Si elije que juega otra mano
                        if otraCarta == 1:
                            flagJuegaUsuario = True
                            flagJuegaCroupier = False
                        
                    # Jugan la carta
                if flagJuegaUsuario:
                    #print((f' TURNO {nombreUsuario} ').center(50, "*"))
                    sumaUsuario += sacarUnaCarta(sumaUsuario)
                    contCartasManoJugador += 1
                    if sumaUsuario == 21 and contCartasManoJugador == 2:
                        print('blackjack natural')
                        contBlackjackNatural += 1
                elif flagJuegaCroupier:
                    print((f' TURNO CROUPIER ').center(50, "*"))
                    sumaCoupier += sacarUnaCarta(sumaCoupier)
                    contCartasManoCroupier += 1
                    if contCartasManoCroupier == 1:
                        flagJuegaUsuario = True
                        flagJuegaCroupier = False
                # Mientras la suma del croupier sea menor a 17 la partida sigue
                if sumaCoupier >= 17:
                    flagJuegaUsuario = False
                    flagJuegaCroupier = False

            # Determinación de ganador
            if (sumaCoupier < sumaUsuario <= 21) or (sumaCoupier > 21 >= sumaUsuario):
                resultado = f"{nombreUsuario} gana"
                # Si el usuario gana recibe el doble de la apuesta y sumamos una victoria al contador
                pozoUsuario += apuesta
                rachaUsuario += 1

            elif (sumaUsuario < sumaCoupier <= 21) or (sumaUsuario > 21 >= sumaCoupier):
                resultado = "La casa gana"
                # Si la casa gana se resta apuesta del pozo y sumamos una victoria al contador
                pozoUsuario -= apuesta
                rachaCoupier += 1

                # maxima perdida (La apuesta siempre sera mayor que cero)
                if perdidaMax < apuesta:
                    perdidaMax = apuesta

            elif sumaUsuario == sumaCoupier and sumaUsuario <= 21:
                resultado = "Hay empate"
                # Si hay empate el pozo queda tal cual
            else:
                resultado = "Ambos pierden"
                # Si ambos pierden
                pozoUsuario -= apuesta

            acumuladorPozo += pozoUsuario
            if rachaUsuario == 0:
                pozoMax = pozoInicial
            else:
                if pozoMax < pozoUsuario:
                    pozoMax = pozoUsuario
            print()
            print((f'=').center(50, "="))
            print((f'{resultado.upper()}').center(50, " "))
            print((f'=').center(50, "="))
            print(f'Puntaje {nombreUsuario}: ', sumaUsuario)
            print('Puntaje Croupier: ', sumaCoupier)
            print('Monto de la apuesta: $', apuesta)
            print(f'El pozo actualizado es de: $ {pozoUsuario}')
            print()
            # Reiniciamos el valor de la apuesta
            apuesta = 0

    ########################### OPCIÓN 3 - SALIR ###########################
    elif opcion == "3":
        # monto maximo que llegó a tener el jugador

        if contManos > 0:
            porc_victoria = rachaUsuario / contManos * 100
            montoPromedio = acumuladorPozo // (contManos + 1)
        else:
            porc_victoria = 0
            montoPromedio = acumuladorPozo
            pozoMax = acumuladorPozo

        print((f' RESUMEN ').center(50, "="))
        print(f'Manos jugadas: {contManos}')
        print(f'Porcentaje de victorias: {round(porc_victoria,2)}%')
        print(
            f'Cantidad de manos con blackjack natural: {contBlackjackNatural}')
        print(f'Pérdida máxima: ${perdidaMax}')
        print(f'Monto max del jugador en el pozo: ${pozoMax}')
        print(f'Racha del coupier: {rachaCoupier}')
        print(f'Acumulador pozo: {acumuladorPozo}')
        print(
            f'Monto promedio que dispuso el jugador para realizar apuestas: ${montoPromedio}')
        break

    else:
        system("clear")
        print((" ERROR: Opción inválida ").center(50, "*"))
        continue

print((f'=').center(50, "="))
print((f'FIN DEL JUEGO').center(50, " "))
print((f'=').center(50, "="))

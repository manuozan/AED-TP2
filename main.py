nombreUsuario = input("Ingrese su nombre")
pozoUsuario = -1
while 100000 < pozoUsuario or pozoUsuario < 0:
    pozoUsuario = int(input("Ingrese el monto del pozo:"))
    if 100000 < pozoUsuario or pozoUsuario < 0:
        print("Ingrese pozo entre 0 y 100000")
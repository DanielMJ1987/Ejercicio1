#Permite validar a un usuario con 3 intentos y los datos de validación correctos almacenados en dos constantes predefinidas.

usuario = str('Daniel')
pw = str('montero')
intentos = 0
atras = 5

while intentos < 5:
    usuario1 = input('Usuario: ')
    pw1 = input('Password: ')
    if usuario1 == usuario and pw1 == pw:
        print("Felicidades")
        intentos = 5
    else:
        atras -= 1
        print("Intentalo otra vez, te quedan " + str(atras))
        intentos += 1



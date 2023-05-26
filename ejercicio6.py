#Dispones de tres números enteros H, M, S correspondientes a hora, minutos y segundos respectivamente,
# debes comprobar si se trata de una hora válida.

H = int(input('Inserta una hora: '))
M = int(input('Inserta los minutos: '))
S = int(input('Inserta los segundos: '))

if H < 24 and M < 60 and S < 60:
    print("La hora corresponde a las : " + str(H) + "H." + str(M) + "M." + str(S) + "S." + "La hora es valida")
else:
    print("La hora introducida no es valida")
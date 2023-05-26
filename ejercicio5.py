#Crea una variable que sea una letra, si es una a muestra el número 7, si es una b, el 9, si es una c el 101
# y si no es ninguno de los tres, indica que se han equivocado de letra


letra = input('Teclea 1 de estas tres letras a , b , c: ')
resu = 0
if letra == str("a"):
    resu = 7
    print(resu)
if letra == str("b"):
    resu = 9
    print(resu)
if letra == str("c"):
    resu = 101
    print(resu)

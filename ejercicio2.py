#Dispones de frase y una letra, solicitados al usuario y debes mostrar la cantidad de veces que aparece la letra en la frase.

cant = 0
frase = input('Inserta una frase: ')
letra = input('Que letra quieres contar: ')

cant = frase.count(letra)

print(cant)


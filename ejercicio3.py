#Suma o resta dos números reales solicita la información al usuario

resu = 0
n = int(input('Inserta un número: '))
n2 = int(input('Inserta un número: '))
n3 = int(input('Inserta + para sumar y - para restar: '))

if n3 == str("+"):
    resu = n + n2
    print(resu)
else:
    resu = n - n2
    print(resu)





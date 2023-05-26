#Indicar cuál es el menor de tres enteros solicitados al usuario

n = int(input('Inserta un número: '))
n2 = int(input('Inserta un número: '))
n3 = int(input('Inserta un número: '))

if n <= n2 and n <= n3:
  print(str(n) + ' es el menor')

if n2 <= n and n2 <= n3:
  print(str(n2) + ' es el menor')

if n3 <= n and n3 <= n2:
  print(str(n3) + ' es el menor')

"""print("Si desea salir ingrese 0")
numero1 = int(input('Inserta un número: '))
if(numero1 != 0)
  numero2 = int(input('Inserta otro número: '))
  """
# Ciclos 
# While: bucle que se repite hasta que no se cumpla su condición 
# Sintaxis:
# iniciar valor de condición
# while condición:
#   acción
#   cambio de condición (!condición)
# Break: Salir de bucle por fuerza bruta 
# Serie de Taylor para e^x=1+x+x^2/2!+x^3/3!+x^4/4!+...+x^n/n!
from math import factorial # Importar la función factorial del módulo math
"""
x,n=3,1
sx=1
while True: # while 1:
    sx += x**n/factorial(n)
    print(sx)   
    n+=1
    if n>10:
        print("Detener")
        break

# Ejemplo 2
n=input("Introduce un número para empezar\n")
sum=0
while n.isnumeric():
    sum += int(n)
    n=input("Introduce un número para sumar\n")
else:
    print("Suma total es: {}".format(sum))

# For: bucle que se repite siempre que se cumpla la condición (iteracciones)
# Sintaxis:
# for recorrido:
#   acciones
# Ejemplo str
s = "Que onda !" 
for c in s: # Extraer cada caracter de un string 
    print(c)
# Ejemplo num
from math import factorial
sx = 0
x = 3
for i in range (0, 27, 1): # Por cada iteración en el rango de 0 a 10 en intervalos de 1
    sx += x**i/factorial(i)
    print(sx)
# En reversa
for i in range (10,0,-1):
    print(i)


# Comando continue: continuar la ejecución
for i in range(101): 
    if i%2 != 0: # Calcular residuo de la operación i/2
        continue # "Vete a la siguente linea"
    print(i) # Imprimir en pantalla números pares 
"""

# Ciclos anidados
for i in range(1,3):
    print("Conteo principal {}".format(i))
    for j in range(1,3):
        print("Conteo secundario", j)

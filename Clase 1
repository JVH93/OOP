# Comentarios: Parte de código que no se ejecuta, nos sirve para hacer anotaciones, se definen por el signo #
# Tema 1: Variables
# Se definen como la relación entre un espacio de memoria y un nombre, 
# consisten en un identificador y una parte de la memoria del dispositivo
# Sintaxis: nombre_variable = valor
# Nota: en Python no es necesario especificar el tipo de dato 
# Existen restricciones en el nombramiento de una variable 
# No pueden empezar ni contener caracteres especiales
# No pueden empezar por números
# No pueden ser llamadas igual que las palabras claves reservadas en Python
# No pueden contener espacios
# Ejemplo en la variable "x" almacenamos un valor numérico 
x=999
# En la variable "y" un valor de cadena de caracteres (string) "" ''
y="Esto es un string"
# Instrucción print permite visualizar el contenido del argumento 
print("El valor de x es: ",x)
print(y)
# Podemos declarar múltiples variables de la siguiente forma 
nombre, edad, sexo = "Pedro" ,22, 'M'
nombre2="Maria"; edad2= 25; sexo2='F'
print (nombre, edad, sexo)
print (nombre2, edad2, sexo2)
# También podemos realizar operaciones matemáticas con las variables 
print("Suma",x+5,"Multiplicación",x*2)
# Si necesitamos el valor lo podemos asignar a otra variable 
z=x-3
print(z)
# Existe un truco cuando se repite la misma operación, es decir, en lugar de hacer x = x + 1 podemos hacer:
x += 2
print (x)
# También tenemos -=, *=, /=, //=, %= y **= 

# Tema 2: Función import 
# Antes de explicar en qué consiste la función import, hay que definir los siguientes conceptos:
# Algoritmo. Conjunto ordenado de operaciones sistemáticas que permite hacer un cálculo y hallar la 
# solución de un problema.
# Función. Bloque de código con un nombre asociado, que recibe cero o más argumentos como entrada, 
# sigue una secuencia de sentencias, la cuales ejecuta una operación deseada y devuelve un valor y/o realiza una tarea.
# Script. Archivo diseñado para ser ejecutado. Puede contener funciones, programas, etc.
# Módulo (librerías). Script que contiene colecciones de funciones, definiciones y declaraciones de Python.
import math
print(math.factorial(5)) #Sintaxis: Escribir nombre del módulo, punto y la función que voy a ocupar de ese módulo
# Si el nombre de la librería es muy largo solemos usar 
import math as mt
print(mt.sqrt(16))
# Para cargar solo una función del módulo (sirve para ejecutar más rápido) usamos
from math import pi
from math import log, exp
print(pi)
# Truco: si utilizamos el símbolo * después de import todas las funciones se cargaran y no tendremos que hacer referencia
from math import * # Tener cuidado con esto
print(radians(180))
# Podemos modificar el nombre de la función proveniente del módulo 
from math import asin as seno_inverso
print(seno_inverso(1))

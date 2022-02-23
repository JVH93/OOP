# Tema 3: Los números en Python 
# En otros lenguajes de programación solemos declarar el tipo de dato que almacenará esa variable
# Python nos da la ventaja de no requerir esa declaración 
# sin embargo, debes conocer que hay dos tipos de datos para números
# los enteros (int) y los flotantes (float)
# podemos usar la función type para conocer este tipo de datos
numero_i=10
td = type (numero_i)
print(td)
numero_f=12.123
print(type (numero_f))
# Para convertir tipos de datos numéricos usamos la función int() y float() [cast]
print(type (int(numero_f)))
# NOTA: NO REDONDEA 
# OPERACIONES: 
# Suma (+), resta (-), división (/), división entera (//), resto (%), potencia (**) [pow()] 

# NÚMEROS COMPLEJOS 
z= 3.5 + 7.78j
z2=complex(2,5)
print(type (z),type (z2))
# Sacar parte real o imaginaria del número complejo 
zr=z.real
zi=z.imag
print("El numero real es {} y el numero imaginario es {}".format(int(zr),zi))
# Otros cálculos 
zc=z.conjugate() #Conjugado
zm=abs(z) #Modulo
print("El conjugado de {} es {} y el modulo es {}".format(z,zc,zm))
# Librería cmath (para trabajar números complejos)
import cmath as nc
print("La fase de {} es {}".format(z,nc.phase(z))) #Fase
zp=nc.polar(z) #Convertir a polar
print("El numero {} en polar es: {}".format(z,zp))
a=nc.rect(1,1.57) #Convertir a rectangular
print(a)

# Texto en Python 
# string: cadena ordenada de caracteres 
s1="Hola "
print (type(s1))
# String literals \\ (backslash), \' (comilla simple), \" (comillas dobles), \n (salto de línea), \t (tabular)
print("Texto arriba \nTexto abajo")
# Concatenar
s2="mundo"
print(s1+s2)
# Texto más número
dia=22
print("Hoy es " + str(dia))
# Colocar variables en texto {}
print("Hoy es {} {} {} {}".format(dia, 1 , 2, 3))
print(f"Hoy es {dia}")
# Substrings [], con valores negativos el conteo será desde el final hasta el principio
print(s1[0])
print(s1[-2])
# Conjunto de substring:
print(s1[1:3])
# Métodos: minúsculas (.lower()), mayusculas (.upper()), conteo de letras (.count())
# Mayúscula la primera (.capitalize()), mayuscula inicio de cada palabra (.tittle())
smay="TEXTO A CONVERTIR"
smin=smay.lower()
print(smin)
print(smay.count('R'))
# Reemplazar 
print(smay.replace("TEXTO","ESCRITO"))
# Dividir (split)
s3="PROGRAMACIÓN AVANZADA ES FÁCIL"
cortado=s3.split(" ")
print(cortado,type(cortado))
# Encontrar .index() .find() .rindex()
print(s3.find("AVANZADA"))
print(s3.find("A",21))
# Longitud de la cadena
print(len(s3))
# Pedir datos a usuario
print("Introduce tu edad")
edad=int(input("Edad: "))
nombre=input("Nombre: ")
print(edad+1)
print("Eres {} y tienes {} años".format(nombre, edad))

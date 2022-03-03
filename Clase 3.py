# Mundo 1-0
verdadero= True
falso= False
print(type(verdadero))
# Negar
print(not verdadero)
# Conjunción (and)
A, B= False, False
print(A and B)
print(not A and not B)
# Disyunción (or)
print(A or B)
print(A or not B)
# Comparaciones 
print(10 == 10) #Igual
print(10 != 10) #Diferente
print(10 <= 7) #Menor que 
print(10 == "10")  #Ojo con el tipo de dato
# Condiciones 
edad=25
print((edad >= 23) and (edad <= 50))
# Para strings se compara el orden alfabético 
# Existen métodos para trabajar con strings como 
s = "Podemos obtener información de un string."
s.startswith("p") # Saber si el string empieza por un carácter o texto específico (distingue M/m)
print("¿El string s empieza con P?",s.startswith("P"))
print("¿El string s termina con un punto?",s.endswith(".")) # Saber si el string termina por un carácter o texto específico (distingue M/m)
print(s.isalnum()) # Saber si el string es alfanumérico (será falso porque contiene espacios)
# También tenemos isalpha(), isdigit(), isspace(), islower(), isupper(), istittle()

# OPERADOR IF
# Cuya sintaxis es:
# if condición:
#    acción 1
#    accion 2
# A diferencia de muchos lenguajes en Python no se utilizan las llaves para indicar el contenido de un ciclo
# El algoritmo a ejecutar será aquel que esté separado con tabulación debajo del inicio del ciclo
# NO TE OLVIDES DE LOS DOS PUNTOS Y LAS TABULACIONES
cal=75
if cal>=70:
    print("Aprobado")
# OPERADOR ELSE
# Cuya sintaxis es:
# if condición:
#    acción
# else:
#    acción     
# ALINEAR IF Y ELSE 
cal = 50
if cal>=70:
    print("Aprobado")
else:
    print("Reprobado")
# OPERADOR ELIF (ELSE IF)
# Cuya sintaxis es:
# if condición1:
#    acción1
# elif condición2:
#    acción2     
# elif condición3:
#    acción3
# else:
#    acción salida   
# ALINEAR IF, ELIF 
#edt= int(input("Dime tu edad\n"))
edt=0
if edt>=60:
    print("Eres muy grande para este trabajo")
elif edt>=23:
    print("Cumples requisito")
else:
    print("Eres muy chico para este trabajo")
# OPERADOR EN LINEA 
# Cuya sintaxis es:
# acción_cierto if condición else acción_falso
edad=18
print("Eres mayor de edad") if edad>=18 else print("Eres menor de edad")
# La importancia de este operador es que podemos definir variables con una condición
n=12
num= "Par" if n%2==0 else "Impar"
print(num)
# Finalmente podemos tener operadores anidados 
edt= 65
sexo="F"
if edt>=60:
    print("Eres muy grande para este trabajo")
elif edt>=23:    
    if sexo=="F":
        print("Cumples requisito de edad y sexo")
    else:
        print("Cumples solo requisito de edad")
else:
    print("Eres muy chico para este trabajo")

"""ESTRUCTURAS DE DATOS"""
# LISTAS
"""Conjunto de elementos ordenados, seperados por comas y escritos entre corchetes []. Los elementos pueden ser de diferente tipo en una misma lista. Los elementos pueden ser modificados (mutables)."""

"""Definiciones de listas"""
l = ["José", 28, 1.72, True] # Declarar lista 
print (l)
print (len(l)) # Longitud de una lista.
print (l[0]) # Imprimir un elemento especifico.
print (l[-1]) # Elemento especifico derecha-izquierda.
print (l[1:3]) # Conjunto de elementos especificos. (1 y 3)
l[2] = "Cambio" # Cambio de elemento de una lista.
print(l)
l.append("Nuevo") # Añadir elemento al final de la lista.
print(l)
l.insert(0,"Inserto") # Añadir elemento en indice de lista.
print(l)
"""RETO: PEDIR A USUARIO LONGITUD DE LISTA Y RELLENAR CON NOMBRES DE PAISES ESA LISTA""" 

n = int(input("¿Cuantos países quieres?\n"))
p = []
for i in range (n):
    p.append(input(f"Introduce el país {i+1}\n"))
print (p)

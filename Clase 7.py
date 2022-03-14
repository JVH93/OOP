# CONJUNTOS
""" Estructura sin orden que no admiten múltiples ocurrencias de un mismo elemento. Pueden ser definidos a partir de una lista con la función set(), o bien, los elementos del conjunto pueden ir entre llaves, {}, y estar separados por comas.

Los conjuntos son:

hetereogéneos: los elementos pueden ser de distinto tipo en un mismo conjunto
no mutables: los elementos no pueden ser modifcados una vez el conjunto ha sido creado
Los conjuntos pueden construirse con la función set() o directamente entre llaves, {}. """

conjunto1 = set([1, 3, 4, 7, 5, 5, 2]) 
print (conjunto1, type(conjunto1))
conjunto2 = {0, 6, 8, 9, 10, 10, 7}
print (conjunto2, type(conjunto2))
conjunto3 = {0, "a", 6, 8, 9, "C", "b", 10, "A", 10, 7, "i"}
print (conjunto3, type(conjunto3)) 
# OJO: PRINT TIENE DETALLES AL MOSTRAR CONJUNTOS

#SUBCONJUNTO 
A, B = {0, 3, 7, 2, 5}, {2, 3, 0}
print(B.issubset(A))

#OPERACIONES CON CONJUNTOS 
A, B = {0, 3, 7, 2, 5}, {2, 3, 1, 6, 8}
print(A | B) # Union 1
print(A.union(B)) # Union 2
print(A & B) # Intersección 1
print(A.intersection(B)) # Intersección 2
print(A - B) # Diferencia 1 
print(A.difference(B)) # Diferencia 2 
print(A.symmetric_difference(B)) # Simetrica 

# TRABAJANDO CON CONJUNTOS 
A.add(10) # Añadir elemento especifico 
print(A)
A.update(B) # Añadir elementos de otro conjunto
print(A)
A.remove(10) # Eliminar un elemento que sabemos que está
A.discard(6) # Eliminar un elemento aunque no sepamos que este
print(A)
print(10 in A) # Saber si un elemento está dentro del conjunto
print(len(A)) # Numero de elementos de un conjunto 

# BUCLES 
for item in A:
    print(item)

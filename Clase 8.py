# TUPLAS
""" Conjunto de elementos, que pueden ser de distintos tipos, separados por comas y escritos entre paréntesis, ().

Las tuplas son:

hetereogéneas: los elementos pueden ser de distinto tipo en una misma tupla
no mutables: los elementos no pueden ser modifcados una vez la tupla ha sido creado """


t1 = ("José", 29, "Ingeniero")
print (t1, type(t1))
t2 = tuple([1, 2, 3])
print (t2, type(t2))
t3 = "a", "b", 30.05, True
print (t3, type(t3))

# TRABAJANDO CON TUPLAS
print(t1[0]) # Elemento cero
print(t2[-1]) # Ultimo elemento
print(t3[2:]) # Elementos del tercero al ultimo
print ("a" in t3) # Saber si tenemos un elemento especifico 
# TRUCO "MODIFICAR" TUPLA 
l = list(t2) # Convierte a lista 
l[2] = "Tres" # Sustituye 
t2 = tuple(l) # Convierte a tupla de nuevo 
print(t2)
# DESEMPAQUETAR TUPLA
(v1, v2, v3) = t1 # Tambien puede ser sin parentesis, TIENE QUE COINCIDIR EL NUMERO DE VARIABLES CON LA CANTIDAD DE ELEMENTOS
print(v1)
print(v2)
print(v3)
# TRUCO PARA EVITAR PUNTO ANTERIOR 
v1, v2, *v = t3 # asterisco completa 
print("v1=", v1,"v2=", v2,"v=", v)
x, _, z = t2 # barra baja ignora 
print (x, z)

# OPERACIONES CON TUPLAS
print (t1 + t2) # Combinar 
print (t3 * 2) # Repetir 
print (len(t1))

# BUCLES 
for elem in t1:
    print (elem)

# ZIP 
items1 = ["a", "b", "c"]
items2 = [1, 2, 3]
items = zip(items1, items2) # "Zip de tuplas"
print (items, type(items))
print(dict(items)) # Zip a diccionario 
items = zip(items1, items2) 
print(tuple(items)) # Zip a tupla 

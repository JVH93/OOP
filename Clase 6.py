""" ESTRUCTURAS DE DATOS"""
# DICCIONARIOS
""" Conjunto de elementos no ordenados escritos entre llaves {}. Constan de claves UNICAS y valores. Asignación.- clave: valor"""
dic = {"José": 28, "Pedro": 30}
print(dic)
# Acceder a elementos.
print(dic["Pedro"])
dicc = {"Nombres": ["María", "Jesús", "Brayan"],
        "Edades": [41, 60, 30]}
print(dicc["Nombres"])
print(dicc.keys()) # Imprimir claves 
print(dicc.values()) # Imprimir valores 
dicc["Nombres"] = ["Isabel", "Kimberly", "Floren"] # Cambio por clave
dicc["Edades"][0] = 25 # Cambio por valor
print(dicc)
""" RETO: HAZ QUE EL USUARIO RELLENE UN DICCIONARIO CON LOS DATOS DE UNA FACTURA (NOMBRE, APELLIDOS, RFC, TOTAL)"""
"""
cliente = {}
cliente["name"] = str(input("Introduzca el nombre del cliente: "))
cliente["surname"] = str(input("Introduzca los apellidos del cliente: "))
cliente["rfc"] = str(input("Introduzca el RFC del cliente: "))
cliente["total"] = float(input("Introduzca el total a pagar del cliente: "))
print (cliente)
"""

print(len(dicc)) # Tamaño del diccionario
# Bucles con diccionarios
for key in dicc:
    print(key, ":", dicc[key])
# Listas en diccionarios 
dicc = {"Nombres": ["María", "Jesús", "Brayan"],
        "Edades": [41, 60, 30]}
# Diccionarios en listas
lista = [dicc, dicc]
print(lista)
# Aplicación
"""
asignaturas = {"Mate": [],
               "Historia": [],
               "Geografía": [],
               "Computación": []}
for key in asignaturas:
    print ("---", key, "---")
    for i in range(2):
        asignaturas[key].append(int(input(f"Calificación del semestre {i+1}: ")))
print ("\nCalificaciones")
for key, value in asignaturas.items():
    print(key, ":", sum(value)/len(value))
"""

# Métodos para diccionarios 
dicc.clear() # Vaciar 
print(dicc)
dicc = {"Nombres": ["María", "Jesús", "Brayan"],
        "Edades": [41, 60, 30]}
diccopia = dicc.copy() # Copiar
print(diccopia)
dicrell = dict.fromkeys(["a", "b", "c"],[1, 2, 3, 4, 5]) #Rellenar
print(dicrell)
print(dicrell.get("a")) # Mejor que el otro método, ya que regresa none
dic2 = {"a": 100, "b": 99}
dicrell.update(dic2)
print(dicrell)
# Método dict()
l = [["x", 1], ["y",2]] # Con lista de dos valores 
print(dict(l))
print (dict(x = 0, y = 1, z = 2)) # Directo

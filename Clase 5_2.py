"""Imprimir"""

# Imprimir todos los elementos de una lista por indice
pa = ["México", "Brasil", "China", "España", "Rusia"]
for i in range(len(pa)):
    print(pa[i])
# Método dos 
for elem in pa:
    print(pa)    

    
"""Operaciones con listas"""

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1+l2) # Concatenar.
print(l1*2) # Repetir (Iniciar un vector).
ln = [0, 1, 0, 1, 2, 1, 0, 0, 5]
print (ln.count(0)) # Contar apariciones de un elemento.
ln.extend([1, 0]) # Extender lista (Aquí podemos añadir más).
print(ln) 
ln.extend(range(3,8)) # Incluso un rango completo. 
print(ln)
print(ln.index(2)) # Obtener primera posición de elemento. 
print(ln.pop()) # Borrar el último elemento de la lista. 
print(ln)
ln = [0, 1, 0, 1, 2, 1, 0, 0, 5]
ln.remove(1) # Elimina la primera aparicion de un elemento.
ln.reverse() # Poner lista inversamente.
print(ln) 
ln.sort() # Ordenar elementos mezclados de menor a mayor.
print(ln)
ln.sort(reverse=True) # Ordenar elementos mezclados de mayor a menor.
print(ln)
"""RETO: PREGUNTAR A USUARIO QUE ELEMENTO QUIERE ELIMINAR DE UNA LISTA DADA Y DEVOLVER LISTA ACTUALIZADA CON PRINT"""
"""
l = ["Pedro", "Pablo", "Juan", "Panfilo", "Justino"]
n = input(f"De esta lista decide que elemento eliminar: {l}\n")
if n in l:
    l.remove(n)
print("La nueva lista es:",l)
"""


"""Convertir"""

lr = list (range(0, 100, 10)) # Crear lista con rango 
print(lr)

"""Listas anidadas"""

la = [
    ["N0_E0", "N0_E1", "N0_E1"],
    ["N1_E0", "N1_E1", "N1_E2", ["N1_S3_E0", "N1_S3_E1"]],
    "N3_E0"]
print (la)
print(la[0][1]) # Obtener elemento de lista anidada
print(la[1][3][1]) 



# MATRICES 
"""Tipo de listas anidadas, donde cada lista 'm' tiene el mismo número de elementos 'n'"""

"""Definiciones"""

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("Primer elemento:",matriz[0][0]) # Accedemos por fila-columna
print("Elemento del medio:", matriz[1][1])
print("Elemento final:", matriz[2][2])
# Mostrar matriz en forma de tabla 
for filas in matriz:
    print (filas)

# Corrimiento de elementos en matriz 
for filas in matriz:
    for columnas in filas:
        print(columnas)

        
"""Operaciones con matrices"""

A = [[1, 0, -3],
     [2, 0, 1],
     [-1, -1, 0]]
B = [[-1, -2, 0],
     [-2, 3, 0],
     [0, 0, -3]]
# SUMA
m = len(A)
n = len(A[0])
# Evaluar que sean de la misma dimensión
if len(A) == len(B) and len(A[0]) == len(B[0]):
    C = [] # Generar matriz de resultado 
    for i in range(m): # Para cada fila 
        C.append([]) # Añadir al final espacio para calculo
        for j in range(n): # Para cada columna (elemento)
            C[i].append(A[i][j] + B[i][j]) # Hacer operacion en fila
    print(C)
else:
    print("Las matrices deben tener la misma dimensión")
for filas in C:
    print (filas) 
# PRODUCTO
A = [[1, 0, -3, 2], 
     [2, 0, 1, 1],
     [-1, 0, -1, 0]]
B = [[-1, -2, 0], 
     [-2, 3, 0], 
     [0, 0, -3], 
     [1, 1, -1]]
m, n, p = len(A), len(B), len(B[0]) # Obtener dimensiones 
C = [] # Matriz resultado
for i in range(m): # Para cada fila de A
  C.append([]) # Crear espacio
  print(f"i = {i}", C) # "Mirar procedimiento"
  for j in range(p): # Por cada elemento en B
    elemento = 0 # Creación    
    for k in range(n): # Por cada elemento en A
      elemento = elemento + A[i][k] * B[k][j] # Calculo según álgebra
      print (f"k = {k}", C)
    C[i].append(elemento)  
    print(f"j = {j}", C) 
for filas in C:
    print (filas) 
    
    
    
"""Libreria Numpy"""

import numpy as np 
# En el cmd de windows: pip install numpy
# Consulta: https://numpy.org/ o https://pypi.org/project/numpy/
A = np.empty((2, 3)) # Crear matriz vacia 2x3
print(A)
B = np.empty_like(A) # Definir matriz a partir de otra 
print(B)
C = np.zeros((4, 5)) # Crear matriz nula (con like igual que empty)
print(C)
D = np.ones((1,3)) # Crear matriz de unos (con like igual que empty)
print(D)
M = np.matrix([[1, 2, 3], # Creación con listas
          [4, 5, 6],
          [7, 8, 9]])
print(M, "\nEl tamaño es:\n", M.shape) 
# Operaciones 
A = np.matrix([[1, 0, -3],
               [2, 0, 1],
               [-1, -1, 0]])
B = np.matrix([[-1, -2, 0],
               [-2, 3, 0],
               [0, 0, -3]])
# Suma 
print(A + B)
# Producto
print(A.dot(B))

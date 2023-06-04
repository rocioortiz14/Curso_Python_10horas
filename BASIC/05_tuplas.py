# Definición

my_tuple = tuple()  # Creación de una tupla vacía utilizando la función tuple()
my_other_tuple = ()  # Creación de una tupla vacía utilizando paréntesis

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")  # Creación de una tupla con elementos
my_other_tuple = (35, 60, 30)

print(my_tuple)  # Imprime la tupla: (35, 1.77, 'Brais', 'Moure', 'Brais')
print(type(my_tuple))  # Imprime el tipo de la variable my_tuple: <class 'tuple'>

# Acceso a elementos y búsqueda

print(my_tuple[0])  # Acceso al primer elemento de la tupla: 35
print(my_tuple[-1])  # Acceso al último elemento de la tupla: 'Brais'
# print(my_tuple[4])  # IndexError: índice fuera de rango
# print(my_tuple[-6])  # IndexError: índice fuera de rango

print(my_tuple.count("Brais"))  # Cuenta el número de apariciones del elemento "Brais" en la tupla: 2
print(my_tuple.index("Moure"))  # Devuelve el índice de la primera aparición del elemento "Moure" en la tupla: 3
print(my_tuple.index("Brais"))  # Devuelve el índice de la primera aparición del elemento "Brais" en la tupla: 2

# my_tuple[1] = 1.80  # TypeError: las tuplas son inmutables, no se pueden modificar sus elementos

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple  # Concatenación de tuplas
print(my_sum_tuple)  # Imprime la tupla resultante: (35, 1.77, 'Brais', 'Moure', 'Brais', 35, 60, 30)

# Subtuplas

print(my_sum_tuple[3:6])  # Obtiene una subtupla que contiene los elementos en las posiciones 3, 4 y 5: ('Moure', 'Brais', 35)

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)  # Convierte la tupla en una lista mutable utilizando la función list()
print(type(my_tuple))  # Imprime el tipo de la variable my_tuple: <class 'list'>

my_tuple[4] = "MoureDev"  # Modifica un elemento en una posición específica de la lista
my_tuple.insert(1, "Azul")  # Inserta un elemento en una posición específica de la lista
my_tuple = tuple(my_tuple)  # Convierte la lista nuevamente en una tupla utilizando la función tuple()
print(my_tuple)  # Imprime la tupla actualizada: (35, 'Azul', 1.77, 'Brais', 'MoureDev', 'Brais')
print(type(my_tuple))  # Imprime el tipo de la variable my_tuple: <class 'tuple'>

# Eliminación

# del my_tuple[2]  # TypeError: las tuplas no admiten eliminación de elementos

del my_tuple  # Elimina la tupla por completo
# print(my_tuple)  # NameError: la variable my_tuple ya no existe

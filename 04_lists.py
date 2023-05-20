### Lists ###

# Definición

my_list = list()  # Creación de una lista vacía utilizando la función list()
my_other_list = []  # Creación de una lista vacía utilizando corchetes

print(len(my_list))  # Imprime la longitud de la lista my_list: 0

my_list = [35, 24, 62, 52, 30, 30, 17]  # Creación de una lista con elementos

print(my_list)  # Imprime la lista my_list: [35, 24, 62, 52, 30, 30, 17]
print(len(my_list))  # Imprime la longitud de la lista my_list: 7

my_other_list = [35, 1.77, "Brais", "Moure"]  # Creación de una lista con diferentes tipos de elementos

print(type(my_list))  # Imprime el tipo de la variable my_list: <class 'list'>
print(type(my_other_list))  # Imprime el tipo de la variable my_other_list: <class 'list'>

# Acceso a elementos y búsqueda

print(my_other_list[0])  # Acceso al primer elemento de la lista: 35
print(my_other_list[1])  # Acceso al segundo elemento de la lista: 1.77
print(my_other_list[-1])  # Acceso al último elemento de la lista: 'Moure'
print(my_other_list[-4])  # Acceso al cuarto elemento de la lista: 35
print(my_list.count(30))  # Cuenta el número de apariciones del elemento 30 en la lista: 2

print(my_other_list.index("Brais"))  # Devuelve el índice de la primera aparición del elemento "Brais" en la lista: 2

age, height, name, surname = my_other_list  # Desempaque de elementos de la lista en variables separadas
print(name)  # Imprime el valor de la variable name: 'Brais'

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]  # Desempaque de elementos seleccionados en variables separadas
print(age)  # Imprime el valor de la variable age: 35

# Concatenación

print(my_list + my_other_list)  # Concatenación de listas: [35, 24, 62, 52, 30, 30, 17, 35, 1.77, 'Brais', 'Moure']
#print(my_list - my_other_list) # No se puede realizar la operación de resta (-) entre listas

# Creación, inserción, actualización y eliminación

my_other_list.append("MoureDev")  # Agrega un elemento al final de la lista
print(my_other_list)  # Imprime la lista actualizada: [35, 1.77, 'Brais', 'Moure', 'MoureDev']

my_other_list.insert(1, "Rojo")  # Inserta un elemento en una posición específica de la lista
print(my_other_list)  # Imprime la lista actualizada: [35, 'Rojo', 1.77, 'Brais', 'Moure', 'MoureDev']

my_other_list[1] = "Azul"  # Actualiza el valor de un elemento en una posición específica de la lista
print(my_other_list)  # Imprime la lista actualizada: [35, 'Azul', 1.77, 'Brais', 'Moure', 'MoureDev']

my_other_list.remove("Azul")  # Elimina la primera aparición del elemento "Azul" de la lista
print(my_other_list)  # Imprime la lista actualizada: [35, 1.77, 'Brais', 'Moure', 'MoureDev']

my_list.remove(30)  # Elimina la primera aparición del elemento 30 de la lista
print(my_list)  # Imprime la lista actualizada: [35, 24, 62, 52, 30, 17]

print(my_list.pop())  # Elimina y devuelve el último elemento de la lista: 17
print(my_list)  # Imprime la lista actualizada: [35, 24, 62, 52, 30]

my_pop_element = my_list.pop(2)  # Elimina y devuelve el elemento en la posición 2 de la lista: 62
print(my_pop_element)  # Imprime el valor del elemento eliminado: 62
print(my_list)  # Imprime la lista actualizada: [35, 24, 52, 30]

del my_list[2]  # Elimina el elemento en la posición 2 de la lista
print(my_list)  # Imprime la lista actualizada: [35, 24, 30]


# Operaciones con listas

my_new_list = my_list.copy()  # Crea una copia de la lista my_list

my_list.clear()  # Elimina todos los elementos de la lista
print(my_list)  # Imprime la lista vacía: []

print(my_new_list)  # Imprime la copia de la lista original: [35, 24, 30]

my_new_list.reverse()  # Invierte el orden de los elementos en la lista
print(my_new_list)  # Imprime la lista invertida: [30, 24, 35]

my_new_list.sort()  # Ordena los elementos de la lista en orden ascendente
print(my_new_list)  # Imprime la lista ordenada: [24, 30, 35]

print(my_new_list[1:3])  # Obtiene una sublista que contiene los elementos en las posiciones 1 y 2: [30, 35]

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo

my_list = "Hola Python"  # Asigna una cadena de texto a la variable my_list
print(my_list)  # Imprime la cadena de texto: "Hola Python"
print(type(my_list))  # Imprime el tipo de la variable my_list: <class 'str'>

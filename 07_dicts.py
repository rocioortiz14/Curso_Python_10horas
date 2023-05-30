### Dictionaries ###

# Definición
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# Se crea un diccionario vacío utilizando el constructor dict(), y se crea un diccionario vacío utilizando las llaves {}.
# Se imprime el tipo de ambos, mostrando que my_dict y my_other_dict son diccionarios.

my_other_dict = {"Nombre": "Brais",
                 "Apellido": "Moure", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

# my_other_dict se redefine como un diccionario con claves "Nombre", "Apellido", "Edad" y 1, y sus respectivos valores.
# my_dict se redefine como un diccionario con claves "Nombre", "Apellido", "Edad", "Lenguajes" y 1, y sus respectivos valores.
# El valor asociado con la clave "Lenguajes" es un conjunto.

print(my_other_dict)
print(my_dict)

# Se imprime el contenido de los diccionarios my_other_dict y my_dict.

print(len(my_other_dict))
print(len(my_dict))

# Se imprime la longitud de los diccionarios, es decir, el número de pares clave-valor en cada uno.

# Búsqueda
print(my_dict[1])
print(my_dict["Nombre"])

# Se accede a los valores en los diccionarios utilizando las claves.
# Se imprime el valor asociado con la clave 1 y la clave "Nombre" en my_dict.

print("Moure" in my_dict)
print("Apellido" in my_dict)

# Se realiza la búsqueda de claves en los diccionarios utilizando el operador in.
# La primera búsqueda devuelve False porque "Moure" no es una clave en my_dict,
# mientras que la segunda búsqueda devuelve True porque "Apellido" es una clave en my_dict.

# Inserción
my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

# Se inserta un nuevo par clave-valor en my_dict utilizando la sintaxis de asignación.
# La clave "Calle" se asocia con el valor "Calle MoureDev".
# Se imprime el diccionario actualizado.

# Actualización
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Se actualiza el valor asociado con la clave "Nombre" en my_dict.
# Se imprime el nuevo valor asociado con la clave "Nombre".

# Eliminación
del my_dict["Calle"]
print(my_dict)

# Se elimina el par clave-valor con la clave "Calle" en my_dict utilizando la declaración del.
# Se imprime el diccionario actualizado.

# Otras operaciones
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

# Se utilizan los métodos items(), keys() y values() para obtener vistas de los pares clave-valor, claves y valores, respectivamente, en my_dict.
# Se imprimen estas vistas.

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print((my_new_dict))

# Se utiliza el método fromkeys() para crear nuevos diccionarios utilizando una secuencia de claves.
# En cada caso, se imprime el diccionario resultante.
# El último caso también se asigna un valor "MoureDev" a todas las claves utilizando el segundo argumento del método.

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())

# Se asigna la vista de los valores del diccionario a la variable my_values.
# Se imprime el tipo de my_values y luego se imprime la vista de los valores.

print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))

# Se utilizan funciones y conversiones para obtener listas, tuplas y conjuntos de los valores o claves del diccionario,
# y se imprimen los resultados.

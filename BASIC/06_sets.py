### Sets ###

# Definición
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

# Se crea un conjunto vacío utilizando el constructor set(), y se crea un diccionario vacío utilizando las llaves {}.
# Se imprime el tipo de ambos, mostrando que my_set es un conjunto y my_other_set es un diccionario.

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))

# my_other_set se redefine como un conjunto que contiene los elementos "Brais", "Moure" y 35.
# Se imprime el tipo del conjunto, que es un conjunto.

print(len(my_other_set))

# Se imprime la longitud del conjunto my_other_set, es decir, el número de elementos en el conjunto.

# Inserción
my_other_set.add("MoureDev")

print(my_other_set)  # Un set no es una estructura ordenada

# Se agrega el elemento "MoureDev" al conjunto utilizando el método add().
# Se imprime el conjunto, mostrando que los conjuntos no mantienen un orden específico.

my_other_set.add("MoureDev")  # Un set no admite repetidos

print(my_other_set)

# Se intenta agregar nuevamente el elemento "MoureDev", pero como los conjuntos no permiten elementos duplicados,
# no se realiza ninguna acción y el conjunto permanece igual.

# Búsqueda
print("Moure" in my_other_set)
print("Mouri" in my_other_set)

# Se realiza la búsqueda de los elementos "Moure" y "Mouri" en el conjunto utilizando el operador in.
# La primera búsqueda devuelve True porque el elemento "Moure" está presente en el conjunto,
# mientras que la segunda búsqueda devuelve False porque el elemento "Mouri" no está presente.

# Eliminación
my_other_set.remove("Moure")
print(my_other_set)

# Se elimina el elemento "Moure" del conjunto utilizando el método remove().
# El conjunto se imprime después de la eliminación, mostrando que el elemento ya no está presente.

my_other_set.clear()
print(len(my_other_set))

# Se utiliza el método clear() para eliminar todos los elementos del conjunto.
# Se imprime la longitud del conjunto después de la eliminación, que es 0.

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Se elimina la variable my_other_set utilizando la declaración del.
# Al intentar imprimir my_other_set después de eliminarlo, se produce un error de NameError porque la variable ya no está definida.

# Transformación
my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

# my_set se redefine como un conjunto que contiene los elementos "Brais", "Moure" y 35.
# Luego, se convierte el conjunto en una lista utilizando la función list().
# Se imprime la lista resultante y se accede al primer elemento de la lista.

my_other_set = {"Kotlin", "Swift", "Python"}

# Se crea un nuevo conjunto llamado my_other_set con elementos "Kotlin", "Swift" y "Python".

# Otras operaciones
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))

# Se realiza una serie de operaciones utilizando conjuntos.
# Se crea my_new_set como la unión de my_set y my_other_set.
# Luego, se realiza la unión de my_new_set consigo mismo, my_set y un conjunto {"JavaScript", "C#"}.
# Se imprime el resultado de esta unión.
# A continuación, se encuentra la diferencia entre my_new_set y my_set utilizando el método difference().
# Se imprime el resultado de esta diferencia.

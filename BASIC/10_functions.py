### Functions ###

# Definición

def my_function():
    print("Esto es una función")


my_function()
my_function()
my_function()

# Se define una función llamada my_function sin parámetros.
# La función imprime el mensaje "Esto es una función".
# Luego, se llama a la función tres veces, lo que resulta en la impresión del mensaje tres veces.

# Función con parámetros de entrada/argumentos

def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

# Se define una función llamada sum_two_values que toma dos parámetros de entrada: first_value y second_value.
# La función imprime la suma de los dos valores.
# Luego, se llama a la función varias veces con diferentes argumentos para probar su funcionamiento.

# Función con parámetros de entrada/argumentos y retorno

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Se define una función llamada sum_two_values_with_return que toma dos parámetros de entrada: first_value y second_value.
# La función calcula la suma de los dos valores y la guarda en la variable my_sum.
# Luego, la función retorna el valor de my_sum.
# Se llama a la función sum_two_values_with_return varias veces y se guarda el resultado en la variable my_result.
# Finalmente, se imprime el valor de my_result.

# Función con parámetros de entrada/argumentos por clave

def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Moure", name="Brais")

# Se define una función llamada print_name que toma dos parámetros de entrada: name y surname.
# La función imprime el nombre y el apellido concatenados.
# Se llama a la función print_name especificando los argumentos por clave, lo que permite cambiar el orden de los argumentos.

# Función con parámetros de entrada/argumentos por defecto

def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "MoureDev")

# Se define una función llamada print_name_with_default que toma tres parámetros de entrada: name, surname y alias.
# El parámetro alias tiene un valor por defecto de "Sin alias".
# La función imprime el nombre, el apellido y el alias concatenados.
# Se llama a la función print_name_with_default en dos ocasiones, una vez sin especificar el valor de alias (utilizando el valor por defecto)
# y otra vez especificando el valor de alias como "MoureDev".

# Función con parámetros de entrada/argumentos arbitrarios

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")

# Se define una función llamada print_upper_texts que toma un número arbitrario de parámetros de entrada.
# Los parámetros de entrada se almacenan en la variable texts como una tupla.
# La función imprime el tipo de texts y luego itera sobre los elementos de texts, imprimiendo cada elemento en mayúsculas.
# Se llama a la función print_upper_texts dos veces, una vez con tres argumentos y otra vez con un solo argumento.

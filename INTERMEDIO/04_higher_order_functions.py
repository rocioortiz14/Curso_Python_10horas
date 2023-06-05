### Higher Order Functions ###
from functools import reduce

# Definición de una función para sumar 1 a un valor
def sum_one(value):
    return value + 1

# Definición de una función para sumar 5 a un valor
def sum_five(value):
    return value + 5

# Definición de una función que recibe dos valores y una función de suma, y retorna la suma de los dos valores utilizando la función de suma proporcionada
def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

# Llamar a la función sum_two_values_and_add_value con los valores 5, 2 y la función sum_one, e imprimir el resultado
print(sum_two_values_and_add_value(5, 2, sum_one))
# Llamar a la función sum_two_values_and_add_value con los valores 5, 2 y la función sum_five, e imprimir el resultado
print(sum_two_values_and_add_value(5, 2, sum_five))


### Closures ###

# Definición de una función que retorna una función interna que suma un valor original más el valor proporcionado
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

# Crear un closure llamando a la función sum_ten con el valor 1
add_closure = sum_ten(1)
# Llamar a la función add_closure con el valor 5 e imprimir el resultado
print(add_closure(5))
# Llamar directamente a la función sum_ten con el valor 5 y luego llamar a la función interna con el valor 1, e imprimir el resultado
print((sum_ten(5))(1))


### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# Map

# Definición de una función para multiplicar un número por 2
def multiply_two(number):
    return number * 2

# Utilizar la función map para aplicar la función multiply_two a cada elemento de la lista numbers y convertir los resultados en una lista
print(list(map(multiply_two, numbers)))
# Utilizar la función map junto con una función lambda para multiplicar cada elemento de la lista numbers por 2 y convertir los resultados en una lista
print(list(map(lambda number: number * 2, numbers)))

# Filter

# Definición de una función para filtrar los números mayores que 10
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

# Utilizar la función filter para aplicar la función filter_greater_than_ten a cada elemento de la lista numbers y convertir los resultados en una lista
print(list(filter(filter_greater_than_ten, numbers)))
# Utilizar la función filter junto con una función lambda para filtrar los números mayores que 10 de la lista numbers y convertir los resultados en una lista
print(list(filter(lambda number: number > 10, numbers)))

# Reduce

# Definición de una función para sumar dos valores
def sum_two_values(first_value, second_value):
    return first_value + second_value

# Utilizar la función reduce para aplicar la función sum_two_values a los elementos de la lista numbers y obtener el resultado acumulativo
print(reduce(sum_two_values, numbers))



### Lambdas ###

# Definición de una función lambda para sumar dos valores
sum_two_values = lambda first_value, second_value: first_value + second_value

# Llamar a la función lambda sum_two_values con argumentos 2 y 4 e imprimir el resultado
print(sum_two_values(2, 4))


# Definición de una función lambda para multiplicar dos valores y restar 3
multiply_values = lambda first_value, second_value: first_value * second_value - 3

# Llamar a la función lambda multiply_values con argumentos 2 y 4 e imprimir el resultado
print(multiply_values(2, 4))


# Definición de una función que retorna una función lambda para sumar tres valores
def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

# Llamar a la función sum_three_values con argumento 5, luego llamar a la función lambda resultante con argumentos 2 y 4, e imprimir el resultado
print(sum_three_values(5)(2, 4))

### List Comprehension ###

# Creamos una lista original
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

# Creamos un rango de números del 0 al 7
my_range = range(8)
print(list(my_range))

# Definimos una nueva lista usando List Comprehension, donde cada elemento es el número original más 1
my_list = [i + 1 for i in range(8)]
print(my_list)

# Definimos una nueva lista usando List Comprehension, donde cada elemento es el número original multiplicado por 2
my_list = [i * 2 for i in range(8)]
print(my_list)

# Definimos una nueva lista usando List Comprehension, donde cada elemento es el número original elevado al cuadrado
my_list = [i * i for i in range(8)]
print(my_list)

# Definimos una función que suma 5 a un número dado
def sum_five(number):
    return number + 5

# Definimos una nueva lista usando List Comprehension, donde cada elemento es el resultado de aplicar la función sum_five al número original
my_list = [sum_five(i) for i in range(8)]
print(my_list)

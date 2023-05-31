### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

# Se define una variable my_condition con un valor inicial de 0.
# Luego se utiliza el bucle while para imprimir el valor de my_condition y aumentarlo en 2 en cada iteración.
# El bucle se ejecuta mientras my_condition sea menor que 10.
# Después de que la condición del bucle no se cumpla, se ejecuta el bloque else (opcional) y se imprime el mensaje.

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

# Se utiliza otro bucle while con una nueva condición.
# En cada iteración, se incrementa my_condition en 1.
# Si my_condition es igual a 15, se imprime un mensaje y se utiliza la instrucción break para salir del bucle.
# Después de la instrucción break, se imprime "La ejecución continúa".

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

# Se utiliza un bucle for para recorrer los elementos de la lista my_list.
# En cada iteración, se asigna un elemento de la lista a la variable element y se imprime su valor.

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)

# Se utiliza un bucle for para recorrer los elementos de la tupla my_tuple.
# En cada iteración, se asigna un elemento de la tupla a la variable element y se imprime su valor.

my_set = {"Brais", "Moure", 35}

for element in my_set:
    print(element)

# Se utiliza un bucle for para recorrer los elementos del conjunto my_set.
# En cada iteración, se asigna un elemento del conjunto a la variable element y se imprime su valor.

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bluce for para diccionario ha finalizado")

# Se utiliza un bucle for para recorrer las claves del diccionario my_dict.
# En cada iteración, se asigna una clave del diccionario a la variable element y se imprime su valor.
# Si la clave es igual a "Edad", se utiliza la instrucción break para salir del bucle.
# Si el bucle se completa sin ejecutar la instrucción break, se ejecuta el bloque else (opcional).

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")

# Se utiliza un bucle for similar al anterior, pero en lugar de utilizar la instrucción break,
# se utiliza la instrucción continue para saltar a la siguiente iteración.
# En este caso, si la clave es igual a "Edad", se omite la impresión de "Se ejecuta".
# Después de que el bucle se complete sin ejecutar la instrucción break, se ejecuta el bloque else (opcional).


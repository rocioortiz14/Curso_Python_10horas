### Conditionals ###

# if

my_condition = False

if my_condition:  # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")

# Se define una variable my_condition como False.
# Luego se utiliza la declaración if para comprobar si la condición es verdadera.
# Como my_condition es False, la condición no se cumple y no se ejecuta la instrucción print.

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

# Se redefine my_condition como el resultado de la operación 5 * 5, que es 25.
# Luego se utiliza la declaración if para comprobar si la condición es verdadera.
# Como my_condition no es igual a 10, la condición no se cumple y no se ejecuta la instrucción print.

# if, elif, else

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")

# Se utiliza la declaración if, elif y else para realizar comprobaciones condicionales múltiples.
# Si la primera condición (my_condition > 10 y my_condition < 20) no se cumple, se pasa a la siguiente condición elif.
# Si la segunda condición (my_condition == 25) se cumple, se ejecuta la instrucción print correspondiente.
# De lo contrario, si ninguna de las condiciones anteriores se cumple, se ejecuta la instrucción en el bloque else.
# Después de la ejecución del bloque if-elif-else, se imprime "La ejecución continúa".

# Condicional con inspección de valor

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")

# Se define una variable my_string como una cadena vacía ("").
# Se utiliza la declaración if para comprobar si la cadena no tiene contenido.
# Como my_string está vacía, la condición not my_string se cumple y se ejecuta la instrucción print correspondiente.
# A continuación, se utiliza otra declaración if para comprobar si my_string es igual a otra cadena específica.
# Como my_string no coincide con la cadena especificada, la condición no se cumple y no se ejecuta la instrucción print.

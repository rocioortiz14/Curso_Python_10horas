### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# Excepción base: try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

# Se intenta sumar numberOne y numberTwo.
# Si se produce una excepción durante la ejecución del bloque try, se captura la excepción y se ejecuta el bloque except.
# En este caso, dado que numberTwo es un valor de tipo cadena en lugar de un número, se producirá un TypeError y se ejecutará el bloque except.

# Flujo completo de una excepción: try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución continúa correctamente")
finally:
    print("La ejecución continúa")

# El bloque try se ejecuta normalmente.
# Si no se produce ninguna excepción, se ejecuta el bloque else.
# Luego, se ejecuta el bloque finally, independientemente de si se produjo una excepción o no.

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Se intenta sumar numberOne y numberTwo.
# Si se produce una excepción de tipo ValueError, se ejecuta el primer bloque except.
# Si se produce una excepción de tipo TypeError, se ejecuta el segundo bloque except.

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)

# Se intenta sumar numberOne y numberTwo.
# Si se produce una excepción de tipo ValueError, se captura la excepción en la variable 'error' y se imprime.
# Si se produce una excepción de cualquier otro tipo, se captura la excepción en la variable 'my_random_error_name' y se imprime.

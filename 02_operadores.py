# Avance 20/05/2023

### Operadores Aritméticos ###

print(3 + 4)    # Suma: 3 + 4 = 7
print(3 - 4)    # Resta: 3 - 4 = -1
print(3 * 4)    # Multiplicación: 3 * 4 = 12
print(3 / 4)    # División: 3 / 4 = 0.75
print(10 % 3)   # Módulo (resto de la división): 10 % 3 = 1
print(10 // 3)  # División entera: 10 // 3 = 3
print(2 ** 3)   # Potencia: 2 ^ 3 = 8
print(2 ** 3 + 3 - 7 / 1 // 4)  # Expresión combinada: 8 + 3 - 7 / 1 // 4 = 10.0

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?")  # Concatenación de cadenas: "Hola Python ¿Qué tal?"
print("Hola " + str(5))  # Conversión de entero a cadena: "Hola 5"


# Operaciones mixtas
print("Hola " * 5)  # Repetición de cadena: "Hola Hola Hola Hola Hola "
print("Hola " * (2 ** 3))  # Repetición de cadena con expresión: "Hola Hola Hola Hola Hola Hola Hola Hola "

my_float = 2.5 * 2
print("Hola " * int(my_float))  # Repetición de cadena con número convertido a entero: "Hola Hola Hola Hola "


### Operadores Comparativos ###

# Operaciones con enteros

print(3 > 4)   # Mayor que: False
print(3 < 4)   # Menor que: True
print(3 >= 4)  # Mayor o igual que: False
print(4 <= 4)  # Menor o igual que: True
print(3 == 4)  # Igualdad: False
print(3 != 4)  # Desigualdad: True


# Operaciones con cadenas de texto
print("Hola" > "Python")  # Comparación de cadenas: False
print("Hola" < "Python")  # Comparación de cadenas: True
print("aaaa" >= "abaa")   # Comparación alfabética por ASCII: False
print(len("aaaa") >= len("abaa"))  # Comparación de longitudes de cadenas: False
print("Hola" <= "Python")  # Comparación de cadenas: True
print("Hola" == "Hola")   # Igualdad de cadenas: True
print("Hola" != "Python")  # Desigualdad de cadenas: True

### Operadores Lógicos ###
# Basada en el Álgebra de Boole 
print(3 > 4 and "Hola" > "Python")  # Operador lógico "and": False
print(3 > 4 or "Hola" > "Python")   # Operador lógico "or": True
print(3 < 4 and "Hola" < "Python")  # Operador lógico "and": True
print(3 < 4 or "Hola" > "Python")   # Operador lógico "or": True
print(3 < 4 or ("Hola" > "Python" and 4 == 4))  # Operadores lógicos combinados: True
print(not (3 > 4))  # Negación lógica: True

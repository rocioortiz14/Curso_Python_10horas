### Challenges ###
##retos tomados de https://retosdeprogramacion.com/semanales2023##
"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def fizzbuzz():
    # Itera sobre los números del 1 al 100
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            # Si el número es divisible por 3 y por 5, imprime "fizzbuzz"
            print("fizzbuzz")
        elif index % 3 == 0:
            # Si el número es divisible por 3, imprime "fizz"
            print("fizz")
        elif index % 5 == 0:
            # Si el número es divisible por 5, imprime "buzz"
            print("buzz")
        else:
            # Si no cumple ninguna condición anterior, imprime el número
            print(index)

# Llama a la función fizzbuzz para ejecutarla y ver los resultados en la consola
fizzbuzz()


"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""


def is_anagram(word_one, word_two):
    # Verificar si las palabras son exactamente iguales (no son anagramas)
    if word_one.lower() == word_two.lower():
        return False
    # Verificar si las palabras, después de convertirlas a minúsculas y ordenar sus letras,
    # son iguales (son anagramas)
    return sorted(word_one.lower()) == sorted(word_two.lower())

# Llamar a la función is_anagram y mostrar el resultado en la consola
print(is_anagram("Amor", "Roma"))


"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""


def fibonacci():
    # Inicializar las variables prev y next para los primeros dos números de la sucesión de Fibonacci
    prev = 0
    next = 1

    # Iterar 50 veces para generar los primeros 50 números de la sucesión de Fibonacci
    for index in range(0, 50):
        # Imprimir el valor actual de prev
        print(prev)
        # Calcular el siguiente número de Fibonacci sumando prev y next
        fib = prev + next
        # Actualizar prev y next para el siguiente ciclo de iteración
        prev = next
        next = fib

# Llamar a la función fibonacci para generar los números de Fibonacci y mostrarlos en la consola
fibonacci()


"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""


def is_prime():
    # Iterar sobre los números del 1 al 100
    for number in range(1, 101):
        # Verificar si el número es mayor o igual a 2 (los números primos son mayores o iguales a 2)
        if number >= 2:
            # Variable para verificar si el número es divisible por algún número menor que él
            is_divisible = False
            # Iterar sobre los números desde 2 hasta el número actual - 1
            for index in range(2, number):
                # Verificar si el número es divisible por algún número menor que él
                if number % index == 0:
                    is_divisible = True
                    break
            # Si el número no es divisible por ningún número menor que él, imprimirlo (es primo)
            if not is_divisible:
                print(number)

# Llamar a la función is_prime para imprimir los números primos del 1 al 100
is_prime()


"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""


def reverse(text):
    # Obtener la longitud del texto
    text_len = len(text)
    # Inicializar una cadena vacía para almacenar el texto invertido
    reversed_text = ""
    # Iterar sobre los índices del texto en orden inverso
    for index in range(0, text_len):
        # Concatenar el carácter correspondiente al índice inverso al texto invertido
        reversed_text += text[text_len - index - 1]
    # Retornar el texto invertido
    return reversed_text

# Llamar a la función reverse y mostrar el resultado en la consola
print(reverse("Hola mundo"))

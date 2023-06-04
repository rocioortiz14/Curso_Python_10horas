my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))  # Imprime la longitud de la cadena my_string: 9
print(len(my_other_string))  # Imprime la longitud de la cadena my_other_string: 13
print(my_string + " " + my_other_string)  # Concatena las dos cadenas e imprime el resultado

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)  # Imprime la cadena con un salto de línea

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)  # Imprime la cadena con una tabulación

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)  # Imprime la cadena con caracteres escapados

#Formateo
name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))  # Formateo de cadenas utilizando format()
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))  # Formateo de cadenas utilizando % (placeholder)
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))  # Concatenación de cadenas " el no recomienda haceerlo asi es  mas trabajo"
print(f"Mi nombre es {name} {surname} y mi edad es {age}")  # Formateo de cadenas utilizando f-strings (infereencia de datos)

# Desempaqueado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)  # Imprime el primer carácter de la cadena: 'p'
print(e)  # Imprime el quinto carácter de la cadena: 'o'

# División
language_slice = language[1:3]
print(language_slice)  # Imprime un segmento de la cadena desde el índice 1 hasta el 2: 'yt'

language_slice = language[1:]
print(language_slice)  # Imprime un segmento de la cadena desde el índice 1 hasta el final: 'ython'

language_slice = language[-2]
print(language_slice)  # Imprime el penúltimo carácter de la cadena: 'o'

language_slice = language[0:6:2]
print(language_slice)  # Imprime un segmento de la cadena desde el índice 0 hasta el 5 con paso 2: 'pto'

# Reverse
reversed_language = language[::-1]
print(reversed_language)  # Imprime la cadena invertida: 'nohtyp'

# Funciones del lenguaje
print(language.capitalize())  # Devuelve la cadena con la primera letra en mayúscula: 'Python'
print(language.upper())  # Devuelve la cadena en mayúsculas: 'PYTHON'
print(language.count("t"))  # Cuenta el número de apariciones del carácter 't' en la cadena: 1
print(language.isnumeric())  # Verifica si la cadena es numérica: False
print("1".isnumeric())  # Verifica si la cadena es numérica: True
print(language.lower())  # Devuelve la cadena en minúsculas: 'python'
print(language.lower().isupper())  # Verifica si la cadena en minúsculas está en mayúsculas: False
print(language.startswith("Py"))  # Verifica si la cadena comienza con "Py": True

### Regular Expressions ###

import re

# match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

# match: buscar al comienzo de la cadena
match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

# match: buscar al comienzo de la cadena (no hay coincidencia)
match = re.match("Esta no es la lección", my_other_string)
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

# match: buscar en toda la cadena
print(re.match("Expresiones Regulares", my_string))

# search

# search: buscar en toda la cadena
search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

# findall: encontrar todas las ocurrencias en la cadena
findall = re.findall("lección", my_string, re.I)
print(findall)

# split

# split: dividir la cadena en función de un patrón
print(re.split(":", my_string))

# sub

# sub: reemplazar las coincidencias con una cadena
print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))


### Regular Expressions Patterns ###

# Para aprender y validar expresiones regulares: https://regex101.com

# Ejemplos de patrones de expresiones regulares

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "angelelcielo@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "angelelcielo@gmail.com"
print(re.findall(pattern, email))

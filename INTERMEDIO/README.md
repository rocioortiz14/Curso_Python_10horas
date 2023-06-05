# Curso_Python_7Horas_Intermedio

## Dates
- Se importan las clases necesarias del módulo datetime para trabajar con fechas y tiempos en Python.
- Se utiliza datetime.now() para obtener la fecha y hora actual y se almacena en la variable now.
- La función print_date(date) se define para imprimir los atributos de una fecha, como el año, mes, día, hora, minutos, segundos y marca de tiempo.
- Se llama a la función print_date(now) para imprimir los atributos de la fecha actual.
- Se realiza la resta entre year_2023 y current_date y se obtiene la diferencia en días.
- Se crean dos objetos timedelta con valores de tiempo y se realiza la resta y suma entre ellos, imprimiendo los resultados.

## Comprensión de listas
- Se crea una lista original llamada my_original_list con los números del 0 al 7 y se imprime.
- Se crea un rango de números del 0 al 7 utilizando range(8) y se convierte en una lista utilizando list(my_range). Luego, se imprime esta lista.
- Se define una nueva lista llamada my_list utilizando List Comprehension, donde cada elemento es el número original más 1. Se utiliza la expresión i + 1 y el bucle for i in range(8) para generar la lista. Se imprime esta nueva lista.
- Se define otra nueva lista llamada my_list utilizando List Comprehension, donde cada elemento es el número original multiplicado por 2. Se utiliza la expresión i * 2 y el bucle for i in range(8) para generar la lista. Se imprime esta nueva lista.

## Retos tomados de https://retosdeprogramacion.com/semanales2023


## Lambdas
Funciones anónimas y concisas en Python. Las lambdas se utilizan cuando se necesita una función simple sin definirla formalmente, y son especialmente útiles en combinación con funciones de orden superior o para expresiones breves.
- Se define una función lambda llamada sum_two_values que suma dos valores. Utiliza la sintaxis lambda first_value, second_value: first_value + second_value.
- Se llama a la función lambda sum_two_values con argumentos 2 y 4 utilizando sum_two_values(2, 4), y se imprime el resultado.
- Se define otra función lambda llamada multiply_values que multiplica dos valores y resta 3. Utiliza la sintaxis lambda first_value, second_value: first_value * second_value - 3.
- Se llama a la función lambda multiply_values con argumentos 2 y 4 utilizando multiply_values(2, 4), y se imprime el resultado.
- Se define una función sum_three_values que retorna una función lambda para sumar tres valores. La función interna lambda utiliza first_value, second_value, y el valor recibido como argumento value en la función externa. La sintaxis es lambda first_value, second_value: first_value + second_value + value.

## Funciones de Orden Superior 
- Se define la función sum_one que suma 1 a un valor dado.
- Se define la función sum_five que suma 5 a un valor dado.
- Se define la función sum_two_values_and_add_value que recibe dos valores y una función de suma. Retorna la suma de los dos valores utilizando la función de suma proporcionada.
- Se llama a la función sum_two_values_and_add_value con los valores 5, 2 y la función sum_one, y se imprime el resultado.
- Se llama a la función sum_two_values_and_add_value con los valores 5, 2 y la función sum_five, y se imprime el resultado.

## Tipos de Errores
- Se muestra un ejemplo de SyntaxError al comentar la línea # print "¡Hola comunidad!". Esto se debe a que en Python 3.x, la función print requiere paréntesis para su uso adecuado.
- Se muestra un ejemplo de NameError al intentar imprimir la variable language sin haberla definido previamente. Al comentar la línea language = "Spanish", se produce este error.
- Se muestra un ejemplo de IndexError al intentar acceder a elementos de una lista utilizando índices que están fuera de rango. Al descomentar la línea # print(my_list[5]), se produce este error.
- Se muestra un ejemplo de ModuleNotFoundError al intentar importar un módulo inexistente. Al descomentar la línea # import maths, se produce este error.
- Se muestra un ejemplo de AttributeError al intentar acceder a un atributo inexistente de un módulo. Al descomentar la línea # print(math.PI), se produce este error.
- Otros.

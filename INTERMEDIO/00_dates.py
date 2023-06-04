### Dates ###

# Importamos las clases necesarias del módulo datetime
from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

# Obtenemos la fecha y hora actual
now = datetime.now()

# Definimos una función para imprimir los atributos de una fecha
def print_date(date):
    print(date.year)       # Imprime el año
    print(date.month)      # Imprime el mes
    print(date.day)        # Imprime el día
    print(date.hour)       # Imprime la hora
    print(date.minute)     # Imprime los minutos
    print(date.second)     # Imprime los segundos
    print(date.timestamp())   # Imprime la marca de tiempo en segundos desde el 1 de enero de 1970

# Llamamos a la función print_date para imprimir los atributos de la fecha actual
print_date(now)

# Creamos un objeto datetime para el 1 de enero de 2023
year_2023 = datetime(2023, 1, 1)

# Llamamos a la función print_date para imprimir los atributos del objeto year_2023
print_date(year_2023)

# Creamos un objeto time con la hora 21:06:00
current_time = time(21, 6, 0)

# Imprimimos la hora, minutos y segundos del objeto current_time
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Obtenemos la fecha actual
current_date = date.today()

# Imprimimos el año, mes y día de la fecha actual
print(current_date.year)
print(current_date.month)
print(current_date.day)

# Creamos un objeto date para el 6 de octubre de 2022
current_date = date(2022, 10, 6)

# Imprimimos el año, mes y día del objeto current_date
print(current_date.year)
print(current_date.month)
print(current_date.day)

# Incrementamos el mes del objeto current_date en 1
current_date = date(current_date.year, current_date.month + 1, current_date.day)

# Imprimimos el mes del objeto current_date
print(current_date.month)

# Realizamos la resta entre year_2023 y now para obtener la diferencia
diff = year_2023 - now
print(diff)

# Realizamos la resta entre year_2023 y current_date y obtenemos la diferencia en días
diff = year_2023.date() - current_date
print(diff)

# Creamos dos objetos timedelta con valores de tiempo
start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

# Realizamos la resta entre end_timedelta y start_timedelta
print(end_timedelta - start_timedelta)

# Realizamos la suma entre end_timedelta y start_timedelta
print(end_timedelta + start_timedelta)

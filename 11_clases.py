### Classes ###

# Definición

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Se define una clase llamada MyEmptyPerson que no tiene ninguna definición adicional.
# Se imprime el tipo de la clase MyEmptyPerson y se crea una instancia de la clase MyEmptyPerson.

# Clase con constructor, funciones y propiedades privadas y públicas

class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)

# Se define una clase llamada Person.
# La clase tiene un constructor (__init__) que toma tres parámetros de entrada: name, surname y alias (con un valor por defecto de "Sin alias").
# El constructor inicializa dos propiedades: full_name, que se compone del nombre, apellido y alias, y __name, que es una propiedad privada que almacena solo el nombre.
# La clase también tiene dos métodos: get_name, que retorna el valor de la propiedad privada __name, y walk, que imprime un mensaje indicando que la persona está caminando.
# Se crean instancias de la clase Person y se accede a sus propiedades y métodos utilizando el operador de punto (.).
# Se imprime el valor de la propiedad full_name, se llama al método get_name para obtener el nombre, y se llama al método walk para que la persona camine.
# Luego, se crea otra instancia de la clase Person con un alias diferente y se realiza el mismo conjunto de operaciones.
# También se muestra cómo se puede cambiar el valor de la propiedad full_name directamente.
# Finalmente, se intenta asignar un valor incorrecto (número entero) a la propiedad full_name, lo que muestra que no hay restricciones de tipo en Python.

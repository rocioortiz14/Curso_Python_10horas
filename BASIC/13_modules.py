### Modules ###

from math import pi as PI_VALUE
import math
from mis_Modulos import sumValue, printValue
import mis_Modulos

mis_Modulos.sumValue(5, 3, 1)
mis_Modulos.printValue("Hola Python!")

# Se importa el módulo 'my_module' y se utilizan las funciones 'sumValue' y 'printValue' definidas en ese módulo.

sumValue(5, 3, 1)
printValue("Hola python")

# Se utiliza directamente la función 'sumValue' y 'printValue' del módulo 'my_module', ya que se importaron individualmente.

print(math.pi)
print(math.pow(2, 8))

# Se accede a la constante 'pi' y a la función 'pow' del módulo 'math' utilizando la sintaxis 'math.<nombre>'.

print(PI_VALUE)

# Se imprime el valor de la constante 'pi' importada como 'PI_VALUE' desde el módulo 'math'.

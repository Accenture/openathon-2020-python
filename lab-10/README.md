<p align="center">
    <img src="../resources/header.png">
</p>

# Lab 10 - Generando un flujo de datos

Ahora que ya hemos creado una clase de utilidades que se encarga de extraer los datos vamos a generar un flujo constante de datos para nuestra aplicación. Para ello, vamos a a crear dos estructuras que almacenen los valores de CPU y RAM de manera circular, guardando un máximo de 100 muestras.

Puedes continuar con el código que hayas escrito tu mismo o, si lo prefieres, puedes tomar como punto de partida el código subido en [este mismo laboratorio](./mi-monitor). 

:dart: ¡Este laboratorio empieza fuerte! Debes crear (igual que hemos hecho en [el laboratoio anterior](../lab-09)) un nuevo módulo python, al que llamaremos monitor, y crearemos dentro del módulo un fichero monitor.py donde definiremos una clase Monitor. Si necesitas ayuda, tienes la solución en [el código del siguiente laboratorio](../lab-10/mi-monitor) :wink:

Ahora que ya hemos creado nuestra clase Monitorio, vamos a preparar, en el método \_\_init\_\_.py un espacio para almacenar los valores que vayamos extrayendo y que posteriormente pintaremos en dos gráficos. Para ello, crearemos un array vacío de longitud 100, e inicializaremos todas sus posiciones a 0:

``` python
# ...

class Monitor():

    def __init__(self):

        # ...

        # Definimos una array de 100 posiciones y lo incializamos con los valores a 0
        self.cpu = [0 for _ in range(100)]
```

Este será nuestra fuente de datos para el índice de uso de la CPU. Como veis, con la sentencia _range_, estamos creando una lista de 100 valores y, en la siguiente sentencia, estamos recorriendo toda la lista insertando un 0 en cada posición. Ahora, vamos a instanciar la clase Extractor que hemos creado en el laboratorio anterior, lo que nos permitirá obtener los valores del % de CPU:

``` python
from util import Extractor

class Monitor():

    def __init__(self):

        # ... 
       
        self.extractor = Extractor()

```

El siguiente paso, será crear dos métodos:
 
:one: El primero, se encargará de actualizar la fuente de información con el valor que reciba como parámetro. 

:two: El segundo, se encargará de invocar a nuestra clase de utilidades Extractor, obtener un nuevo valor e invocar al primer método que hemos creado para actualizar el valor sobre la estructura. 

El código para el primer método es el siguiente:

``` python
    def update_cpu_data(self, nuevo_valor):
        # Elimina el primer valor de la lista
        self.cpu = self.cpu[1:]
        
        self.cpu.append(nuevo_valor)   
```

¡Aquí está! Este método nos permitirá añadir un nuevo valor a la lista del índice de uso de la CPU, valor que recibirá como parámetro. Ahora prepararemos la función que se encargue de invocar a esta tras haber obtenido un nuevo valor:

``` python
    def get_cpu_data(self):
        self.update_cpu_data(self.extractor.get_cpu_percent())
```

Ya tenemos listos nuestros dos métodos. Para probarlo, vamos a preparar un pequeño código que ejecutará la actualización de la CPU con el intervalo que especifiquemos como parámetro de entrada:

``` python
# ...
import time

class Monitor:    

   def __init__(self, refresh):
   
        # ...
   
        while True:
            self.get_cpu_data()
            print("CPU: {}".format(self.cpu))
            time.sleep(refresh/1000)
```

Para crear una instancia de Monitor y que se ejecute el código que acabamos de definir, vamos a añadir en nuestro fichero principal \_\_main\_\_.py el siguiente código:

``` python
from monitor import Monitor

try:

    # ...

    Monitor(1000)

except IndexError as index_error:
     print('Por favor, tienes que indicar la velocidad de refresco como parámetro de entrada')
     sys.exit(-1)
except ValueError as value_error:
     print('{} no es un valor válido'.format(refresh))
     print('Por favor, la velocidad de refresco tiene que ser un número entre 100 y 1000')
     sys.exit(-1)
```

:memo: Ejecuta ahora tu código. Si todo ha ido bien, deberías ver cómo se imprimen los valores en la consola, con el intervalo de refresco que hayamos indicado como parámetro de entrada. Ten en cuenta que estamos imprimiendo por consola el array con los valores, por lo que los valores irán "entrando" por la derecha:

```shell script
CPU: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 77.3]
CPU: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 77.3, 56.1]

...

CPU: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 77.3, 56.1, 33.1, 26.4, 29.4, 54.3, 42.0, 32.9, 20.2, 29.7, 22.5, 39.8, 32.8, 12.5, 17.3, 20.3, 23.6, 14.7, 17.7, 26.3, 18.3, 15.8, 21.5, 37.1, 82.6, 81.7, 38.3, 32.0]
```

:dart: ¡Reto! Tenemos que hacer los mismos pasos, pero esta vez para extraer los valores de la memoria RAM, ¿Te ves capaz? Si lo necesitas, en [el código fuente del siguiente laboratorio](../lab-11/mi-monitor) tienes la solución. 

Una vez que ya hemos definido los dos flujos de datos que tendrá nuestra aplicación, es momento de ponerle cara! En el próximo laboratorio vamos a diseñar la interfaz del monitor.

[< Lab 09](../lab-09) | [Lab 11 >](../lab-11)

<p align="center">
    <img src="../resources/header.png">
</p>

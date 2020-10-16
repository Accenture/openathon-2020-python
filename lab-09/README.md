<p align="center">
    <img src="../resources/header.png">
</p>

# Lab 09 - Extrayendo los datos

En este laboratorio vamos a centrarnos en obtener los datos de los que se nutrirá nuestra interfaz gráfica. Para ello, vamos a crear un nuevo módulo Python y aprender a utilizar una librería que nos facilite el acceso a los datos.

Puedes continuar con el código que hayas escrito tu mismo o, si lo prefieres, puedes tomar como punto de partida el código subido en [este mismo laboratorio](./mi-monitor). 

## Instalando librerías a través del fichero requirements.txt

Ya hemos visto como se instala una librería en Python a través del comando pip. Sin embargo, en aplicaciones más estructuradas se suele utilizar una definición de requisitos, lo que sería equivalente a incluir una dependencia con Maven o Gradle en Java. Para ello, crearemos en la raíz de la aplicación un fichero con el nombre requirements.txt con el siguiente contenido:

```
psutil==5.7.0
```

Ahora, si nos situamos en la ruta base del proyecto, podemos ejecutar el comando:

``` shell script
pip install -r requirements.txt
```

De este modo, se instalarán todas las dependencias que necesitemos.

:bulb: El fichero requirements.txt se puede generar de forma automática. A veces, cuando sabemos que funciona una aplicación en un determinado entorno, podemos generar el fichero requirements.txt de forma automática para "congelar" las versiones que se están utilizando en dicho entorno y así garantizar que cuando nos llevemos la aplicación a otra máquina, siga funcionando exactamente igual.Para ello, podemos utilizar el comando pip:

``` shell script
pip freeze > requirements.txt
```

Eso si, ten en cuenta que este comando, incluirá en tu fichero requirements.txt todas las librerías que tienes instaladas, independientemente de que las utilices o no en el proyecto.

## Accediendo a los valores de CPU y RAM

Para hacer una primera prueba de cómo se obtienen los datos, vamos a importar la librería psutil en nuestro \_\_main\_\_.py y vamos a incluir una sentencia que nos permita imprimir en consola el valor actual del uso de la memoria RAM y CPU. Para ello, añadiremos el siguiente código:

``` python
import psutil

# ...

print('CPU (%): {}'.format(psutil.cpu_percent()))
print('RAM (%): {}'.format(psutil.virtual_memory()._asdict()['percent']))
```

:memo: Vamos a ejecutar ahora nuestra aplicación. Deberíamos obtener la siguiente salida:

```
Bienvenido al Openathon VII!
La frecuencia de refresco es 150
CPU (%): 42.9
RAM (%): 93.4
```

:warning: No te preocupes, por ahora, si ves que el valor de CPU sale a 0. Verás más adelante, como este valor se actualizará correctamente.

## Creando un módulo de utilidades

Como comentamos anteriormente, para mantener el código fuente más organizado, vamos a crear un módulo de utilidades. Para ello, en el nivel raíz del proyecto, crearemos una carpeta "util", con el comando:

```shell script
mkdir util
``` 

También puedes utilizar el explorador de archivos si te sientes más cómodo :wink:.

Dentro de esta carpeta, vamos a crear un fichero con el nombre extractor.py. En este fichero, crearemos una clase Extractor con dos métodos: uno para obtener el uso de la CPU y otro para obtener el uso de la memoria RAM.

En primer lugar, crearemos la clase Extractor. A este clase, le añadiremos un método de inicialización, lo que sería el equivalente a un constructor en Java. Esto nos puede ser de ayuda para inicializar ciertas variables o realizar algunas configuraciones pero, en este caso, simplemente incluiremos una línea de log. 

```python

class Extractor:

    def __init__(self):
        print('Se ha creado la clase Extractor')
```  

Ahora, debemos crear un fichero \_\_init\_\_.py donde declaremos las clases que tiene nuestro módulo disponibles para ser importadas.

```python
from util.extractor import Extractor
```

## Añadiendo lógica a nuestro módulo de utilidades

Ahora que ya hemos creado el módulo de utilidades, es hora de añadirle la lógica que necesitará nuestra aplicación. Vamos a crear dos funciones en la clase Extractor que acabamos de definir, que nos permitan obtener los valores del uso de la CPU y de la memoria RAM.

```python
import psutil

# ...

def get_virtual_memory_percent(self):
    return psutil.virtual_memory()._asdict()['percent']
```

## Utilizando nuestra nueva clase de utilidades

Ha llegado la hora de utilizar nuestra clase de utilidades. Para ello, vamos a cambiar la sentencias que añadimos al principio de este laboratorio por las llamadas a nuestra nueva clase de utilidades.

```python
from util import Extractor

# ...

extractor = Extractor()

print('RAM (%): {}'.format(extractor.get_virtual_memory_percent()))
```

:memo: Vamos a ejecutar de nuevo nuestra aplicación. Obtendremos la misma salida que en la ejecución anterior (los valores obtenidos, como son instantáneos, pueden variar).

:dart: ¡Reto! Tenemos que hacer una función que nos permita obtener el % de la CPU utilizada y añadir una sentencia print como la que hemos visto para que se imprima el valor obtenido por consola. ¿Sabrías como hacerlo? En [el código del siguiente laboratorio](../lab-10/mi-monitor) tienes la solución :wink:

[< Lab 08](../lab-08) | [Lab 10 >](../lab-10)

<p align="center">
    <img src="../resources/header.png">
</p>

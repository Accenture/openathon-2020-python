<p align="center">
    <img src="../resources/header.png">
</p>

# Lab 08 - Inicializando la aplicación

Vamos a inicializar nuestra aplicación Python. Lo primero de todo, si no lo estamos ya, será situarnos dentro de la carpeta que hemos creado en el laboratorio anterior, la cuál contiene nuestro entorno de trabajo virtual.

```shell script
cd mi-monitor
```

Ahora, vamos a crear dentro de esta carpeta un fichero con el nombre \_\_main\_\_.py. Este fichero será el punto de entrada a nuestra aplicación, lo que sería el equivalente al método main en Java. Por ahora, escribiremos en este fichero la siguiente línea:

```python
print('Bienvenido al Openathon VII!')
```

## Lanzando una aplicación Python

Ahora que hemos creado nuestro fichero principal, vamos a ejecutarlo y comprobar que se muestra en consola el texto que hemos escrito. Lanzar una aplicación Python puede hacerse de diferentes maneras:

1. Ejecutar Python sobre el fichero \_\_main\_\_.py.
    ```shell script
    python.exe mi-monitor\__main__.py
    ```

2. Ejecutar Python sobre la carpeta del proyecto, Python buscará el fichero \_\_main\_\_.py automáticamente.
    ```shell scriptzip 
    python.exe mi-monitor
    ```
3. Comprimir nuestra aplicación en un zip y ejecutar Python sobre el fichero zip. Para ello, creamos un fichero zip con el contenido de la carpeta mi-monitor y ejecutamos el comando:
     ```shell script
     python.exe mi-monitor.zip
     ```
:memo: Prueba a lanzar la aplicación que acabamos de crear de las tres maneras que acabamos de ver, deberías obtener el mismo resultado.

## Capturando parámetros de entrada

Como comentamos en el laboratorio anterior, una de las funcionalidades de nuestra aplicación, será capturar un parámetro de entrada que nos permita configurar la frecuencia de refresco de los valores des RAM y CPU. Para ello, debemos trabajar con [el módulo sys](https://docs.python.org/3/library/sys.html). 

Vamos a escribir el siguiente código en nuestro fichero \_\_main\_\_.py:

```python
import sys

#...

refresh = sys.argv[1]   
refresh = int(refresh)
print('La frecuencia de refresco es {}'.format(refresh))
```

:memo: Prueba a lanzar la aplicación de una de las tres maneras que hemos visto. Si la ejecutas tal cual lo has hecho antes, obtendrás el siguiente error:

```shell script
IndexError: list index out of range. 
```

Esto es completamente normal, ¿Por qué? Porque estamos intentado acceder al elemento 1 de los parámetros de entrada, pero ¡No estamos incluyéndolo en nuestra invocación!. Para pasar un parámetro de entrada, simplemente tienes que añadir después del nombre del script, el valor que quieras:

```shell script
python.exe mi-monitor 500
```

Deberías ver en la salida de consola lo siguiente:

```shell script
Bienvenido al Openathon VII!
La frecuencia de refresco es 500
```

## Validando la entrada

Vamos a hacer ahora una serie de validaciones de entrada, para asegurar que nos llega el parámetro. Aprovecharemos, también, para definir un rango razonable para ese parámetro. ¡Manos a la obra!

En primer lugar, vamos a definir un bloque try-catch que englobe el código que hemos escrito hasta el momento y vamos a capturar la excepción que vimos antes:

```python
import sys

try:

    # ...

except IndexError as index_error:
    print('Por favor, tienes que indicar la velocidad de refresco como parámetro de entrada')
    sys.exit(-1)
```

:memo: Lanza ahora la aplicación sin indicarle un parámetro de entrada, verás que obtendremos una salida controlada:

```shell script
Bienvenido al Openathon VII!
Por favor, tienes que indicar la velocidad de refresco como parámetro de entrada
```

Una vez nos hemos asegurado que se nos envíe el parámetro de entrada, vamos a validar que tenga un valor razonable de refresco. Para ello, una vez que obtenemos el valor del parámetro de entrada, vamos a añadir una sentencia de control *if*, comprobando que el valor esté comprendido entre 100 y 1000 milisegundos. Si el valor está fuera de ese intervalo, lanzaremos con la instrucción *raise* la excepción *ValueError*.
 
 :dart: ¿Te ves capaz de hacerlo tú solo? Recuerda que, una vez que lances la excepción *ValueError* debes capturarla en un nuevo *except* (para los que estén acostumbrados a trabajar con Java, sería equivalente a definir un *multi-catch*). Si te atascas con la solución, la tienes disponible en [el siguiente laboratorio](../lab-09/mi-monitor) :wink:. 
 
¡Ya está! Ya tenemos totalmente contralados y validados los parámetros de entrada de nuestra aplicación y hemos aprendido a crear una aplicación Python desde cero y a ejecutarla de diferentes formas. En el siguiente laboratorio instalaremos la librería que nos permitirá acceder a nuestro sistema y comenzaremos a obtener los datos de CPU y RAM, que nutrirán nuestras gráficas.

[< Lab 07](../lab-07) | [Lab 09 >](../lab-09)

<p align="center">
    <img src="../resources/header.png">
</p>

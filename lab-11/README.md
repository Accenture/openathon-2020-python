<p align="center">
    <img src="../resources/header.png">
</p>

# Lab 11 - Poniéndole cara a nuestra aplicación

En este laboratorio vamos a construir la interfaz de nuestra aplicación, para lo que haremos uso de la adaptación de la librería Qt para Python (PyQt5). Si no conoces PyQt5 o quieres saber más sobre ella, puedes acceder a su [documentación oficial](https://www.riverbankcomputing.com/static/Docs/PyQt5/). Además, haremos uso de la librería pyqtgraph para dibujar las gráficas, puedes saber más a través de su [documentación oficial](https://pyqtgraph.readthedocs.io/en/latest/).

Puedes continuar con el código que hayas escrito tu mismo o, si lo prefieres, puedes tomar como punto de partida el código subido en [este mismo laboratorio](./mi-monitor). 

## Añadiendo dependencias al fichero requirements.txt

Lo primero de todo será añadir las librerías con las que trabajaremos. Añadiremos las siguientes dependencias a nuestro fichero requirements.txt:

```
# ...
PyQt5==5.15.0
PyQt5-sip==12.8.0
pyqtgraph==0.11.0
```

Ahora debemos ejecutar el install de nuevo, para que se descarguen e instalen las nuevas dependencias. ¿Recuerdas el comando? Si no lo recuerdas, puedes consultar [el laboratorio nueve](../lab-09).

## Creando una aplicación Qt

Para poder trabajar con interfaces, debemos hacer que nuestra aplicación sea una aplicación Qt. ¿Cómo lo conseguiremos? Con una clase que genere una ventana (QMainWindow). Para ello, modificaremos la clase Monitor que hemos creado en la laboratorio anterior añadiendo las siguientes líneas:

```python
from PyQt5.QtWidgets import QMainWindow

# Definimos nuestra clase Monitor como la ventana principal de la aplicación (QMainWindow)
class Monitor(QMainWindow):

    def __init__(self, refresh):
        # Invocamos al método init del padre
        super(Monitor, self).__init__()
        
        # Mostramos la ventana de la aplicación
        self.show()

        # ...
```

> En algunos casos el VSCode puede mostrar problemas si teneis instalado el verificador de código *pylint* "No name 'QApplication' in module 'PyQt5.QtWidgets'", "No name 'QWidget' in module 'PyQt5.QtWidgets'". Esto es debido a que *pylint* no carga extensiones C por defecto como las de *PyQt5*. Para solucionarlo se puede editar "Preferences: Open Settings (JSON)" (buscad con Ctrl+Shift+P) añadiendo un nuevo elemento al JSON:
>```json
>    "python.linting.pylintArgs": ["--extension-pkg-whitelist=PyQt5"]
>```

Ahora, para que la ventana se cree correctamente, debemos añadir en nuestro fichero \_\_main\_\_.py las siguientes líneas, subtituyendo la invocación a la clase Monitor que ya teníamos:

```python
from PyQt5.QtWidgets import QApplication

try:
    # ...
    
    # Se crea la aplicación Qt (QApplication)
    app = QApplication(sys.argv)
    # Se instancia la clase Monitor
    monitor = Monitor(refresh)
    # Se espera a la finalización de la aplicación para salir de nuestro programa Python
    sys.exit(app.exec_())

except IndexError as index_error:
    print('Por favor, tienes que indicar la velocidad de refresco como parámetro de entrada')
    sys.exit(-1)
except ValueError as value_error:
    print('{} no es un valor válido'.format(refresh))
    print('Por favor, la velocidad de refresco tiene que ser un número entre 100 y 1000')
    sys.exit(-1)
```

Si ejecutas este código, verás como la ventana se muestra. Prueba a poner el cursor del ratón encima de la ventana y comprobarás que "no responde". Acabamos de crear nuestra primera aplicación Qy y se queda colgada. ¿Por qué ocurre esto? Porque tenemos al hilo principal de nuestra aplicación metido en el bucle infinito que creamos de prueba en el laboratorio anterior (lo cuál, a propósito, es una muy mala práctica) y nunca se desbloquea. Sin embargo, si ponemos el comando show después del bucle infinito, ¿te imaginas lo que ocurrirá?

¡En efecto! La sentencia show nunca se ejecutará y, por tanto, la ventana nunca se mostrará.

> :warning: En linux es posible que no tengas instalados los paquetes de *Qt* que permiten operar con este tipo de ventanas y visualices un error del tipo:
>```shell 
>   qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
>    This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
>   Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl, xcb.
>   Aborted (core dumped)
>``` 
> Para ello hay que instalar el paquete mediante el siguiente comando (Ubuntu):
>```shell 
>   sudo apt-get install qt5-default
>``` 

## Preparando la interfaz de nuestro monitor

Ahora que ya hemos conseguido generar una ventana vacía, vamos a diseñar la interfaz visual. Como habíamos comentado, vamos a mostrar dos gráficas, por lo que primero de todo será definir cómo se van a organizar nuestros widgets (es decir, definir el layout), para luego añadir los *widgets* correspondientes. En nuestra clase Monitor (nuestra ventana Qt), vamos a añadir el siguiente código dentro del método \_\_init\_\_.py, en tres bloques diferentes para facilitar su comprensión:

```
from util import Extractor
import time

class Monitor:

    def __init__(self, refresh):

        print('Se ha creado la clase Monitor')

        # Invocamos al método init del padre
        super(Monitor, self).__init__()

        ###########################################################################
        # Bloque 1: Definir el Widget principal y el layout de nuestra aplicación #
        ###########################################################################

        ###########################################################################
        # Bloque 2: Definir el contenido de nuestro layout                        #
        ###########################################################################

        ###########################################################################
        # Bloque 3: Añadir los widgets generados a su contenedor                  #
        ###########################################################################

        # Mostramos la ventana de la aplicación
        self.show()

        self.cpu = [0 for _ in range(100)]
        self.memory = [0 for _ in range(100)]

        self.extractor = Extractor()
```

En el bloque 1, introducimos el siguiente código:

``` python
# Se importan las siguientes clases
from PyQt5.QtWidgets import QMainWindow,  QWidget, QLabel, QVBoxLayout
import pyqtgraph as pg

# Definir el Widget principal
widget = QWidget()

# Definimos el layout, en forma de vertical box
vertical_box = QVBoxLayout()
# Le indicamos que coja todo el ancho de la ventana
vertical_box.addStretch(1)
```

Una vez que ya hemos definido nuestro layout, es hora de empezar a añadir elementos a nuestra interfaz. Como habrás podido comprobar, a cada elemento que se añade a nuestra interfaz, Qt lo denomina *widget*. ¡Vamos a definir nuestros dos primeros widgets!

:one: Una etiqueta (QLabel) que mostrará el título de nuestro primer gráfico

:two: Un gráfico temporal utilizando la librería pyqtgraph

Para ello, tendremos que añadir en el bloque 2, el siguiente código fuente:

``` python

# Creamos un widget de tipo label (QLabel)
self.cpu_label = QLabel()
# Le asignamos el texto "CPU (0%)"
self.cpu_label.setText('CPU (0%)')

# Creamos un widget para mostrar el gráfico
self.plot_cpu = pg.PlotWidget()

```

Finalmente, en el bloque 3, agrupamos todos los widgets en su contenedor:

``` python
# Añadimos el QLabel a nuestro layout (será el elemento que actúe como primera fila)
vertical_box.addWidget(self.cpu_label)

# Añadimos el gráfico vacío a nuestro layout (será el elemento que actúe como segunda fila)
vertical_box.addWidget(self.plot_cpu)

# Asignamos al widget principal nuestro layout
widget.setLayout(vertical_box)

# Asignamos el widget a la ventana principal
self.setCentralWidget(widget)
```

¡Ya está! Acabamos de construir una ventana Qt que dibujará una interfaz con dos widgets: una etiqueta y un gráfico.

:warning: Si ejecutas ahora el código, seguirás viendo la ventana bloqueada a causa de nuestro bucle while infinito. En el siguiente apartado, nutriremos de datos nuestro gráfico y quitaremos ese bucle tan feo de nuestra aplicación.

## Vinculando las fuentes de datos

Todo gráfico necesita datos para pintar. Si recuerdas, en [el laboratorio 10](../lab-10) conseguimos construir dos flujos de datos: uno para el índice de uso de la CPU y otro para el de la memoria RAM. Vamos a enlazar ambos flujos con la interfaz y, cada vez que haya un nuevo dato, en lugar de pintarlo en consola, haremos que se pinte en nuestro gráfico.

En primer lugar, al comienzo del método \_\_init\_\_.py, definiremos un array de 100 posiciones que actuará como eje de las x:

```python
class Monitor(QMainWindow):

    def __init__(self, refresh):
        
        # Definimos una lista de 100 posiciones
        self.cpu_x = list(range(100))
        
        # ...
        
```

Vamos ahora a configurar el gráfico de la CPU que hemos definido en la sección anterior. Debes tener en cuenta que el gráfico debemos configurarlo **después** de haberlo instanciado y **antes** de añadirlo al layout, así que, antes de nada vamos a identificar dónde tenemos que colocar nuestro código:

``` python

# Creamos un widget para mostrar el gráfico
self.plot_cpu = pg.PlotWidget()

#############################################
# Bloque de configuración del gráfico       #
#############################################

# Añadimos el gráfico vacío a nuestro layout (será el elemento que actúe como segunda fila)
vertical_box.addWidget(self.plot_cpu)

```

Si configuras el widget después de haberlo añadido al layout, lo que ocurrirá es que no cogerá la configuración que le indiques.

Una vez que hemos identificado donde colocar nuestro código fuente, vamos a incluír la configuración:

``` python
# Definimos el color de fondo, en este caso, blanco
self.plot_cpu.setBackground('w')

# Definimos el rango del eje Y, como hablamos de porcentajes, será entre 0 y 100
self.plot_cpu.setYRange(0, 100)

# Definimos el estilo de la línea (puedes escoger otro color si te gusta más)
pen = pg.mkPen(color=(120, 0, 0))

# Creamos la línea de la CPU y la asociamos al gráfico
self.data_line_cpu = self.plot_cpu.plot(self.cpu_x, self.cpu, pen=pen)
```

Vamos ahora a adaptar el método que actualiza los datos de los valores de CPU para que actualice la información de ambos ejes, la línea y el título del gráfico. Substituye la función completa por el código que se muestra a continuación:

``` python
def update_cpu_data(self, nuevo_valor):
    # Se desplaza el eje de las x una posición
    self.cpu_x = self.cpu_x[1:]
    self.cpu_x.append(self.cpu_x[-1] + 1)

    # Se añade un nuevo valor al eje de las y
    self.cpu = self.cpu[1:]
    self.cpu.append(nuevo_valor)

    # Se actualiza la línea pasandole la lista de valores de x e y
    self.data_line_cpu.setData(self.cpu_x, self.cpu)

    # Se actualiza el texto de la QLabel para mostrar el último valor extraído
    self.cpu_label.setText('CPU ({}%)'.format(nuevo_valor))
```

Ahora que ya hemos actualizado la línea, es hora de eliminar ese bucle tan feo que habíamos creado para cambiarlo por un timer que pone a nuestra disposición la librería Qt para hacer refrescos de datos de forma periódica, el QtTimer. Cuando creemos que el timer, vamos a realizar las siguientes acciones:

:one: Definir el intervalo de refresco

:two: Definir los métodos que queremos que se ejecuten, según el intervalo de refresco

:three: Arrancar el timer

Este código, debemos añadirlo justo encima de la sentencia ````self.show()````:


``` python
from PyQt5 import QtCore

# ...

# Creamos el timer
self.timer = QtCore.QTimer()
# Establecemos la velocidad de refresco
self.timer.setInterval(refresh)
# Conectamos el método que extrae los datos de la CPU
self.timer.timeout.connect(self.get_cpu_data)
# Invocamos al método start, para lanazar la ejecución del timer
self.timer.start()

self.show()

```

Una vez añadido el bloque de código, vamos a eliminar las siguientes líneas:

``` python
while True:
    self.get_cpu_data()
    self.get_memory_data()
    print("CPU: {}".format(self.cpu))
    print("RAM: {}".format(self.memory))
    time.sleep(refresh/1000)
```

:memo: Ejecuta el código. Si todo ha ido bien, te saldrá una ventana, donde se mostrará el gráfico de la CPU y se irá refrescando según la velocidad que le hayamos indicado.

:dart: ¡Tu turno! Te toca, ahora, construir el gráfico de la memoria RAM. Debes seguir los mismos pasos que hemos realizado para el gráfico de la CPU. Al final, deberías conseguir que se mostrasen ambas gráficas (una encima de otra). Tienes el código de la solución [en el siguiente laboratorio](../lab-12/mi-monitor) :wink:

En el siguiente laboratorio convertiremos nuestra aplicación en reactiva de forma que la actualización de la interfaz se haga de forma más eficiente.

[< Lab 10](../lab-10) | [Lab 12 >](../lab-12)

<p align="center">
    <img src="../resources/header.png">
</p>

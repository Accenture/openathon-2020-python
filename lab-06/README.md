<p align="center">
    <img src="../resources/header.png">
</p>

# Lab 06 - Módulos y paquetes. Uso de Pip

## Indice

1. [Uso básico de pip](#uso-basico-de-pip)
2. [Test yourself!](#test-yourself-100)

## Uso básico de pip

Un módulo no es más que una serie de fichero python con funciones, clases y variables:

```python
# fichero modulo.py

def funcion(x, y):
  return x + y
```

```python
# otro fichero .py

import modulo

print(modulo.funcion(5, 4))
```

En el ejemplo anterior hemos creado un modulo con una función, y lo hemos importado en otro fichero.

Podriamos importar solo la funcion:

```python
from modulo import funcion

print(funcion(5, 4))
```

Tambien podriamos darle un alias al import:

```python
import modulo as md

print(md.funcion(5, 4))
```

## Uso de pip

Pip es un gestor de paquetes/modulos python. A partir de la versión 3.4 viene ya instalado:

```sh
pip --version
pip 20.1.1 from /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pip (python 3.8)
```

En caso de que no lo tengais, seguir las siguientes instrucciones en una consola:

1. Primero descargamos el fichero get-pip.py

   ```sh
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   ```

2. Luego lo ejecutamos con python:

   ```sh
   python get-pip.py
   ```

3. Por último ejecutamos pip para ver que se ha instalado:

   ```sh
   pip --version
   ```

#### Ejemplo de instalación en Linux Ubuntu

1. Para instalar *pip* en sobre el *python3* preinstalado en Ubuntu 20.x :

   ```sh
    sudo apt update
    sudo apt install python3-pip
   ```
2. Esto instala *pip* y todas sus dependencias. Para comprobar la instalación:

   ```sh
    pip3 --version
    pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
   ```
   
## Continuando con su uso

Su uso es muy sencillo. Para instalar cualquier paquete la sentencia es:

```sh
pip install <name_package>
```

Por ejemplo que lo usaremos más adelante:

```sh
pip install PyQt5
```

Esto instalará en nuestro equipo el módulo PyQt5.

## Test yourself! :100:

Para comenzar con la instalación de paquetes, vamos a utilizar [pandas](https://pypi.org/project/pandas/). Esta es una librería muy conocida para análisis de datos. Como fuente de datos usaremos un fichero con todos los Pokemon e imprimiremos los 5 primeros:

```python
   #                   Name Type 1  ... Speed  Generation  Legendary
0  1              Bulbasaur  Grass  ...    45           1      False
1  2                Ivysaur  Grass  ...    60           1      False
2  3               Venusaur  Grass  ...    80           1      False
3  3  VenusaurMega Venusaur  Grass  ...    80           1      False
4  4             Charmander   Fire  ...    65           1      False

[5 rows x 13 columns]
```

> Como ayuda mirar las funciones read_csv y head

[^1]: Los datos los he obtenido del siguiente [enlace](https://www.kaggle.com/abcsds/pokemon)



## Siguientes pasos :rocket:

Con la instalación de paquetes Python ya estamos listos para empezar a desarrollar una aplicación con complejidad usando Python como lenguaje. 

En el siguiente laboratorio comenzaremos la creación de una aplicación similar al monitor de actividad de Windows para más tarde hacerla reactiva.



[< Lab 05](../lab-05) | [Lab 07 >](../lab-07)

<p align="center">
    <img src="../resources/header.png">
</p>

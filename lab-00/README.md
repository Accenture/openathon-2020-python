<p align="center">
    <img src="../resources/header.png">
</p>

# Lab 00 - Bienvenidos al mundo de Python :snake::hand:

Python es un lenguaje de programación lanzando en 1991. Es utilizado en muchos sectores, desarrollo de aplicaciones web, scripting, etc. Recientemente ha alcanzado una alta popularidad debido al crecimiento del Data Science. Esto debido a dos caractericticas de Python:

- Fácil curva de aprendizaje debido a su sintaxis similar al Inglés.
- Una amplia comunidad con multitud de framework, bibliotecas, etc.

Actualmente existen dos versiones, la 2 y la 3. Ambas no son compatibles y lo recomendado es utilizar la versión 3 ya que la 2 se mantiene como legacy.

En este laboratorio daremos los primeros pasos en el mundo de Python, desde la instalación del interprete hasta la ejecución de nuestro primer programa en Python.

## Indice

1. [Instalación del intérprete](#instalación-del-intérprete)

2. [Instalación del IDE](#instalación-del-ide)

3. [Test yourself!](#test-yourself-100)

## Instalación del intérprete

Para la instalación del intérprete seguimos los siguientes pasos:

1. Abrimos un navegador y vamos al siguiente [enlace](https://www.python.org/downloads/release/python-386/)

2. Hacemos scroll hasta el final de la página y elegimos el enlace correspondiente a nuestro sistema operativo (Windows, Linux-Like u OSX)

3. Tras instalar el intérprete, abrimos una consola. Si pregunta si lo añade al PATH, indica que sí.

4. Ejecutamos _python3_. Si ves un mensaje similar al siguiente, ya habremos terminado:

   ```sh
   Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27)
   [Clang 6.0 (clang-600.0.57)] on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   ```
    Si no reconoce el comando _python3_, probamos el comando _python_.
> No instalamos la versión 3.9 porque da problemas de dependencias con pip

> :warning: Si lo estás haciendo en Windows y al ejecutar el comando nos lleva a Microsoft Store haremos lo siguiente:
>
> 1. En la barra de búsqueda de Windows escribimos _App Execution Aliases_.
> 2. Dentro de la ventana de Settings, desmarcamos a _Off_ aquellas relativas a _python_.
> 3. Volvemos a ejecutar el comando en la consola.


## Instalación del IDE

Como en otros lenguajes existen multitud de Entornos de Desarrollo. En caso de Python podemos hablar principalmente de tres:

- VisualStudio Code
- Pycharm
- Spider

En este punto os explicaremos como instalar VisualStudio Code, pero podéis utilizar el que queráis. De hecho, los laboratios se puede llevar a cabo sin ningún IDE.

Primero, tendremos que instalar VisualStudio Code:

1. Vamos al siguiente [enlace](https://code.visualstudio.com/download).
2. Elegimos la versión del SO que corresponda y lo instalamos como cualquier otro programa (si os pregunta si queréis añadir al PATH indicar que sí).

VisualStudio Code es un editor el cual podemos enriquecer con extensiones. Por defecto, ya viene con una extensión para que podemos programar y ejecutar código python:

1. Crea un nuevo fichero que acabe en *.py*
   1. Click en File > New.
   2. Haz click en File > Save y llamado *ejemplo.py*
2. Revisa que en la barra de abajo de editor, aparece Python 3.8.X, donde X es tu versión, y arriba a la derecha el botón Play. Ese botón te permitirá ejecutar el fichero.

## Test yourself! :100:

Vamos a validar si tenemos todo correctamente instalado. Para ello, vamos a abrir una terminal (cmd en Windows) y ejecutar el interprete:

```sh
$ python3
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Si todo va bien veremos un mensaje y un promt de python. Ahora ejecutamos:

```python
>>> input("Are you ready? ")
Are you ready?
```

Si crees que estás listo, escribe _Yes_!!!! :1st_place_medal:.

```python
>>> input("Are you ready? ")
Are you ready? Yes
'Yes'
```

En el caso del editor, escribe la sentencia *input("Are you ready? ")* en el fichero que creaste anteriormente, y dale al Play. Se te abrirá una terminal abajo, y podrás contestar _Yes_!!!! :1st_place_medal:.

## Siguientes pasos :rocket:

Hemos llevado a cabo la instalación de las herramientas básicas: el interprete y un IDE. En el próximo laboratorio, veremos los tipos básicos de Python y a empezar a trabajar con ellos.

[Lab 01 >](../lab-01) 

<p align="center">
    <img src="../resources/header.png">
</p>


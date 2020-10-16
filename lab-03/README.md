<p align="center">
    <img src="../resources/header.png">
</p>

# Lab 03 - Uso de funciones

## Indice

1. [Funciones](#funciones)
2. [Funciones lambda](#funciones-lambda)
3. [Test yourself!](#test-yourself-100)

## Funciones

Una función no es más que un conjunto de sentencias agrupadas bajo un mismo nombre, el nombre de una función. Estas pueden tener entrada y/o salida:

```python
def <nombre_funcion> (<param1>, <param2>, ...):
  sentencia_1
  sentencia_2
  sentencia_3
  ...
```

Como podeis ver la estructura es:

- Usamos la palabra clave **def** para indicar que es una función.
- Indicamos un **nombre_funcion**, que sera el que usemos al llamarla.
- Puede recibir 0...n parametros
- Usamos **:** para indicar el inicio de la función.

:warning: *Recuerda **usar espacios** en cada una de las sentencias que estén dentro de la función.*

Veamos el siguiente ejemplo:

```python
def suma (x, y):
  z = x + y
  return z
```

- La función se llama **suma**
- Recibe dos parámetros: **x** e **y**
- Devuelve, en este caso un valor que será la suma de *x* e *y*

> Como puedes ver en Python no declaramos el tipo que devuelve la función, ya que en Python no declaramos el tipo de las variables, y por lo tanto, tampoco de los parametros de entrada a la función

Para llamar a la función seria:

```python
print(suma(5, 3))
```

>:warning: La función hay que definirla antes de llamarla. Esto es debido a que es un lenguaje interpretado y si la llamas antes de definirla, el interprete te dará un error.



Existen varias formas diferentes de definir los argumentos de la función:

### Uso de *

Hay ocasiones donde no sabemos el número de parámetros de una función, para ello tenemos el carácter *:

```python
def print_nombres(*nombres): # nombres será una tupla realmente
  for i in nombres:
    print(i)
    
print_nombres("Juan", "Pedro", "Samuel") # le pasamos 3 argumentos
```



### Uso de keyword

Como has visto, el orden de los parámetros es importante. Una forma de saltarse este requisito es usar parametros nombrados mediante *clave = valor*:

```python
def resta (x, y):
  return x - y
print(resta(9, 8))
print(resta(y = 8, x = 9))
```

### Uso de **

Antes hemos visto el uso de *, cuando ponemos dos es equivalente a usar parámetros nombrados (en lugar de tener una tupla, tenemos un diccionario):

```python
def personas(**args):
  print(args["primera"])
  
personas(primera = "Pedro", segunda = "Juan")
```

### Pasar un valor por defecto

Podemos pasar un valor por defecto a un parámetro, cuando se le llama sin ningún valor para ese parámetro (este debe ser el último):

```python
def suma (x, y = 3):
  return x + y

print(suma(5)) # devuelve 8
```

## Funciones lambda

Las funciones lambda tienen un extenso uso en Python. No son más que funciones anónimas (no tienen nombre, no se declaran) que sólo pueden tener una sentencia:

```python
hola_lambda = lambda x : x + 5
print(hola_lambda(5)) # imprime 10
```

Esto sería equivalente a:

```python
def hola_lambda(x):
  return x + 5

print(hola_lambda(5))
```

Como ves la lectura es más sencilla.

## Test yourself! :100:

Para validar los conocimientos adquiridos y que no resulte tan aburrido :sleeping:, os proponemos resolver el siguiente ejercicio:

_En el laboratorio anterior resolvimos un problema que consistia en crear una lista de numeros pares del 1 al 100 a partir de otra. Te propongo crear una función que indique si un número es par o no, y la utilices en la solución anterior. Puedes hacer lo mismo pero con números impares definiendo una función lambda_

## Siguientes pasos :rocket:

En este capitulo hemos trabajado con funciones. En el próximo comenzaremos con el mundo de los objetos.



[< Lab 02 ](../lab-02)  | [Lab 04 >](../lab-04) 

<p align="center">
    <img src="../resources/header.png">
</p>

<p align="center">
    <img src="../resources/header.png">
</p>

# Lab 02 - Uso avanzado de Python

## Indice

1. [Flujos de control](#flujos-de-control)
2. [List comprehension](#list-comprehension)
3. [Test yourself!](#test-yourself-100)


## Flujos de control

En Python tenemos tres flujos de control:

- If-else
- for
- while

### If-else

Hemos utilizado la sentencia if en el lab-01, para comprobar si un elemento estaba en una colección. Como puedes ver, if como su nombre indica permite realizar cierta acción/es en función de una condición booleana:

```python
x = 10
y = 20

if x < y:
  print("x = {} es menor que y = {}".format(x, y))
```

[^1]: Si no recuerdas el método format, revisa el capitulo *Trabajando con Strings* del lab-01.

La sintaxis esta formada por la palabra especial **if**, una **condición**, **dos puntos** y como en todas las estructuras en python, dentro del if estaran todas aquellas sentencias que estén tabuladas:

*if [condicion]:*

*<dos_espacios> sentencia1*

*<dos_espacios> sentencia1*

> Recuerda que en Python los bloques se distinguen por : y la tabulación. En otros lenguajes, como Java o C los : es equivalente a la {}

Existe otra palabra especial **elif**, para concatenar condiciones excluyentes:

```python
x = 4

if x == 3:
  print("x es 3")
elif x == 4:
  print("x es 4")
```

Por otra parte, tenemos **else**, para indicar que ninguna de las condiciones anteriores se han cumplido:

```python
x = 4

if x == 2:
  print("x es 2")
elif x == 3:
  print("x es 3")
else:
  print("x es otro numero")
```



Dentro de las condiciones más allá de los operadores de comparación (==, !=, <=, ...) podemos utilizar los operadores booleanos **and** y **or**:

```python
x = 5
y = 2
z = 3

if x > y and x > z:
  print("x es mayor que y, y que z")

```

```python
x = 5
y = 2
z = 8

if x > y or x > z:
  print("x es mayor que y, o es mayor que z")
```

> :warning: Estos operadores actúan en **cortocircuito**, es decir, en el caso del **and**, si la primera condición es falsa, no se evalua la segunda. En el caso del **or**, si la primera es verdadera, no se evalua la segunda.

### while

La sentencia *while* permite ejecutar un grupo de sentencias, mientras una condición sea verdadera:

```python
i = 30
while i > 0: # se ejecuta hasta que i valga 0
  print(i)
  i = i - 1
```

Existen dos sentencias especiales que permiten saltar ese comportamiento:

- **break**: permite salir del bucle
- **continue**: permite ir directamente a la siguiente iteración

```python
i = 0
while i < 10: # mientras i sea menor que 10
  i = i + 1
  if i == 3: 
    continue # 3 nunca se imprimirá
  if i == 5:
    break # cuando lleguemos a 5 saldremos del while
  print(i)
```

Una última sentencia importante en relación con *while* es el uso de *else* para ejecutar código una vez hemos salido del bucle:

```python
i = 0
while i < 10:
  print(i)
  i = i + 1
else:
  print("el while ha finalidado")
```

> :warning: El *else* de un *while* no se ejecuta si se ha salido del bucle con *break*.

### for

La sentencia **for** ya la hemos utilizado en el lab-01, para recorrer las colecciones y los Strings:

```python
lista = [0, 1, 2]

for number in lista:
  print(number)
  
nombre = 'Joslain'
for i in nombre:
  print(i)
```

Como en el caso del while tenemos también las sentencias **continue**, **break** y **else**.

Una función muy utilizada en Python es *range*:

```python
for i in range(5):
  print(i) # imprime los numeros del 0 al 4

for i in range(0, 6):
	print(i) # imprime los numeros del 0 al 5

for i in range(0, 11, 2): # del 0 al 11 en saltos de 2
  print(i) # imprime 0 2 4 6 8 10

```

> Realmente range es un **generador** ya que no devuelve una lista si no que en cada iteracción te va devolviendo el siguiente elemento. Si quieres saber más, mira el siguiente [enlace](https://docs.python.org/3.3/library/stdtypes.html?highlight=range#range).

## List comprehension

La comprehension de lista no es más que una forma de crear listas de forma compacta:

```python
cuadrados = [i * i for i in range(10)] # cuadrados es [1, 4, 9, ...]
```

Podemos incluir condiciones:

```python
cuadrados = [i for i in range(10) if i%2 == 0] # cuadrados es [0, 2, 4, ...]
```

Como podeis ver podemos ver que hay 4 partes:

```python
lista = [expresión for elemento in coleccion (if condición)]
```

- **expresión**: puede ser por ejemplo una llamada a una función, o una expresión en sí misma, sobre los elementos de la colección, que será lo que se añada la lista resultante.
- **elemento**:sería cada elemento dentro de la colección
- **coleccion**: la colección en si misma. Puede ser una lista, tupla, diccionarios, etc.
- **condición**: podemos incluir una colección para filtrar los elementos dentro de la colección.

## Test yourself! :100:

Propongo el siguiente ejercicio para poner a prueba tu aprendizaje respecto de los flujos de control y de la list comprehension:

_Supongamos que tenemos una lista de numeros del 1 al 100. Te propongo obtener la lista sólo de aquellos números pares. Haz una versión con list comprehension y otra sin ella._

```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9,...]
resultado = [2, 4, 6, 8, ...]
```

> Te aconsejo investigar acerca de la funcion range para generar números.

## Siguientes pasos :rocket:

En este capitulo hemos trabajado con flujos de control y comprensión de listas. Ya casi eres un **hero python** :fire:. En el siguiente laboratorio, empezamos con las funciones.

[< Lab 01](../lab-01)  | [Lab 03>](../lab-03) 

<p align="center">
    <img src="../resources/header.png">
</p>


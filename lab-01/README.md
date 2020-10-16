<p align="center">
    <img src="../resources/header.png">
</p>

# Lab 01 - Uso básico de Python

En este laboratorio, empezaremos a *jugar* con la pequeña serpiente, desde la creación de variables hasta conocer cada uno de los tipos básicos que existen en Python, muy similares a los de otros lenguajes de alto nivel como Java.

## Indice

1. [Comentarios](#comentarios)
2. [Creación de variables](#creaci%C3%B3n-de-variables)
3. [Tipos de datos básicos](#tipos-de-datos-básicos)
4. [Operadores](#operadores)
5. [Tipos de datos avanzados](#tipos-de-datos-avanzados-colecciones)
6. [Trabajando con Strings](#trabajando-con-strings)
7. [Test yourself!](#test-yourself-100)

## Comentarios

Los comentarios es texto del código fuente que el compilador/interprete ignoran ya que aportan información al programador, no a la funcionalidad del programa.

En Python, hay dos tipos de comentarios

- Comentar una sola línea con **#**.
- Comentar varias lineas con **'''**.

```python
# Esto es un comentario de una sola línea
```

```python
'''
Esto
es
un comentario
de muchas líneas
'''
```

> Es una buena práctica comentar el código, pero de forma significativa. Especialmente, cuando el código es complejo o para aclarar la lógica de negocio.
>

## Creación de variables

Una variable se utiliza en los lenguajes de programación para poder hacer referencia (*leer/modificar*) a una dirección de memoria de forma semántica. Es decir, nos permite almacenar un determinado valor para después poder usarlo mediante una referencia significativa para los programadores. 

Las variables tienen un tipo, por ejemplo, entero o string (cadena de caracteres), aunque lo veremos más adelante. Por ejemplo en pseudocodigo:

```
Ordenador, creame una variable de tipo string, llamada mi_nombre y con valor Joslain
```

De esta forma, a lo largo del programa podriamos usar la variable *mi_nombre*.

A diferencias de otros lenguajes,  en Python, no es necesario indicar el tipo de la variable, ya que el interprete deduce el tipo de la variable por el valor asignado, por ejemplo:

```
Ordenador, creame una variable llamada mi_nombre y con valor Joslain
```

Como vemos solo decimos el nombre de la variable (*mi_nombre*)  y su valor *Joslain*. En este caso, se deduciria que el valor es de tipo string.

Si vemos un ejemplo en Python sería:

```python
mi_nombre = 'Joslain'
```

En este caso:

- **mi_nombre**: sería el nombre de la variable.
- **=**: sería el operador de asignación (a una variable le *asignamos* un valor)
- **'Joslain'**: sería el valor asignado a dicha variable

> Las comillas simples es para indicar en Python que es de tipo String

Podríamos cambiar el valor de la variable es decir:

```python
mi_nombre = 'Joslain'
mi_nombre = 'Jos'
```

Como vemos, en la primera sentencia se crearía la variable, y en la segunda cambiamos su valor. Si lo probamos en la terminal, podemos ver su último valor:

```sh
>>> mi_nombre = 'Joslain'
>>> mi_nombre = 'Jos'
>>> mi_nombre
'Jos'
>>>
```

> Como buena práctica, las variables en Python, van en minuscula y separadas por guiones bajos.

## Tipos de datos básicos

En Python, como en otros lenguajes, existen unos tipo de variables básicos:

### Entero (int)

El primero tipo sería *int*, por ejemplo, el valor 5:

```python
numero = 5
```

### Decimal (float)

Otro tipo sería *float*, para poder trabajar con decimales (se usa el **.**):

```python
decimal = 3.14
```

### Boolean (bool)

Otro tipo muy importante, sería el *bool*, para trabajar con condiciones es decir, *True* y *False*:

```python
verdadero = True
falso = False
```

### String

Por último, tendriamos el tipo string, para trabajar con cadenas de caracteres:

```python
saludo = 'Bienvenido al Openathon'
despedida = "¡Te espero en el siguiente!"
```

Puedes observar que para indicar que es un string, usamos **'** y **"**.

> Existe un método en Python, que permite saber el tipo de una variable pasándola como parámetro. Por ejemplo: 
>
> ```sh
> >>> type(mi_nombre)
> <class 'str'>
> ```

## Operadores

### Operadores numéricos

En Python tenemos los siguientes operadores numéricos:

- **+**: permite sumar dos números.

  ```python
  x = 7
  y = 5
  z = x + y
  print(z) # 12
  ```

  > print es un método que permite mostrar texto por la salida estándar:
  >
  > ```sh
  > >>> x = 5
  > >>> print(x)
  > 5
  > ```

- **-**: permite restar dos números.

  ```python
  x = 7
  y = 5
  z = x - y
  print(z) # 2
  ```

  

- **\***: permite multiplicar dos números.

  ```python
  x = 7
  y = 5
  z = x * y
  print(z) # 35
  ```

  

- **/**: permite realizar la división real de dos números.

  ```python
  x = 7
  y = 5
  z = x / y
  print(z) # 1.4
  ```

  

- **//**: devuelve la división entera de dos números.

  ```python
  x = 7
  y = 5
  z = x // y
  print(z) # 1
  ```

  

- **%**: permite calcular el resto de la división de dos números.

  ```python
  x = 7
  y = 5
  z = x % y
  print(z) # 2
  ```

### Operadores de comparación

Como en otros lenguajes tenemos **<**(menor), **>**(mayor), **<=**(menor o igual), **>=**(mayor o igual), **==**(igual) y **!=** (distinto). 

```sh
>>> 7 < 5
False
>>> 2 > 1
True
>>> 5 <= 2
False
>>> 3 >= 0
True
>>> 3 == 3
True
>>> 5 != 3
True
```



> Los operadores de comparación siempre devuelven boleados (True o False)

## Tipos de datos avanzados (colecciones)

### Listas

Es una coleccion con las siguientes propiedades:
- Es heterogénea, puede estar compuesta por elementos de distinto tipo
- Es mutable, se pueden modificar sus elementos 
- Es indexada, se puede acceder a cada elemento por un indice que corresponde con la posición en la colección

Un ejemplo sería:

```python
lista = [1, 5, 4]
```

A los elementos se puede acceder por la posición (comienza en 0):

```python
lista[0] # devuelve 1
lista[1] # devuelve 5
lista[2] # devuelve 4
```

Los indices pueden ser negativos siendo -1 el último, -2 el penúltimo...

```python
lista[-1] # devuelve 4
lista[-2] # devuelve 5
lista[-3] # devuelve 1
```

Tambien podemos obtener un subconjunto de la lista, indicando un rango:

```python
lista[0:2] # devuelve [1, 5]
lista[:2]  # devuelve [1, 5]
lista[1:]  # devuelve [5, 4]
lista[:]   # devuelve la lista entera
```

> Como se ve en el rango [a:b], a esta incluido y b no.
>
> Si no indicamos a, empieza en 0
>
> Si no indicamos b, acaba al final

Como anteriormente, podemos indicar indices negativos en el rango, para ir de atrás hacia delante:

```python
lista[-1:] # devuelve [4], el último elemento
```



Para modificar un valor, simplemente indicamos el indice:

```python
lista[0] = 3 # la lista quedaria, [3, 5 , 4]
```



Para recorrer una lista usariamos lo que llamamos un bucle:

```python
for i in lista:
  print(i)
```



Para verificar si un elemento existe en una lista:

```python
if 5 in lista:
  print('ok')
```



Para saber la longitud de una lista:

```python
longitud = len(lista)  #devuelve 3
print(longitud)

```

Para añadir un elemento:

```python
lista.append(10) # lista ahora es [1, 5, 4, 10]
lista.insert(0, 7) # lista ahora es [7, 1, 5, 4, 10]
```

> **append** permite añadir un elemento al final de la lista
>
> **insert** es para insertar un elemento en una posición especifica desplazando el resto de elementos


Para eliminar un elemento especifico (*remove*, *pop* y *del*):

```python
lista = [1, 2, 3]
lista.remove(1) # lista ahora es [2, 3]
```

```python
lista = [1, 2, 3]
lista.pop() # lista ahora es [1, 2]
lista.pop(0) # lista ahora es [2]
```

```python
lista = [1, 2, 3]
del lista[0] # lista ahora es [2, 3]
del lista # la variable lista se ha eliminado
```

```python
lista = [1, 2, 3]
lista.clear() # lista ahora es []
```


> pop permite eliminar el último elemento de la lista o de una posición específica



Otro aspecto útil, es copiar listas. :warning: Es importante tener en cuenta que las listas son referencias por lo que si hacemos *lista_copy = lista*, realmente las dos variables apuntan a los mismos datos.

Por lo que para hacer una copia del contenido existen dos métodos (*copy* y *list*):

```python
lista_copy = lista.copy()
lista_copy = list(lista)
```

Por último, tenemos la concatenacion de listas, es decir, unir dos listas en una:

```python
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

lista_3 = lista_1 + lista_2
```

> Existen otras formas de concatenar listas pero no vamos a entrar en ellas.

Si quieres saber más acerca de listas te animo a visitar la [documentación oficial de Python3](https://docs.python.org/3/tutorial/datastructures.html).

### Tuplas

Es una coleccion con las siguientes propiedades:


- Es heterogénea, puede estar compuesta por elementos de distinto tipo
- Es inmutable, no  se pueden modificar sus elementos 
- Es indexada, se puede acceder a cada elemento por un indice que corresponde con la posición en la colección

Como se puede ver, realmente es una lista pero que no podemos modificar. Un ejemplo sería:

```python
tupla = (1, 2, 3)
```

La forma de acceder a los elementos es igual que en las listas, mediante el indice y pudiendo usar rangos (slicing):

```python
tupla[0] # devuelve 1
tupla[0:2] # devuelve (1, 2)
```

Para recorrer la tupla es igual que una lista mediante un bucle for:

```python
for i in tupla:
  print(i)
```

Podemos ver si un elemento existe en la tupla, igual que en la lista:

```python
if 1 in tupla:
  print('Existe')
```

Podemos usar el método len para conocer si longitud, igual que en la lista:

```python
tupla = (1, 2 ,3)
len(tupla) # devuelve 3
```

:bulb:

> Un caso curioso en Python es la creación de una tupla con un solo elemento (válido tambien para listas):
>
> ```python
> tupla = (1) # realmente tupla vale 1, es un int
> ```
>
> Para poder hacerlo, hay que añadir una coma al final:
>
> ```python
> tupla= (1,) # ahora si es una tupla
> ```



Finalmente, podemos unir como en las listas, dos tuplas usando el operador *+*.

A modo resumen se presenta la siguiente tabla:

|       | Inmutable          | Ordenada         | Indexadas          | Duplicados         |
| ----- | ------------------ | ---------------- | ------------------ | ------------------ |
| Lista | :no_entry_sign:    | :no_entry_sign:  | :white_check_mark: | :white_check_mark: |
| Tupla | :white_check_mark: | :no_entry_sign:  | :white_check_mark: | :white_check_mark: |



### Conjuntos

Los conjuntos son colecciones con las siguientes propiedades:

- No están ordenadas.
- No están indexadas.
- Son mutables.

[^1]: Son mutables a medias. Puedes añadir nuevos elementos y eliminar, pero no modificar los ya insertados.

Es decir, es una lista pero donde el orden de inserción no está garantizado.

Para crear un conjunto:

```python
conjunto = { 1, 2, 3 }
```

Para recorrer el conjunto usamos un bucle for:

```python
for i in conjunto:
  print(i)
```

Para comprobar si un elemento está en el conjunto:

```python
if 1 in conjunto:
  print("Existe")
```

Para añadir nuevos elementos podemos usar *add* o *update*:

```python
conjunto.add(4) # ahora conjunto es {1,2,3,4}
conjunto.update([5,6,7]) # ahora conjunto es {1,2,3,4,5,6,7}
```

Podemos como con las listas y las tuplas, obtener la longitud con *len*.

```python
conjunto = {1,2,3}
len(conjunto) # devuelve 3
```

Para eliminar elementos del conjunto, podemos usar *remove* o *discard*:

```python
conjunto = {1,2,3}
conjunto.remove(2) # ahora conjunto es {1,3}
conjunto.discard(3) # ahora conjunto es {1}
```

> La diferencia entre remove y discard, es que si el elemento no existe, remove lanza un error y discard no.

Si queremos vaciar el conjunto podemos usar *clear* como en las listas, o *del* para eliminarlo completamente.

Para unir dos conjuntos, no tenemos el operador *+* como en el caso de las listas y las tuplas:

```python
conjunto_1 = {1,2,3}
conjunto_2 = {4,5,6}

conjunto_3 = conjunto_1.union(conjunto_2)
```

[^2]: Cuando unimos conjuntos, los elementos duplicados se descartan

Podemos introducir los elementos de un conjunto al final de otro con el método *update*:

```python
conjunto_1 = {1,2,3}
conjunto_2 = {4,5,6}

conjunto_1.update(conjunto_2) # ahora conjunto_1 es {1,2,3,4,5,6}
```

Si quieres saber más de los conjuntos mira la [documentación oficial de Python3](https://docs.python.org/3/tutorial/datastructures.html#sets).

A modo resumen se presenta la siguiente tabla:


|          | Inmutable          | Ordenada         | Indexadas          | Duplicados         |
| -------- | ------------------ | ---------------- | ------------------ | ------------------ |
| Lista    | :no_entry_sign:    | :no_entry_sign:  | :white_check_mark: | :white_check_mark: |
| Tupla    | :white_check_mark: | :no_entry_sign:  | :white_check_mark: | :white_check_mark: |
| Conjunto | :no_entry_sign:    | :no_entry_sign:  | :no_entry_sign:    | :no_entry_sign:    |


### Diccionarios

Los diccionarios con colecciones con las siguientes características:

- No están ordenadas.
- Están indexadas, permite acceder a los elementos por su clave.
- Son mutables.

Como puedes ver son como las listas pero con elementos de tipo pares clave-valor:

```python
diccionario = {"1": "Pedro", "2": 27} # 1 y 2 son claves. Pedro y 27 son valores
```

Para acceder a los elementos accedemos por las claves o mediante *get*:

```python
diccionario["1"]     # devuelve "Pedro"
diccionario.get("1") # devuelvel "Pedro"
```

Para cambiar un valor, lo hacemos a través de la clave (si no existe esa clave, lo crea):

```python
diccionario["2"] = 30     # diccionario es {"1": "Pedro", "2": 30}
diccionario["3"] = "Hola" # diccionario es {"1": "Pedro", "2": 30, "3": "Hola"}
```

Para recorrer un diccionario usamos un bucle for:

```python
for i in diccionario:
  print(i) # imprime las claves
 
for i in diccionario:
  print(diccionario[i]) # imprimimos el valor

for i in diccionario.values(): # devuelve los valores
  print(i)

for clave, valor in diccionario.items(): # devuelve pares (clave, valor)
  print(clave, valor)
```

Como en las colecciones anteriores, si queremos saber si una clave esta o la longitud usamos *if in* y *len*:

```python
if "1" in diccionario:
  print("La clave 1 existe")
  
len(diccionario) # devuelve 3
```

Para eliminar elementos del diccionario podemos usar los métodos *pop*, *popitem* y *del*:

```python
diccionario.pop("1")  # borramos por clave
diccionario.popitem() # borramos el ultimo elemento insertado
del diccionario["1"]
del diccionario # eliminamos completamente el diccionario
```

Para vaciar el diccionario usamos el método clear como en las colecciones anteriores.

Para copiar diccionarios, podemos usar el método *copy()* o bien el constructor *dict*:

```python
diccionario = {"1": "Pedro", "2": 27}
diccionario_copy = dict(diccionario)
```

Si quieres saber más sobre los diccionarios te invito a mirar la [documentación oficial](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).

Finalmente, revisa la tabla resumen:




|             | Inmutable          | Ordenada         | Indexadas          | Duplicados         |
| ----------- | ------------------ | ---------------- | ------------------ | ------------------ |
| Lista       | :no_entry_sign:    | :no_entry_sign:  | :white_check_mark: | :white_check_mark: |
| Tupla       | :white_check_mark: | :no_entry_sign:  | :white_check_mark: | :white_check_mark: |
| Conjunto    | :no_entry_sign:    | :no_entry_sign:  | :no_entry_sign:    | :no_entry_sign:    |
| Diccionario | :no_entry_sign:    | :no_entry_sign:  | :white_check_mark: | :no_entry_sign:    |

## Trabajando con strings

Como indicamos antes los Strings en Python se crean usando *'* o *"*:

```python
string_1 = "Esto es un string"
string_2 = 'Esto es un string'
```

Podemos crear lo que se denomina, string multilinea usando **"""** o **'''** (como en los comentarios multilinea :arrow_up:):

```python
multilinea = """Esto
es
un
string
multinea
"""
print(multilinea) # devuelve 'Esto\nes\nun\nstring\nmultinea\n'
```

> Un dato curioso es que en Python el tipo char no existe, para representar un caracter hay que crear un string de longitud 1

En Python los strings se consideran un array de caracteres, es decir, que podemos acceder por indice y por rango a un subcojunto del string (esto se conoce como **slicing**):

```python
nombre = "Joslain"
nombre[0] # devuelve "J"

nombre[0:3] # devuelve "Jos"
```

Para saber la longitud de un string usamos el método *len*.

Podemos comprobar si un substring esta en un string usando *if in*:

```python
saludo = "Hola mundo"
if "Hola" in saludo:
  print("Existe")
```

Para concatenar strings podemos usar el operador *+*, como en el caso de las listas:

```python
nombre = "Pedro"
apellidos = "Paz"
completo = nombre + " " + apellidos
```

Nos podemos preguntar que ocurre si ejecuto lo siguiente:

```python
string = "Pedro tiene "
edad = 10
frase = string + edad
```

¿​Dará un error :thinking:? La respuesta es sí, porque no hace un casting automático como en otros lenguajes (Java por ejemplo, :coffee:).

Para enfrentar este problema tenemos el método *format*:

```python
string = "Pedro tiene {} años"
edad = 10
frase = string.format(edad) # frase es Pedro tiene 10 años
```

Existen multitud métodos para trabajar con String en Python, te aconsejo revisar la [documentación oficial.](https://docs.python.org/3/library/string.html)

## Test yourself! :100:

Ahora llega el momento de probar tus habilidades en Python. Para ello te propongo resolver los siguientes problemas, de los cuales muestro la entrada y salida, pero no la solución, pues en muchos casos esta no es única:

_Tenemos que crear un diccionario fibonnaci. Por clave tendrá la posición, y por valor la lista de números fibonnaci hasta esa posición. Se pide además dar una salida formateada del diccionario_

```python
entrada = 5
# fibonnaci es un diccionario
fibonnaci[5] # la salida sería [1,2,3,5,8]
```

## Siguientes pasos :rocket:

En este laboratorio hemos visto los tipos básicos en Python. En el próximo empezamos a ver los flujos de control, además de las maravillosas comprensión de listas.

[< Lab 00 ](../lab-00)  | [Lab 02 >](../lab-02) 

<p align="center">
    <img src="../resources/header.png">
</p>


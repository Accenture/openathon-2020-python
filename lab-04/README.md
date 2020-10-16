<p align="center">
    <img src="../resources/header.png">
</p>

# Lab 04 - El mundo de los objetos

## Indice

1. [En Python todo es un objeto](#en-python-todo-es-un-objeto)
2. [Clases](#clases)
3. [Variables/Métodos de clase](#variablesmétodos-de-clase)
4. [Metodos privados](#metodos-privados)
5. [None es null](#none-es-null)
6. [Test yourself!](#test-yourself-100)

## En Python todo es un objeto

La *programación orientada a objetos (POO)* es un paradigma de programación donde se programa pensando en objetos. Los objetos tienen un estado y una funcionalidad, y se relacionan entre ellos (unos usan otros, unos dependen de otros, etc). 

Es algo inherente al lenguaje de programación. Existen multitud de lenguajes orientados a Objetos: Java, C++, etc. <u>Python sólo es uno de muchos.</u>

Algo particular de Python, es que **todo es un objeto**, incluso las funciones lo son. 

```python
def mi_funcion(x, y):
  return x + y

print(type(mi_funcion))
```

Si ejecutamos el ejemplo anterior verás que la clase de mi_funcion es **<class 'function'>**. ¿Y que es eso de *clase* :thinking:? Los objetos vienen definidos por una clase. Esta no es mas que un esquema donde definimos los atributos del objeto (define su estado) y sus funciones (define su comportamiento).

```sh
# Esto es pseudocodigo, ¡no Python!
Persona {
	nombre
	apellidos
	edad
	
	getNombre() {
		return nombre
	}
	
}
```

En ejemplo anterior tenemos la clase Persona con tres atributos y un método.

En el caso de la funcion, su clase es **Function**.

## Clases

Para crear clases en Python lo haríamos de la siguiente forma:

```python
class Persona:
  #...
```

Como podeis ver se usa la palabra clave **class** e indicamos el nombre de la clase. Para poder crear una instancia de la clase, tenemos que añadir un constructor:

```python
class Persona:
  
  # Constructor de la clase Persona
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  
```

- Hemos creado la clase Persona.
- Tiene un constructor que recibe dos argumentos: nombre y edad
- Al hacer self.<name> estamos añadiendo atributos a la clase. En este caso, nombre y edad.

Además del constructor, podemos añadir otros métodos:

```python
class Persona:
  
  # Constructor de la clase Persona
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    
  def one_function(self):
    return self.edad * 5
```

- Hemos añadido un método *one_function*.

> self es una palabra clave para referirse a mi misma instancia

> Si os fijáis, tanto en el constructor como en la función hemos añadido self como argumento.  Es un requisito de Python para dentro de la función/constructor poder acceder a los atributos de la clase.



Veamos un ejemplo:

```python
class Persona:
  
  # Constructor de la clase Persona
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    
  def one_function(self):
    return self.edad * 5
 

jorge = Persona('Jorge', 25) # llamada al constructor de Persona
print(jorge.one_function()) # imprime 125

jorge.edad = 10 # hemos modificado el valor de edad en la instancia de jorge
```

## Variables/Métodos de clase

En el apartado anterior hemos visto atributos y métodos de instancia, es decir, para poder acceder a ellos necesitamos crear una instancia de la clase.

En python, existen las *variables estáticas* que se definen fuera de cualquier método de la clase:

```python
class Persona:
   saludo = 'Hola mundo'
  
print(Persona.saludo) # imprime Hola Mundo
```

Tambien existen los métodos de clase y estáticos:

```python
class Persona:
  
   @classmethod
   def metodo_de_clase(cls):
    	print('Hola, soy un metodo de clase')
   
   @staticmethod
   def metodo_estatico():
    	print('Hola, soy un metodo estatico, por lo que no se pasa cls')
      
Persona.metodo_de_clase()
Persona.metodo_estatico()
```

**@classmethod** y **@staticmethod** son decoradores. Es un modo de indicarle a Python el tipo de función. Como ves en ambos casos podemos llamar a los métodos *sin instanciar la clase*.

>La diferencia entre ellos está en que el método de clase, recibe *cls* como argumento, mientras que el estatico no (sería el equivalente a static method en Java). Hemos visto antes que *self* es la palabra clave que se usa para referirse a la propia instancia (al objeto), en cambio *cls* es usada por convención (puede usarse otro nombre) para referirse a la copia del prototipo de la clase

Si quieres saber más de @classmethod, mira el siguiente [enlace](https://docs.python.org/3/library/functions.html#classmethod).

Si quieres saber más de @staticmethod, mira el siguiente [enlace](https://docs.python.org/3/library/functions.html#staticmethod).

## Metodos privados

Un método privado es aquel sólo accesible dentro de la propia clase. Se usa para definir métodos auxiliares que no necesitamos exponer fuera de la clase (esto se llama **encapsulación**). 

Los métodos privados como tal no existen en Python. En Java tenemos la palabra clave *private* para declarar un método como privado. En python lo equivalente es lo siguiente:

```python
class Persona:
  
  def metodo_publico(self):
    print('dentro del metodo_publico')
    self.__metodo_privado()
    pass
  
  def __metodo_privado(self):
    print('dentro del __metodo_privado')
    pass
```

Como ves la diferencia esta en el que nombre empieza por  **__(dos guiones bajos).**

Si lo probamos, verás que no puedes llamar a __metodo_privado:

```python
persona = Persona()
persona.metodo_publico()
persona.__metodo_privado() # Lanza un error
```

En cambio podemos llamarlo realmente:

```python
persona._Persona__metodo_privado() # ¡Estamos llamando al método privado!
```

Por este motivo, realmente no es un método privado :cowboy_hat_face:.

## None es Null

Una instancia no es más que una referencia a una dirección de memoria, una variable que apunta a un objeto. Puede ser que tengamos una variable *vacia*, es decir, que no apunte a ninguna dirección de memoria (Un string vacio si ocupa memoria :+1:).

Para representar eso, existe el tipo None en Python:

```python
no_ocupo_memoria = None
print(type(no_ocupo_memoria)) # imprime <class 'NoneType'>
```

## Test yourself! :100:

En este laboratorio os proponemos el siguiente reto:

_Crear una clase Hero con cuatro atributos: nombre, sexo, saludo y nivel (del 1 al 100). Crea varios personajes y crea un método lucha que recibirá dos parámetros, de tipo Hero y en base al nivel de poder mostrará un saludo o otro. Por cierto comprueba que los parámetros no sean nulos._

## Siguientes pasos :rocket:

Este laboratorio ha sido denso, pero hemos conseguido ser expertos en POO. En el siguiente le toca el turno a las excepciones :negative_squared_cross_mark:.



[< Lab 03](../lab-03) | [Lab 05 >](../lab-05)



<p align="center">
    <img src="../resources/header.png">
</p>

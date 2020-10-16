<p align="center">
    <img src="../resources/header.png">
</p>

# Lab 05 - El mundo de las excepciones

## Indice

1. [Excepciones](#excepciones)
2. [Test yourself!](#test-yourself-100)

## Excepciones

Una excepción es un error que interrumple la ejecución normal del programa. Un error típico podría ser dividir por 0:

```python
>>> a = 5
>>> b = 0
>>> a/b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Como veis Python ha lanzado la excepción **ZeroDivisionError**.

La excepciones pueden capturarse, es decir, puede ser que tengamos error internos controlados y queramos hacer una cosa u otra en función del error.

Para ello existe el bloque **try..except**:

```python
numero = "Hola"
try:
  int(numero)
except:
  print('Eyy! Eso no es un numero')

print('El programa continua... porque hemos capturado la excepción')
```

En otro caso el error hubiera sido:

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'Hola'
```

Podemos capturar una excepción concreta:

```python
numero = "Hola"
try:
  int(numero)
except ValueError:
  print('Eyy! Eso no es un numero')

print('El programa continua... porque hemos capturado la excepción')
```

En el mismo try, podríamos tener tantos except como queramos.

Existe el bloque **finally** que se ejecuta siempre, haya o no una excepción:

```python
numero = "Hola"
try:
  int(numero)
except ValueError:
  print('Eyy! Eso no es un numero')
finally:
  print('Yo me ejecuto siempre')
```

Por otro lado, podemos meter un **else**, igual que ocurría con el bucle for y while. En este caso, se ejecuta si todo ha ido bien:

```python
numero = "Hola"
try:
  int(numero)
except ValueError:
  print('Eyy! Eso no es un numero')
else:
  print('Yo me ejecuto si todo ha ido ok')
finally:
  print('Yo me ejecuto siempre')
```

[^1]: Si no recuerdas el else en los bucles, repasa el [lab-02](../lab-02)

## Test yourself! :100:

Las excepciones son muy importantes en programación, por lo que te animo a hacer el siguiente reto con mucho detalle:

_Define un método que reciba una palabra y devuelva el numero de vocales diferentes que contiene. Debes comprobar que sea un string. En caso de que no sea un string lanzaras una excepción de tipo ValueError. En caso de que no tenga vocales lanzaras una excepción propia NoVocalsError. Si tiene al menos una vocal, retornaras el número. El programa llamante tendra que capturas las dos excepciones e imprimir mensajes diferentes._

> Las excepciones propias no son mas que clases derivadas de Exception, si se quiere mostrar un mensaje con dejar la definición por defecto es suficiente:
>
> ```python
> class NoVowelsError(Exception):
>   pass
> ```

## Siguientes pasos :rocket:

En este laboratorio hemos trabajado con el concepto de excepción. En el siguiente laboratorio terminaremos la primera parte del Openathon con la instalción de parquetes Python mediante pip.



[< Lab 04](../lab-04) | [Lab 06 >](../lab-06)

<p align="center">
    <img src="../resources/header.png">
</p>

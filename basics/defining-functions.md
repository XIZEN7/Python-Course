# Definición de funciones personalizadas

## ¿Por qué debo usar funciones personalizadas?

Echa un vistazo a este código:

```python
print("************")
print("Hello World!")
print("************")

print("*************")
print("Enter a word:")
print("*************")

word = input()

if word == 'python':
    print("*******************")
    print("You entered Python!")
    print("*******************")
else:
    print("**************************")
    print("You didn't enter Python :(")
    print("**************************")
```

Luego compáralo con este código:

```python
print_box("Hello World!")
print_box("Enter a word:")
word = input()
if word == 'python':
    print_box("You entered Python!")
else:
    print_box("You didn't enter Python :(")
```

## Primeras funciones

La palabra clave `pass` no hace nada.

```python
>>> pass
>>>
```

Usémoslo para definir una función que no hace nada.

```python
>>> def do_nothing():
...     pass
...
>>> do_nothing
<function do_nothing at 0x7f56b74e9598>
>>>
```

Parece estar funcionando hasta ahora, tenemos una función. Es solo un valor que
se asigna a una variable llamada `do_nothing`. Puedes ignorar el
Cosas `0xblablabla` por ahora.

Aquí se necesita el `pase` porque sin él, Python no sabe cuándo
la función finaliza y nos da un error de sintaxis. No necesitamos el
`pass` cuando nuestras funciones contienen algo más.

Veamos qué sucede si llamamos a nuestra función.

```python
>>> do_nothing()
>>>
```

Aquí vamos. No hizo nada en absoluto.

¿Tal vez podríamos hacer algo en la función en su lugar?

```python
>>> def print_hi():
...     print("Hi!")
...
>>> print_hi()
Hi!
>>>
```

Esta funcionando. ¿Qué tal print una variable en la función?

```python
>>> def print_message():
...     print(message)
...
>>> message = "Hello World!"
>>> print_message()
Hello World!
>>>
```

De nuevo, funciona. ¿Qué hay de establecer una variable en la función?

```python
>>> def get_username():
...     username = input("Username: ")
...
>>> get_username()
Username: me
>>> username
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'username' is not defined
>>>
```

¡Eso fue raro! ¿Por qué no funcionó?

## Locales y globales

Hasta ahora no hemos usado nada más que **variables globales**. Se les llama
globales porque las mismas variables están disponibles en cualquier parte de nuestro
programa, incluso en funciones.

```python
>>> a = 1
>>> b = "hi"
>>> c = "hello"
>>> def print_abc():
...     print(a, b, c)
...
>>> print_abc()
1 hi hello
>>>
```

Pero también hay **variables locales**. Solo existen **dentro**
funciones, y se eliminan cuando la función sale.

```python
>>> def thingy():
...     d = "hello again, i'm a local variable"
...     print('inside thingy:', d)
...
>>> thingy()
inside thingy: hello again, i'm a local variable
>>> d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>>
```

Dibujemos un diagrama de estas variables:

![Locales y globales.](../images/locals-and-globals.png)

Sin embargo, modificar una variable global en el lugar desde una función es fácil.

```python
>>> stuff = ['global stuff']
>>> def add_stuff():
...     stuff.append('local stuff')
...
>>> add_stuff()
>>> stuff
['global stuff', 'local stuff']
>>>
```

Esto solo funciona para cambiar en el lugar, no podemos asignar un nuevo valor a
La variable.

```python
>>> def set_stuff_to_something_new():
...     stuff = ['more local stuff']
...
>>> set_stuff_to_something_new()
>>> stuff
['global stuff', 'local stuff']
>>>
```

## Input

**Nota:** Esta sección no tiene nada que ver con la función `input` que
se usa como `word = input ("ingrese algo:")`.

Hasta ahora nuestras funciones parecen estar realmente aisladas del resto de nuestro
¡código, y apesta! Pero en realidad no están tan aislados como podrías
creo que lo son.

Pensemos en lo que hace la función de print. Se necesita un argumento
y lo imprime. ¿Quizás una función personalizada también podría tomar un argumento?

```python
>>> def print_twice(message):
...     print(message)
...     print(message)
...
>>>
```

Aquí `message` es un argumento. Cuando llamemos a la función obtendremos un
variable local llamada mensaje que apuntará a lo que sea que pasemos
a `print_dos veces`.

Esta función se puede llamar de dos maneras:

- Usar un **argumento posicional**.

  Esta es la forma recomendada para funciones que toman solo uno o dos
  argumentos Yo haría esto en mi código.

  ```python
  >>> print_twice("hi")
  hi
  hi
  >>>
  ```

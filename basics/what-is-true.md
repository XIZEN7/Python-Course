# Booleanos

## Converting to Booleans

Como podemos ver, el valor booleano de la mayoría de las cadenas es True. los
la única cadena que tiene un valor booleano falso es la cadena vacía,
`''` o `""`:

```python
>>> bool('')
False
>>>
```

La mayoría de las otras cosas también se tratan como False si están vacías y
True si no están vacíos.

```python
>>> bool([1, 2, 3])
True
>>> bool([])
False
>>> bool((1, 2, 3))
True
>>> bool(())
False
>>> bool({'a': 1, 'b': 2})
True
>>> bool({})
False
>>>
```

None and zero atambién son números falsos, pero positivos y negativos.
son tratados como True

```python
>>> bool(None)
False
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool(1)
True
>>> bool(-1)
True
>>>
```

La mayoría de las otras cosas también se tratan como verdaderas.

```python
>>> bool(OSError)
True
>>> bool(print)
True
>>>
```

## ¿Cuándo y por qué debemos usar los valores booleanos de las cosas?

Se recomienda confiar en el valor booleano cuando estamos haciendo
algo con cosas como listas y tuplas. De esta manera nuestro código
funcionará incluso si obtiene un valor de un tipo diferente al que nosotros
esperaba que llegara originalmente.

Por ejemplo, este código no funciona bien si le damos
algo más que una lista. Piensa que tuplas vacías,
las cadenas y los diccionarios no están vacíos solo porque no lo están
listas vacías:

```python
>>> def is_this_empty(thing):
...     if thing == []:
...         print("It's empty!")
...     else:
...         print("It's not empty.")
...
>>> is_this_empty([1, 2, 3])
It's not empty.
>>> is_this_empty([])
It's empty!
>>> is_this_empty(())
It's not empty.
>>> is_this_empty('')
It's not empty.
>>> is_this_empty({})
It's not empty.
>>>
```

Podríamos mejorar el código comparándolo con diferentes vacíos
cosas.

```python
>>> def is_this_empty(thing):
...     if thing == [] or thing == () or thing == '' or thing == {}:
...         print("It's empty!")
...     else:
...         print("It's not empty.")
...
>>>
```

También hay casos en los que no debemos confiar en el valor booleano.
Cuando estamos haciendo cosas con números y Zero, es mejor
simplemente compare con None o Zero. Como esto:

```python
if number != 0:
    print("number is not zero")

if value is not None:
    print("value is not None")
```

Not like this:

```python
if number:
    print("number is not zero")

if value:
    print("value is not None")
```

Usamos `is not` en lugar de `!=` en el primer ejemplo porque
la guía oficial lo recomienda. La razón es que es posible crear un valor que no es realmente None pero parece
None cuando lo comparamos con None usando `==` o `!=`, y queremos
para asegurarnos de que no tratamos valores como None.

Entonces, así es como debemos verificar si algo es None:

```python
if not value: ...      # no es bueno si queremos verificar None
if value == None: ...  # Mejor
```

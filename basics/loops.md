# Bucles

En programación, un **bucle** significa repetir algo varias veces.
Hay diferentes tipos de bucles:

- [While loops](#while-loops) repiten algo mientras una condición es verdadera.
- [Not While](#notw-loops) repetir algo mientras una condición es falsa.
- [For loops](#for-loops) repetir algo para cada elemento de algo.

## While loops

Los bucles while son muy similares a las sentencias if.

```python
its_raining = True
while its_raining:
    print("Oh crap, it's raining!")
print("It's not raining anymore.")
```

Si no está familiarizado con los bucles while, la salida del programa puede ser un
un poco sorprendente:

      it's raining!
      it's raining!
      it's raining!
      it's raining!
        (etc...)

En este ejemplo, `its_raining` fue la **condición**. si algo en
el ciclo while habría establecido `its_raining` en False, el ciclo
habría terminado y el programa habría impreso `Ya no llueve`.

Vamos a crear un programa que haga justamente eso:

```python
its_raining = True
while its_raining:
    print("It's raining!")
    answer = input("Or is it? (y=yes, n=no) ")
    if answer == 'y':
        print("Oh well...")
    elif answer == 'n':
        its_raining = False     # fin del bucle while
    else:
        print("Enter y or n next time.")
print("It's not raining anymore.")
```

Corriendo el programa>

    It's raining!
    Or is it? (y=yes, n=no) i dunno
    Enter y or n next time.
    It's raining!
    Or is it? (y=yes, n=no) y
    Oh well...
    It's raining!
    Or is it? (y=yes, n=no) n
    It's not raining anymore.

El ciclo while no verifica la condición todo el tiempo, solo verifica
al principio.

```python
>>> its_raining = True
>>> while its_raining:
...     its_raining = False
...     print("It's not raining, but the while loop doesn't know it yet.")
...
It's not raining, but the while loop doesn't know it yet.
>>>
```

También podemos interrumpir un ciclo incluso si la condición sigue siendo verdadera usando
la palabra clave `romper`. En este caso, estableceremos la condición en True y confiaremos
en nada más que `break` para finalizar el ciclo.

```python
while True:
    answer = input("Is it raining? (y=yes, n=no) ")
    if answer == 'y':
        print("It's raining!")
    elif answer == 'n':
        print("It's not raining anymore.")
        break   # end the loop
    else:
        print("Enter y or n.")
```

La salida del program es está:

    Is it raining? (y=yes, n=no) who knows
    Enter y or n.
    Is it raining? (y=yes, n=no) y
    It's raining!
    Is it raining? (y=yes, n=no) n
    It's not raining anymore.

A diferencia de establecer la condición en False, romper el ciclo lo finaliza.
inmediatamente.

```python
>>> while True:
...     break
...     print("This is never printed.")
...
>>>
```

## While not

```python
raining = False
while not raining:
    print("It's not raining.")
    if input("Is it raining? (y/n) ") == 'y':
        raining = True
print("It's raining!")
```

## For loops

Digamos que tenemos [una lista](lists-and-tuples.md) de cosas que queremos
impresión. Para imprimir cada elemento en él, podríamos hacer un montón de impresiones:

```python
stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']

print(stuff[0])
print(stuff[1])
print(stuff[2])
print(stuff[3])
print(stuff[4])
```

La salida del programa es esta:

    hello
    hi
    how are you doing
    im fine
    how about you

Pero esto solo imprimirá cinco elementos, por lo que si agregamos algo a
cosas, no se va a imprimir. O si quitamos algo de
cosas, obtendremos un error que dice "índice de lista fuera de rango".

También podríamos crear una variable de índice y usar un bucle while:

```python
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> length_of_stuff = len(stuff)
>>> index = 0
>>> while index < length_of_stuff:
...     print(stuff[index])
...     index += 1
...
hello
hi
how are you doing
im fine
how about you
>>>
```

Pero tenemos `len()` y una variable de índice que necesitamos incrementar y una
while loop y muchas otras cosas de las que preocuparse. eso es mucho trabajo
solo para imprimir cada artículo.

Aquí es cuando entran los bucles for:

Ejemplos:

```python
>>> for thing in stuff:
...     # esto se repite para cada elemento de cosas, es decir, primero
...     # for stuff[0], luego for stuff[1], etc.
...     print(thing)
...
hello
hi
how are you doing
im fine
how about you
>>>
```

```python
>>> for short_string in 'abc':
...     print(short_string)
...
a
b
c
>>> for item in (1, 2, 3):
...     print(item)
...
1
2
3
>>>
```

Si podemos hacer un bucle for sobre algo, entonces ese algo es **iterable**.
Las listas, tuplas y cadenas son todas iterables.

Solo hay una gran limitación para recorrer las listas. Nosotros
no debe modificar la lista en el bucle for. Si lo hacemos, los resultados pueden
ser sorprendente:

```python
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> for thing in stuff:
...     stuff.remove(thing)
...
>>> stuff
['hi', 'im fine']
>>>
```

En su lugar, podemos crear una copia de stuff y recorrerlas.

```python
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> for thing in stuff.copy():
...     stuff.remove(thing)
...
>>> stuff
[]
>>>
```

O si solo queremos borrar una lista, podemos usar `clear`

```python
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> stuff.clear()
>>> stuff
[]
>>>
```

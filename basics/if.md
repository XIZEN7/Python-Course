# If, else y elif

## Uso de sentencias if

Ahora sabemos lo que es Verdadero y Falso.

```python
>>> 1 == 1
True
>>> 1 == 2
False
>>>
>>> its_raining = True
>>> its_raining
True
>>>
```

Pero, ¿y si queremos ejecutar código diferente dependiendo de algo?
Ahí es cuando entra el `if`.

```python
>>> its_raining = True
>>> if its_raining:
...     print("It's raining!")
...
It's raining!
>>> its_raining = False
>>> if its_raining:
...     print("It's raining!")        # nothing happens
...
>>>
```

El aviso cambió de `>>>` a `...`. Significaba que Python está
esperando que siga escribiendo. Cuando terminé, solo presioné Enter
dos veces.

Una cosa importante a tener en cuenta es que la línea con una impresión es la
**indentación**. Puede presionar la tecla tabulador, o si no funciona
solo presiona espacio unas cuantas veces.

Pero, ¿por qué es `if its_raining` en lugar de `if (its_raining)`?

`if` es una **palabra clave**.

```python
>>> if = 123
  File "<stdin>", line 1
    if = 123
       ^
SyntaxError: invalid syntax
>>>
```

**Funciones** como `imprimir` necesitan `()` después de su nombre para funcionar. Pero `if`
es **una palabra clave**, no una función, por lo que no necesita `()`. pitón tiene
funciones y palabras clave separadas porque es posible crear funciones personalizadas
funciones, pero no es posible crear palabras clave personalizadas. Es por eso
Las palabras clave generalmente se usan para cosas "mágicas" que serían difíciles de
hacer con sólo funciones.

También tenga en cuenta que las sentencias if comprueban la condición una sola vez, por lo que si es asi
configúrelo como falso más tarde, la declaración if no lo notará.

```python
>>> its_raining = True
>>> if its_raining:
...     its_raining = False
...     print("It's not raining, but this runs anyway.")
...
It's not raining, but this runs anyway.
>>>
```

## Usando else

¿Qué pasa si queremos imprimir un mensaje diferente si no está lloviendo? Nosotros
podría hacer algo como esto:

```python
its_raining = True
its_not_raining = not its_raining

if its_raining:
    print("It's raining!")
if its_not_raining:
    print("It's not raining.")
```

Ahora nuestro programa imprimirá un valor diferente dependiendo de lo que
el valor de `its_raining`

También podemos agregar `not its_raining` directamente a la segunda declaración if:

```python
its_raining = True

if its_raining:
    print("It's raining!")
if not its_raining:
    print("It's not raining.")
```

Pero podemos hacerlo aún mejor usando `else`.

```python
its_raining = True

if its_raining:
    print("It's raining!")
else:
    print("It's not raining.")
```

La parte else simplemente se ejecuta cuando la instrucción if no se ejecuta. no lo hace
verifique la condición nuevamente.

```python
>>> its_raining = True
>>> if its_raining:
...     its_raining = False
... else:
...     print("It's not raining, but this still doesn't run.")
...
>>>
```

Combinando `else` con la función de entrada podemos hacer un programa que
pide una contraseña y comprueba si es correcta.

```python
print("Hello!")
password = input("Enter your password: ")

if password == "secret":
    print("That's correct, welcome!")
else:
    print("Access denied.")
```

El programa imprime diferentes cosas dependiendo de lo que ingresemos:

```
Hello!
Enter your password: secret
Welcome!
```

```
Hello!
Enter your password: lol
Access denied.
```

Usar la función de ingreso de contraseñas no funciona muy bien porque
no podemos ocultar la contraseña con asteriscos. Hay mejores formas de conseguir
una contraseña del usuario, pero no debe preocuparse por eso todavía.

## Evitar la indentation con elif

Si tenemos más de una condición para verificar, podríamos hacer esto:

```python
print("Hello!")
word = input("Enter something: ")

if word == "hi":
    print("Hi to you too!")
else:
    if word == "hello":
        print("Hello hello!")
    else:
        if word == "howdy":
            print("Howdyyyy!")
        else:
            if word == "hey":
                print("Hey hey hey!")
            else:
                if word == "gday m8":
                    print("Gday 4 u 2!")
                else:
                    print("I don't know what", word, "means.")
```

Este código es un desastre. Necesitamos indentar cada vez mas para verificar más palabras. Aquí buscamos 5 palabras diferentes, por lo que tenemos 5 niveles
de indentación. Si tuviéramos que comprobar 30 palabras, el código sería
volverse muy ancho y sería difícil trabajar con él.

En lugar de escribir `else`, indentar mas y escribir `if` podemos
simplemente escribir `elif`, que es la abreviatura de `else if`. así:

```python
print("Hello!")
word = input("Enter something: ")

if word == "hi":
    print("Hi to you too!")
elif word == "hello":
    print("Hello hello!")
elif word == "howdy":
    print("Howdyyyy!")
elif word == "hey":
    print("Hey hey hey!")
elif word == "gday m8":
    print("Gday 4 u 2!")
else:
    print("I don't know what", word, "means.")
```

Ahora el programa es más corto y mucho más fácil de leer.

Tenga en cuenta que las partes `elif` solo se ejecutan si nada antes de ellas coincide, y `else` se ejecuta solo cuando ninguno de los `elifs` coincide. si tuviéramos
usa `if` en su lugar, todos los valores posibles siempre serán verificados y el
La parte `else` se ejecutaría siempre excepto cuando la palabra sea `"gday m8"`. Esto es
por qué usamos `elif` en lugar de `if`.

Por ejemplo, este programa imprime solo `hello`...

```python
if 1 == 1:
    print("hello")
elif 1 == 2:
    print("this is weird")
else:
    print("world")
```

...but this prints `hello` _and_ `world`:

```python
if 1 == 1:
    print("hello")
if 1 == 2:
    print("this is weird")
else:
    print("world")
```

Ahora `else` pertenece a la parte `if 1 == 2` y **no tiene nada que
ver con la parte `if 1 == 1`. Por otro lado, la versión elif
**agrupó los múltiples ifs juntos\*\* y `else` pertenecía a todos
a ellos. Agregar una línea en blanco hace que esto sea obvio:

```python
if 1 == 1:
    print("hello")

if 1 == 2:
    print("this is weird")
else:
    print("world")
```

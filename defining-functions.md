# Definición de funciones personalizadas

Probablemente ha pasado un tiempo desde que leíste sobre el uso de funciones.
[Lea sobre esto nuevamente] (using-functions.md) si es necesario.

## ¿Por qué debo usar funciones personalizadas?

Echa un vistazo a este código:

```python
print("************")
print("¡Hola mundo!")
print("************")

print("*************")
print("Ingrese una palabra:")
print("*************")

palabra = entrada()

si palabra == 'python':
    print("*******************")
    print("¡Usted ingresó a Python!")
    print("*******************")
más:
    print("**************************")
    print("No ingresaste Python :(")
    print("**************************")
```

Luego compáralo con este código:

```python
print_box("¡Hola mundo!")
print_box("Ingrese una palabra:")
palabra = entrada()
si palabra == 'python':
    print_box("¡Has entrado en Python!")
más:
    print_box("No ingresaste Python :(")
```

En este tutorial aprenderemos a definir una función `print_box`
que imprime texto en un cuadro. Podemos escribir el código para print el
cuadro una vez, y luego utilícelo varias veces en cualquier parte del programa.

[Dividir un programa largo en funciones simples](larger-program.md) también
hace que el código sea más fácil de trabajar. Si hay un problema con el código
podemos probar las funciones una por una y encontrar el problema fácilmente.

## Primeras funciones

La palabra clave `pass` no hace nada.

```python
>>> pass
>>>
```

Usémoslo para definir una función que no hace nada.

```python
>>> def hacer_nada():
...     pass
...
>>> hacer_nada
<función no hacer nada en 0x7f56b74e9598>
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
>>> hacer_nada()
>>>
```

Aquí vamos. No hizo nada en absoluto.

¿Tal vez podríamos hacer algo en la función en su lugar?

```python
>>> def print_hola():
... print("¡Hola!")
...
>>> print_hola()
¡Hola!
>>>
```

Esta funcionando. ¿Qué tal print una variable en la función?

```python
>>> def print_mensaje():
... print (mensaje)
...
>>> mensaje = "¡Hola mundo!"
>>> print_mensaje()
Hola Mundo!
>>>
```

De nuevo, funciona. ¿Qué hay de establecer una variable en la función?

```python
>>> def obtener_nombre_de_usuario():
... nombre de usuario = entrada ("Nombre de usuario:")
...
>>> obtener_nombre_de_usuario()
nombre de usuario: yo
>>> nombre de usuario
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
>>> un = 1
>>> b = "hola"
>>> c = "hola"
>>> def print_abc():
... print (a, b, c)
...
>>> print_abc()
1 hola hola
>>>
```

Pero también hay **variables locales**. Solo existen **dentro**
funciones, y se eliminan cuando la función sale.

```python
>>> def cosita():
... d = "hola de nuevo, soy una variable local"
... print ('cosa interior:', d)
...
>>> cosita()
cosita interior: hola de nuevo, soy una variable local
>>> re
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>>
```

Dibujemos un diagrama de estas variables:

![Locales y globales.](../images/locals-and-globals.png)

Sin embargo, modificar una variable global en el lugar desde una función es fácil.

```python
>>> cosas = ['cosas globales']
>>> def añadir_cosas():
... cosas.append('cosas locales')
...
>>> añadir_cosas()
>>> cosas
['cosas globales', 'cosas locales']
>>>
```

Esto solo funciona para cambiar en el lugar, no podemos asignar un nuevo valor a
La variable.

```python
>>> def poner_cosas_en_algo_nuevo():
... cosas = ['más cosas locales']
...
>>> poner_cosas_en_algo_nuevo()
>>> cosas
['cosas globales', 'cosas locales']
>>>
```

## Aporte

**Nota:** Esta sección no tiene nada que ver con la función `input` que
se usa como `palabra = entrada ("ingrese algo:")`.

Hasta ahora nuestras funciones parecen estar realmente aisladas del resto de nuestro
¡código, y apesta! Pero en realidad no están tan aislados como podrías
creo que lo son.

Pensemos en lo que hace la función de print. Se necesita un argumento
y lo imprime. ¿Quizás una función personalizada también podría tomar un argumento?

```python
>>> def print_dos veces(mensaje):
... print (mensaje)
... print (mensaje)
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
  >>> print_dos veces("hola")
  hola
  hola
  >>>
  ```

  Cuando la función la estaba ejecutando

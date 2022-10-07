# Definición y uso de clases personalizadas

## ¿Qué son las clases?

Python viene con muchas clases que ya conocemos.

```python
>>> str
<class 'str'>
>>> int
<class 'int'>
>>> list
<class 'list'>
>>> dict
<class 'dict'>
>>>
```

Llamando a estas clases como si fueran funciones crear una nueva **instancia**
de esta. Por ejemplo, `str()` crea una instancia de `str`, también conocida como
string.

```python
>>> str()
''
>>> int()
0
>>> list()
[]
>>> dict()
{}
>>>
```

También podemos obtener la clase de una instancia con `type()`:

```python
>>> type('')
<class 'str'>
>>> type(0)
<class 'int'>
>>> type([])
<class 'list'>
>>> type({})
<class 'dict'>
>>>
```

Digamos que hacemos un programa que procesa datos sobre sitios web.
Con una clase personalizada, no estamos limitados a `str`, `int` y otras clases
Python viene con. En su lugar, podemos definir una clase de sitio web y hacer
Sitios web y procesar información sobre sitios web directamente. Definiendo nuestro
tipos propios como este se llama **programación orientada a objetos**.

## Primera clase

En Python, `pass` no hace nada.

```python
>>> pass
>>>
```

Usémoslo para definir una clase vacía.

```python
>>> class Website:
...     pass
...
>>> Website
<class '__main__.Website'>
>>>
```

El `pass` es necesario aquí, al igual que [cuando se definen funciones que no
nada](definiendo-funciones.md#primeras-funciones).

```python
>>> github = Website()
>>> github
<__main__.Website object at 0x7f36e4c456d8>
>>> type(github)
<class '__main__.Website'>
>>>
```

Podemos decir que `github` es "una instancia de sitio web", "un sitio web
objeto" o "un sitio web". Todos estos significan lo mismo.

Ahora podemos adjuntar más información sobre github a nuestro sitio web.

```python
>>> github.url = 'https://github.com/'
>>> github.founding_year = 2008
>>> github.free_to_use = True
>>>
```

También podemos acceder a la información fácilmente.

```python
>>> github.url
'https://github.com/'
>>> github.founding_year
2008
>>> github.free_to_use
True
>>>
```

Como puede ver, nuestro sitio web es mutable, como lo son las listas, no inmutable
como son los strings. Podemos cambiar el sitio web en el lugar sin crear un
nuevo sitio web.

`url`, `founding_year` y `free_to_use` no son variables, son
**atributos**. Más específicamente, son **atributos de instancia**.
La mayor diferencia es que necesitamos usar un punto para establecer y
obteniendo valores de atributos, pero no necesitamos eso con variables.

Los módulos también usan atributos de instancia para acceder a su contenido. Para
ejemplo, cuando hacemos `random.randint`, `random` es una instancia de módulo y
`randint` es uno de sus atributos.

Si creamos otro sitio web, ¿tiene la misma `url`, `founding_year`?
y `free_to_use`?

```python
>>> effbot = Website()
>>> effbot.url
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Website' object has no attribute 'url'
>>>
```

Primero necesitamos definir los atributos para effbot también.

Los atributos se almacenan en un diccionario llamado `__dict__`. No es
recomienda usarlo para el código que necesita ser confiable, pero es un
forma práctica de ver qué atributos contiene la instancia.

```python
>>> github.__dict__
{'free_to_use': True,
 'founding_year': 2008,
 'url': 'https://github.com/'}
>>> effbot.__dict__
{}
>>>
```

## Atributos de clase

¿Qué sucede si establecemos un atributo de la clase 'Sitio web' en algún valor?
en lugar de hacer eso a una instancia?

```python
>>> Website.is_online = True
>>> Website.is_online
True
>>>
```

## Funciones y métodos

Vamos a [definir una función](defining-functions.md) que imprima información
sobre un sitio web.

```python
>>> def website_info(website):
...     print("URL:", website.url)
...     print("Founding year:", website.founding_year)
...     print("Free to use:", website.free_to_use)
...
>>> website_info(github)
URL: https://github.com/
Founding year: 2008
Free to use: True
>>>
```

Parece estar funcionando. Deberíamos poder obtener información sobre todos
sitios web, así que tal vez deberíamos adjuntar la función `website_info` al
Clase de sitio web?

```python
>>> Website.info = website_info
>>> Website.info(github)
URL: https://github.com/
Founding year: 2008
Free to use: True
>>>
```

Está funcionando, pero `Website.info(github)` requiere mucho tipeo, así que
¿No sería mucho mejor `github.info()`?

```python
>>> github.info()
URL: https://github.com/
Founding year: 2008
Free to use: True
>>>
```

¿Qué diablos pasó? No definimos un `github.info`, simplemente
trabajado mágicamente!

`Website.info` es nuestra función `website_info`, así que `github.info`
también debe ser la misma función. Pero `Website.info` toma un `sitio web`
argumento, que no le dimos cuando llamamos a `github.info()`!

¿Pero `github.info` es lo mismo que `Website.info`?

```python
>>> Website.info
<function website_info at 0x7f36e4c39598>
>>> github.info
<bound method website_info of <__main__.Website object at 0x7f36e4c456d8>>
>>>
```

No lo es.

En cambio, `github.info` es un **método**. Si establecemos una función como
atributo de clase, las instancias tendrán un método con el mismo nombre.
Los métodos son "enlaces" a las funciones de atributo de clase. Asi que
`Website.info(github)` hace lo mismo que `github.info()`,
y cuando se llama a `github.info()`, se obtiene automáticamente
`github` como argumento.

En otras palabras, **`Class.method(instance)` hace lo mismo que
`instancia.método()`**. Esto también funciona con clases integradas, por
ejemplo `'hello'.lower()` es lo mismo que `str.lower('hello')`.

## Definición de métodos al definir la clase

Tal vez podríamos definir un método cuando hacemos la clase en lugar de agregar
¿eso mas tarde?

```python
>>> class Website:
...     def info(self):     # self será github
...         print("URL:", self.url)
...         print("Founding year:", self.founding_year)
...         print("Free to use:", self.free_to_use)
...
>>> github = Website()
>>> github.url = 'https://github.com/'
>>> github.founding_year = 2008
>>> github.free_to_use = True
>>> github.info()
URL: https://github.com/
Founding year: 2008
Free to use: True
>>>
```

Esta funcionando. El argumento `self` en `Website.info` era `github`.
También podrías llamarlo de otra forma, como `yo`, `este` o `instancia`,
pero usa `self` en su lugar. Otros usuarios de Python se han acostumbrado y
la guía de estilo oficial también lo recomienda.

Todavía necesitamos configurar `url`, `founding_year` y `free_to_use` manualmente.
¿Tal vez podríamos agregar un método para hacer eso?

```python
>>> class Website:
...     def initialize(self, url, founding_year, free_to_use):
...         self.url = url
...         self.founding_year = founding_year
...         self.free_to_use = free_to_use
...     def info(self):
...         print("URL:", self.url)
...         print("Founding year:", self.founding_year)
...         print("Free to use:", self.free_to_use)
...
>>> github = Website()
>>> github.initialize('https://github.com/', 2008, True)
>>> github.info()
URL: https://github.com/
Founding year: 2008
Free to use: True
>>>
```

Eso funciona. Los atributos que definimos en el método de inicialización también son
disponible en el método info. También podríamos acceder a ellos directamente desde
`github`, por ejemplo con `github.url`.

Pero todavía tenemos que llamar a `github.initialize`. En Python, hay
un método "mágico" que se ejecuta cuando creamos un nuevo sitio web llamando al
Clase de sitio web. Se llama `__init__` y no hace nada por defecto. Si
nuestro método `__init__` toma otros argumentos además de uno mismo, podemos llamar al
class con argumentos y se le darán a `__init__`. Como esto:

```python
>>> class Website:
...     def __init__(self, url, founding_year, free_to_use):
...         self.url = url
...         self.founding_year = founding_year
...         self.free_to_use = free_to_use
...     def info(self):
...         print("URL:", self.url)
...         print("Founding year:", self.founding_year)
...         print("Free to use:", self.free_to_use)
...
>>> github = Website('https://github.com/', 2008, True)
>>> github.info()
URL: https://github.com/
Founding year: 2008
Free to use: True
>>>
```

## ¿Cuándo debo usar las clases?

No hagas esto:

```python
class MyProgram:

    def __init__(self):
        print("Hello!")
        word = input("Enter something: ")
        print("You entered " + word + ".")


program = MyProgram()
```

Debes evitar usar cosas como `print` y `input` en `__init__`
método. El método `__init__` debe ser simple y solo debe establecer
cosas claras.

Por lo general, no debería usar una clase si solo va a hacer una
instancia de él, y tampoco necesita una clase si solo va
tener un método. En este ejemplo, `MyProgram` tiene solo un método y
solo una instancia.

Haga funciones en su lugar, o simplemente escriba su código sin ninguna función si
es lo suficientemente corto para eso. Este programa hace lo mismo y es
mucho más legible:

```python
print("Hello!")
word = input("Enter something: ")
print("You entered " + word + ".")
```

# Diccionarios

Ahora sabemos cómo funcionan [lists and tuples](lists-and-tuples.md) y cómo
a [for loop](loops.md#for-loops) sobre ellos. Si hacemos algún tipo de
programa que necesita realizar un seguimiento de los nombres de las personas y sus mascotas favoritas,
podemos usar una lista para eso:

```python
names_and_pets = [
    ('Cristina', 'gatos'),
    ('Carlos', 'Perros y gatos'),
    ('Luna', 'gatos'),
]
```

Luego, para comprobar si los gatos son las mascotas favoritas de Cristina, podemos hacer
`('Cristina', 'gatos') en nombres_y_mascotas`. O podemos agregar nuevas personas
mascotas favoritas fácilmente agregando nuevas tuplas `(nombre, mascotas)` a la lista.

Pero, ¿y si necesitamos verificar si sabemos algo sobre la
mascotas favoritas? `'Carlos' en nombres_y_mascotas` siempre es Falso porque el
lista de mascotas consta de pares `(nombre, mascotas)` en lugar de solo nombres, por lo que
necesita hacer un bucle sobre toda la lista de mascotas:

```python
found_Carlos = False
for pair in names_and_pets:
    if pair[0] == 'Carlos':
        found_Carlos = True
        break
if found_Carlos:
```

¿O si necesitamos saber cuáles son las mascotas favoritas de Carlos? Que
también requiere revisar toda la lista.

```python
pets = None
for pair in names_and_pets:
    if pair[0] == 'Carlos':
        pets = pair[1]
        break
# asegúrese de que las mascotas no sean Ninguna y haga algo con ellas
```

Como puede ver, una lista de pares `(name, pets)` no es ideal
manera de almacenar nombres y mascotas favoritas.

## ¿Qué son los diccionarios?

Una mejor manera de almacenar información sobre mascotas favoritas podría ser un
diccionario:

```python
favorite_pets = {
    'Cristina': 'gatos',
    'Carlos': 'Perros y gatos',
    'Luna': 'gatos',
}
```

Aquí `'Cristina'` y `'Carlos'` son **claves** en el diccionario, y
`'gatos'` y `'Perros y gatos'` son sus **valores**. Los diccionarios son
a menudo nombrados por sus valores. Este diccionario tiene mascotas favoritas como su
así que nombré la variable `favorite_pets`.

Hay algunas diferencias importantes entre los diccionarios y las listas de pares:

- Los diccionarios no están ordenados. **No hay garantías** sobre qué
  ordenar que aparezcan los pares `name: pets` cuando hacemos algo
  con el diccionario.
- Verificar si una clave está en el diccionario es simple y rápido. nosotros no
  necesita recorrer todo el diccionario.
- Obtener el valor de una clave también es simple y rápido.
- No podemos tener la misma clave en el diccionario varias veces, pero
  varias claves diferentes pueden tener el mismo valor. Esto significa que
  **varias personas no pueden tener el mismo nombre, pero pueden tener el mismo
  las mismas mascotas favoritas**.

Pero espera... ¡esto se parece mucho a las variables! Nuestras variables no son
ordenado, obtener un valor de una variable es rápido y fácil y no podemos
tienen varias variables con el mismo nombre.

Las variables en realidad se almacenan en un diccionario. podemos conseguir eso
diccionario con la función globals. En este diccionario, las claves son
los nombres y valores de las variables son a lo que apuntan nuestras variables.

```python
>>> globals()
{'names_and_pets': [('Cristina', 'gatos'),
                    ('Carlos', 'Perros y gatos'),
                    ('Luna', 'gatos')],
 'favorite_pets': {'Luna': 'gatos',
                   'Carlos': 'Perros y gatos',
                   'Cristina': 'gatos'},
 ...many other things we don't need to care about...
}
>>>
```

Pero espera... ¡esto se parece mucho a las variables! Nuestras variables no son
ordenadas, obtener un valor de una variable es rápido y fácil y no podemos
tienen varias variables con el mismo nombre.

Las variables en realidad se almacenan en un diccionario. podemos conseguir eso
diccionario con la función globals. En este diccionario, las claves son
los nombres y valores de las variables son a lo que apuntan nuestras variables.

## ¿Qué podemos hacer con los diccionarios?

Los diccionarios tienen algunas similitudes con las listas. Por ejemplo, ambos
las listas y los diccionarios tienen una longitud.

```python
>>> len(names_and_pets)     # contiene 3 elementos
3
>>> len(favorite_pets)    # contiene 3 pares key:value
3
>>>
```

Podemos obtener un valor de una clave con `the_dict[key]`. esto es mucho más fácil
y más rápido que for-looping sobre una lista de pares.

```python
>>> favorite_pets['Carlos']
'Perros y gatos'
>>> favorite_pets['Luna']
'gatos'
>>>
```

Pero podemos agregar nuevos pares `clave: valor` o cambiar los valores de los existentes
llaves haciendo `the_dict[key] = value`.

```python
>>> favorite_pets['Steven'] = 'pinguinos'
>>> favorite_pets['Steven']
'pinguinos'
>>> favorite_pets['Steven'] = 'perros'
>>> favorite_pets['Steven']
'perros'
>>> favorite_pets
{'Luna': 'gatos',
 'Steven': 'perros',
 'Cristina': 'gatos',
 'Carlos': 'Perros y gatos'}
>>>
```

Para recorrer un diccionario obtiene sus claves y verificar si algo
está en el diccionario comprueba si el diccionario tiene una clave como esa. Este
puede ser confuso al principio, pero te acostumbrarás.

```python
>>> 'Steven' in favorite_pets
True
>>> 'perros' in favorite_pets
False
>>> for name in favorite_pets:
...     print(name)
...
Carlos
Steven
Luna
Cristina
>>>
```

Los diccionarios tienen un método de valores que podemos usar si queremos hacer
algo con los valores:

```python
>>> favorite_pets.values()
dict_values(['perros', 'gatos', 'Perros y gatos', 'gatos'])
>>>
```

El método de valores devolvió un objeto `dict_values`. cosas como esta
se comportan de forma muy parecida a las listas y, por lo general, no es necesario convertirlas a una lista.

```python
>>> for pets in favorite_pets.values():
...     print(pets)
...
perros
gatos
Perros y gatos
gatos
>>>
```

## Limitaciones

A veces puede ser útil usar listas como claves de diccionario, pero
simplemente no funciona No voy a explicar por qué Python no permite
esto porque normalmente no tenemos que preocuparnos por eso.

```python
>>> stuff = {['a', 'b']: 'c', ['d', 'e']: 'f'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>>
```

Por otro lado, las tuplas funcionan bien:

```python
>>> stuff = {('a', 'b'): 'c', ('d', 'e'): 'f'}
>>> stuff
{('a', 'b'): 'c', ('d', 'e'): 'f'}
>>>
```

Los valores de un diccionario pueden ser cualquier cosa.

```python
>>> stuff = {'a': [1, 2, 3], 'b': [4, 5, 6]}
>>> stuff
{'a': [1, 2, 3], 'b': [4, 5, 6]}
>>>
```

## Ejemplos

Este programa cuenta cuántas veces aparecen palabras en una oración.
`sentence.split()` crea una lista de palabras en la oración, observa
`help(str.split)` para más información.

```python
sentence = input("Ingrese una oración: ")

counts = {}     # {palabra: contador, ...}
for word in sentence.split():
    if word in counts:
        # Hemos visto esta palabra antes
        counts[word] += 1
    else:
        # Esta es la primera vez que aparece esta palabra
        counts[word] = 1

print()     # Muestra una linea vacia
for word, count in counts.items():
    if count == 1:
        # "1 vez"
        print(word, "aparece una vez en la oración")
    else:
        print(word, "aparece", count, "veces en la oración")
```

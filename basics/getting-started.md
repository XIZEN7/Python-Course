# Comenzando con Python

[Ejecutar Python] (instalación-python.md).

El `>>>` significa que Python está listo y podemos ingresar un comando. los
La idea básica es realmente simple: ingresamos un comando, presionamos Enter, enter
otro comando, presione Entrar y continúe.

Probablemente aún no conozca ningún comando de Python. Veamos qué pasa
si solo escribimos algo y presionamos Enter.

Escribimos python y luego enter

```python
>>>
>>>
>>>
>>>
```

Eso funciono. ¿Qué hay de los números?

```python
>>> 123
123
>>> -123
-123
>>> 3.14
3.14
>>> -12.3
-12.3
>>>
```

Allá vamos, les devuelve el echo.

En algunos países, los números decimales se escriben con una coma, como `3,14`
en lugar de `3.14`. ¿Quizás Python lo sabe?

```python
>>> 3,14
(3, 14)
>>>
```

No recibimos ningún error... ¡pero `(3, 14)` no es lo que esperábamos!
De ahora en adelante, usemos un punto con números decimales, porque `3.14`
funcionó bien Más adelante aprenderemos qué es `(3, 14)`.

## Comentarios

**Los comentarios son texto que no hacen nada cuando se ejecutan.**
Se pueden crear escribiendo un `#` y luego un texto después,
y son útiles cuando nuestro código sería difícil de entender sin ellos.

```python
>>> 1 + 2
3
>>>
```

Una vez más, pongo un espacio después del `#` y múltiples espacios antes solo para
hacer las cosas más fáciles de leer.

Si escribimos un comentario en una línea sin código, el aviso cambia
de `>>>` a `...`. Para ser honesto, no tengo idea de por qué hace eso y yo
creo que sería mejor si se quedara como `>>>`. El aviso va
volver a `>>>` cuando presionemos Enter de nuevo.

```python
>>> # Hola mundo
...
>>>
```

## Strings

Los strings son pequeños fragmentos de texto que podemos usar en nuestros programas. Podemos
crear stings simplemente escribiendo un texto entre comillas.

```python
>>> 'hello'
'hello'
>>> 'this is a test'
'this is a test'
>>>
```

Los strins también se pueden escribir con "" en lugar de ''.
Esto es útil cuando necesitamos poner comillas dentro del string.

```python
>>> "hello there"
'hello there'
>>> "it's sunny"
"it's sunny"
>>>
```

También es posible agregar comillas simples y comillas dobles en el mismo
cadena, pero la mayoría de las veces no necesitamos hacer eso, así que no voy a
para hablar de eso ahora.

Los strings pueden unirse fácilmente con `+` o repetirse con `*`:

```python
>>> "hello" + "world"
'helloworld'
>>> "hello" * 3
'hellohellohello'
>>>
```

Tenga en cuenta que un `#` dentro de una cadena no crea un comentario.

```python
>>> "strings can contain # characters"
'strings can contain # characters'
>>>
```

## Usar Python como calculadora

Escribamos algunas cosas matemáticas en Python y veamos qué hace.

```python
>>> 17 + 3
20
>>> 17 - 3
14
>>> 17 * 3
51
>>> 17 / 3
5.666666666666667
>>>
```

Agregué un espacio a ambos lados de `+`, `-`, `*` y `/`. Todo lo haría
trabajar sin esos espacios también:

```python
>>> 4 + 2 + 1
7
>>> 4+2+1
7
>>>
```

Sin embargo, recomiendo siempre agregar los espacios porque hacen que el código
más fácil de leer.

Las cosas se calculan en el mismo orden que en matemáticas. Los paréntesis `(`
y `)` también funcionan de la misma manera.

```python
>>> 1 + 2 * 3        # 2 * 3 Es calculado primero
7
>>> (1 + 2) * 3      # 1 + 2 Es calculado primero
9
>>>
```

También puede omitir espacios para mostrar lo que se calcula primero. Pitón
lo ignora, pero nuestro código será más fácil de leer para las personas.

```python
>>> 1 + 2*3         # Ahora observamos como 2*3 es calculado primero
7
>>>
```

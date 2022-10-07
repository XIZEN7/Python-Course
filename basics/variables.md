# Variables, Booleanos y Ninguno

## Variables

Las variables son fáciles de entender. Simplemente **señalan valores**.

```python
>>> a = 1 # crea una variable llamada a que apunte a 1
>>> b = 2 # crea otra variable
>>> un # obtiene el valor al que apunta la variable
1
>>> segundo
2
>>>
```

Dibujemos un diagrama de estas variables.

![Diagrama de variables](../images/variables1.png)

También podemos cambiar el valor de una variable después de configurarla.

```python
>>> a = 2 # hacer un punto a 2 en lugar de 1
>>> un
2
>>>
```

Así que ahora nuestro diagrama se ve así:

![Diagrama de variables](../images/variables2.png)

Establecer una variable en otra variable obtiene el valor de la otra
variable y establece la primera variable para que apunte a ese valor.

```python
>>> un = 1
>>> b = a # esto hace que b apunte a 1, no a
>>> un = 5
>>> b # b no cambió cuando a cambió
1
>>>
```

Intentar acceder a una variable que no está definida crea un error
mensaje.

```python
>>> cosita
Rastreo (llamadas recientes más última):
  Archivo "<stdin>", línea 1, en <módulo>
NameError: el nombre 'cosita' no está definido
>>>
```

Las variables son simples de entender, pero hay algunos detalles que
hay que tener en cuenta:

- Las variables siempre apuntan a un valor, **nunca apuntan a otro
  variable**. Es por eso que las flechas en nuestros diagramas siempre van hacia la izquierda.
  a derecha.
- Múltiples variables pueden apuntar al mismo valor, pero una variable
  no puede apuntar a varios valores.
- Los valores a los que apuntan las variables también pueden apuntar a otros valores.
  Aprenderemos más sobre eso cuando hablemos de
  [listas](lists-and-tuples.md).

Las variables son una parte importante de la mayoría de los lenguajes de programación y
permitir a los programadores escribir programas mucho más grandes de lo que podrían escribir
sin variables

Los nombres de variables distinguen entre mayúsculas y minúsculas, como muchas otras cosas en Python.

```python
>>> cosa = 1
>>> COSA = 2
>>> cosa = 3
>>> cosa
1
>>> COSA
2
>>> cosa
3
>>>
```

También hay palabras que no se pueden usar como nombres de variables.
porque están reservados por el propio Python y tienen un significado especial.
Se llaman **palabras clave**, y podemos ejecutar `help('keywords')`
para ver la lista completa si queremos.
Aprenderemos a usar la mayoría de ellos más adelante en este tutorial. Tratando de usar un
palabra clave como nombre de variable provoca un error de sintaxis.

```python
>>> si = 123
  Archivo "<stdin>", línea 1
    si = 123
       ^
Error de sintaxis: sintaxis invalida
>>>
```

Al asignar algo a una variable usando `=`, el lado derecho de
el `=` siempre se ejecuta antes del lado izquierdo. Esto significa que podemos
hacer algo con una variable en el lado derecho, luego asignar el resultado
de vuelta a la misma variable en el lado izquierdo.

```python
>>> un = 1
>>> un = un + 1
>>> un
2
>>>
```

Para hacer algo con una variable (por ejemplo, para agregarle algo)
también puede usar `+=`, `-=`, `*=` y `/=` en lugar de `+`, `-`, `*` y
`/`. Los "avanzados" `%=`, `//=` y `**=` también funcionan.

```python
>>> un += 2 # un = un + 2
>>> un -= 2 # un = un - 2
>>> un *= 2 # un = un * 2
>>> un /= 2 # un = un / 2
>>>
```

Esto no se limita a números enteros.

```python
>>> a = 'hola'
>>> un *= 3
>>> a += 'mundo'
>>> un
'holaholaholamundo'
>>>
```

Ahora también entendemos por qué escribir hola en el aviso no funcionó en
el comienzo de este tutorial. Pero podemos asignar algo a un
variable llamada hola y luego escriba hola:

```python
>>> hola = 'hola'
>>> hola
'Hola a todos'
>>>
```

## Nombres de variables buenos y malos

Los nombres de las variables pueden tener varios caracteres. pueden contener
mayúsculas, números y algunos otros caracteres, pero la mayoría de los
tiempo debemos usar nombres de variables simples y en minúsculas. También podemos usar
guiones bajos Por ejemplo, estos nombres de variables son buenos:

```python
>>> número_mágico = 123
>>> saludo = "¡Hola mundo!"
>>>
```

No use nombres de variables como este, **estas variables son _malas_**:

```python
>>> magicNumber = 3.14 # se ve raro
>>> Saludo = "¡Hola!" # también se ve raro
>>> x = "¡Hola de nuevo!" # ¿Qué diablos es x?
>>>
```

Todas estas variables funcionan bien, pero otros programadores de Python
no quiero que los uses. La mayoría del código de Python no usa nombres de variables
que contienen letras Mayúsculas como `magicNumber` y `Greeting`, por lo que
otras personas que lean tu código pensarán que se ve raro si usas
a ellos. El problema con `x` es que es demasiado corto y la gente no tiene
idea de lo que es. Recuerda que a los matemáticos les gusta averiguar qué x
es, pero los programadores odian eso.

## Booleanos

Hay dos valores booleanos, verdadero y falso. En Python, y en muchos
otros lenguajes de programación, `=` está asignando y `==` está comparando.
`a = 1` establece a en 1, y `a == 1` comprueba si a es igual a 1.

```python
>>> un = 1
>>> un == 1
Verdadero
>>> un = 2
>>> un == 1
Falso
>>>
```

`a == 1` es lo mismo que `(a == 1) == True`, pero `a == 1` es más
legible, por lo que la mayoría de las veces no deberíamos escribir `== True` en ninguna parte.

```python
>>> un = 1
>>> un == 1
Verdadero
>>> (a == 1) == Verdadero
Verdadero
>>> un = 2
>>> un == 1
Falso
>>> (a == 1) == Verdadero
Falso
>>>
```

## Ninguna

Ninguno yo

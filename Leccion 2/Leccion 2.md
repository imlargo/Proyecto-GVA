# Leccion 2: Operaciones fundamentales con vectores y sus propiedades

Asi como se pueden realizar ciertas operaciones con los numeros, los vectores tambien tienen operaciones fundamentales. Una de estas operaciones es la multiplicación de un vector por un número real.


### Multiplicacion por un escalar.

**Multiplicación de vectores por un número**

A los números, ahora les diremos escalares, y a esta operacion se le llama multiplicación de un vector por un escalar.

> Convertir la palabra "número" en "escalar"

Podemos entender la multiplicación de un vector por un escalar como “estirar” ese vector según un número específico.

> Convertir la palabra "escalar" en "estirar"

Si el número es positivo, el vector se estira en la misma dirección que tiene, mientras que si es negativo, el vector se "estira" en dirección opuesta.

> Estirar el vector de manera positiva y luego negativa

En este caso cuando hablo de dirección me refiero a “hacia donde apunta” ese vector, recordemos que un vector se diferencia de un punto en el hecho de que el vector tiene una direccion, y esa direccion es la direccion en la que apunta el vector saliendo desde el origen hasta su punta,

 como explique anteriormente, y cuando multiplicamos un vector por un número negativo, esta dirección se invierte.

**Como afecta la longitud**

Un aspecto fundamental a resaltar es que la multiplicación de un vector por un escalar tiene el efecto de multiplicar la longitud original del vector por ese mismo número. En otras palabras, si tenemos un vector de longitud 'n', la nueva longitud después de escalar será 'n \* m'. Por cierto, a esa longitud del vecto se le dice magnitud y se simboliza como ||v||

Para multiplicar un escalar por un vector simplemente multiplicamos el escalar por cada componente del vector.


### Recta y rayos generados por un vector.

Como vimos anteriormente, multiplicar un vector por un escalar tiene el efecto de "estirar" ese vector.
En este caso, si le damos a n la libertad de tomar el valor de cualquier numero real, entonces obtenemos esta recta, que es el conjunto de todos los vectores resultantes de multiplicar v por n (es decir, por cualquier numero real). A esta recta se le llama, la recta generada por V

De igual forma, , si consideramos todos los posibles vectores resultantes de multiplicar nuestro vector v por un número n positivo entonces obtenemos el rayo positivo de v, son todos los vectores que se obtienen al multiplicar un vector por un escalar positivo

De igual forma, si consideramos todos los posibles vectores resultantes de multiplicar nuestro vector v por un número real n, pero con la restricción de que debe ser positivo, obtenemos el rayo positivo de v. Estos son todos los vectores que se obtienen al multiplicar un vector por un escalar positivo.

Análogamente, si multiplicamos un vector por un escalar n negativo, obtenemos el rayo negativo de nuestro vector v, que es el conjunto de todos los vectores resultantes de multiplicar v por un escalar n negativo.

El concepto de recta generada por un vector tiene implicaciones importantes en el tema que veremos a continuación

### Dependencia e Independencia lineal y sus diferentes significados

Como vimos anteriormente, cualquier vector A puede generar una recta, la recta generada por A, que es el conjunto de todos los vectores resultantes de escalar A por un número real.

Ahora, si un vector B es un múltiplo escalar de A (es decir, B = nA), entonces podemos decir que B y A son linealmente dependientes.

Podemos comprender esto de varias maneras; dos vectores son linealmente dependientes si uno es un múltiplo escalar del otro, es decir, uno está en la recta generada dell otro.

También es importante saber que si son linealmente dependientes, entonces B = nA, pero al mismo tiempo A = nB, por lo tanto B está en la recta generada por A, y al mismo tiempo A está en la recta generada por B, y tambien B es un múltiplo escalar de A…

Todo esto se refiere a la dependencia lineal. Ahora bien, ¿cómo podemos saber algebraicamente si dos vectores son linealmente dependientes? Podríamos encontrar un número "n" que satisfaga que B = nA. Partiendo de esto, llegamos a la definición del producto cruzado (Del cual no hare la demostración de donde sale la formula)

Dos vectores son linealmente dependientes si el producto cruzado entre ellos es cero (0).
El producto cruzado se calcula …

De igual manera, dos vectores son linealmente independientes si el producto cruzado entre ellos es distinto de cero, es decir, no existe ningún n que satisfaga B = nA y B no es un múltiplo escalar de A.

## Suma de vectores.

**Como se hace algebraicamente**


**Como se ve**

# Ideas

Suma y resta de vectores. (Resta = suma \* -1), diferentes maneras de hacerlo
(Demostrar propiedades?)

La suma de vectores se realiza sumando componente por componente

Visualmente la podemos entender como tomar el segundo vector y colocarlo en la cabeza del segundo vector, de manera que el inicio del segundo vector sea la punta del primer vector

#Animación

…

Regla del paralelogramo y sus propiedades

. . .
Descomposición Canónica y Combinaciones lineales

. . .
Span of vectors, hallar escalares, cuando es posible y la excepción

> - [ ] Aclarar que no todo es re técnico sino que se simplifican algunas cosas que pueden no ser del todo “fieles” a la explicación matemática.

# Leccion 2: Operaciones fundamentales con vectores y sus propiedades

Asi como se pueden realizar ciertas operaciones con los numeros, los vectores tambien tienen operaciones fundamentales. Una de estas operaciones es la multiplicación de un vector por un número real.


### Multiplicacion por un escalar.

**Multiplicación de vectores por un número**

A los números, ahora les diremos escalares, y a esta operacion se le llama multiplicación de un vector por un escalar.

> - [ ] Convertir la palabra "número" en "escalar"

Podemos entender la multiplicación de un vector por un escalar como “estirar” ese vector según un número específico.

> - [ ] Convertir la palabra "escalar" en "estirar"

Si el número es positivo, el vector se estira en la misma dirección que tiene, mientras que si es negativo, el vector se "estira" en dirección opuesta.

> - [ ] Estirar el vector de manera positiva y luego negativa

En este caso cuando hablo de dirección me refiero a “hacia donde apunta” ese vector, recordemos que un vector se diferencia de un punto en el hecho de que el vector tiene una direccion, y esa direccion es la direccion en la que apunta el vector saliendo desde el origen hasta su punta,

> - [ ] Mostrar un vector y su direccion

**Como se escala algebraicamente**

> - [ ] Escalamos un vector y mostramos el proceso por componentes

Para multiplicar un escalar por un vector simplemente multiplicamos el escalar por cada componente del vector.

**Como afecta la longitud**

> - [ ] Dibujar un vector, hacer corchetes con su longitud, y poner un n con su longitud

Un aspecto fundamental a resaltar es que la multiplicación de un vector por un escalar tiene el efecto de multiplicar la longitud original del vector por ese mismo número.

> - [ ] Escalar el vector, y mostrar la nueva longitud

En otras palabras, si tenemos un vector de longitud 'n', la nueva longitud después de escalar será 'n \* m'. 

> - [ ] Convertir la longitud en n veces la magnitud

Por cierto, a esa longitud del vector se le dice magnitud y se simboliza como ||v||, pero hablaremos de ella mas adelante a fondo

- La magnitud de un vector es la longitud del vector, es decir, la distancia entre el origen y la punta del vector.

> - [ ] **??? Demostracion de pq afecta la magnitud!!!**


### Recta y rayos generados.

> - [ ] Escalamos un vector y mostramos el proceso por componentes

Como vimos anteriormente, multiplicar un vector por un escalar tiene el efecto de "estirar" ese vector.

**Recta generada**

> - [ ] n E R

En este caso, si le damos a n la libertad de tomar el valor de cualquier numero real, entonces obtenemos esta recta:

> - [ ] Dibujamos una recta

Que es el conjunto de todos los vectores resultantes de multiplicar nuestro vector v por cualquier numero real. A esta recta se le llama, la recta generada por V.

> - [ ] Notacion matemtica

**Rayos generados**

- Rayo positivo

> - [ ] Mostramos el rayo positivo

Ahora, si restringimos los valores de n y consideramos todos los posibles vectores resultantes de multiplicar nuestro vector v por un número n positivo entonces obtenemos el rayo positivo de v, y nos damos cuenta que el rayo positivo sigue la misma direccion en la que apunta nuestro vector, lo cual tiene sentido pq como dije anteriormente, al multiplicar un vector por un escalar positivo, el vector se estira en la misma direccion que tiene.

- Rayo negativo

> - [ ] Mostramos el rayo negativo

Análogamente, si multiplicamos nuestro vector v por un escalar n negativo, obtenemos el rayo negativo de nuestro vector v, podemos ver que al multiplicar nuestro vector v por un escalar negativo obtenemos los vectores que apuntan en dirección opuesta a v.

- El concepto de recta generada por un vector tiene implicaciones importantes en el tema que veremos a continuación


### Dependencia e Independencia lineal

**Dependencia lineal**

> - [ ] Concepto de dependencia lineal

Si un vector A es un múltiplo escalar de otro vector B (se denota A = nB ), entonces podemos decir que los vectores A y B son linealmente dependientes. Cuando dos vectores no son linealmente dependientes decimos que son linealmente independientes.

> - [ ] Dibujar vectores (2, 4) y (1, 2) y sus etiquetas

- Por ejemplo los vectores A = (2, 4) y B = (1, 2) son linealmente dependientes, ya que A = 2B.

> - [ ] Dibujar vectores (2, 4) y (1, 2) y mostrar que A = 2B

Podemos comprender esto de varias maneras:
- Dos vectores son linealmente dependientes si uno es un múltiplo escalar del otro, es decir
- Uno está en la recta generada del otro.

> - [ ] Multiplo escalar = en la recta generada

También es importante saber que si son linealmente dependientes, entonces A = nB, pero al mismo tiempo B = rA, por lo tanto A está en la recta generada por B, y al mismo tiempo B está en la recta generada por A, ya que es la misma recta.

> Resaltar las rectas generadas


**Producto cruzado**

Ahora bien, ¿cómo podemos determinar algebraicamente si dos vectores son linealmente dependientes? Una forma sería encontrar un número "n" que haga que A = nB, pero existe un método más rápido y sencillo.

- Partiendo de esto, llegamos a la definición del producto cruzado

> - [ ] Definicion producto cruzado

El producto cruzado entre dos vectores A y B es una operacion que nos dice si dos vectores son linealmente dependientes o no.

Nota: Esta operacion tambien tiene otras aplicaciones importantes, pero eso se vera mas adelante.

> - [ ] Definicion producto cruzado algebraicamente, con 2 vectores (a, b) y (c, d)

El producto cruzado se calcula multiplicando en cruz y restando, $a \cdot c - b \cdot d$.

> - [ ] Dependencia lineal con el producto cruzado

Sean A = (a, b) y B = (c, d) vectores del plano. A y B son linealmente dependientes si y sólo si ad − bc = 0

> - [ ] Animacion producto cruzado por componentes

Por ejemplo en nuestro caso, el producto cruzado entre A = (1, 2) y B = (2, 4) es $1 \cdot 4 - 2 \cdot 2 = 0$, por lo tanto A y B son linealmente dependientes.

> - [ ] Animacion producto cruzado por componentes con numeros

De igual manera, dos vectores son linealmente independientes si el producto cruzado entre ellos es distinto de cero, es decir, no existe ningún n que satisfaga B = nA, es decir B no es un múltiplo escalar de A ni viceversa.

Ahora, si por alguna razon queremos encontrar ese n que satisface B = nA, simplemente planteamos una ecuacion con las componentes de los vectores:

> - [ ] Convertir a ecuaciones de componentes y despejar n

- Como que escalar un vector implica multiplicar el escalar por cada una de sus componentes, entonces podemos expresar "esto" como "esto", y si encontramos ese n, entonces los vectores son linealmente dependientes, sino, son linealmente independientes.


## Suma de vectores.

Ahora que ya sabemos multiplicar un vector por un escalar, podemos pasar a la siguiente operacion fundamental con vectores, la suma de vectores.

**Como se hace algebraicamente**

> - [ ] Suma de vectores por componentes

La suma de vectores se realiza sumando componente por componente, es decir, sumamos las componentes x de los vectores y las componentes y de los vectores por separado.

> - [ ] ejemplo con vectores (1, 2) y (3, 4)

Por ejemplo, si tenemos los vectores A = (1, 2) y B = (3, 4), entonces la suma de A y B es (1 + 3, 2 + 4) = (4, 6).

> Dibujamos el nuevo vector

Ahora me gustaria dar una explicacion de porque esto tiene sentido, por ejemplo, si el primer vector (1, 2) significa dar 1 paso a la derecha y 2 pasos hacia arriba, y el segundo vector (3, 4) significa dar 3 pasos a la derecha y 4 pasos hacia arriba, entonces la suma de estos dos vectores significa dar 1 paso a la derecha, luego 2 pasos hacia arriba, y luego 3 pasos a la derecha y 4 pasos hacia arriba.


**Como se ve**

# Ideas

Suma y resta de vectores. (Resta = suma \* -1), diferentes maneras de hacerlo
(Demostrar propiedades?)


Visualmente la podemos entender como tomar el segundo vector y colocarlo en la cabeza del segundo vector, de manera que el inicio del segundo vector sea la punta del primer vector

#Animación

…

Regla del paralelogramo y sus propiedades

. . .
Descomposición Canónica y Combinaciones lineales

. . .
Span of vectors, hallar escalares, cuando es posible y la excepción

> - [ ] - [ ] Aclarar que no todo es re técnico sino que se simplifican algunas cosas que pueden no ser del todo “fieles” a la explicación matemática.

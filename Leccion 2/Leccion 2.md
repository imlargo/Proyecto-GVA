<!-- Titulo:
Operaciones fundamentales con vectores y sus propiedades
-->

<!-- 
- Vector: $\begin{bmatrix} 1 \\ 2 \end{bmatrix}$
-->

Asi como se pueden hacer operaciones con números, los vectores también tienen operaciones fundamentales. Una de ellas es la _multiplicación_ de un vector por un número real.

### Multiplicacion por un escalar.
---

<!-- **Multiplicación de vectores por un número** -->

<!-- Convertir la palabra "número" en "escalar" -->

A los números ahora les llamaremos **escalares**, y a esta operación la llamaremos multiplicación de un vector por un escalar.

<!-- Convertir la palabra "escalar" en "estirar?" -->

<!-- Estirar el vector de manera positiva y luego negativa -->

> Podemos entender la multiplicación de un vector por un escalar como _estirar_ ese vector en cierta cantidad. Al multiplicar un vector por un escalar positivo, el vector se _estira_ en la misma _dirección_ que ya tiene, mientras que si el escalar es negativo, el vector se _estira_ en dirección opuesta.

<!-- Mostrar un vector y su direccion -->

<!-- **Como se escala algebraicamente** -->

<!-- Escalamos un vector -->

Ahora, ¿cómo se representa esto algebraicamente? Para multiplicar un escalar por un vector, simplemente multiplicamos el escalar por cada una de las **componentes** del vector, de esta manera:

<!-- Hacemos la operacion mostrando por componentes -->

- **$n$** $\cdot \vec{v} =$   **$n$** $\cdot \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} n \cdot x \\ n \cdot y \end{bmatrix}$

Por ejemplo, si tenemos el vector **$\vec{v}$**, donde  $\vec{v} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$ y lo multiplicamos por el escalar $2$, entonces obtenemos:

> $$ 2 \cdot \vec{v} = 2 \cdot \begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 2 \cdot 1 \\ 2 \cdot 2 \end{bmatrix} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$$

Donde el vector resultante apunta en la misma direccion que ya tenia, pero ahora es el doble de _largo_ (más adelante explicaré el por qué). De igual manera manera, si multiplicamos el vector **$\vec{v}$** por -2, entonces obtenemos:

> $$ -2 \cdot \vec{v} = -2 \cdot \begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} -2 \cdot 1 \\ -2 \cdot 2 \end{bmatrix} = \begin{bmatrix} -2 \\ -4 \end{bmatrix}$$

Y ahora el vector resultante tambien es el doble de _largo_, pero apunta en _dirección_ opuesta a la que tenia el vector inicial.

En este caso cuando hablo de **dirección** me refiero a _"hacia donde apunta"_ ese vector, recordemos que los vectores siempre siguen la dirección _hacia donde apuntan_, es decir, hacia donde se extienden, yendo desde el origen hasta el punto donde terminan.

**Como afecta la longitud.**

<!-- Dibujar un vector, hacer corchetes con su longitud, y poner un n con su longitud -->

Un aspecto muy importante que me gustaria resaltar es que la multiplicación de un vector por un escalar tiene el efecto de multiplicar la longitud original del vector por ese mismo número.

> **Nota:** A la longitud de un vector se le llama su **magnitud**, se simboliza como **$|| \vec{v} ||$**, y es la distancia desde el origen hasta la punta del vector. Pero veremos ese tema en otra leccion mas adelante.

<!-- Escalar el vector, y mostrar la nueva longitud -->

En otras palabras, si tenemos un vector **$\vec{v}$** de longitud **$m$**, es decir $|| \vec{v} || = m$, la nueva longitud después de escalar el vector será $m \cdot n = || n \cdot \vec{v} || = n \cdot || \vec{v} || = n \cdot m $. Por ejemplo, si tenemos un vector **$\vec{v}$** de longitud 3, y lo multiplicamos por el escalar 2, entonces la longitud del vector resultante será $2 \cdot 3 = 6$.

<!-- Animacion con el vector (3, 4) -->

Por ejemplo, el vector $\vec{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$ tiene **magnitud** 5 ( $|| \vec{v} || = 5$ ), y lo multiplicamos por el escalar 1.5, entonces obtenemos el vector

> $$ 1.5 \cdot \begin{bmatrix} 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 1.5 \cdot 3 \\ 1.5 \cdot 4 \end{bmatrix} = \begin{bmatrix} 4.5 \\ 6 \end{bmatrix} \overset{Donde}{\rightarrow} || \begin{bmatrix} 4.5 \\ 6 \end{bmatrix} || = 7.5 = 1.5 \cdot || \vec{v} ||$$

El cual tiene **magnitud** 7.5, es decir, 1.5 veces la _longitud_ original. A continuacion veremos algunas consecuencias de poder multiplicar un vector por un escalar.

### Recta y rayos generados.
---

**Recta generada por un vector.**

<!-- Escalamos un vector y mostramos el proceso por componentes -->

Como vimos anteriormente, multiplicar un vector por un escalar tiene el efecto de _estirar_ ese vector.

<!-- n E R -->

En este caso, si le damos a nuestro escalar $n$ la libertad de tomar el valor de cualquier numero real, entonces obtenemos esta recta:

<!-- Dibujamos una recta y n recorriendo todos los reales (Puntos sobre la recta como conjunto) -->

Esta recta se le llama la _**recta generada por $\vec{v}$**_, se simboliza $L_{\vec{v}}$ y es el conjunto de todos los vectores resultantes de multiplicar nuestro vector $\vec{v}$ por cualquier numero real.

> $$L_{\vec{v}} = \{ \; \begin{bmatrix} x \\ y \end{bmatrix} \; : \; n \cdot \vec{v} = \begin{bmatrix} x \\ y \end{bmatrix}, \; n \in \mathbb{R} \; \}$$

<!-- Notacion matemtica -->

**Rayos generados**

- Rayo positivo

<!-- Mostramos el rayo positivo -->

Ahora, si restringimos los valores de $n$ y consideramos todos los posibles vectores resultantes de multiplicar nuestro vector $\vec{v}$ por un número n positivo entonces obtenemos el _**rayo positivo de $\vec{v}$**_.

Y nos damos cuenta que el rayo positivo sigue la misma direccion en la que apunta nuestro vector.

- Rayo negativo

<!-- Mostramos el rayo negativo -->

De igual manera, si multiplicamos nuestro vector $\vec{v}$ por un escalar $n$ negativo, obtenemos el _**rayo negativo de $\vec{v}$**_.

Podemos ver que al multiplicar nuestro vector $\vec{v}$ por un escalar negativo obtenemos los vectores que apuntan en dirección opuesta a $\vec{v}$.

- El concepto de recta generada por un vector tiene implicaciones importantes en el tema que veremos a continuación


### Dependencia e Independencia lineal
---

**Dependencia lineal**

<!-- Concepto de dependencia lineal -->

Ya sabemos que al escalar un vector obtenemos otro vector _estirado_, si al vector resultante le llamamos $\vec{B}$ y al vector original le llamamos $\vec{A}$, entonces podemos decir que $\vec{B}$ es un múltiplo escalar de $\vec{A}$, es decir $n \cdot \vec{A} = \vec{B}$, donde $n$ es el escalar que multiplicamos por $\vec{A}$ para obtener a $\vec{B}$.

Cuando un vector es un multiplo escalar de otro, se dice que son **linealmente dependientes**, y no son linealmente dependientes decimos que son **linealmente independientes**.

<!-- Dibujar vectores (2, 4) y (1, 2) y sus etiquetas -->

- Por ejemplo los vectores $\vec{B} = \begin{bmatrix} 2 \\ 2 \end{bmatrix}$ y $\vec{A} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$ son linealmente dependientes, ya que $2 \cdot \vec{A} = \vec{B}$. Y por lo tanto $\vec{B}$ es un multiplo escalar de $\vec{A}$.

<!-- Dibujar vectores (2, 4) y (1, 2) y mostrar que $\vec{A} = 2 \cdot \vec{B}$ -->

Podemos comprender el concepto de dependencia lineal de varias maneras:
- Dos vectores son linealmente dependientes si uno es un múltiplo escalar del otro, es decir
- Uno está en la recta generada del otro.

<!-- Multiplo escalar = en la recta generada -->

También es importante saber que si son linealmente dependientes, entonces $\vec{A} = n \cdot \vec{B}$, pero al mismo tiempo $\vec{B} = r \cdot \vec{A}$, por lo tanto $\vec{A}$ está en la recta generada por $\vec{B}$, y al mismo tiempo $\vec{B}$ está en la recta generada por $\vec{A}$, ya que es la misma recta.

> Resaltar las rectas generadas


**Producto cruzado**

Ahora bien, ¿cómo podemos determinar algebraicamente si dos vectores son linealmente dependientes? es decir, si uno es un multiplo escalar del otro?.
Una forma sería encontrar un número **$n$** que haga que $n \cdot \vec{A} = \vec{B}$, pero existe un método más rápido y sencillo.

- Partiendo de esto, llegamos a la definición del producto cruzado

<!-- Definicion producto cruzado -->

> El producto cruzado entre dos vectores $\vec{A}$ y $\vec{B}$ es una operacion que nos dice si dos vectores son linealmente dependientes o no.

<!-- Definicion producto cruzado algebraicamente, con 2 vectores $\begin{bmatrix} a \\ b \end{bmatrix} $ y $\begin{bmatrix} c \\ d \end{bmatrix}$ compontentes -->

El producto cruzado se calcula multiplicando en cruz y restando, asi, $a \cdot d - b \cdot c$.

Y listo, el resultado de esa operacion nos dice si los vectores son linealmente dependientes o no.

<!-- Dependencia lineal con el producto cruzado -->

> Sean $\vec{A} = \begin{bmatrix} a \\ b \end{bmatrix}$ y $\vec{B} = \begin{bmatrix} c \\ d \end{bmatrix}$ vectores del plano. $\vec{A}$ y $\vec{B}$ son linealmente dependientes **si y sólo si** su producto cruzado es igual a cero: **$a \cdot d - b \cdot c = 0$**.

<!-- Animacion producto cruzado por componentes -->

Por ejemplo en nuestro caso, el producto cruzado entre $\vec{A} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$ y $\vec{B} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$ es $1 \cdot 4 - 2 \cdot 2 = 0$, por lo tanto $\vec{A}$ y $\vec{B}$ son linealmente dependientes.

<!-- Animacion producto cruzado por componentes con numeros -->

De igual manera, dos vectores son linealmente independientes si el producto cruzado entre ellos es distinto de cero, es decir, no existe ningún **$n$** que satisfaga $n \cdot \vec{A} = \vec{B}$, es decir $\vec{B}$ no es un múltiplo escalar de $\vec{A}$ ni viceversa.

Ahora, si por alguna razon queremos encontrar ese **$n$** que satisface $n \cdot \vec{A} = \vec{B}$, simplemente planteamos una ecuacion con las componentes de los vectores:

<!-- Convertir a ecuaciones de componentes y despejar n -->

- Como que escalar un vector implica multiplicar el escalar por cada una de sus **componentes**, entonces podemos expresar "esto" como "esto", y si encontramos ese **$n$**, entonces los vectores son linealmente dependientes, sino, son linealmente independientes.


### Suma de vectores.
---

Ahora que ya sabemos multiplicar un vector por un escalar, podemos pasar a la siguiente operacion fundamental con vectores, la suma de vectores.

**Como se hace algebraicamente**

<!-- Suma de vectores por componentes -->

La suma de vectores se realiza sumando componente por componente, es decir, sumamos las componentes x de los vectores y las componentes y de los vectores por separado.

<!-- ejemplo con vectores (1, 2) y (3, 4) -->

Por ejemplo, si tenemos los vectores $\vec{A} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$ y $\vec{B} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$, entonces la suma de $\vec{A}$ y $\vec{B}$ es $\begin{bmatrix} 1 + 3 \\ 2 + 3 \end{bmatrix} = \begin{bmatrix} 4 \\ 6 \end{bmatrix}$

> Dibujamos el nuevo vector

**Como se ve**

Visualmente la podemos entender como tomar el segundo vector y colocarlo en la cabeza del segundo vector, de manera que el inicio del segundo vector sea la punta del primer vector

mueve el segundo vector de manera que su cola se sitúe en la punta del primero. Luego, si dibujas un nuevo vector desde la cola del primero hasta donde ahora se encuentra la punta del segundo, ese nuevo vector es la suma de ambos.

> Ahora me gustaria dar una explicacion de porque esto tiene sentido, por ejemplo, si el primer vector (1, 2) significa dar 1 paso a la derecha y 2 pasos hacia arriba, y el segundo vector (3, 4) significa dar 3 pasos a la derecha y 4 pasos hacia arriba, entonces la suma de estos dos vectores significa dar 1 paso a la derecha, luego 2 pasos hacia arriba, y luego 3 pasos a la derecha y 4 pasos hacia arriba.


**Propiedades**

- Una propiedad dice que la suma de vectores es conmutativa, es decir, $\vec{A} + \vec{B} = \vec{B} + \vec{A}$.

<!-- Dibujar vectores (1, 2) y (3, 4) y mostrar que $\vec{A}$ + $\vec{B}$ = $\vec{B}$ + A -->

Si lo vemos de forma visual, nos damos cuenta que es lo mismo, y tiene sentido con la definicion que di anteriormente

De aqui sale la regla del paralelogramo (propiedades?)

**Resta de vectores**

Suma y resta de vectores. (Resta = suma \* -1), diferentes maneras de hacerlo
(Demostrar propiedades?)

<!-- Aclarar que no todo es re técnico sino que se simplifican algunas cosas que pueden no ser del  todo “fieles” a la explicación matemática. -->

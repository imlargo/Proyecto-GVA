<!-- Titulo:
Operaciones fundamentales con vectores y sus propiedades
-->

<!-- 
- Vector: $\begin{bmatrix} 1 \\ 2 \end{bmatrix}$
-->

Asi como se pueden hacer operaciones con números, los vectores también tienen _operaciones fundamentales_. Una de ellas es la _multiplicación_ de un vector por un número real.

### Multiplicacion por un escalar. {#lesson-escalar}
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

$$n \cdot \vec{v} = n \cdot \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} n \cdot x \\ n \cdot y \end{bmatrix}$$

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

### Recta y rayos generados. {#lesson-recta-rayos}
---

**Recta generada por un vector.**

<!-- Escalamos un vector y mostramos el proceso por componentes -->
<!-- n E R -->

Como vimos anteriormente, multiplicar un vector por un escalar tiene el efecto de _estirar_ ese vector. Ahora, si le damos a nuestro escalar **$n$** la libertad de tomar el valor de cualquier numero real, entonces obtenemos una recta. Esta recta se le llama la _**recta generada por $\vec{v}$**_, se simboliza $L_{\vec{v}}$, y es el conjunto de todos los multiplos escalares de nuestro vector $\vec{v}$, es decir, el conjunto de todos los vectores resultantes de multiplicar $\vec{v}$ por cualquier _numero_ real.

<!-- Dibujamos una recta y n recorriendo todos los reales (Puntos sobre la recta como conjunto) -->

> $$L_{\vec{v}} = \{ \; \begin{bmatrix} x \\ y \end{bmatrix} \; : \; n \cdot \vec{v} = \begin{bmatrix} x \\ y \end{bmatrix}, \; n \in \mathbb{R} \; \}$$

<!-- Notacion matemtica -->

**Rayos generados**

<!-- Mostramos el rayo positivo -->
Ahora, si limitamos los valores de **$n$** solo a números positivos, obtenemos el _**rayo positivo**_ de $\vec{v}$, se simboliza con $R_{\vec{v}}^{+}$ y es el conjunto de todos los vectores resultantes de multiplicar $\vec{v}$ por un escalar positivo.

- Además, podemos darnos cuenta de que el _rayo positivo_ de $\vec{v}$ es una "recta" que sigue la misma _dirección_ que $\vec{v}$. Esto tiene sentido, ya que al escalar $\vec{v}$ por un número positivo obtenemos otro vector que está _estirado_ en la misma dirección. Por lo tanto, el conjunto de puntos forma una _semirrecta_ que se extiende infinitamente en la misma dirección que $\vec{v}$.

> $$R_{\vec{v}}^{+} = \{\begin{bmatrix} x \\ y \end{bmatrix} : n \cdot \vec{v} = \begin{bmatrix} x \\ y \end{bmatrix}, n > 0 \}$$

<!-- Mostramos el rayo negativo -->

De igual manera, si restringimos los valores de **$n$** solo a numeros negativos obtenemos el _**rayo negativo**_ de $\vec{v}$, se simboliza con $R_{\vec{v}}^{-}$ y es el conjunto de vectores resultantes forma una recta que se extiende en la dirección opuesta a la del vector $\vec{v}$

> $$R_{\vec{v}}^{-} = \{\begin{bmatrix} x \\ y \end{bmatrix} : n \cdot \vec{v} = \begin{bmatrix} x \\ y \end{bmatrix}, n < 0 \}$$

El concepto de recta generada por un vector tiene implicaciones importantes en el tema que veremos a continuación.


### Dependencia e Independencia lineal {#lesson-dependencia-lineal}
---

**Dependencia lineal**

<!-- Concepto de dependencia lineal -->

Ya sabemos que al escalar un vector obtenemos otro vector _estirado_, si al vector resultante le llamamos $\vec{B}$ y al vector original le llamamos $\vec{A}$, es decir, $n \cdot \vec{A} = \vec{B}$, entonces podemos decir que $\vec{B}$ es un múltiplo escalar de $\vec{A}$, donde $n$ es el escalar que multiplicamos por $\vec{A}$ para obtener a $\vec{B}$.

> Cuando un vector es un multiplo escalar de otro, se dice que son **linealmente dependientes**, y cuando no son linealmente dependientes decimos que son **linealmente independientes**.

<!-- Dibujar vectores (2, 4) y (1, 2) y sus etiquetas -->

Por ejemplo: los vectores $\vec{B} = \begin{bmatrix} 2 \\ 2 \end{bmatrix}$ y $\vec{A} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$ son linealmente dependientes, ya que $2 \cdot \vec{A} = \vec{B}$, es decir  $\vec{B}$ es un multiplo escalar de $\vec{A}$.

<!-- Dibujar vectores (2, 4) y (1, 2) y mostrar que $\vec{A} = 2 \cdot \vec{B}$ -->

También notamos que el concepto de dependencia lineal implica que ambos vectores se encuentran en la misma recta generada, pero ¿por qué tiene sentido esto? Dado que uno de los vectores es simplemente una versión escalada o estirada del otro, entonces está en la recta generada del vector inicial. A su vez, la recta generada de cualquier vector y sus múltiplos escalares es la misma. Por lo tanto, están en la misma recta generada, lo cual significa tambien que ambos vectores son multiplos escalares del otro.

<!-- Multiplo escalar = en la recta generada -->

> Si dos vectores son linealmente dependientes, entonces $n \cdot \vec{A} = \vec{B}$, pero al mismo tiempo $r \cdot \vec{B} = \vec{A}$, por lo tanto $\vec{A}$ está en la recta generada por $\vec{B}$, y al mismo tiempo $\vec{B}$ está en la recta generada por $\vec{A}$, ya que es la misma recta.

<!-- Resaltar las rectas generadas -->


**Producto cruzado**

Ahora bien, ¿cómo podemos determinar algebraicamente si dos vectores $\vec{A}$ y $\vec{B}$ son linealmente dependientes? es decir, si uno es un multiplo escalar del otro?. Una forma sería encontrar un número **$n$** que cumpla que $n \cdot \vec{A} = \vec{B}$, pero existe un método más rápido y sencillo, y partiendo de esto, llegamos a la definición del producto cruzado:

<!-- Definicion producto cruzado -->

> El producto cruzado  entre dos vectores $\vec{A}$ y $\vec{B}$ ( se simboliza $\vec{A}$ **$ \times$** $\vec{B}$ ) es una operación que se realiza entre dos vectores y nos da como resultado un numero, el cual nos dice si los vectores son linealmente dependientes o no.

<!-- Definicion producto cruzado algebraicamente, con 2 vectores $\begin{bmatrix} a \\ b \end{bmatrix} $ y $\begin{bmatrix} c \\ d \end{bmatrix}$ compontentes -->

Se calcula multiplicando en cruz y restando de esta manera:

$$ \vec{A} \times \vec{B} = \begin{bmatrix} a \\ b \end{bmatrix} \times \begin{bmatrix} c \\ d \end{bmatrix} = a \cdot d - b \cdot c $$

<!-- Dependencia lineal con el producto cruzado -->
Ahora, como vimos, ese resultado de realizar la operacion del producto cruzado $a \cdot d - b \cdot c$ nos da un numero, si el valor del producto cruzado es 0 entonces los vectores son **linealmente dependientes**, y si es distinto de cero ($\neq 0$) entonces son linealmente independientes

> Sean $\vec{A} = \begin{bmatrix} a \\ b \end{bmatrix}$ y $\vec{B} = \begin{bmatrix} c \\ d \end{bmatrix}$ vectores del plano. $\vec{A}$ y $\vec{B}$ son linealmente dependientes **si y sólo si** su producto cruzado es igual a cero: **$a \cdot d - b \cdot c = 0$**

<!-- Animacion producto cruzado por componentes -->

Por ejemplo en nuestro caso, el producto cruzado entre $\vec{A} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$ y $\vec{B} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$ es $1 \cdot 4 - 2 \cdot 2 = 0$, por lo tanto $\vec{A}$ y $\vec{B}$ son linealmente dependientes.

<!-- Animacion producto cruzado por componentes con numeros -->

De igual manera, dos vectores son linealmente independientes si el producto cruzado entre ellos es distinto de cero, es decir, no existe ningún **$n$** que satisfaga $n \cdot \vec{A} = \vec{B}$, es decir $\vec{B}$ no es un múltiplo escalar de $\vec{A}$ ni viceversa.

Ahora, si por alguna razon ya sabemos que los vectores son linealmente dependientes y queremos encontrar ese **$n$** que satisface $n \cdot \vec{A} = \vec{B}$, simplemente planteamos una ecuacion con las componentes de los vectores:

<!-- Convertir a ecuaciones de componentes y despejar n -->

- Como que escalar un vector implica multiplicar el escalar por cada una de sus **componentes**, entonces podemos expresar "esto" como "esto", y si encontramos ese **$n$**, entonces los vectores son linealmente dependientes, sino, son linealmente independientes.

> **Nota:** en **$\mathbb{R}^{2}$** el producto cruzado se calcula de esta manera, pero mas adelante nos daremos cuenta que realmente tiene muchos otros significados mas complejos, por lo tanto en esta leccion explico el producto cruzado de manera superficial y presentando su utilidad en el caso de dependencia lineal


### Suma de vectores. {#lesson-suma}
---

Ahora que ya sabemos multiplicar un vector por un escalar, podemos pasar a la siguiente operacion fundamental con vectores, la cual es la suma de vectores.

**Como se hace algebraicamente**

<!-- Suma de vectores por componentes -->

La suma de vectores se realiza sumando componente por componente, es decir, sumamos la componente _x_ de los vectores y la componentes _y_ de los vectores por separado.

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

### Resta de vectores {#lesson-resta}
---

Suma y resta de vectores. (Resta = suma \* -1), diferentes maneras de hacerlo
(Demostrar propiedades?)

<!-- Aclarar que no todo es re técnico sino que se simplifican algunas cosas que pueden no ser del  todo “fieles” a la explicación matemática. -->


### Algunas propiedades de las operaciones
---

**Propiedades de la multiplicacion por escalar**
- $1 \cdot \vec{A} = \vec{A}$
- $r \cdot (s \cdot \vec{A}) = (rs) \cdot \vec{A}$
- $r \cdot (\vec{A} + \vec{B}) = r \cdot \vec{A} + r \cdot \vec{B} $
- $(r + s) \cdot \vec{A} = r \cdot \vec{A} + s \cdot \vec{A}$

**Propiedades de la suma de vectores**
- $ \vec{A} + \vec{B} = \vec{B} + \vec{A} $
- $ (\vec{A} + \vec{B}) + Z = \vec{A} + (\vec{B} + Z) $
- $ \vec{A} + O = \vec{A} = O + \vec{A} $
- $ \vec{A} - \vec{A} = 0 $
- $ \vec{A} - \vec{B} \neq \vec{B} - \vec{A}$

**Propiedades del producto cruz**
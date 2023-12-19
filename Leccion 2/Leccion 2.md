# Operaciones fundamentales con vectores y sus propiedades

Asi como se pueden realizar ciertas operaciones con los numeros, los vectores tambien tienen operaciones fundamentales. Una de estas operaciones es la multiplicación de un vector por un número real.

Requisitos:
- Componentes
- Direccion

### Multiplicacion por un escalar.

**Multiplicación de vectores por un número**

A los números, ahora les diremos escalares, y a esta operacion se le llama multiplicación de un vector por un escalar.

> - [ ] Convertir la palabra "número" en "escalar"

Podemos entender la multiplicación de un vector por un escalar como “estirar” ese vector en cierta cantidad.

> - [ ] Convertir la palabra "escalar" en "estirar?"

Al multiplicar un vector por un escalar positivo, el vector se estira en la misma dirección que ya tiene, mientras que si el escalar es negativo, el vector se "estira" en dirección opuesta.

> - [ ] Estirar el vector de manera positiva y luego negativa

- Por ejemplo, si tenemos el vector (1, 2) y lo multiplicamos por el escalar 2, entonces obtenemos el vector (2, 4), que es el vector (1, 2) estirado en la misma dirección que ya tenía.

- Y de la misma manera, si multiplicamos el vector (1, 2) por el escalar -2, entonces obtenemos el vector (-2, -4), que es el vector (1, 2) estirado en dirección opuesta.

En este caso cuando hablo de dirección me refiero a “hacia donde apunta” ese vector, recordemos que un vector se diferencia de un punto en el hecho de que el vector tiene una direccion, y esa direccion es la direccion en la que apunta el vector saliendo desde el origen hasta su punta.

> - [ ] Mostrar un vector y su direccion

**Como se escala algebraicamente**

> - [ ] Escalamos un vector

Ahora, como se ve esto algebraicamente?, para multiplicar un escalar por un vector simplemente multiplicamos el escalar po

> - [ ] Hacemos la operacion mostrando por componentes

**Como afecta la longitud**

> - [ ] Dibujar un vector, hacer corchetes con su longitud, y poner un n con su longitud

Un aspecto muy importante que me gustaria resaltar es que la multiplicación de un vector por un escalar tiene el efecto de multiplicar la longitud original del vector por ese mismo número.

> - [ ] Escalar el vector, y mostrar la nueva longitud


En otras palabras, si tenemos un vector de longitud 'n', la nueva longitud después de escalar será 'n \* m'. 

> - [ ] Animacion con el vector (3, 4)

- Por ejemplo, si tenemos el vector (3, 4) que tiene longitud 5, y lo multiplicamos por el escalar 1.5, entonces obtenemos el vector (4.5, 6), que tiene longitud 7.5, es decir, 1.5 veces la longitud original.


> - [ ] Convertir la longitud en n veces la magnitud

Por cierto, a esa longitud del vector se le dice magnitud y se simboliza como ||v||, pero hablaremos de ella mas adelante a fondo

- La magnitud de un vector es la longitud del vector, es decir, la distancia entre el origen y la punta del vector.

> - [ ] **??? Demostracion de pq afecta la magnitud!!!**



### Recta y rayos generados. (Por un vector)

> - [ ] Escalamos un vector y mostramos el proceso por componentes

Como vimos anteriormente, multiplicar un vector por un escalar tiene el efecto de "estirar" ese vector.

**Recta generada**

> - [ ] n E R

En este caso, si le damos a nuestro escalar "(numero?)" n la libertad de tomar el valor de cualquier numero real, entonces obtenemos esta recta:

> - [ ] Dibujamos una recta y n recorriendo todos los reales (Puntos sobre la recta como conjunto)

Esta recta se le llama "la recta generada por V" y es el conjunto de todos los vectores resultantes de multiplicar nuestro vector v por cualquier numero real.

> - [ ] Notacion matemtica

**Rayos generados**

- Rayo positivo

> - [ ] Mostramos el rayo positivo

Ahora, si restringimos los valores de n y consideramos todos los posibles vectores resultantes de multiplicar nuestro vector v por un número n positivo entonces obtenemos el rayo positivo de v.

Y nos damos cuenta que el rayo positivo sigue la misma direccion en la que apunta nuestro vector.

- Rayo negativo

> - [ ] Mostramos el rayo negativo

De igual manera, si multiplicamos nuestro vector v por un escalar n negativo, obtenemos el rayo negativo de nuestro vector v

Podemos ver que al multiplicar nuestro vector v por un escalar negativo obtenemos los vectores que apuntan en dirección opuesta a v.

- El concepto de recta generada por un vector tiene implicaciones importantes en el tema que veremos a continuación


### Dependencia e Independencia lineal

**Dependencia lineal**

> - [ ] Concepto de dependencia lineal

Ya sabemos que al escalar un vector obtenemos otro vector "estirado", si al vector resultante le llamamos B y al vector original le llamamos A, entonces podemos decir que B es un múltiplo escalar de A, es decir nA = B, donde n es el escalar que multiplicamos por A para obtener a B.

Cuando un vector es un multiplo escalar de otro, se dice que son linealmente dependientes, y no son linealmente dependientes decimos que son linealmente independientes.

> - [ ] Dibujar vectores (2, 4) y (1, 2) y sus etiquetas

- Por ejemplo los vectores B = (2, 4) y A = (1, 2) son linealmente dependientes, ya que 2A = B. Y por lo tanto B es un multiplo escalar de A.

> - [ ] Dibujar vectores (2, 4) y (1, 2) y mostrar que A = 2B

Podemos comprender el concepto de dependencia lineal de varias maneras:
- Dos vectores son linealmente dependientes si uno es un múltiplo escalar del otro, es decir
- Uno está en la recta generada del otro.

> - [ ] Multiplo escalar = en la recta generada

También es importante saber que si son linealmente dependientes, entonces A = nB, pero al mismo tiempo B = rA, por lo tanto A está en la recta generada por B, y al mismo tiempo B está en la recta generada por A, ya que es la misma recta.

> Resaltar las rectas generadas


**Producto cruzado**

Ahora bien, ¿cómo podemos determinar algebraicamente si dos vectores son linealmente dependientes? es decir, si uno es un multiplo escalar del otro?.
Una forma sería encontrar un número "n" que haga que nA = B, pero existe un método más rápido y sencillo.

- Partiendo de esto, llegamos a la definición del producto cruzado

> - [ ] Definicion producto cruzado

El producto cruzado entre dos vectores A y B es una operacion que nos dice si dos vectores son linealmente dependientes o no.

> - [ ] Definicion producto cruzado algebraicamente, con 2 vectores (a, b) y (c, d) compontentes

El producto cruzado se calcula multiplicando en cruz y restando, asi, $a \cdot d - b \cdot c$.

Y listo, el resultado de esa operacion nos dice si los vectores son linealmente dependientes o no.

> - [ ] Dependencia lineal con el producto cruzado

Sean A = (a, b) y B = (c, d) vectores del plano. A y B son linealmente dependientes si y sólo si su producto cruzado es igual a cero, ad − bc = 0

> - [ ] Animacion producto cruzado por componentes

Por ejemplo en nuestro caso, el producto cruzado entre A = (1, 2) y B = (2, 4) es $1 \cdot 4 - 2 \cdot 2 = 0$, por lo tanto A y B son linealmente dependientes.

> - [ ] Animacion producto cruzado por componentes con numeros

De igual manera, dos vectores son linealmente independientes si el producto cruzado entre ellos es distinto de cero, es decir, no existe ningún n que satisfaga nA = B, es decir B no es un múltiplo escalar de A ni viceversa.

Ahora, si por alguna razon queremos encontrar ese n que satisface nA = B, simplemente planteamos una ecuacion con las componentes de los vectores:

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

**Como se ve**

Visualmente la podemos entender como tomar el segundo vector y colocarlo en la cabeza del segundo vector, de manera que el inicio del segundo vector sea la punta del primer vector

mueve el segundo vector de manera que su cola se sitúe en la punta del primero. Luego, si dibujas un nuevo vector desde la cola del primero hasta donde ahora se encuentra la punta del segundo, ese nuevo vector es la suma de ambos.

- Ahora me gustaria dar una explicacion de porque esto tiene sentido, por ejemplo, si el primer vector (1, 2) significa dar 1 paso a la derecha y 2 pasos hacia arriba, y el segundo vector (3, 4) significa dar 3 pasos a la derecha y 4 pasos hacia arriba, entonces la suma de estos dos vectores significa dar 1 paso a la derecha, luego 2 pasos hacia arriba, y luego 3 pasos a la derecha y 4 pasos hacia arriba.


**Propiedades**

- Una propiedad dice que la suma de vectores es conmutativa, es decir, A + B = B + A.

> - [ ] Dibujar vectores (1, 2) y (3, 4) y mostrar que A + B = B + A

Si lo vemos de forma visual, nos damos cuenta que es lo mismo, y tiene sentido con la definicion que di anteriormente


De aqui sale la regla del paralelogramo (propiedades?)


**Resta de vectores**

Suma y resta de vectores. (Resta = suma \* -1), diferentes maneras de hacerlo
(Demostrar propiedades?)


> - [ ] Aclarar que no todo es re técnico sino que se simplifican algunas cosas que pueden no ser del todo “fieles” a la explicación matemática.

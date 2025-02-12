import numpy as np;
from manim import *;

# - - - Operaciones entre vectores - - -
def sum_v(v1, v2):
    return (np.array(v1) + np.array(v2)).tolist()

def res_v(v1, v2):
    return (np.array(v1) - np.array(v2)).tolist()

def escalar(v, n):
    return [v[0] * n, v[1] * n]

def dot(v1, v2):
    return (v1[0] * v2[0] + v1[1] * v2[1])

def ort(v):
    return [-v[1], v[0]]

def rot_v(vector, angulo):
    x, y = np.array(vector)
    x_new = x * cos(angulo) - y * sin(angulo)
    y_new = x * sin(angulo) + y * cos(angulo)
    return np.array([x_new, y_new]).tolist()

def proyectar(vector_A, vector_B):
    vector_A = np.array(vector_A)
    vector_B = np.array(vector_B)
    dot_product = np.dot(vector_A, vector_B)
    magnitude_squared = np.dot(vector_B, vector_B)
    projection = (dot_product / magnitude_squared) * vector_B
    return projection.tolist()

# - - - Mobjects - - - 

def resaltar(objeto, color = TEAL_C, tiempo = 1):
    # Retorna la animacion q se debe mostrar con self.play()
    return ShowPassingFlash(
        SurroundingRectangle(objeto, color = color, buff = 0.25),
        run_time=tiempo, time_width=0.2
    )

def delinear(objeto, color = TEAL_C, tiempo = 1):
    # Retorna la animacion q se debe mostrar con self.play()
    return ShowPassingFlash(
        objeto.copy().set_color(color),
        run_time=tiempo, time_width=0.2
    )

# - - - Math - - - 

def sin(x):
    return np.sin(np.radians(x))

def cos(x):
    return np.cos(np.radians(x))

# - - - Generadores - - - 
cordsMatrix = lambda v: Matrix([[ v[0] ], [ v[1] ]])
getVectorCordsT = lambda v: MathTex(r"\begin{bmatrix} {} & {} \\".format(v[0], v[1]) + r"\end{bmatrix}")
getVectorName = lambda name: MathTex(f"\\vec{{{name}}}")

getColor = lambda string: ManimColor.from_hex(string)
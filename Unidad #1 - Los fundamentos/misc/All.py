import numpy as np

def sum_v(v1, v2):
    return [(v1[0] + v2[0]), (v1[1] + v2[1])]

def res_v(v1, v2):
    return [(v1[0] - v2[0]), (v1[1] - v2[1])]

def escalar(v, n):
    return [v[0] * n, v[1] * n]


def sin(x):
    return np.sin(np.radians(x))

def cos(x):
    return np.cos(np.radians(x))
    
def ortogonal(v):
    return [-v[1], v[0]]
    

def rot_vec(vector, angulo):
    x, y = np.array(vector)
    x_new = x * cos(angulo) - y * sin(angulo)
    y_new = x * sin(angulo) + y * cos(angulo)
    return np.array([x_new, y_new]).tolist()


def proyect(vector_A, vector_B):
    vector_A = np.array(vector_A)
    vector_B = np.array(vector_B)
    dot_product = np.dot(vector_A, vector_B)
    magnitude_squared = np.dot(vector_B, vector_B)    
    projection = (dot_product / magnitude_squared) * vector_B
    return projection.tolist()


def transformations(time, *args):
    init = args[0]
    self.play(Create(init))
    self.wait(time)
    for i in range(1, len(args)):
        self.play(Transform(init, args[i]))
        self.wait(time)
    return init

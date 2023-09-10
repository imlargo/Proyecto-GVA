def ortogonal(v):
    return [-v[1], v[0]]

def rot_vec(vector, angulo):
    angle_radians = np.radians(angulo)
    x, y = np.array(vector)
    x_new = x * np.cos(angle_radians) - y * np.sin(angle_radians)
    y_new = x * np.sin(angle_radians) + y * np.cos(angle_radians)
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
from manim import *


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




class PlaneScene(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(self,
            include_background_plane = True,
            include_foreground_plane = True,
            #background_plane_kwargs = None,
            #foreground_plane_kwargs = None,
            show_coordinates = True,
            show_basis_vectors = True,
            leave_ghost_vectors = True
            )
        
    def construct(self):
        self.vectores()
        self.wait()
        
        
    def vectores(self):
        vector1 = Vector([1, 2], color = PURPLE_A)
        label1 = vector1.coordinate_label(color = PURPLE_A)
        
        vector2 = Vector([2, -1], color = TEAL_A)
        label2 = vector2.coordinate_label(color = TEAL_A)
        
        vector3 = Vector([3, 1], color = YELLOW_C)
        label3 = vector3.coordinate_label(color = YELLOW_C)
        
        titulo1 = Tex("Suma de vectores :3").to_corner(UP + LEFT)
        titulo2 = Tex("El orden no importa!").to_corner(UP + LEFT)
        
        newVector1 = Vector([1, 2], color = PURPLE_A)
        
        sumaVec = (MathTex(r"\vec{A} + \vec{B} = \vec{X}")).to_corner(DOWN + LEFT)
        sumaComp = MathTex(r"\begin{bmatrix} 1\\ 2\\ \end{bmatrix} + \begin{bmatrix} 2\\ -1\\ \end{bmatrix}").to_corner(DOWN + LEFT)
        sumaResult = MathTex(r"\begin{bmatrix} 1\\ 2\\ \end{bmatrix} + \begin{bmatrix} 2\\ -1\\ \end{bmatrix} = \begin{bmatrix} 3\\ 1\\ \end{bmatrix}").to_corner(DOWN + LEFT)
        
        self.play(Create(vector1), Create(label1))
        self.play(Create(vector2), Create(label2))
        
        self.play(Create(titulo1))
        
        self.play(Write(sumaVec))
        self.wait(1)
        self.play(Transform(sumaVec, sumaComp))
        self.wait(1)
        self.play(ApplyMethod(vector1.shift, vector2.get_end()))
        self.play(Create(vector3), Create(label3), Transform(sumaComp, sumaResult))
        
        #Segunda parte ---
        self.wait(1)
        self.play(Transform(titulo1, titulo2), FadeOut(vector3), FadeOut(label3))
        self.wait()
    
        self.play(Transform(vector1, newVector1))
        self.wait(1)
        self.play(ApplyMethod(vector2.shift, newVector1.get_end()))
        
        self.wait()
        self.play(Create(vector3), Create(label3))
        self.wait(2)

        pass
        
        
    def sum_vectores(self):
        vector1 = Vector([1, 2], color = PURPLE_A)
        label1 = vector1.coordinate_label(color = PURPLE_A)
        
        vector2 = Vector([2, -1], color = TEAL_A)
        label2 = vector2.coordinate_label(color = TEAL_A)
        
        vector3 = Vector([3, 1], color = YELLOW_C)
        label3 = vector3.coordinate_label(color = YELLOW_C)
        
        titulo1 = Tex("Suma de vectores :3").to_corner(UP + LEFT)
        titulo2 = Tex("El orden no importa!").to_corner(UP + LEFT)
        
        newVector1 = Vector([1, 2], color = PURPLE_A)
        
        sumaVec = (MathTex(r"\vec{A} + \vec{B} = \vec{X}")).to_corner(DOWN + LEFT)
        sumaComp = MathTex(r"\begin{bmatrix} 1\\ 2\\ \end{bmatrix} + \begin{bmatrix} 2\\ -1\\ \end{bmatrix}").to_corner(DOWN + LEFT)
        sumaResult = MathTex(r"\begin{bmatrix} 1\\ 2\\ \end{bmatrix} + \begin{bmatrix} 2\\ -1\\ \end{bmatrix} = \begin{bmatrix} 3\\ 1\\ \end{bmatrix}").to_corner(DOWN + LEFT)
        
        self.play(Create(vector1), Create(label1))
        self.play(Create(vector2), Create(label2))
        
        self.play(Create(titulo1))
        
        self.play(Write(sumaVec))
        self.wait(1)
        self.play(Transform(sumaVec, sumaComp))
        self.wait(1)
        self.play(ApplyMethod(vector1.shift, vector2.get_end()))
        self.play(Create(vector3), Create(label3), Transform(sumaComp, sumaResult))
        
        #Segunda parte ---
        self.wait(1)
        self.play(Transform(titulo1, titulo2), FadeOut(vector3), FadeOut(label3))
        self.wait()
    
        self.play(Transform(vector1, newVector1))
        self.wait(1)
        self.play(ApplyMethod(vector2.shift, newVector1.get_end()))
        
        self.wait()
        self.play(Create(vector3), Create(label3))
        self.wait(2)

        
        pass
    
    def resta_vectores(self):
        

        
        pass
        
        
test = PlaneScene()
test.render()
from IPython.display import clear_output
#clear_output()
from IPython.display import HTML
from base64 import b64encode
video_path =  '/content/media/videos/1080p60/PlaneScene.mp4'
video_file = open(video_path, "rb")
video_bytes = video_file.read()
video_encoded = b64encode(video_bytes).decode("ascii")
HTML(f'<video width="1280" height="720" controls><source src="data:video/mp4;base64,{video_encoded}" type="video/mp4"></video>')
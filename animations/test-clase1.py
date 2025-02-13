from manim import *
from misc.All import *


class PlaneScene(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(self,
            include_background_plane = True,
            include_foreground_plane = True,
            #background_plane_kwargs = None,
            #foreground_plane_kwargs = None,
            show_coordinates = False,
            show_basis_vectors = False,
            leave_ghost_vectors = True
            )
        
    def construct(self):
        self.sum_vectores([2,1], [-3, 1])
        self.wait()
        
        
    def vectores(self):
        pass

            
    def trig(self):

        angulo = ValueTracker(0)

        def get_scaled_vector():
            v = Vector([3 * cos(angulo.get_value()), 3 * sin(angulo.get_value())], color = TEAL_C)            
            return v
        
        def get_line_x():
            x = [3 * cos(angulo.get_value()), 3 * sin(angulo.get_value()), 0]
            y = [0, 3 * sin(angulo.get_value()), 0]
            return Line(np.array(y), np.array([0,0,0]), color = GREEN_C)

        def get_line_y():
            x = [(3 * cos(angulo.get_value())), (3 * sin(angulo.get_value())), 0]
            y = [3 * cos(angulo.get_value()), 0, 0]
            return Line(np.array([0, 0, 0]), np.array(y), color = RED_C)
        
        def get_point_x():
            return Dot(point = [3 * cos(angulo.get_value()), 0, 0], color = RED_C)#.scale(3)

        def get_point_y():
            return Dot(point = [0, 3 * sin(angulo.get_value()), 0], color = GREEN_C)#.scale(3)
        
        def get_point():
            clear_output()
            return Dot(point = [3 * cos(angulo.get_value()), 3 * sin(angulo.get_value()), 0], color = PURPLE_A)#.scale(3)
        
        def tex_cos():
            tex = f"cos({int(angulo.get_value())}" + r"^{\circ})"
            return MathTex(tex).scale(0.7).move_to(np.array([4, 0.5,0]))

        def tex_sin():
            tex = f"sin({int(angulo.get_value())}" + r"^{\circ})"
            return MathTex(tex).scale(0.7).move_to(np.array([0,3.5,0]))

        def tex_vec():
            x = f"cos({int(angulo.get_value())}" + r"^{\circ})"
            y = f"sin({int(angulo.get_value())}" + r"^{\circ})"
            return Matrix([[x], [y]]).scale(0.7).move_to(np.array([5,2.5,0]))
        
        graph = ImplicitFunction(lambda x, y: (x ** 2) +  (y ** 2) - 9,color = PURPLE_A)

        v = always_redraw(get_scaled_vector)
        point = always_redraw(get_point)
        lineCos = always_redraw(get_line_x)
        lineSin = always_redraw(get_line_y)
        pointX = always_redraw(get_point_x)
        pointY = always_redraw(get_point_y)
        texCos = always_redraw(tex_cos)
        texSin = always_redraw(tex_sin)
        label = always_redraw(tex_vec)
        

        self.play(Create(v), Create(graph), Create(label), Create(texCos), Create(texSin), Create(point), Create(lineCos), Create(lineSin), Create(pointX), Create(pointY))
        self.play(angulo.animate.set_value(120), run_time = 3)
        self.wait()
        self.play(angulo.animate.set_value(-60), run_time = 2)
        self.wait()
        self.play(angulo.animate.set_value(270), run_time = 3)        
        

        
    def desc(self):
        v = [2,1]
        v_ort = ortogonal(v)
        
        x = [2, 3]
        
        vector1 = Vector(v, color = PURPLE_A)
        label1 = vector1.coordinate_label(color = PURPLE_A).scale(0.7)
        
        vector2 = Vector(v_ort, color = PURPLE_A)
        label2 = vector2.coordinate_label(color = PURPLE_A).scale(0.7)
        
        vX = Vector(x, color = YELLOW_C)
        label3 = vX.coordinate_label(color = YELLOW_C).scale(0.7)
        
        titulo1 = Tex("Descomposicion ortogonal").scale(0.7).to_corner(UP + RIGHT)
        
        msg = (MathTex(r"\vec{A} \cdot \vec{B} = 0")).scale(0.7).to_corner(UP + LEFT)
        msg2 = (MathTex(r"\vec{B} = \vec{A}^{\perp}")).scale(0.7).to_corner(UP + LEFT)
        msg3 = (MathTex(r"\vec{A} \cdot \vec{B} = 0")).scale(0.7).to_corner(UP + LEFT)

        sum1 = (MathTex(r"\vec{X} = P_{\vec{A}}(\vec{X}) + P_{\vec{B}}(\vec{X})")).scale(0.7).to_corner(UP + LEFT)
        sum2 = (MathTex(r"\vec{X} = P_{\vec{A}}(\vec{X}) + P_{\vec{A}^{\perp}}(\vec{X})")).scale(0.7).to_corner(UP + LEFT)

        self.play(Create(titulo1))
        self.play(Create(vector1), run_time = 0.5) #Create(label1)
        self.play(Create(vector2), run_time = 0.5) # Create(label2)
        

        self.play(Write(msg))
        self.wait()
        self.play(Transform(msg, msg2))
        self.wait()
        self.play(Transform(msg, msg3))
        self.wait()
        self.play(FadeOut(msg))

        self.play(Create(vX))
        self.wait()

        self.play(Create(sum1))
        self.wait()
        self.play(Transform(sum1, sum2))
        self.wait()

        pA = Vector(proyect(x, v), color = TEAL_A)
        pB = Vector(proyect(x, v_ort), color = TEAL_A)
        
        aux = vX.copy()
        line = Line(vX.get_end(), pA.get_end())
        self.play(Create(line))
        self.play(Transform(aux, pA))
        self.add(pA)
        self.remove(aux)
        self.play(FadeOut(line))
        self.wait()
        
        aux = vX.copy()
        line = Line(vX.get_end(), pB.get_end())
        self.play(Create(line))
        self.play(Transform(aux, pB))
        self.add(pB)
        self.remove(aux)
        self.play(FadeOut(line))
        
        self.play(FadeOut(vector1), FadeOut(vector2))
        aux = pA.copy()
        self.play(ApplyMethod(pA.shift, pB.get_end()))
        self.wait(1)
        self.play(Transform(pA, aux))
        self.wait()
        self.play(ApplyMethod(pB.shift, pA.get_end()))
       

        
    def sum_vectores(self, v1, v2):
        vector1 = Vector(v1, color = PURPLE_A)
        label1 = vector1.coordinate_label(color = PURPLE_A).scale(0.7)
        
        vector2 = Vector(v2, color = TEAL_A)
        label2 = vector2.coordinate_label(color = TEAL_A).scale(0.7)
        
        vector3 = Vector((np.array(v1) + np.array(v2)), color = YELLOW_C)
        label3 = vector3.coordinate_label(color = YELLOW_C).scale(0.7)
        
        titulo1 = Tex("Suma de vectores :3").to_corner(UP + LEFT)
        titulo2 = Tex("El orden no importa!").to_corner(UP + LEFT)
        
        newVector1 = Vector(np.array(v1), color = PURPLE_A)
        
        sumaVec = (MathTex(r"\vec{A} + \vec{B} = \vec{X}")).to_corner(DOWN + LEFT)
        sumaVec2 = (MathTex(r"\vec{B} + \vec{A} = \vec{X}")).to_corner(DOWN + LEFT)
        
        sumaComp = MathTex(r"\begin{bmatrix} 1\\ 2\\ \end{bmatrix} + \begin{bmatrix} 2\\ -1\\ \end{bmatrix}").to_corner(DOWN + LEFT)
        sumaResult = MathTex(r"\begin{bmatrix} 1\\ 2\\ \end{bmatrix} + \begin{bmatrix} 2\\ -1\\ \end{bmatrix} = \begin{bmatrix} 3\\ 1\\ \end{bmatrix}").to_corner(DOWN + LEFT)
        
        self.play(Create(vector1), Create(label1))
        self.play(Create(vector2), Create(label2))
        
        self.play(Create(titulo1))
        
        self.play(Write(sumaVec))
        self.wait()
        #self.play(Transform(sumaVec, sumaComp))
        
        #self.wait(1)
        self.play(ApplyMethod(vector1.shift, vector2.get_end()))
        self.play(Create(vector3), Create(label3)) #, Transform(sumaComp, sumaResult)
        
        #Segunda parte ---
        self.play(Transform(sumaVec, sumaVec2))
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
    
    
    
    
    def rotar_vectores(self, vector, angulo):
        
        vector1 = Vector(vector, color = PURPLE_A)
        label1 = vector1.coordinate_label(color = PURPLE_A)
            
        vector2 = Vector(rot_vec(vector, angulo), color = TEAL_A)
        label2 = vector2.coordinate_label(color = TEAL_A)
        self.play(Create(vector1), Create(label1))
        self.wait()
        self.play(Rotate(vector1, angle= np.radians(angulo), about_point=ORIGIN, rate_func=linear))
        self.wait()
        self.play(Transform(vector1, vector2), Transform(label1, label2))
        self.wait()
        pass
        
        
test = PlaneScene()
test.render()
from IPython.display import clear_output
clear_output()
from IPython.display import HTML
from base64 import b64encode
video_path =  '/content/media/videos/1080p60/PlaneScene.mp4'
video_file = open(video_path, "rb")
video_bytes = video_file.read()
video_encoded = b64encode(video_bytes).decode("ascii")
HTML(f'<video width="1280" height="720" controls><source src="data:video/mp4;base64,{video_encoded}" type="video/mp4"></video>')

from manim import *
import numpy as np

def sum_v(v1, v2):
    return [(v1[0] + v2[0]), (v1[1] + v2[1])]

def res_v(v1, v2):
    return [(v1[0] - v2[0]), (v1[1] - v2[1])]

def escalar(v, n):
    return [v[0] * n, v[1] * n]

class PlaneScene(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(self,
            include_background_plane = True,
            include_foreground_plane = False,
            show_coordinates = True,
            show_basis_vectors = False,
            leave_ghost_vectors = True
            )
        
    def construct(self):
        self.escalando()
        self.wait()

    def resaltar(self, objeto):
        pass    

    def escalando(self):
        
        v = [2,1]
       
        #Hacemos la pareja ordenada v = (2,1) como vector
        vector = Vector(v, color = RED_A)
        name = MathTex(r"n \cdot \vec{v}", color = RED_A)
        label = vector.coordinate_label(color = RED_A).to_corner(UP+LEFT)

        
        #Vector aleatorio?
        n = ValueTracker(1)
        
        graph = ImplicitFunction(lambda x, y: y - ((1/2) * x),color = PURPLE_A).set_stroke(opacity = 0.7, width=2) 
        
        punto = always_redraw(lambda: Dot(point = np.array(escalar(v,n.get_value()) + [0]), color = YELLOW))
        vector = always_redraw(lambda: Vector(escalar(v,n.get_value()), color = RED_A))
        name = always_redraw(lambda: MathTex(str(round(n.get_value(),1)) + r" \cdot \vec{v}", color = RED_A).shift((vector.get_end() - vector.get_start()) / 2).shift(UP * 0.5))
        vlabel = always_redraw(lambda: MathTex(str(round(n.get_value(),1)) + r" \cdot \begin{bmatrix} 2\\ 1\end{bmatrix}", color = RED_A).to_corner(UP+LEFT))

        nameBefore = MathTex(r"n \cdot \vec{v}", color = RED_A).shift((vector.get_end() - vector.get_start()) / 2).shift(UP * 0.5)
        labelBefore = MathTex(r"n \cdot \begin{bmatrix} 2\\ 1\end{bmatrix}", color = RED_A).to_corner(UP+LEFT)

        self.play(Create(vector), Create(punto), Create(nameBefore), Create(labelBefore))
        self.wait(1)
        self.play(Create(name), Create(vlabel), FadeOut(labelBefore), FadeOut(nameBefore))
        
        #Cambiando los valores de n
        self.play(n.animate.set_value(2), run_time = 3)
        self.wait(1)
        self.play(n.animate.set_value(-1), Create(graph), run_time = 2)
        self.wait(0.5)
        self.play(n.animate.set_value(-3), run_time = 3)
        self.play(n.animate.set_value(2.5), run_time = 2)

        self.play(FadeOut(vector), FadeOut(punto), FadeOut(name), FadeOut(vlabel))
        pass

    def rayo_recta(self):

        pass
    
    def dependencia_lineal(self):
        pass

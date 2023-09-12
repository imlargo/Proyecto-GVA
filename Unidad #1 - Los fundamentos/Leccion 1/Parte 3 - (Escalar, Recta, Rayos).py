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
        self.rayo_recta()
        self.wait()

    def resaltar(self, objeto, tiempo, color):
        return ShowPassingFlash(SurroundingRectangle(objeto, color = color, buff = 0.25), run_time=tiempo, time_width=0.2)

    def escalando(self):
        
        v = [2,1]
        n = ValueTracker(1)
        #Hacemos la pareja ordenada v = (2,1) como vector
        vector = Vector(v, color = RED_A)
        name = MathTex(r"n \cdot \vec{v}", color = RED_A)
        label = vector.coordinate_label(color = RED_A).to_corner(UP+LEFT)

        # --- Escalamos el vector con una animacion continua ---
        #Definimos todas las variables
        graph = ImplicitFunction(lambda x, y: y - ((1/2) * x),color = PURPLE_A).set_stroke(opacity = 0.7, width=2) 
        
        punto = always_redraw(lambda: Dot(point = np.array(escalar(v,n.get_value()) + [0]), color = YELLOW))
        vector = always_redraw(lambda: Vector(escalar(v,n.get_value()), color = RED_A))
        name = always_redraw(lambda: MathTex(str(round(n.get_value(),1)) + r" \cdot \vec{v}", color = RED_A).shift((vector.get_end() - vector.get_start()) / 2).shift(UP * 0.5))
        vlabel = always_redraw(lambda: MathTex(str(round(n.get_value(),1)) + r" \cdot \begin{bmatrix} 2\\ 1\end{bmatrix}", color = RED_A).to_corner(UP+LEFT))

        nameBefore = MathTex(r"n \cdot \vec{v}", color = RED_A).shift((vector.get_end() - vector.get_start()) / 2).shift(UP * 0.5)
        labelBefore = MathTex(r"n \cdot \begin{bmatrix} 2\\ 1\end{bmatrix}", color = RED_A).to_corner(UP+LEFT)

        rectaGen = MathTex(r"L_{\vec{v}}").move_to(np.array([-3, 2, 0])).scale(1.25)
        conjunto = MathTex(r"n \cdot \vec{v} \ | \ n \in \mathbb{R}").to_corner(DOWN + RIGHT)
        

        #Creamos el vector
        self.play(Create(vector), Create(punto), Create(nameBefore), Create(labelBefore))
        self.wait(1)
        self.play(FadeOut(labelBefore), FadeOut(nameBefore), Create(name), Create(vlabel))

        #Cambiando los valores de n
        self.play(n.animate.set_value(2), run_time = 3)
        self.wait(1)
        self.play(n.animate.set_value(-1), Create(graph), Create(rectaGen), Create(conjunto), run_time = 2)
        self.play(self.resaltar(rectaGen, 1, TEAL_C), self.resaltar(conjunto, 1, TEAL_C) )
        self.play(n.animate.set_value(-3), run_time = 3)
        self.play(n.animate.set_value(2.5), run_time = 2)

        #Resaltamos los datos importantes
        self.play(FadeOut(vector), FadeOut(punto), FadeOut(name), FadeOut(vlabel))
        self.play(self.resaltar(conjunto, 1, TEAL_C), (ShowPassingFlash(
                ImplicitFunction(lambda x, y: y - ((1/2) * x),color = BLUE),
                run_time=2,
                time_width=0.2
            )), (ShowPassingFlash(
                SurroundingRectangle(rectaGen, color = TEAL_C, buff = 0.25),
                run_time=2,
                time_width=0.2
            )))
        self.play(FadeOut(graph), FadeOut(rectaGen), FadeOut(conjunto)) 
        pass

    def rayo_recta(self):
        v = [2,1]
        n = ValueTracker(1)       
        #Hacemos la pareja ordenada v = (2,1) como vector
        vector = Vector(v, color = RED_A)
        name = MathTex(r"n \cdot \vec{v}", color = RED_A)
        label = vector.coordinate_label(color = RED_A).to_corner(UP+LEFT)

        # --- Escalamos el vector con una animacion continua ---
        #Definimos todas las variables
        punto = always_redraw(lambda: Dot(point = np.array(escalar(v,n.get_value()) + [0]), color = YELLOW))
        vector = always_redraw(lambda: Vector(escalar(v,n.get_value()), color = RED_A))
        name = always_redraw(lambda: MathTex(str(round(n.get_value(),1)) + r" \cdot \vec{v}", color = RED_A).shift((vector.get_end() - vector.get_start()) / 2).shift(UP * 0.5))
        vlabel = always_redraw(lambda: MathTex(str(round(n.get_value(),1)) + r" \cdot \begin{bmatrix} 2\\ 1\end{bmatrix}", color = RED_A).to_corner(UP+LEFT))

        rayPos = ImplicitFunction(lambda x, y: y - ((1/2) * x),color = PURPLE_A, x_range = [0, 7]).set_stroke(opacity = 0.8, width=3) 
        rayNeg = ImplicitFunction(lambda x, y: y - ((1/2) * x),color = PURPLE_A, x_range = [0, -7]).set_stroke(opacity = 0.8, width=3) 
        
        nameBefore = MathTex(r"n \cdot \vec{v}", color = RED_A).shift((vector.get_end() - vector.get_start()) / 2).shift(UP * 0.5)
        labelBefore = MathTex(r"n \cdot \begin{bmatrix} 2\\ 1\end{bmatrix}", color = RED_A).to_corner(UP+LEFT)

        rayGen = MathTex(r"R_{\vec{v}}^{+}").move_to(np.array([5, 1, 0])).scale(1.25)
        raynegGen = MathTex(r"R_{\vec{v}}^{-}").move_to(np.array([-2, -2.5, 0])).scale(1.25)
        conjunto = MathTex(r"n \cdot \vec{v} \ | \ n > 0").next_to(rayGen, DOWN, buff = 0.5)
        conjunto.add_background_rectangle(BLACK)

        #Creamos los objetos en el plano
        self.play(Create(vector), Create(punto), Create(nameBefore), Create(labelBefore))
        self.wait(1)
        self.play(FadeOut(labelBefore), FadeOut(nameBefore), Create(name), Create(vlabel))

        #... Rayo Positivo ...
        self.play(n.animate.set_value(2), Create(rayPos), Create(rayGen), Create(conjunto), run_time = 3)
        self.play(self.resaltar(rayGen, 1, TEAL_C), self.resaltar(conjunto, 1, TEAL_C))
        self.play(n.animate.set_value(0.5), run_time = 2)
        self.play(n.animate.set_value(0.25), run_time = 2)
        self.play(n.animate.set_value(3), run_time = 2)
        self.play(n.animate.set_value(1), run_time = 2)
        #Resaltamos los datos importantes
        self.play(
            (ShowPassingFlash((rayPos.copy().set_color(TEAL_C)), run_time=2, time_width=0.2)),
            (ShowPassingFlash(SurroundingRectangle(rayGen, color = TEAL_C, buff = 0.25), run_time=2, time_width=0.2))
            )
        self.play(FadeOut(rayPos), FadeOut(rayGen), FadeOut(conjunto))
        
        #... Rayo negativo ...
        conjunto = MathTex(r"n \cdot \vec{v} \ | \ n < 0").next_to(raynegGen, DOWN, buff = 0.5)
        conjunto.add_background_rectangle(BLACK)
        self.play(n.animate.set_value(-1), Create(rayNeg), Create(raynegGen), Create(conjunto), run_time = 3)
        self.play(self.resaltar(raynegGen, 1, TEAL_C), self.resaltar(conjunto, 1, TEAL_C))
        self.play(n.animate.set_value(-0.5), run_time = 2)
        self.play(n.animate.set_value(-0.25), run_time = 2)
        self.play(n.animate.set_value(-3), run_time = 2)
        self.play(n.animate.set_value(-1), run_time = 2)
        #Resaltamos los datos importantes
        self.play(
            (ShowPassingFlash((rayNeg.copy().set_color(TEAL_C)), run_time=2, time_width=0.2)),
            (ShowPassingFlash(SurroundingRectangle(raynegGen, color = TEAL_C, buff = 0.25), run_time=2, time_width=0.2))
            )
        self.play(FadeOut(rayNeg), FadeOut(raynegGen), FadeOut(conjunto), FadeOut(vector))
        pass
    
    def escalar_longitud(self):
        pass

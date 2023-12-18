# Imports
from manim import *;
import numpy as np;
        
# Escena en el plano
class PlaneScene(LinearTransformationScene):
    def __init__(self):
        # Configuracion del plano
        LinearTransformationScene.__init__(self,
            include_background_plane = True,
            include_foreground_plane = True,
            show_coordinates = True,
            show_basis_vectors = False,
            leave_ghost_vectors = False
            )
        pass


    def construct(self):
        #self.sum_vectores()
        self.resta_vectores()
        #self.paralelogramo()
        self.wait()
        
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
        self.play(
            self.resaltar(conjunto, 1, TEAL_C),
            (ShowPassingFlash(
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
        self.play(FadeOut(rayNeg, raynegGen, conjunto, vector, punto, vlabel, name))
        pass
    
    def escalar_longitud(self):
        pass


                
    def sum_vectores(self):
        
        v1 = [4, 1]
        v2 = [1, 2]
        suma = sum_v(v1, v2)
        
        #Elementos
        punto = Dot(point = np.array([suma[0],suma[1] ,0]), color = YELLOW)

        vector1 = Vector(v1, color = PURPLE_A)
        label1 = vector1.coordinate_label(color = PURPLE_A).scale(0.7)
        name1 = MathTex(r"\vec{A}", color = PURPLE_A).scale(0.7).shift((vector1.get_end() - vector1.get_start()) / 2).shift(UP * 0.5)

        vector2 = Vector(v2, color = TEAL_A)
        label2 = vector2.coordinate_label(color = TEAL_A).scale(0.7)
        name2 = MathTex(r"\vec{B}", color = TEAL_A).scale(0.7).shift((vector2.get_end() - vector2.get_start()) / 2).shift(UP * 0.5)

        vector3 = Vector(suma, color = YELLOW_C)
        label3 = vector3.coordinate_label(color = YELLOW_C).scale(0.7)
        name3 = MathTex(r"\vec{X}", color = YELLOW_C).scale(0.7).shift((vector3.get_end() - vector3.get_start()) / 2).shift(UP * 0.5)
        

        #Propiedades
        sumaVec = (MathTex(r"\vec{A} + \vec{B} = \vec{X}")).to_corner(DOWN + LEFT)
        sumaVec2 = (MathTex(r"\vec{B} + \vec{A} = \vec{X}")).to_corner(DOWN + LEFT)
        sumaVec3 = (MathTex(r"\vec{A} + \vec{B} = \vec{B} + \vec{A}")).to_corner(DOWN + LEFT)
        aux = sumaVec.copy()

        self.play(Create(vector1), Create(label1), Create(name1))
        self.play(Create(vector2), Create(label2), Create(name2))
        
        #A + B = B + A
        self.play(Write(sumaVec))
        self.wait()
        self.play(Transform(sumaVec, sumaVec2))
        self.play(Transform(sumaVec, sumaVec3))
        self.play(Transform(sumaVec, aux))

        self.play(FadeOut(label1), FadeOut(label2))

        #Mover a la cabeza ... A -> B
        aux = vector1.copy()
        aux_name = name1.copy()
        self.play(ApplyMethod(vector1.shift, vector2.get_end()), ApplyMethod(name1.shift, vector2.get_end()))
        self.play(Create(vector3), Create(label3), Create(name3), Create(punto))
        self.wait(1)
        self.play(Transform(vector1, aux), FadeOut(vector3), FadeOut(label3), FadeOut(name3), Transform(name1, aux_name))
        
        #Mover a la cabeza ... B -> A
        aux2 = vector2.copy()
        aux_name = name2.copy()
        self.play(ApplyMethod(vector2.shift, aux.get_end()), ApplyMethod(name2.shift, aux.get_end()))
        self.play(Create(vector3), Create(label3), Create(name3))
        self.wait(1)
        self.play(Transform(vector2, aux2), FadeOut(vector3), FadeOut(punto), FadeOut(name3), FadeOut(label3), Transform(name2, aux_name))
        
        #Ley del paralelogramo?
        self.play(FadeOut(vector1), FadeOut(vector2), FadeOut(name1),FadeOut(name2),)
        vectors = [
            ([ 5,  1], [-2, 1]),
            ([-3, -1], [-1, 2]),
            ([ 2, -3], [ 2, 1]),
            #([-4,  1], [3, -3])
            ]

        a = ValueTracker(0)
        b = ValueTracker(0)
        c = ValueTracker(0)
        d = ValueTracker(0)

        punto = always_redraw(lambda: Dot(point = np.array([a.get_value() + c.get_value(), b.get_value() + d.get_value(), 0]), color = YELLOW))
        
        vector1 = always_redraw(lambda: Vector([a.get_value(), b.get_value()], color = TEAL_C))
        vector2 = always_redraw(lambda: Vector([c.get_value(), d.get_value()], color = PURPLE_C))        
        vector3 = always_redraw(lambda: Vector([a.get_value() + c.get_value(), b.get_value() + d.get_value()], color = YELLOW))

        subV1 = always_redraw(lambda: vector1.copy().shift(vector2.get_end()))
        subV2 = always_redraw(lambda: vector2.copy().shift(vector1.get_end()))

        name1 = always_redraw(lambda: MathTex(r"\vec{A}", color = TEAL_A).scale(0.8).shift((vector1.get_end() - vector1.get_start()) / 2).shift(UP * 0.5))
        name2 = always_redraw(lambda: MathTex(r"\vec{B}", color = PURPLE_A).scale(0.8).shift((vector2.get_end() - vector2.get_start()) / 2).shift(UP * 0.5))
        name3 = always_redraw(lambda: MathTex(r"\vec{X}", color = YELLOW).scale(0.8).shift(punto.get_center()).shift(UP * 0.5))
        self.play(Create(vector1), Create(vector2), Create(subV1), Create(subV2), Create(punto), Create(vector3), Create(name1), Create(name2), Create(name3))

        for par in vectors:
            vA = par[0]
            vB = par[1]
            
            self.play(a.animate.set_value(vA[0]), b.animate.set_value(vA[1]), c.animate.set_value(vB[0]), d.animate.set_value(vB[1]), run_time = 3)
            self.wait(1)

    def resta_vectores(self):
        
        v1 = [4, 1]
        v2 = [1, 2]
        suma = res_v(v1, v2)
        
        #Elementos
        punto = Dot(point = np.array([suma[0],suma[1] ,0]), color = YELLOW)

        vector1 = Vector(v1, color = PURPLE_A)
        label1 = vector1.coordinate_label(color = PURPLE_A).scale(0.7)
        name1 = MathTex(r"\vec{A}", color = PURPLE_A).scale(0.7).shift((vector1.get_end() - vector1.get_start()) / 2).shift(UP * 0.5)

        vector2 = Vector(v2, color = TEAL_A)
        label2 = vector2.coordinate_label(color = TEAL_A).scale(0.7)
        name2 = MathTex(r"\vec{B}", color = TEAL_A).scale(0.7).shift((vector2.get_end() - vector2.get_start()) / 2).shift(UP * 0.5)

        minusV2 = Vector(escalar(v2, -1), color = TEAL_A)
        nameM2 = MathTex(r"-1 \cdot \vec{B}", color = TEAL_A).scale(0.7).shift((minusV2.get_end() - minusV2.get_start()) / 2).shift(RIGHT * 0.6)
        
        vector3 = Vector(suma, color = YELLOW_C)
        label3 = vector3.coordinate_label(color = YELLOW_C).scale(0.7)
        name3 = MathTex(r"\vec{A} - \vec{B}", color = YELLOW_C).scale(0.7).shift((vector3.get_end() - vector3.get_start()) / 2).shift(DOWN * 0.5)
        

        #Propiedades
        sumaVec = (MathTex(r"\vec{A} - \vec{B} = \vec{X}")).to_corner(DOWN + LEFT)
        sumaVec2 = (MathTex(r"\vec{A} - \vec{B} = -1 \cdot ( \vec{B} - \vec{A} )")).to_corner(DOWN + LEFT)
        sumaVec3 = (MathTex(r"\vec{A} + (-1) \cdot \vec{B} = \vec{A} - \vec{B} = \vec{X}")).to_corner(DOWN + LEFT)
        aux = sumaVec.copy()

        self.play(Create(vector1), Create(label1), Create(name1))
        self.play(Create(vector2), Create(label2), Create(name2))
        
        #Propiedades
        self.play(Write(sumaVec))
        self.wait()
        self.play(Transform(sumaVec, sumaVec2))
        self.wait()
        self.play(Transform(sumaVec, sumaVec3))
        self.wait()
        self.play(FadeOut(label1), FadeOut(label2))

        #... A + -B
        self.play(Create(minusV2), Create(nameM2), FadeOut(vector2), FadeOut(name2))
        self.wait(1)
    
        aux = minusV2.copy()
        aux_name = nameM2.copy()
        self.play(ApplyMethod(minusV2.shift, vector1.get_end()), ApplyMethod(nameM2.shift, vector1.get_end()))
        self.play(Create(vector3), Create(label3), Create(name3), Create(punto))
        self.wait(1)
        self.play(Transform(minusV2, aux), FadeOut(vector3), FadeOut(label3), FadeOut(name3), Transform(nameM2, aux_name))
        
        self.play(FadeOut(minusV2), FadeOut(vector1), FadeOut(nameM2),FadeOut(name1), FadeOut(punto))
        
        
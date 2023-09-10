from manim import *

class LineScene(Scene):
    def construct(self):
        recta = NumberLine(
            x_range = [-10, 10, 1],
            unit_size = 0.6,
            include_numbers = True,
            font_size = 24,
        )
        
        value = ValueTracker(0)

        def getPoint():
            return Dot(point = recta.n2p(value.get_value()), color = RED_A) 
        
        def updateArrow(arrow):
            arrow.move_to(recta.n2p(value.get_value())).shift(UP * 0.5)

        def updateLine():
            return Line(np.array([0,0,0]), recta.n2p(value.get_value()), color = RED_A)
            
        punto = always_redraw(getPoint)
        line = always_redraw(updateLine)

        arrow = Arrow(start= UP, end= DOWN, color = PURPLE_A).scale(0.4, scale_tips=True)
        arrow.add_updater(updateArrow)

        self.play(Create(recta), Create(punto), Create(arrow), Create(line)) 
        self.play(value.animate.set_value(-5), run_time = 3)
        self.wait()


class PlaneScene(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(self,
            include_background_plane = True,
            include_foreground_plane = True,
            show_coordinates = True,
            show_basis_vectors = False,
            leave_ghost_vectors = False
            )
        
    def construct(self):
        #Generamos el plano y destacamos el origen O
        O = MathTex(r"\vec{O}").shift((UP*0.5) + (RIGHT*0.5)).set_color(RED_A)
        self.play(Write(O))
        self.wait()

        #Les ponemos nombres a los ejes
        ejeX = Tex("Eje X").shift(UP + RIGHT).scale(0.7).set_color(GREEN_C)
        ejeY = Tex("Eje Y").shift(UP + RIGHT).scale(0.7).set_color(RED_C)
        
        self.play(Write(ejeX))
        self.play(ApplyMethod(ejeX.move_to, np.array([6, 0.5, 0])))
        self.wait()

        self.play(Write(ejeY))
        self.play(ApplyMethod(ejeY.move_to, np.array([0.5, 3.5, 0])))
        self.wait()

        #Representamos un punto, hacemos linea y pasos en X y en Y
        v = [3,2]
        punto = Dot(point = np.array([3,2,0]), color = YELLOW)
        self.play(Create(punto))
        self.play(FadeOut(punto.copy()), FadeOut(O))

        #...Pasos...
        lineaX = Line(np.array([0,0,0]), np.array([3,0,0]), color = GREEN_C) 
        lineaY = Line(np.array([3,0,0]), np.array([3,2,0]), color = RED_C)
        self.play(Create(lineaX))
        self.wait()
        self.play(Create(lineaY))
        self.wait()

        #Hacemos la pareja ordenada v = (1,2) como vector
        vector = Vector(v, color = TEAL_C)
        name = MathTex(r"\vec{v}", color = PURPLE_A)
        label = vector.coordinate_label(color = TEAL_C)
        
        self.play(Create(vector))
        self.label_vector(vector, name)
        self.wait(1)
        self.play(Create(label))
        self.wait()

        #Vector aleatorio?
        self.play(FadeOut(ejeX), FadeOut(ejeY))
        self.play(FadeOut(vector), FadeOut(punto), FadeOut(name), FadeOut(label), FadeOut(lineaX), FadeOut(lineaY))
        self.wait()

        vectors = [
            [2, 1],
            [-3, -1],
            [2,-3],
            [-4, 1],
        ]

        x = ValueTracker(0)
        y = ValueTracker(0)
        
        punto = always_redraw(lambda: Dot(point = np.array([x.get_value(), y.get_value(), 0]), color = YELLOW))
        lineaX = always_redraw(lambda: Line(np.array([0,0,0]), np.array([x.get_value(),0,0]), color = GREEN_C)) 
        lineaY = always_redraw(lambda: Line(np.array([x.get_value(),0,0]), np.array([x.get_value(),y.get_value(),0]), color = RED_C))
        vector = always_redraw(lambda: Vector([x.get_value(), y.get_value()], color = TEAL_C))
        name = always_redraw(lambda: MathTex(r"\vec{v}", color = PURPLE_A).scale(0.8).shift((vector.get_end() - vector.get_start()) / 2))
        label = always_redraw(lambda: vector.coordinate_label(color = TEAL_C))

        self.play(Create(lineaX), Create(lineaY), Create(vector), Create(label), Create(punto), Create(name))

        for v1, v2 in vectors:
            self.play(x.animate.set_value(v1), y.animate.set_value(v2), run_time = 2)
        
        self.play(FadeOut(vector), FadeOut(punto), FadeOut(name), FadeOut(label), FadeOut(lineaX), FadeOut(lineaY))
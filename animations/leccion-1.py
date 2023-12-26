# Imports
from manim import *;
from misc.misc import *;
import numpy as np;

# Escena simple
class BaseScene(Scene):
    def construct(self):
        recta = NumberLine(
            x_range = [-10, 10, 1],
            unit_size = 0.6,
            include_numbers = True,
            font_size = 24,
        )
        
        numberValue = ValueTracker(0)
        arrow = Arrow(start= UP, end= DOWN, color = PURPLE_A).scale(0.4, scale_tips=True)

        getPoint = lambda: Dot(point = recta.n2p(numberValue.get_value()), color = RED_A)
        updateArrow = lambda arrow: arrow.move_to(recta.n2p(numberValue.get_value())).shift(UP * 0.5)
        updateLine = lambda: Line(np.array([0,0,0]), recta.n2p(numberValue.get_value()), color = RED_A)
            
        punto = always_redraw(getPoint)
        line = always_redraw(updateLine)
        arrow.add_updater(updateArrow)

        # // > Animación recta real, puntos en ella y punto q se mueve con flecha apuntando < //
        self.play(
            Create(recta),
            Create(punto),
            Create(arrow),
            Create(line)
        )
        self.play(delinear(recta, TEAL_C, 1))
        self.play(numberValue.animate.set_value(-5), run_time = 3)
        self.wait()
        self.play(numberValue.animate.set_value(0), run_time = 3)
        self.wait()
        self.play(numberValue.animate.set_value(3), run_time = 2)
        self.clear()
        pass

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
        
        # // > Generar el plano, escribimos _$\mathbb{R}^{2}$_, ponemos ejes y resaltamos el Origen < //
        origen = MathTex(r"\vec{O}").shift((UP*0.5) + (RIGHT*0.5)).set_color(RED_A)
        r2 = MathTex(r"\mathbb{R}^{2}")

        # Escribir el origen y r2
        self.play(Write(origen), Write(r2))
        self.wait()

        # Resaltar el origen y ejes
        self.play(
            resaltar(origen, TEAL_C, 1),
            delinear(r2, TEAL_C, 1)
        )

        # // > Les ponemos nombres a los ejes e indicamos su direccion < //
        lineX = Line(np.array([-5,0,0]), np.array([5,0,0]))
        lineY = Line(np.array([0,-5,0]), np.array([0,5,0]))

        tagX = Tex("eje X").move_to(np.array([6, 1, 0])).scale(0.7).set_color(GREEN_C)
        tagY = Tex("eje Y").move_to(np.array([1, 3.5, 0])).scale(0.7).set_color(RED_C)
        
        self.play(Write(tagX))
        self.play(delinear(lineX, GREEN_C, 1))
        self.wait()

        self.play(Write(tagY))
        self.play(delinear(lineY, RED_C, 1))
        self.wait()

        # // > Representamos un punto en el plano y lo movemos al rededor < //
        v = [3,2]
        punto = Dot(point = np.array([3,2,0]), color = YELLOW)
        self.play(Create(punto))
        self.play(FadeOut(origen, tagX, tagY))

        # // > Dejamos un punto y hacemos pasos en componentes X y Y. < //

        #...Pasos...
        lineaX = Line(np.array([0,0,0]), np.array([3,0,0]), color = GREEN_C) 
        lineaY = Line(np.array([3,0,0]), np.array([3,2,0]), color = RED_C)
        self.play(Create(lineaX))
        self.wait()
        self.play(Create(lineaY))
        self.wait()

        # // > Indicamos la pareja ordenada (3, 2) y resaltamos sus coordenadas < //
        cords = MathTex(r"\begin{pmatrix} 3 \\ 2 \end{pmatrix}")
        textPunto = Tex("Punto")

        self.play(Write(cords), Write(textPunto))
        self.play(resaltar(cords))

        # // > Resaltar la palabra "punto" < //
        self.play(resaltar(textPunto))

        # // > Convertir la palabra punto por vector, convertir el punto (2, 1) a vector, indicar direccion < //
        vector = Vector(v, color = TEAL_C)
        name = MathTex(r"\vec{v}", color = PURPLE_A)

        self.play(
            Transform(textPunto, Tex("Vector")),
            Transform(cords, MathTex(r"\begin{bmatrix} 3 \\ 2 \end{bmatrix}")),
            Create(vector)
        )

        self.play(resaltar(textPunto))

        # // > Resaltar direccion con una flecha y passing light < //
        self.wait()
        self.play(delinear(vector, RED_C, 1))
        self.wait()

        # // > Indicar el vector (2, 1), el punto (2, 1) y resaltar direccion < //
        
        # // > Indicar componentes y mostrar pasos < //
        

        """
        self.play(FadeOut(tagX), FadeOut(tagY))
        self.play(FadeOut(vector), FadeOut(punto), FadeOut(name), FadeOut(label), FadeOut(lineaX), FadeOut(lineaY))
        self.wait()

        vectors = [ [5, 1], [-3, -1], [2,-3], [-4, 1] ]

        x = ValueTracker(0)
        y = ValueTracker(0)
        
        punto = always_redraw(lambda: Dot(point = np.array([x.get_value(), y.get_value(), 0]), color = YELLOW))
        lineaX = always_redraw(lambda: Line(np.array([0,0,0]), np.array([x.get_value(),0,0]), color = GREEN_C)) 
        lineaY = always_redraw(lambda: Line(np.array([x.get_value(),0,0]), np.array([x.get_value(),y.get_value(),0]), color = RED_C))
        vector = always_redraw(lambda: Vector([x.get_value(), y.get_value()], color = TEAL_C))
        name = always_redraw(lambda: MathTex(r"\vec{v}", color = PURPLE_A).scale(0.8).shift((vector.get_end() - vector.get_start()) / 2).shift(UP * 0.5))

        self.play(Create(lineaX), Create(lineaY), Create(vector), Create(punto), Create(name))

        for v1, v2 in vectors:
            self.play(x.animate.set_value(v1), y.animate.set_value(v2), run_time = 2)
        
        self.play(FadeOut(vector), FadeOut(punto), FadeOut(name), FadeOut(lineaX), FadeOut(lineaY))
        """        
        
        
        
        # // > Limpiar plano, mostrar el origen como coordenadas, notacion y resaltar < //
        
        # // > Dibujar un vector nuevamente con componentes, direccion y resaltar < //
        
        # // > Mostrar meme < //
        self.clear()
        pass

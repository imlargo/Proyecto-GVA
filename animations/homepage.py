# Imports
from manim import *;
from misc.misc import *;
import numpy as np;

class MainScene(Scene):
    def construct(self):
        # > - Crear grid del plano - <
        planeGrid = NumberPlane(
            background_line_style = {
                "stroke_color": getColor("#D2A6FF"),
            },
            axis_config = {
                "color": TEAL_C,
            }
        )

        self.add(planeGrid)
        self.play(
            Create(planeGrid, run_time=3, lag_ratio=0.1)
        )

        self.wait(2)

        self.play(
            FadeOut(planeGrid)
        )
       
        # > - Resaltar rectas - <
        rectas = [
            ImplicitFunction(lambda x, y: y - ((1/2) * x + b), color = PURPLE_A).set_stroke(opacity = 0.7, width=2) 
            for b in range(-3, 4)
        ]

        for recta in rectas:
            self.play(
                delinear(recta, getColor("#D2A6FF"))
            )
            self.wait(0.2)

        # > - Animacion onda vectores - <
        self.clear()
        self.vectorSpace()

    def vectorSpace(self):
        initFunc = lambda pos: np.sin(pos[1]) * RIGHT + np.cos(pos[0]) * UP
        funcs = [
            VectorField.scale_func(initFunc, 0.5),
            VectorField.scale_func(initFunc, 0.2),
            VectorField.scale_func(initFunc, 0.1),
            VectorField.scale_func(initFunc, 0.2),
            VectorField.scale_func(initFunc, 0.5),
        ]

        vector_field = ArrowVectorField(initFunc)
        vector_field.set_color(
            getColor("#D2A6FF")
        )
        self.add(vector_field)
        self.wait()

        for func in funcs:
            self.play(vector_field.animate.become(ArrowVectorField(func)))
            self.wait()
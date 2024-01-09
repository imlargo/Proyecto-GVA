# Imports
from manim import *;
from misc.misc import *;
import numpy as np;

class MainScene(Scene):
    def construct(self):
        # > - Crear grid del plano - <
        planeGrid = NumberPlane(
            background_line_style = {
                "stroke_color": getColor("#e1c6fd"),
            },
            axis_config = {
                "color": getColor("#a546e5"),
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

        ]
        # > - Animacion onda vectores - <


    def vectorSpace():
        initFunc = lambda pos: np.sin(pos[1]) * RIGHT + np.cos(pos[0]) * UP
        funcs = [
            VectorField.scale_func(initFunc, 0.5),
            VectorField.scale_func(initFunc, 0.2)
        ]

        vector_field = ArrowVectorField(initFunc)
        self.add(vector_field)
        self.wait()

        for func in funcs:
            self.play(vector_field.animate.become(ArrowVectorField(func)))
            self.wait()
# Imports
from manim import *;
from misc.misc import *;
import numpy as np;

class MainScene(Scene):
    def construct(self):
        # > - Crear grid del plano - <
        planeGrid = NumberPlane(
            background_line_style = {
                "stroke_color": RED_C,
            },
            axis_config = {
                "color": BLUE,
            }
        )

        self.add(planeGrid)
        self.play(
            Create(planeGrid, run_time=3, lag_ratio=0.1),
        )
        self.wait(2)

        # > - Resaltar rectas - <

        rectas = [

        ]


        # > - Animacion onda vectores - <
# Imports
from manim import *;
from misc.misc import *;
import numpy as np;

class MainScene(Scene):
    def construct(self):
        self.camera.background_color = getColor("#16265C")
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
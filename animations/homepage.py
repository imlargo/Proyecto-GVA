# Imports
from manim import *;
from misc.misc import *;
import numpy as np;

class MainScene(Scene):
    def construct(self):
        self.vectorField()
        pass

    def plane(self):
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

        """for recta in rectas:
            self.play(
                delinear(recta, getColor("#D2A6FF"))
            )
            self.wait(0.2)"""

        # > - Animacion onda vectores - <
        self.clear()
        self.vectorSpace()

    def vectorSpace(self):
        funcs = [
            lambda pos: np.array([pos[1], pos[0], 0 ]), # X
            lambda pos: np.array([np.sin(pos[0] / 2) - np.cos(pos[1] / 2), np.sin(pos[0] / 2), 0 ]), # Flow home
            lambda pos: np.array([1, np.sin(pos[0]*pos[0] + pos[1]*pos[1]), 0 ]), # Waves circle
            lambda pos: np.array([pos[1] - np.cos((pos[0]*pos[0] + pos[1]*pos[1]) ** 0.5), np.cos((pos[0]*pos[0] + pos[1]*pos[1]) ** 0.5), 0 ]),
        ]
        initFunc = funcs[-1]

        getColor = lambda string: ManimColor.from_hex(string)
        colors = [
            RED_A, TEAL_C, getColor("#AF62FF"), getColor("#D2A6FF") 
        ]

        stream_lines = StreamLines(initFunc, stroke_width=2, max_anchors_per_line=30, colors = colors)
        vector_field = ArrowVectorField(initFunc, colors = colors)

        self.add(stream_lines)
        self.add(vector_field)

        stream_lines.start_animation(warm_up=True, flow_speed=1.5)
        self.wait(3)

        getColor = lambda string: ManimColor.from_hex(string)
        v = ValueTracker(0)
        a = always_redraw(lambda: ArrowVectorField(
            lambda pos: np.array([pos[1] * np.sin(v.get_value()), pos[0] * np.sin(v.get_value()), 0 ]),
            colors = [
                TEAL_C, RED_A, getColor("#D2A6FF"), getColor("A146FF")
            ]
        ))
        self.play(Create(a))
        self.play(v.animate.set_value(3), run_time = 3)

    def vectorField(self):
        getColor = lambda string: ManimColor.from_hex(string)
        colors = [
            TEAL_C, RED_A, getColor("#BB52FF"), getColor("#B369FF"), getColor("#C184FF"), getColor("#D2A6FF")
        ]
        v = ValueTracker(0)

        streamFunc = lambda pos: np.array([np.sin(pos[0] / 2) - np.cos(pos[1] / 2), np.sin(pos[0] / 2), 0 ])

        stream_lines = StreamLines(streamFunc, stroke_width=2, max_anchors_per_line=30, colors = colors)
        vector_field = always_redraw(
            lambda: ArrowVectorField(
                lambda pos: (0.5 * ((np.cos(2 * v.get_value())) + 1)) * np.array([np.sin(pos[0] / 2) - np.cos(pos[1] / 2), np.sin(pos[0] / 2), 0 ]),
                colors = colors
            )
        )

        self.add(stream_lines)
        self.play(Create(vector_field))

        stream_lines.start_animation(warm_up=True, flow_speed=1.5)
        self.play(v.animate.set_value(3 * PI), run_time = 12)


    def streamlines(self):
        getColor = lambda string: ManimColor.from_hex(string)
        colors = [
            TEAL_C, RED_A, getColor("#BB52FF"), getColor("#B369FF"), getColor("#C184FF"), getColor("#D2A6FF")
        ]

        streamFunc = lambda pos: np.array([pos[1] - np.cos((pos[0]*pos[0] + pos[1]*pos[1]) ** 0.5), np.cos((pos[0]*pos[0] + pos[1]*pos[1]) ** 0.5), 0 ])
        stream_lines = StreamLines(streamFunc, stroke_width=2, max_anchors_per_line=30, colors = colors)

        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(3)
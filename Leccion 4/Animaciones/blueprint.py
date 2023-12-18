# Imports
from manim import *;
import numpy as np;

# Escena simple
class baseScene(Scene):
    def construct(self):
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
        pass
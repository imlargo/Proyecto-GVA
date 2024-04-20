# Imports
from manim import *;
from misc.misc import *;
import numpy as np;

# Escena simple
class BaseScene(Scene):
    def construct(self):
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
        self.clear()
        pass
    
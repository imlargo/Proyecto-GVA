from manim import *

class PlaneScene(LinearTransformationScene):
    def __init__(self):

        LinearTransformationScene.__init__(self,
            include_background_plane = True,
            include_foreground_plane = True,
            background_plane_kwargs = {
                    "x_range" : [-10, 10, 1],
                    "y_range": [-10, 10, 1],
                    "x_length": 10,
                    "y_length": 8,
                },
            foreground_plane_kwargs = None,
            show_coordinates = True,
            show_basis_vectors = True,
            leave_ghost_vectors = True
            )
        
    def construct(self):
        matrix = [[1, 1], [0, 1]]
        self.apply_matrix(matrix)
        self.wait()
        
        

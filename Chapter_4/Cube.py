from Mesh3D import *
class Cube(Mesh3D):
    def __init__(self):
        self.vertices =[(0.5, -0.5, 0.5),
                         (-0.5, -0.5, 0.5),
                         (0.5, 0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (0.5, 0.5, -0.5),
                         (-0.5, 0.5, -0.5)]
        self.triangles = [0, 2, 3, 0, 3, 1, 1, 2, 3]
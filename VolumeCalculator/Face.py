import numpy as np 
import math

class Face:
    def __init__(self, vertices):
        def NormalFinder(vertices):
             edge1 = np.subtract(vertices[0], vertices[2])
             edge2 = np.subtract(vertices[1], vertices[0])
             return np.cross(edge1, edge2)
          
        self.Vertices = vertices
        initialNormal = NormalFinder(vertices)
        crossMagn = math.sqrt(sum(initialNormal[i]*initialNormal[i] for i in range(3)))
        
        self.Normal = np.divide(initialNormal, crossMagn)
        self.Area = crossMagn/2.0
import numpy as np 
import math

class Face:

    """ Constructor of the Face class"""
    def __init__(self, vertices):

        """ NormalFinder function finds the normal vector
        of the given polygonal face (the result is not normalizd)  
        """
        def NormalFinder(vertices):
             edge1 = np.subtract(vertices[0], vertices[2])
             edge2 = np.subtract(vertices[1], vertices[0])
             return np.cross(edge1, edge2)
          
        self.Vertices = vertices
        initialNormal = NormalFinder(vertices)

        # this line calculates the magnitude of the cross product
        crossMagn = math.sqrt(sum(initialNormal[i]*initialNormal[i] for i in range(3)))
        
        # Normalize the obtained normal vector:
        self.Normal = np.divide(initialNormal, crossMagn)
        
        # the area of a triangle is the magnitude of the crosss product of two of its edges
        self.Area = crossMagn/2.0 
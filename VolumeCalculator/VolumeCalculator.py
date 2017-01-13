import sys
import numpy as np 
import unittest
from Face import Face

""" CalculateVolume function takes the faces of a tessellated model
and calculates its volume
"""
def CalculateVolume(faces):
    volume = 0
    for face in faces:
        # for every face, the volume of the tetrahedrun is calculated
        # the tetrahedron is made with 4 vertices: 3 vertices of the face and the origin
        tetrahedronVolume = face.Area * (sum(face.Normal[:]*face.Vertices[0][:])) /3.0
        
        # depending on the direction of the normal vector, the volume of the tertrahedron  
        # can be either negative or positive
        volume += tetrahedronVolume
    return volume

def main():
    # meshes dictionary contains the name of the meshes (keys) and the imported arrays(value)
    meshes = {'unit_cube_qppp': np.load('../Meshes/unit_cube_qppp.npy'),
              'shell': np.load('../Meshes/shell.npy'),
              'Robot_Maker_Faire_65pc': np.load('../Meshes/Robot_Maker_Faire_65pc.npy')}
    
    # PreCalculatedValues dictionary contains the name of the meshes (keys) and the precalculated 
    # values of their volume (value)
    preCalculatedValues = {'unit_cube_qppp': 1.0,
                          'shell': 3.6586764273,
                          'Robot_Maker_Faire_65pc': 43677.4258266209}

    for importedArray in meshes.keys(): 
        faces = list()
        for face in meshes[importedArray]:
            faces.append(Face(face))
        volume = CalculateVolume(faces)
        test = round(volume, 10) - preCalculatedValues[importedArray] == 0.0
        toPrint = ''
        if (test):
            toPrint = 'successful'
        else:
            toPrint = 'unsuccessful'
        print "Unit test on " + importedArray, ': ', toPrint
    input()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
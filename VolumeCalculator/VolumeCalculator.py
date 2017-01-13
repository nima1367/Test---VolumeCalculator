import sys
import numpy as np 
from Face import Face

def CalculateVolume(faces):
    volume = 0
    for face in faces:
        tetrahedronVolume = face.Area * (sum(face.Normal[:]*face.Vertices[0][:])) /3.0
        volume += tetrahedronVolume
    return volume

def main():
    mesh = np.load('../Meshes/unit_cube_qppp.npy')
    faces = list()
    for face in mesh:
        faces.append(Face(face))
    volume = CalculateVolume(faces)
    input()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
import sys
import numpy as np 
from Face import Face

def CalculateVolume(faces):
    volume = 0
    for face in faces:
        tetrahedronVolume = face.Area * (sum(face.Normal[:]*face.Vertices[0][:])) /3.0
        volume += tetrahedronVolume
    return volume
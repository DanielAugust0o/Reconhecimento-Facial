import cv2
import os
import numpy as np

eigenface = cv2.face.EigenFaceRecognizer(40, 800)

def getImagemComId() :
    caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]
    #print(caminhos)
    faces = []

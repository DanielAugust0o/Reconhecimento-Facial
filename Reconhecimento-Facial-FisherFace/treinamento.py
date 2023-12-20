import cv2
import os
import numpy as np

eigenface = cv2.face.EigenFaceRecognizer(40, 800)
fisherface = cv2.face.FisherFaceRecognizer()
lbph = cv2.face.LBPHFaceRecognizer()

def getImagemComId() :
    caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]
    #print(caminhos)
    faces = []

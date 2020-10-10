import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

### VARIABLES ###

#True mientras se presiona el mouse, falso mientras el mouse esta libre
dibuja = False
ix,iy = -1,-1


#FUNCIONES
def dibujar_rectangulo(evento,x,y,flags,params):
    global ix, iy, dibuja

    if evento == cv2.EVENT_LBUTTONDOWN:
        dibuja=True
        ix,iy=x,y
    elif evento == cv2.EVENT_MOUSEMOVE:
        if dibuja == True:
            cv2.rectangle(image,(ix,iy),(x,y),(0,255,0),-1)
    elif evento == cv2.EVENT_LBUTTONUP:
        dibuja = False
        cv2.rectangle(image,(ix,iy),(x,y),(0,255,0),-1)

#MOSTRAR LA IMAGEN
image = np.zeros((512,512,3))

cv2.namedWindow(winname='imagen')

cv2.setMouseCallback('imagen',dibujar_rectangulo)

while True:
    cv2.imshow('mydrawing',image)
    #Espera ser cerrada por la tecla Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
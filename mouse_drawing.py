import cv2
import numpy as np

#############
## FUNCION ##
#############
def dibuja_circulo(evento,x,y,flags,param):
    
    if evento == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),2)
    elif evento == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),-1)


cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing',dibuja_circulo)
############################
###MUESTRA IMAGEN CON OPENCV###
############################

img = np.zeros((512,512,3))

while True:
    cv2.imshow('my_drawing',img)
    
    if cv2.waitKey(20) & 0xFF==27:
        break
cv2.destroyAllWindows()

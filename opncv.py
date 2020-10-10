import cv2
import numpy as np
import matplotlib.pyplot as plt
#abriendo una imagen con openCV y saliendo presionando teclas
img = cv2.imread('7a.jpeg')

while True:
    cv2.imshow('pup',img)
    #Que significa la linea de abajo??
    #Es una constante hexadecimal que es 11111111
    #SI ESPERAMOS AL MENOS 1ms Y hemos presionado la tecla Esc (Valor para la tecla Esc)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()


#Dibujando imagen en negro
blank_img = np.zeros(shape=(512,512,3),dtype=np.int16)

plt.imshow(blank_img)
#plt.show()

#Dibujando rectangulo en la imagen anterior
cv2.rectangle(blank_img,pt1=(384,200),pt2=(500,150),color=(255,255,0),thickness=10) #marcador permanente en la imagen

plt.imshow(blank_img)
plt.show()
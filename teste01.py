import cv2 
from matplotlib import pyplot as plt

#Carregando a imagem em escala de cinza

img = cv2.imread('simples.jpg', cv2.IMREAD_GRAYSCALE) # poderia ser também 0(ZERO) no segundo paramentro

# Fazendo a limiriarização:  5 formas

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


titles = ['Original image', 'BINARY','BINARY_INV','TRUNC','TOZERO', 'TOZERO_INV']

images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# USANDO UM FOR PARA ATRIBUIR UM TITULO PARA CADA IMAGEM
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()


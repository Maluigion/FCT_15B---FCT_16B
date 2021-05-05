#-------------------------------------------------------------------------------
# Name:        Traitement du son
# But :        FCT 16B 
# Author:      Philippe - Amine
#
# Created:     21/04/2021
# Copyright:   (c) Philippe&Amine 2021
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#inspiré de : https://www.youtube.com/watch?v=iXNsAYOTzgM
#inspiré de : https://dev.to/simarpreetsingh019/detecting-geometrical-shapes-in-an-image-using-opencv-4g72

import numpy as np
import cv2
from PIL import Image

img = cv2.imread('HeartVe.jpg')
imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret , thrash = cv2.threshold(imgGry, 50 , 255, 1)
contours , hierarchy = cv2.findContours(thrash, 1, 2)

contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
cv2.drawContours(img, [biggest_contour], 0, (120,120,0), 10)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5

if len(approx) == 3:
    print('Triangle')
elif len(approx) == 4 :
    x, y , w, h = cv2.boundingRect(approx)
    aspectRatio = float(w)/h
    if aspectRatio >= 0.95 and aspectRatio < 1.05:
        #cv2.drawContours(img, [contour], 0, (120,120,0), 10)
        print('Carré')
    else:
        #cv2.drawContours(img, [contour], 0, (120,120,0), 10)
        print('Rectangle')
elif len(approx) == 5 :
    #cv2.drawContours(img, [contour], 0, (120,120,0), 10)
    print('Pentagone')
elif len(approx) == 10 :
    #cv2.drawContours(img, [contour], 0, (120,120,0), 10)
    print('Etoile')
elif len(approx) == 12 :
    #cv2.drawContours(img, [contour], 0, (120,120,0), 10)
    print('Croix')
elif len(approx) > 12 and len(approx) < 50:
    #cv2.drawContours(img, [contour], 0, (120,120,0), 10)
    print('Cercle')
elif len(approx) > 50 and len(approx) < 2000:
    #cv2.drawContours(img, [contour], 0, (120,120,0), 50)
    print('Coeur')
else :
    print('Pas de forme détecté')

# It converts the BGR color space of image to HSV color space
#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            
# Threshold of blue in HSV space
#lower_blue = np.array([0,0,255]) #plus foncé
#upper_blue = np.array([99, 95, 200]) #plus clair
        
# preparing the mask to overlay
#mask = cv2.inRange(hsv, lower_blue, upper_blue)
            
# The black region in the mask has the value of 0,
# so when multiplied with original image removes all non-blue regions
#result = cv2.bitwise_and(img, img, mask = mask)

#Couleur du fond
im = Image.open('HeartVe.jpg')
w, h = im.size
crop_im = im.crop((200, 40, w-170, h-100)) #crop image 
res = crop_im.getcolors(crop_im.size[0]*crop_im.size[1]) 

def couleur(res):

    max = 0
    maxi = 0

    for i in range(1,len(res)):
        if res[i][0] > max:
            max = res[i][0]
            maxi = i

    col = res[maxi][1]

    r = col[0]
    g = col[1]
    b = col[2]

    if r in range(g-10,g+10) and r in range (b-10,b+10):
        del res[maxi]
        return couleur(res)

    return(col)

col = couleur(res)
print(col)

R = col[0]
G = col[1]
B = col[2]

if (200<R<250 and G>160 and B<100):
    print('Jaune')
elif (R>150 and G<100 and B<100):
    print('Rouge')
elif (R<120 and G>150 and B<150):
    print('Vert')
elif (R<100 and G>100 and B>200):
    print('Bleu')
elif (R>100 and G<100 and B>100):
    print('Magenta')
elif (R>200 and G>100 and B<100):
    print('Orange')
elif (150< R <200 and G<100 and B>150):
    print('Violet')
else:
    print('Mauvais encadrement')

cv2.imshow("labiz",img)
crop_im.show()

cv2.waitKey(0) 
cv2.waitKey(0)
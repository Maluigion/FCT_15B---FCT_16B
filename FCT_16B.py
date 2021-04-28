#-------------------------------------------------------------------------------
# Name:        Traitement du son
# But :        FCT 16B 
# Author:      Philippe - Amine - Coline
#
# Created:     21/04/2021
# Copyright:   (c) Philippe&Amine 2021
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#inspiré de : https://dev.to/simarpreetsingh019/detecting-geometrical-shapes-in-an-image-using-opencv-4g72

import numpy as np
import cv2
from PIL import Image

img = cv2.imread('carreO.jpg')
imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

crop_img = img[500:1000, 200:1800]

color = ([0, 0, 0])
thickness = 2

#ret , thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
#contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

contours , hierarchy = cv2.findContours(imgGry,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5, None, 0, 0)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5

    if len(approx) == 3:
        cv2.putText( img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, color, thickness, 1, None)
    elif len(approx) == 4 :
        x, y , w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        #print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio < 1.05:
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, color, thickness, 1, None)
            print('Carré')
        else:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, color, thickness, 1, None)
            print('Rectangle')

    elif len(approx) == 5 :
        cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        print('Pentagone')
    elif len(approx) == 10 :
        cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, color, thickness, 1, None)
        print('Etoile')
    elif len(approx) == 12 :
        cv2.putText(img, "cross", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, color, thickness, 1, None)
        print('Croix')
    elif len(approx) > 12:
        cv2.putText(img, "heart", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, color, thickness, 1, None)    
        print('Coeur')
    else :
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, color, thickness, 1, None)
        print('Cercle')


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
im = Image.open("carreO.jpg")
res = im.getcolors(im.size[0]*im.size[1]) 

max = res[0][0]
maxi = 0
i=0
for i in range(1,len(res)):
    if res[i][0] > max:
        max = res[i][0]
        maxi = i

col = res[maxi][1]
print(col)
R = col[0]
G = col[1]
B = col[2]

if (R>100 and G>100 and B<100):
    print('Jaune')
elif (R>150 and G<100 and B<100):
    print('Rouge')
elif (R<100 and G>150 and B<100):
    print('Vert')
elif (R<100 and G<100 and B>200):
    print('Bleu')
elif (R>100 and G<100 and B>100):
    print('Magenta')
elif (R>150 and G>100 and B<100):
    print('Orange')
else:
    print('Violet')


cv2.imshow('img', crop_img)

#cv2.namedWindow("output", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions                       # Read image
#imS = cv2.resize(img, (1000,500))                    # Resize image
#cv2.imshow("yaaay", imS)                            # Show image
#cv2.waitKey(0) 

#cv2.imshow('mask', mask)
#cv2.imshow('result', result)
cv2.waitKey(0)


#cv2.destroyAllWindows()

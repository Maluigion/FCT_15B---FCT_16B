#-------------------------------------------------------------------------------
# Name:        Traitement du son
# But :        FCT 15B 
# Author:      Philippe - Amine
#
# Created:     21/04/2021
# Copyright:   (c) Philippe&Amine 2021
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#Inspiré de :
#https://www.f-legrand.fr/scidoc/docimg/numerique/tfd/spectreson3/spectreson3.html

#import math
#import numpy as np
#from matplotlib.pyplot import *
import scipy.io.wavfile as wave
#from numpy.fft import fft
#import Tkinter

rate,data = wave.read('testchut.wav')   #Récupération du fichier audio
n = data.size     #Récupération du nombre d'échantillons
duree = 1.0*n/rate   #Calcul de la durée du signal audio


#print(rate)
#print(n)    
#print(duree)
#print(data)

#UTILISE POUR CALCULER LE VECTEUR TEMPS
#te = 1.0/rate
#t = np.zeros(n)
#for k in range(n):
#    t[k] = te*k


#AFFICHAGE DU SIGNAL
#figure(figsize=(12,4))
#plot(t,data)
#xlabel("t (s)")
#ylabel("amplitude")
#axis([0,10,data.min(),data.max()])
#grid()

s=[]    #silence
b=[]    #son

if data[0]>1000:
    isAsound=True
else:
    isAsound=False       #True si son, False si silence

cpt = 0

for i in range(len(data)):
    if isAsound==True:
        if data[i]==0 and data[i+1]==0:
            isAsound=False
            b.append(1.0*cpt/rate)
            cpt = 1
        else:
            cpt += 1
    else:
        if abs(data[i]) > 3000:
            isAsound = True
            s.append(1.0*cpt/rate)
            cpt = 1
        else:
            cpt +=1

if isAsound == True:
    b.append(1.0*cpt/rate)
else:
    s.append(1.0*cpt/rate)

print("silence:")
print(s)
print("son:")
print(b)

## TODO 
## que faire des infos ?
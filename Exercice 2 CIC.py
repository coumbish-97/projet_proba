import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
from scipy.stats import norm
from math import *

### Exercice 2

#Histogramme contient les 5000 réalisations des expériences
Histogramme = []
n = 10000
for i in range(5000):


   #Le vecteur Y contient les yi (Y[i]). 
    Y = chi2.rvs(2, size = n)
        
    #Y_barre représente y_n_barre, la moyenne
    Y_barre = sum(Y)/n

    #Z_barre représente z_n_barre, la variable aléatoire transformée
    Z_barre = sqrt(n)*(Y_barre-2)/2

    Histogramme.append(Z_barre)

#on trace l'histogramme correspondant aux valeurs de Z_barre
plt.hist(Histogramme)
#on trace l'histogramme correspondant à une distribution normale
N = norm.rvs(size = n)
#plt.hist(N)

plt.show()



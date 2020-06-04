import numpy as np
import matplotlib.pyplot as plt

### Exercice 1 

#L'expérience est effectuée pour 4 valeurs différentes de n
for n in [10,100,1000,1000]:
    #Histogramme contient les 5000 réalisations des expériences
    Histogramme = []

    for i in range(5000):

        #Le vecteur Y contient les yi (Y[i]). 
        Y = np.random.rand(n)*10
        
        #Y_barre représente y_n_barre
        Y_barre = sum(Y)/n
        Histogramme.append(Y_barre)

    #on trace l'histogramme correspondant aux valeurs de la moyenne
    plt.hist(Histogramme)

plt.show()




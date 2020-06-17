

import string
import urllib.request
import matplotlib.pyplot as plt

x = urllib.request.urlopen('https://r-stat-sc-donnees.github.io/LesMiserables1.txt')

livre=str(x.read().decode("utf-8-sig"))



livre = livre.lower()




livre = livre.replace('\r', ' ').replace('\n', ' ')



mots = livre.split()



N_un = []
P_un = []
w_un = 0
T = 0
for mot in (mots):
    if mot == 'un':
        w_un+=1
    T+=1
    N_un.append(w_un)
    P_un.append(w_un/T)
        


plt.plot(P_un)




N_et = []
P_et = []
w_et = 0
T = 0
for mot in (mots):
    if mot == 'et':
        w_et+=1
    T+=1
    N_et.append(w_et)
    P_et.append(w_et/T)
        



plt.plot(P_et)



N_le = []
P_le = []
w_le = 0
T = 0
for mot in (mots):
    if mot == 'le':
        w_le+=1
    T+=1
    N_le.append(w_le)
    P_le.append(w_le/T)
        



plt.plot(P_le)



N_il = []
P_il = []
w_il = 0
T = 0
for mot in (mots):
    if mot == 'il':
        w_il+=1
    T+=1
    N_il.append(w_il)
    P_il.append(w_il/T)
        


plt.plot(P_il)



N_est = []
P_est = []
w_est = 0
T = 0
for mot in (mots):
    if mot == 'est':
        w_est+=1
    T+=1
    N_est.append(w_est)
    P_est.append(w_est/T)

plt.plot(P_est)


plt.show()


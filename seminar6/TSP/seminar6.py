# script pentru testul selectiei parintilor - selectia de tip SUS cu distributie fps cu sigma-scalare
import numpy as np

import generare_init as gi
import matplotlib.pyplot as grafic
#pentru legenda - ajustare
import matplotlib.patches as mpatches


#doar pt fct fitness pozitive
def fps(calitati):
    p = calitati.copy()/sum(calitati)
    q=p.copy()
    #p = [calitati[i]/sum(calitati) for i in range(len(calitati))]
    #p = np.array(p)
    for i in range(1,len(calitati)):
        q[i]=q[i]+q[i-1]
    return q

def fps_sigma(calitati):
    medie = np.mean(calitati)
    varianta = np.std(calitati)
    v= medie - 2*varianta
    g=[calitati[i] - v for i in range(n)]
    if sum(g)>0:
        q=fps(g)
    else:
        q=fps(calitati)
    return q

def SUS(populatie, calitati,dim,n,probabilitate):
    parinti = populatie.copy()
    calitati_p = calitati.copy()
    q = probabilitate(calitati)
    raspuns = np.random.uniform(0,1/dim)
    i,k = 0,0
    while i<dim:
        while raspuns<q[k]:
            parinti[i] = populatie[k].copy()
            calitati_p[i] = calitati[k]
            raspuns+=1/dim
            i+=1
        k+=1  #trecem la urmatorul individ
    return parinti, calitati_p

def ruleta(populatie, calitati, dim , n, probabilitate):
    parinti = populatie.copy()
    calitati_p = calitati.copy()
    q = probabilitate(calitati)  #sau fps_sigma pt calitati mai bune, nu mai e distributie uniforma
    for i in range(dim):
        raspuns = np.random.uniform(0,1) #invart ruleta
        k=0
        while q[k]<raspuns:
            k+=1
        parinti[i] = populatie[k].copy()
        calitati_p[i] = calitati[k]
    return parinti, calitati_p

def turneu(populatie, calitati, dim , n):
    parinti = np.zeros([dim,n], "int")
    calitati_p = np.zeros(dim)
    for i in range(dim):
        pozitii = np.random.randint(0,dim,2) #generam 2 pozitii aleatoare de la 0 la dim pop
        if calitati[pozitii[0]]>calitati[pozitii[1]]:
            parinti[i] = populatie[pozitii[0]].copy()
            calitati_p[i] = calitati[pozitii[0]]
        else:
            parinti[i] = populatie[pozitii[1]].copy()
            calitati_p[i] = calitati[pozitii[1]]
    return parinti, calitati_p

#generarea aleatoare a unei populatii
dim=20
p,v,n=gi.gen("costuri.txt",dim)
# calculul parintilor si calitatii acestora utilizand selectia SUS cu FPS cu sigma-scalare


#parinti,valori=ruleta(p,v,dim,n, fps)
#parinti,valori=SUS(p,v,dim,n,fps_sigma)
parinti,valori=turneu(p,v,dim,n)


x=range(dim)
grafic.plot(x,v,"go",markersize=16)
grafic.plot(x,valori,"ro",markersize=10)
red_patch = mpatches.Patch(color='red', label='Calitatile parintilor')
green_patch = mpatches.Patch(color='green', label='Calitatile populatiei curente')
grafic.legend(handles=[red_patch,green_patch])
grafic.show()
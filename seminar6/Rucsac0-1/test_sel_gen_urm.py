# script pentru testul selectiei generatiei urmatoare - selectia de tip elitist
import numpy as np
from FunctiiSelectii import elitism
import generare_init as gi
import matplotlib.pyplot as grafic
#pentru legenda
import matplotlib.patches as mpatches

#generarea aleatoare a doua populatii
dim=12
cmax=30
pop1,cal1,n=gi.gen("cost.txt","valoare.txt",cmax,dim)
pop2,cal2,n=gi.gen("cost.txt","valoare.txt",cmax,dim)
genu,valori=elitism(pop1,cal1,pop2,cal2,dim)
#constituirea populatiei cu dim liste fiecare cu n+1 valori

x=[i for i in range(dim)]
grafic.plot(x,cal1,"go",markersize=18,label="Populatia curenta")
grafic.plot(x,cal2,"bo",markersize=14,label="Populatia de copii mutati")
grafic.plot(x,valori,"ro",markersize=11,label="Geneartia urmatoare")

grafic.legend(loc="lower left")
grafic.show()


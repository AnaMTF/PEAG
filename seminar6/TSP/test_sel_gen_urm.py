# script pentru testul selectiei generatiei urmatoare - selectia de tip elitist
import numpy as np
from FunctiiSelectii import elitism
import generare_init as gi
import matplotlib.pyplot as grafic


#generarea aleatoare a doua populatii
dim=12
p1,v1,n=gi.gen("costuri.txt",dim)
p2,v2,n=gi.gen("costuri.txt",dim)
genu,valori=elitism(p1,v1,p2,v2,dim)
print('populatia1 cu valori')
print(v1)
print('populatia2 cu valori')
print(v2)
print('selectat:')
print(valori)
x=[i for i in range(dim)]
grafic.plot(x,v1,"go",markersize=18,label='Populatia curenta')
grafic.plot(x,v2,"bo",markersize=14,label='Populatia de copii')
grafic.plot(x,valori,"ro",markersize=10,label='Generatia urmatoare')
grafic.legend(loc="lower right")
grafic.show()


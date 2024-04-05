# script pentru testul selectiei parintilor - selectia de tip turneu
import numpy as np
from FunctiiSelectii import turneu
import generare_init as gi
import matplotlib.pyplot as grafic
#pentru legenda - afisare ajustata
#generarea aleatoare a unei populatii
dim=10
cmax=30
k=2
pop,cal,n=gi.gen("cost.txt","valoare.txt",cmax,dim)
parinti,valori=turneu(pop,cal,dim,n,k)

x=[i for i in range(dim)]
grafic.plot(x,cal,"go",markersize=16,label="Populatia curenta")
grafic.plot(x,valori,"ro",markersize=10,label="Populatia de parinti")
grafic.legend(loc="lower left")
grafic.show()


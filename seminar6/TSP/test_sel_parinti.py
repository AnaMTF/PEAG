# script pentru testul selectiei parintilor - selectia de tip SUS cu distributie fps cu sigma-scalare
import numpy as np
from FunctiiSelectii import *

import generare_init as gi
import matplotlib.pyplot as grafic
#pentru legenda - ajustare
import matplotlib.patches as mpatches


#generarea aleatoare a unei populatii
dim=12
p,v,n=gi.gen("costuri.txt",dim)
# calculul parintilor si calitatii acestora utilizand selectia SUS cu FPS cu sigma-scalare
parinti,valori=SUS(p,v,dim,n)


x=range(dim)
grafic.plot(x,v,"go",markersize=16)
grafic.plot(x,valori,"ro",markersize=10)
red_patch = mpatches.Patch(color='red', label='Calitatile parintilor')
green_patch = mpatches.Patch(color='green', label='Calitatile populatiei curente')
grafic.legend(handles=[red_patch,green_patch])
grafic.show()
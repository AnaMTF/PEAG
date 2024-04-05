import numpy as np
from FunctiiMutatieIndivizi import m_perm_inversiune
import matplotlib.pyplot as grafic

#f. obiectiv
def foTSP(p,c):
    n=p.size
    val=0
    for i in range(n-1):
        val+=c[p[i],p[i+1]]
    val+=c[p[0],p[n-1]]
    return 100/val


#genereaza populatia initiala
#I:
# fc - numele fisierului costurilor
# dim - numarul de indivizi din populatie
#E: pop,val - populatia initiala si vectorul valorilor
#  pentru testul mutatiei si matricea c
def gen(fc,dim):
    #citeste datele din fisierul nxn al costurilor
    c=np.genfromtxt(fc)
    #n=dimensiunea problemei
    n = c.shape[0]
    #defineste o variabila ndarray dimx(n+1) cu toate elementele 0
    pop=np.zeros([dim,n],dtype="int")
    val=np.zeros(dim,dtype="float")
    for i in range(dim):
        #genereaza candidatul permutare cu n elemente
        pop[i] = np.random.permutation(n)
        # evalueaza candidat
        val[i] = foTSP(pop[i],c)
    ind=[i for i in range(dim)]
    grafic.plot(ind,val,"gs",markersize=12)
    return pop, val,c



#MUTATIE
 # operatia de mutatie a descendentilor obtinuti din recombinare

    # I: po,vo - populatia copiilor si vectorul calitatilor
    #   dim,n - dimensiunile
    #    pm - probabilitatea de mutatie
    #    c - matricea costurilor
    # E: descm - [mpo,mvo] - indivizii obtinuti
def mutatie_populatie(pcopii,vcopii,c,pm):
    mpo=pcopii.copy()
    mvo=vcopii.copy()
    dim=mpo.shape[0]
    n=mpo.shape[1]
    for i in range(dim):
        r=np.random.uniform(0,1)
        if r<=pm:
            x=mpo[i]
            y=m_perm_inversiune(x,n)
            mpo[i]=y
            mvo[i]=foTSP(y,c)
    ind = [i for i in range(dim)]
    grafic.plot(ind, mvo, "rs", markersize=9)
    return mpo,mvo

if __name__=="__main__":
    p,v,c=gen("costuri.txt",20)
    o,vo=mutatie_populatie(p,v,c,0.2)
    grafic.show()
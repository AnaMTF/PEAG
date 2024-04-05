import numpy as np

#f. obiectiv
def foTSP(p,c,n):
    val = 0
    for i in range(n - 1):
        val = val + c[p[i]][p[i+1]]
    val = val+c[p[0]][p[n-1]]
    return 1/val


#genereaza populatia initiala
#I:
# fc - numele fisierului costurilor
# dim - numarul de indivizi din populatie
#E: populatia initiala si vectorul valorilor
def gen(fc,dim):
    #citeste datele din fisierul nxn al costurilor
    c=np.genfromtxt(fc)
    #n=dimensiunea problemei
    n = len(c)
    #defineste o variabila ndarray dimx(n+1) cu toate elementele 0
    pop=np.zeros((dim,n),dtype=int)
    val=np.zeros(dim,dtype=float)
    for i in range(dim):
        #genereaza candidatul permutare cu n elemente
        pop[i] = np.random.permutation(n)
        # evalueaza candidat
        val[i] = foTSP(pop[i,:n],c,n)
    return pop, val,n




import numpy as np
import matplotlib.pyplot as grafic


#verifica fezabilitatea alegerii x si calculeaza si f. obiectiv
def ok(x,c,v,max):
    val=np.dot(x,v)
    cost=np.dot(x,c)
    return cost<=max, val


#genereaza populatia initiala
#I:
# fc, fv - numele fisierelor cost, valoare
# max - capacitatea maxima
# dim - numarul de indivizi din populatie
# E:
# c,v - parametri de iesire necesari in rezolvarea problemei
#pop - populatia insotita de calitati

def gen(fc,fv,max,dim):
    #citeste datele din fisierele cost si valoare
    c=np.genfromtxt(fc)
    v=np.genfromtxt(fv)
    #n=dimensiunea problemei
    n=len(c)
    #lucreaza cu populatia ca lista de dim elemente - liste cu cate n+1 indivizi
    pop=[]
    #adun valorile indivizilor creati pentru reprerzentarea grafica
    vectv=[]
    for i in range(dim):
        gata=False
        while gata == False:
            #genereaza candidatul x cu elemente pe [0,1]
            x=np.random.uniform(0,1,n)
            gata,val=ok(x,c,v,max)
        #am gasit o solutie candidat fezabila, in data de tip ndarray (vector) x
        # x este transformat in lista
        x=list(x)
        # adauga valoarea
        x=x+[val]
        vectv=vectv+[val]
        #adauga la populatie noul individ cu valoarea f. obiectiv - adauga inca o lista cu n+1 elemente ca element al listei pop
        pop=pop+[x]
    ind=[i for i in range(dim)]
    grafic.plot(ind,vectv,"gs",markersize=12)
    return pop, c, v

def mutatie_neuniforma(x,sigma,a,b):
    p = np.random.normal(0, sigma)
    y = x + p
    if y > b:
        y = b
    elif y < a:
        y = a
    return y


#mutatie asupra populatiei de copii
# I:pop - populatia de dimensiuni dimx(n+1)
#   pm - probabilitatea de mutatie
#   c,v,max - datele problemeu
#   sigma - pasul de mutatie
#E: - mpop - populatia mutata

def mutatie_populatie(pop,c,v,max,pm,sigma):
    # copiem populatia curenta in rezultatul mpop
    mpop=pop.copy()
    dim=len(pop)
    n=c.size
    #adun valorile indivizilor mutati pentru reprerzentarea grafica
    valv=[]
    for i in range(dim):
        #copiem in x individul i
        x=pop[i][:n].copy()
        for j in range(n):
            #genereaza aleator daca se face mutatie in individul i gena j
            r=np.random.uniform(0,1)
            if r<=pm:
                #mutatie neuniforma
                x[j]=mutatie_neuniforma(x[j],sigma,0,1)
        #individul rezultat sufera posibil mai multe mutatii
        #daca este fezabil, este pastrat
        fez, val = ok(x,c, v, max)
        if fez:
            x=x+[val]
            mpop[i]=x.copy()
            valv=valv+[val]
        else:
            #nu modific nimic in populatie
            valv=valv+[pop[i][n]]
    ind=[i for i in range(dim)]
    grafic.plot(ind,valv,"rs",markersize=9)
    return mpop


if __name__=="__main__":
    max=50
    dim=10
    p,c,v=gen("cost.txt","valoare.txt",max,dim)
    o=mutatie_populatie(p,c,v,max,0.8,0.7)
    grafic.show()



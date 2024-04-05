import matplotlib.pyplot as grafic
import numpy as np
from FunctiiCrossoverIndivizi import crossover_uniform


#verifica fezabilitatea alegerii x si calculeaza si f. obiectiv
def ok(x,c,v,max):
    val=np.dot(x,v)
    cost=np.dot(x,c)
    return cost<=max,val


#genereaza populatia initiala
#I:
# fc, fv - numele fisierelor cost, valoare
# max - capacitatea maxima
# dim - numarul de indivizi din populatie
#E: pop, cal - populatia initiala, calitatile acesteia
def gen(fc,fv,max,dim):
    #citeste datele din fisierele cost si valoare
    c=np.genfromtxt(fc)
    v=np.genfromtxt(fv)
    #n=dimensiunea problemei
    n=len(c)
    #lucreaza cu populatia ca lista de dim elemente - liste cu cate n indivizi
    pop=[]
    cal=[]
    for i in range(dim):
        gata=False
        while gata == False:
            #genereaza candidatul x cu elemente 0,1
            x=np.random.randint(0,2,n)
            gata,val=ok(x,c,v,max)
        #am gasit o solutie candidat fezabila, in data de tip ndarray (vector) x
        # x este transformat in lista
        x=list(x)
        # adauga valoarea
        cal=cal+[val]
        #adauga la populatie noul individ
        pop=pop+[x]
    return pop,cal,c,v,max



#crossover pe populatia de parinti pop, de dimensiune dimx(n+1)
# I: pop,cal - ca mai sus
#     c, v, max - datele problemei
#     pc- probabilitatea de crossover
#E: po, co - populatia copiilor, calitatile copiilor
# este implementata recombinarea asexuata
def crossover_populatie(pop,cal,c,v,max,pc):
    dim=len(pop)
    n=c.size
    po=pop.copy()
    co=cal.copy()
    #populatia este parcursa astfel incat sunt selectati indivizii 0,1 apoi 2,3 s.a.m.d
    for i in range(0,dim-1,2):
        #selecteaza parintii
        x = pop[i].copy()
        y = pop[i+1].copy()
        r = np.random.uniform(0,1)
        if r<=pc:
            # crossover x cu y - uniform: mai potrivit aici
            c1,c2=crossover_uniform(x ,y ,n)
            fez, val = ok(c1, c, v, max)
            if fez:
                po[i]=c1.copy()
                co[i]=val
            fez, val = ok(c2, c, v, max)
            if fez:
               po[i+1]=c2.copy()
               co[i+1]=val
    figureaza(cal,co, dim)
    return po,co


def figureaza(valori, val, dim):
    x = [i for i in range(dim)]
    grafic.plot(x, valori, "ko", markersize=12, label='Parinti')
    grafic.plot(x, val, "ro", markersize=9, label='Copii')
    #definire legenda
    grafic.legend(loc="lower left")
    grafic.xlabel('Indivizi')
    grafic.ylabel('Fitness')
    grafic.show()

if __name__=="__main__":
    pop,val,c,v,max=gen("cost.txt","valoare.txt",50,10)
    po,co=crossover_populatie(pop,val,c,v,max,0.8)


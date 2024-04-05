import matplotlib.pyplot as grafic
import numpy as np
from FunctiiCrossoverIndivizi import crossover_singular


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
            #genereaza candidatul x cu elemente in [0,1]
            x=np.random.uniform(0,1,n)
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

def aritmetica_singulara(p1, p2, alpha):
    c1 = p1.copy()
    c2 = p2.copy()
    n = len(p1)
    i = np.random.randint(0, n)
    c1[i] = p1[i] * alpha + p2[i] * (1 - alpha)
    c2[i] = p1[i] * (1 - alpha) + p2[i] * alpha
    return c1, c2

def crossover_populatie(pop,cal,c,v,max,pc,alpha): #alpha e ponderea
    dim = len(pop) #dimensiunea populatiei
    copii=pop.copy() #copii este copia populatiei
    valori_copii = val.copy() #valori_copii este copia valorilor
    for i in range ( 0, dim -1, 2): #parcurgem populatia din 2 in 2
        p1 = pop[i].copy()
        p2 = pop[i+1].copy()
        r = np.random.uniform(0,1)
        if r<= pc:
            c1,c2 = aritmetica_singulara(p1, p2, alpha) #c1 si c2 sunt copiii obtinuti prin crossover
            f1,v1 = ok(c1,c,v,max)
            if f1: #verificam daca primul copil e fezabil f1 are true/ false daca costul < max
                copii[i] = c1.copy()
                valori_copii[i] = v1
            f2,v2 = ok(c2,c,v,max) #al doilea copil
            if f2:
                copii[i+1] = c2.copy()
                valori_copii[i+1] = v2
    return copii, valori_copii


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
    alpha=0.3
    dim = 10
    max = 50
    pc = 0.8
    pop,val,c,v,max=gen("cost.txt","valoare.txt",max,dim)
    po,co=crossover_populatie(pop,val,c,v,max,pc,alpha)
    figureaza(val,co, dim)
    #print(po)


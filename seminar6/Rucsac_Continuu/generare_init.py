import numpy as np

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
    return pop,cal, n



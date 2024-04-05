import numpy as np
import matplotlib.pyplot as grafic


#f. obiectiv
def foNR(x):
    # functia obiectiv pentru problema reginelor

    # I: x - individul (permutarea) evaluat(a), n-dimensiunea problemei
    # E: c - calitate (numarul de perechi de regine care nu se ataca

    n=x.size
    c = n*(n-1)/2
    for i in range(n-1):
        for j in range(i+1,n):
            if abs(i-j)==abs(x[i]-x[j]):
                c-=1
    return c


#figurarea populatiei prin punctele (indice individ, calitate) - pentru a vedea variabilitatea in populatie
def reprezinta_pop(pop,dim,n):
    #fig = grafic.figure()
    x=[i for i in range(dim)]
    y=[pop[i][n] for i in range(dim)]
    grafic.plot(x,y,"gs",markersize=11)
    grafic.title("Calitatile indivizilor generați în populația inițială")
    grafic.xlabel("Index individ")
    grafic.ylabel("Calitate individ")
    grafic.show()


#genereaza populatia initiala
#I:
# n - dimensiunea prolemei
# dim - numarul de indivizi din populatie
#E: pop - populatia initiala
def gen(n,dim):
    #defineste o variabila ndarray cu toate elementelo nule
    pop=np.zeros((dim,n+1),dtype=int)
    for i in range(dim):
        #genereaza candidatul permutare cu n elemente
        pop[i,:n]=np.random.permutation(n)
        pop[i,n]=foNR(pop[i,:])
    reprezinta_pop(pop, dim, n)
    return pop


if __name__=="__main__":
    p = gen(8, 30)
    print(p)


#sau apel in consolă
#import generare_init as gi
#p=gi.gen(8,30)

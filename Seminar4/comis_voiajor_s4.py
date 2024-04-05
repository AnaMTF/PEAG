#reprezentare prin permutari
import numpy as np
import matplotlib.pyplot as grafic

def evaluare(p, C):
    n = p.size
    cost = C[p[n-1], p[0]]
    for i in range(n-1):
        cost += C[p[i], p[i+1]]
    return 100/cost  # ca sa nu mai avem valori foarte mici

def generare(dim, C):
    n = C.shape[0]
    populatie = np.zeros([dim,n],dtype=int)
    calitati = np.zeros(dim)
    for i in range(dim):
        populatie[i] = np.random.permutation(n)
        calitati[i] = evaluare(populatie[i], C)
    grafic.plot([i for i in range(dim)], calitati, "bo", markersize=12)
    return populatie, calitati

def mutatie_inversiune(p):
    n=p.size
    r=p.copy()
    i = np.random.randint(0,n-2)  #ca sa evitam drumurile sa fie identice
    j = np.random.randint(i+1,n-1)
    r[i:j+1] = [p[k] for k in range(j,i-1,-1)]
    return r

def mutatie_populatie(pop, cal, C, pm):
    mpop = pop.copy()
    mcal = cal.copy()
    dim = pop.shape[0] #numarul de indivizi
    for i in range(dim):
        r = np.random.uniform(0,1)
        if r < pm:
            individ_mutat = mutatie_inversiune(pop[i])
            mpop[i] = individ_mutat.copy()
            mcal[i] = evaluare(individ_mutat, C)
    grafic.plot([i for i in range(dim)],mcal, "ro", markersize=7)
    return mpop, mcal

if __name__ == "__main__":
    Costuri = np.genfromtxt("costuri.txt")
    dim = 18
    pm = 0.2
    pop, cal = generare(dim, Costuri)
    pm,cm = mutatie_populatie(pop, cal, Costuri, pm)
    grafic.show()

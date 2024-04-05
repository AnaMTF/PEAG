import numpy as np

def fitness(p,castig):
    return np.dot(p,castig)

def cerinta_a(dim,castig):
    n=castig.size
    populatie=np.zeros([dim,n],dtype="int")
    calitati=np.zeros(dim)
    for i in range(dim):
        populatie[i]=np.random.permutation(n)
        calitati[i]=fitness(populatie[i],castig)
    return populatie, calitati

def inversiune(p):
    n=len(p)
    i=np.random.randint(0,n-1)
    j=np.random.randint(i+1,n)
    r=p.copy()
    r[i:j+1]=[p[k] for k in range(j,i-1,-1)]
    return r

def cerinta_b(populatie,calitati,pm,castig):
    dim=populatie.shape[0]
    populatie_m=populatie.copy()
    calitati_m=calitati.copy()
    for i in range(dim):
        r=np.random.uniform(0,1)
        if r<=pm:
            print('Mutatie in ',populatie[i], ' calitatea ',calitati[i])
            populatie_m[i]=inversiune(populatie[i])
            calitati_m[i]=fitness(populatie_m[i],castig)
            print('Rezulta    ',populatie_m[i], ' calitatea ',calitati_m[i])

    return populatie_m, calitati_m

if __name__=="__main__":
    castig=np.genfromtxt("castig.txt")
    dim=20
    pm=0.2
    populatie,calitati=cerinta_a(dim,castig)
    print(populatie, calitati)
    populatie_m,calitati_m=cerinta_b(populatie,calitati,pm,castig)

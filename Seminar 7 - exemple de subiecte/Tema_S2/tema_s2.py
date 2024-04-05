import numpy as np


#functia fitness

def fitness(x):
    return x[1]*(np.sin(x[0]-2)**2)+x[2]+x[3]


def cerinta_a(dim):
    populatie=np.zeros([dim,5])
    print("POPULATIA INITIALA")
    for i in range(dim):
        populatie[i,:4]=np.random.randint([1, -1, 10,10], [1500, 2500, 250,250], 4)
        populatie[i,4]=fitness(populatie[i,:4])
        print(populatie[i])
    return populatie


def recombinare_unif(x,y):
    copil1=x.copy()
    copil2=y.copy()
    prob=np.random.uniform(0,1,4)
    for i in range(4):
        if prob[i]>0.5:
            copil1[i],copil2[i]=y[i],x[i]
    return copil1, copil2


def cerinta_b(populatie,pc):
    print("\n\nPOPULATIA DE COPII")
    dim=len(populatie)
    copii=populatie.copy()
    for i in range(0,dim-1,2):
        r=np.random.uniform(0,1)
        if r<=pc:
            #selectarea indivizilor, fara calitatile lor
            p1=populatie[i][:4].copy()
            p2=populatie[i+1][:4].copy()
            c1,c2=recombinare_unif(p1,p2)
            copii[i][:4]=c1
            copii[i][4]=fitness(c1)
            copii[i+1][:4] = c2
            copii[i+1][4] = fitness(c2)
        print(copii[i])
        print(copii[i+1])
    return copii

if __name__=="__main__":
    p=cerinta_a(10)
    c=cerinta_b(p,0.8)



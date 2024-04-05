import numpy as np

def fitness(x):
    return sum(x), sum(x)%2==0

def generare_pop(dim):
    populatie = np.zeros([dim, 18], dtype="int")
    i=0
    while i<dim:
        populatie[i,:17] = np.random.randint(0,2,17)
        populatie[i,17], ok = fitness(populatie[i,:17])
        if ok:
            i+=1
    return populatie

def turneu_k(populatie, k):  #k = nr indivizi din care fac turneu
    parinti = populatie.copy()
    dim = len(populatie) #nr de linii
    for i in range(dim):
        pozitii=np.random.randint(0,dim,k)  #k pozitii intre 0 si dim)
        v_max = populatie[pozitii[0],17]
        indice = pozitii[0]
        for j in range(1,k):
            if v_max < populatie[pozitii[j],17]:
                v_max = populatie[pozitii[j],17]
                indice = pozitii[j]
        parinti[i] = populatie[indice].copy()
    return parinti


if __name__ == "__main__":
    dim = 12
    populatie = generare_pop(dim)
    print("Populatie \n", populatie)

    k=2
    parinti = turneu_k(populatie,k)
    print("\nParinti\n", parinti)
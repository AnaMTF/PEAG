import numpy as np

#PRIMU PAS FUNCTIA FITNESS

def fct_fitness(x):
    return x[1]*np.sin(x[0] -2)**2 + x[2] + x[3]

#GENERARE DIN MULTIMEA PE CARE E DEFINITA FUNCTIA

def generare_pop(dim, a, b):   #a-capat stg, b-capat drpt, dim-dimensiunea pop
    #matrice de 5 coloane, pe ultima e calitatea, pe primele 4 valorile lui x,y,z,t
    populatie = np.zeros([dim,5])
    for i in range(dim):
        populatie[i,:4] = np.random.randint(a,b,4) #generez aleatoriu populatia xyzt
        populatie[i,4] = fct_fitness(populatie[i,:4])
    return populatie

def r_uniforma(x,y):
    c1=x.copy()
    c2=y.copy()
    p=np.random.uniform(0,1,4)
    for i in range(4):
        if p[i]>0.5:
            c1[i],c2[i] = y[i], x[i] #testam doar valorile mai mari de 0.5
    return c1,c2

def recombinare_pop(parinti,pc):  #pc probabilitate crossover(recombinare)
    copii = parinti.copy()  #copiem parintii drept valori initiale ale copiilor
    dim = parinti.shape[0]
    #dim = len(parinti)    #dim  e  nr de linii din paritni
    for i in range(0, dim-1, 2):
        raspuns = np.random.uniform(0,1)
        if raspuns <=pc:
            copii[i,:4], copii[i+1,:4] = r_uniforma(parinti[i,:4], parinti[i+1,:4])
            copii[i,4] = fct_fitness(copii[i,:4])
            copii[i+1,4] = fct_fitness(copii[i+1,:4])
    return copii

if __name__ == "__main__":
    # TEST GENERARE POP
    a=[1,-1,10,10]
    b = [1501, 2501, 251, 251]
    dim = 10
    populatie = generare_pop(dim,a,b)
    print("Parinti \n",populatie)

    # GENERARE COPII CU RECOMBINARE
    pc = 0.7
    copii = recombinare_pop(populatie, pc)
    print("\nCopii \n", copii)


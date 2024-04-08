import numpy as np

def f_fitness(p):
    n = len(p)
    rezultat = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if p[i] == j and p[j] == i:
                rezultat +=1
    return rezultat

def gen_pop(dim,n):
    pop = np.zeros([dim, n+1],dtype=int)
    for i in range(dim):
        pop[i, :n] = np.random.permutation(n)
        pop[i,n] = f_fitness(pop[i,:n])
    return pop

if __name__ == '__main__':
    dim = 10
    n = 5
    populatie = gen_pop(dim,n)
    print(populatie)

import numpy as np

def f_fitness(x):
    n = len(x)
    rezultat = 0
    for i in range(n):
        for j in range(i+1, n-1):
            if(x[i] == j and x[j]==i):
                rezultat += 1
    return rezultat

def gen_pop(dim,n):
    pop = np.zeros((dim, n+1),dtype=int)
    for i in range(dim):
        pop[i,:n] = np.random.permutation(n)
        pop[i,n] = f_fitness(pop[i,:n])
    return pop

if __name__ == '__main__':
    dim = 10
    n = 6
    pop = gen_pop(dim,n)
    print(pop)
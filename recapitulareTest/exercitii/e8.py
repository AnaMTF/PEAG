import numpy as np

def f_fitness(x):
    n = len(x)
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if(abs(x[i] - x[j]) == abs(i-j)):
                count += 1
    rezultat = n*(n-1)/2 - count
    return rezultat

def gen_pop(dim,n):
    pop = np.zeros((dim, n+1),dtype=int)
    for i in range(dim):
        pop[i,:n] = np.random.permutation(n)
        pop[i,n] = f_fitness(pop[i,:n])
    return pop

if __name__ == '__main__':
    dim = 10
    n = 8
    pop = gen_pop(dim,n)
    print(pop)
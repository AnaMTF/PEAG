import numpy as np

def f_fitness(x,y):
    rezultat = y + np.sin(x-2)**2
    return rezultat

def gen_pop(dim):
    pop = np.zeros((dim,33), dtype=int)
    x = np.random.randint(low=1,high=1501,size=dim)
    y = np.random.randint(-1,2501,size=dim)
    for i in range(dim):
        pop[i,:16] = np.array(list(np.binary_repr(x[i],width=16)),dtype=int)
        pop[i, 16:32] = np.array(list(np.binary_repr(y[i],width=16)),dtype=int)
        pop[i,32] = f_fitness(x[i],y[i])
    return pop

if __name__ == '__main__':
    dim = 4
    populatie = gen_pop(dim)
    print(populatie)

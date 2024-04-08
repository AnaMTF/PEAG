import numpy as np
np.set_printoptions(linewidth=np.inf)

def f_fitness(x):
    return sum(x)

def gen_pop(dim):
    pop = np.zeros((dim,8),dtype=int)
    for i in range(dim):
        pop[i,:7] = np.random.randint(0,2, size=7)
        pop[i,7] = f_fitness(pop[i,:7])
    return pop


if __name__ == '__main__':
    dim = 10
    pop = gen_pop(dim)
    print(pop)
import numpy as np
import graycode as gc

np.set_printoptions(linewidth=np.inf)

def fitness(x):
    return x**2

def codif_gray(x):
    x = int(x, 2)
    return bin(x ^ (x >> 1))[2:]

def gen_pop(dim):
    pop = np.zeros((dim,10), dtype=int)
    x = np.random.randint(1, 351, dim)
    for i in range(dim):
        pop[i,:9] = np.array(list(codif_gray(bin(x[i])[2:]).zfill(9)))
        pop[i,9] = fitness(x[i])
    return pop

if __name__ == '__main__':
    dim = 10
    pop = gen_pop(dim)
    print(pop)
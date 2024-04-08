import numpy as np

def f_fitness(x):
    rezultat = np.sin(x-2)**2
    return rezultat

def gen_pop(dim):
    pop = np.zeros((dim, 13),float)
    for i in range(dim):
        pop[i,:12] = np.random.randint(0,2,12)
        integer = int("".join(map(str, pop[i, :12])).replace('.', ''), 2)
        pop[i,12] = f_fitness(integer)
    return pop

if __name__ == '__main__':
    dim = 10
    pop = gen_pop(dim)
    print(pop)

import numpy as np

def f_fitness(x):
    rez = np.sin(x-2)**2 -np.cos(2*x)
    return rez

def gen_pop(dim):
    pop = np.zeros((dim,10),dtype=int)
    numar = np.random.randint(1,501,dim)
    for i in range(dim):
        pop[i,:9] = [int(x) for x in bin(numar[i])[2:].zfill(9)]
        pop[i,9] = f_fitness(numar[i])
    return pop

if __name__ == '__main__':
    dim = 33
    pop = gen_pop(dim)
    print(pop)
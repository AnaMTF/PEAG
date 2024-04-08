import numpy as np
np.set_printoptions(linewidth=np.inf)

def f_fitness(x):
    rezultat = 1+np.sin(2*x[0]-x[2]) +np.cos(x[1])
    return rezultat

def gen_pop(dim):
    pop = np.zeros((4,dim))
    for i in range(dim):
        pop[0,i] = np.random.uniform(-1,1)
        pop[1,i] = np.random.uniform(0,1)
        pop[2,i] = np.random.uniform(-2,1)
        pop[3,i] = f_fitness(pop[:3,i])
    return pop

if __name__ == '__main__':
    dim = 10
    pop = gen_pop(dim)
    print(pop)
import numpy as np
np.set_printoptions(linewidth=np.inf)

def f_fitness(x):
    rezultat = 1+np.sin(2*x[0]-x[2]) + (x[1]*x[3])**(1/3)
    return rezultat

def gen_pop(dim):
    pop = np.zeros((5,dim))
    for i in range(dim):
        pop[0,i] = np.random.uniform(-1,1)
        pop[1,i] = np.random.uniform(0,0.2)
        pop[2,i] = np.random.uniform(0,1)
        pop[3,i] = np.random.uniform(0,5)
        pop[4,i] = f_fitness(pop[:4,i])
    return pop


if __name__ == '__main__':
    dim = 10
    pop = gen_pop(dim)
    print(pop)
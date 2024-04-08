import numpy as np

def f_fitness(x):
    rezultat = x[1]*(np.sin(x[0]-2)**2) + x[2] +x[3]
    return rezultat

def subiect_a(dim, a, b): #a - capat stg, b capat drpt
    # matrice de 5 coloane, pe ultima e calitatea, pe primele 4 valorile lui x,y,z,t
    populatie = np.zeros(shape=dim,dtype=int)
    for i in range(dim):
        populatie[i,:4] = np.random.randint(low=a,high=b,size=4)
        populatie[i,4] = f_fitness(populatie[i,:4])
    return populatie



if __name__ == '__main__':
    a = [1,-1,10,10]
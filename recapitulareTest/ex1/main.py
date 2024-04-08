import numpy as np


def f_fitness(p, castig):
    return np.dot(p, castig)


def subiect_a(dim, castig):
    n = castig.size
    populatie = np.zeros([dim, n], dtype='int')
    calitati = np.zeros(dim)
    for i in range(dim):
        populatie[i] = np.random.permutation(n)
        calitati[i] = f_fitness(populatie[i], castig)
    return populatie, calitati


def mutatie_inversiune(p):
    n = len(p)
    i = np.random.randint(0, n - 1)
    j = np.random.randint(i + 1, n)
    rezultat = p.copy()
    rezultat[i:j + 1] = [p[k] for k in range(j, i - 1, -1)]
    return rezultat


def subiect_b(populatie, calitati, pm, castig):
    dim = populatie.shape[0]
    populatie_mutata = populatie.copy()
    calitati_p_mutata = calitati.copy()
    for i in range(dim):
        prob = np.random.uniform(0, 1)
        if prob <= pm:
            print('Mutatie in ', populatie[i], ' calitatea ', calitati[i])
            populatie_mutata[i] = mutatie_inversiune(populatie[i])
            calitati_p_mutata[i] = f_fitness(populatie_mutata[i], castig)
            print('Rezulta    ', populatie_mutata[i], ' calitatea ', calitati_p_mutata[i])
    return populatie_mutata, calitati_p_mutata


if __name__ == '__main__':
    castig = np.genfromtxt("ex1/castig.txt")
    dim = 20
    pm = 0.2
    populatie, calitati = subiect_a(dim, castig)
    print("Populatie \n", populatie, "\n calitati \n", calitati)
    populatie_mutata, calitati_p_mutata = subiect_b(populatie, calitati, pm, castig)

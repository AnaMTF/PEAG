# Cerinta 1: Pentru reprezentarea binara: alegeti un domeniu de definitie (functie de 2 variabile, domeniu real) si
# un punct din acest domeniu. Generati toti vecinii punctului ales.
import numpy as np


def generate_interval(n):
    a = np.random.randint(-n * n, n * n)
    b = np.random.randint(-n * n, n * n)
    if a == b:
        return generate_interval(n)
    if a > b:
        return b, a
    return a, b


def generate_point(low, high):
    if low >= high:
        low, high = high, low
    return np.random.randint(low, high)


def generate_binary_neighbours(point, low, high):
    bp = list(np.binary_repr(point))
    neighbours = []
    if point > 0:
        for i in range(len(bp)):
            aux = bp.copy()
            aux[i] = '0' if aux[i] == '1' else '1'
            aux = ''.join(aux)
            if int(aux, 2) >= low and int(aux, 2) <= high:
                neighbours.append(aux)
    else:
        for i in range(1, len(bp)):
            aux = bp.copy()
            aux[i] = '0' if aux[i] == '1' else '1'
            aux = ''.join(aux)
            if int(aux, 2) >= low and int(aux, 2) <= high:
                neighbours.append(aux)
    return neighbours


def print_binary_neighbours(neighbours):
    for neighbour in neighbours:
        print("\t\t bin(elem) = {}, elem = {}".format(neighbour, int(neighbour, 2)))


# Cerinta 2: Pentru reprezentarea cu numere reale: alegeti un domeniu de definitie (functie de 2 variabile,
# domeniu real) si un punct din acest domeniu. Generati toti vecinii punctului ales.

def generate_real_neighbours(point, low, high):
    neighbours = []
    nz = np.random.choice([1, 2, 3, 4], p=[0.25, 0.25, 0.25, 0.25])
    print("Precizia va fi la {} ".format(nz) + "zecimale." if nz > 1 else "zecimala.")
    epsilon = 1 / (10 ** nz)
    nrc = np.random.randint(1, 10)
    print("Numarul de vecini va fi: {}".format(nrc * 2))
    for i in range(nrc):
        aux1 = point + (i - nrc) * epsilon
        aux2 = point - (i - nrc) * epsilon
        if aux1 >= low and aux1 <= high:
            neighbours.append(aux1)
        if aux2 >= low and aux2 <= high:
            neighbours.append(aux2)
    return sorted(neighbours)


def print_real_neighbours(neighbours):
    for neighbour in neighbours:
        print("\t\t elem = {}".format(neighbour))


if __name__ == "__main__":
    print("Tema 1:")
    a, b = generate_interval(10)
    print("Interval: [{}, {}]".format(a, b))
    point = generate_point(a, b)
    print("x ∈ [{}; {}]: bin(x) = {}, x = {}".format(a, b, np.binary_repr(point), point))
    neighbours = generate_binary_neighbours(point, a, b)
    print_binary_neighbours(neighbours)

    print("\n\nTema 2:")
    a, b = generate_interval(10)
    print("Interval: [{}, {}]".format(a, b))
    point = generate_point(a, b)
    print("x ∈ [{}; {}]: x = {}".format(a, b, point))
    neighbours = generate_real_neighbours(point, a, b)
    print_real_neighbours(neighbours)

import copy

import numpy

sol = []
maxA = []

def verificareCost(v, n, c, cmax):
    suma = 0
    for i in range(n):
        suma += v[i] * c[i]
    return suma <= cmax

def verificareRaza(v, n, r):
    raza = 0
    suma = 0
    for i in range(n):
        raza += v[i] * r[i]
        suma += v[i]
    if suma != 0:
        media = raza / suma
    else:
        return False
    return media > 40

def autonomie(v, n, a):
    aut = 0
    sum = 0
    for i in range(n):
        aut = v[i] * a[i]
        sum = sum + v[i]
    if sum != 0:
        return aut / sum
    else:
        return -1

def Backtracking(v, nr, n, cmax, c, r, a):
    if nr == n:
        g = verificareRaza(v, n, r)
        if g == True:
            temp = autonomie(v, n, a)
            cv = copy.deepcopy(v)
            sol.append(cv)
            maxA.append(temp)
    else:
        for i in range(101):
            v[nr] = i
            f = verificareCost(v, nr+1, c, cmax)
            if f:
                Backtracking(v, nr+1, n, cmax, c, r, a)

n=3
v = numpy.zeros([n], dtype=int)
cmax = 5000
c = [100, 60, 50]
a = [6000, 4200, 2800]
r = [30, 48, 32]
Backtracking(v, 0, n, cmax, c, r, a)
valm = numpy.max(maxA)
i = numpy.where(maxA == valm)
print(sol[i[0][0]], valm)




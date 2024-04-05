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

def vecini(v, n, c, cmax, r, a):
    vec = []
    cal = []
    for i in range(n):
        y = v.copy()
        y[i] = numpy.random.randint(0, 101, 1)
        if verificareRaza(v, n, r) and verificareCost(v, n, c, cmax):
            vec = vec + [y]
            val = autonomie(v, n, a)
            cal = cal + [val]
    return vec, cal

def CAerianaHC(c, cmax, r, a, dim):
    puncte = []
    calitati = []
    n = len(c)
    for i in range(dim):
        gata = False
        local = False
        while gata == False:
            v = numpy.random.randint(0, 101, n)
            gata = verificareRaza(v, n, r) and verificareCost(v, n, c, cmax)
            val = autonomie(v, n, a)
        while local == False:
            vec, cal = vecini(v, n, c, cmax, r, a)
            if len(cal) == 0:
                local = True
            else:
                valm = numpy.max(cal)
                i = numpy.where(cal == valm)
                vn = vec[i[0][0]]
                if valm > val:
                    v = vn
                    val = valm
                else:
                    local = True
        puncte = puncte + [v]
        calitati = calitati + [val]

    puncte = numpy.asarray(puncte)
    calitati = numpy.asarray(calitati)

    valm = numpy.max(cal)
    i = numpy.where(cal == valm)
    sol = puncte[i[0][0]]

    return sol, valm, puncte, calitati

n=3
v = numpy.zeros([n], dtype=int)
cmax = 5000
c = [100, 60, 50]
a = [6000, 4200, 2800]
r = [30, 48, 32]
sol, valm, puncte, calitati = CAerianaHC(c, cmax, r, a, 100)
print("Urmatorul program de achizitie asigura o autonomie medie maxima, o valoare medie")
print("a razei de evitare a coliziunilor mai mare de 40 km si se incadreaza in suma")
print("disponibila pentru achizitie. Se cumpara: ")
print(sol[0]," avioane de tip A,")
print(sol[1], " avioane de tip B si ")
print(sol[2], " avioane de tip C.")
print("Autonomia medie obtinuta cu acest program de achizitie este: ", valm)
import numpy

def foNR(v, n):
    c = n * (n-1) / 2
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(i-j) == abs(v[i] - v[j]):
                c = c - 1
    return c, c == n * (n-1) / 2

def vecini(v, n):
    vec = []
    cal = []
    for i in range(n-1):
        for j in range(i+1, n):
            y = v.copy()
            aux = y[i]
            y[i] = y[j]
            y[j] = aux
            val, gata = foNR(y, n)
            if gata:
                vec = vec + [y]
                cal = cal +[val]
    return vec, cal

def NRegineHC(n, dim):
    puncte = []
    calitati = []
    for i in range(dim):
        gata = False
        local = False
        while gata == False:
            v = numpy.random.permutation(n)
            val, gata = foNR(v, n)
        while local == False:
            vec, cal = vecini(v, n)
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

    sol = []
    for i in range(dim):
        if i == 0:
            sol.append(puncte[i])
        else:
            ok = 0
            for j in range(len(sol)):
                ok2 = 0
                for k in range(n):
                    if sol[j][k] != puncte[i][k]:
                        ok2 = 1
                if ok2 == 0:
                    ok = 1
            if ok == 0:
                sol.append(puncte[i])
    return numpy.asarray(sol)

n = int(input("Introduceti dimensiunea tablii de sah:"))
puncte = NRegineHC(n, 20)
print(puncte)


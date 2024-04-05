import numpy as np

def evaluare(s, cost, val, CMax):
    val_tot = np.dot(s,val)
    cost_tot = np.dot(s,cost)
    return val_tot, cost_tot<=CMax

def generare(dim_pop, cost, val, CMax):
    coloane_n = cost.size
    populatie = np.zeros([dim_pop,coloane_n])
    calitati = np.zeros(dim_pop)

    i = 0
    while i<dim_pop:
        individ = np.random.uniform(0,0.1,coloane_n)
        val_individ, ok_individ = evaluare(individ, cost, val, CMax)
        if ok_individ:
            populatie[i] = individ.copy()
            calitati[i] = val_individ
            i+=1
    return populatie, calitati

if __name__ == "__main__":
    cost=np.genfromtxt("cost.txt")
    val = np.genfromtxt("valoare.txt")
    dim = 10
    CMax = 10
    p_init,c_init = generare(dim, cost, val, CMax)
    for i in range (dim):
        print("Individul ", i+1, " : ", p_init[i], " calitate ", c_init[i], "\n" )

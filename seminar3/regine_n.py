import  numpy as np

def calitate(permutare):
    n = permutare.size
    val = int(n*(n-1)/2)
    for i in range(n-1):
        for j in range(i+1,n):
            if abs(i-j)==abs(permutare[i]-permutare[j]):
                val -=1
    return val

def generare(n , dim):
    pop_fit = np.zeros([dim, n+1], dtype="int")
    for i in range (dim):
        individ = np.random.permutation(n)
        #pop_fit[i,:n]=individ.copy()
        #pop_fit[i, n] = calitate(individ)
        pop_fit[i, :-1] = individ.copy()
        pop_fit[i, -1] = calitate(individ)
    return pop_fit

if __name__ == "__main__":
    dim = 10
    n = 8
    p_init = generare(n,dim)
    for i in range (dim):
        print("Individul ", i+1, " : ", p_init[i,:n], " calitate ", p_init[i,n] )

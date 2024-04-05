import numpy as np

#descriere PMX - varianta
#echivalent cu functia crossover_PMX din FunctiiCrossoverIndivizi

def c_PMX(x,y,i,j):
    n=len(x)
    copil=-np.ones(n,dtype="int")
    copil[i:j+1]=x[i:j+1]
    for k in range(i,j+1):
        if not y[k] in copil:
            poz=k
            while copil[poz]>-1:
                poz=np.where(y==copil[poz])[0][0]
            copil[poz]=y[k]
    z=[y[i] for i in range(n) if not y[i] in copil]
    poz_libere=[k for k in range(n) if copil[k]==-1]
    for i in range(len(poz_libere)):
        copil[poz_libere[i]]=z[i]
    return copil


def PMX(x,y):
    n=len(x)
    i=np.random.randint(0,n-1)
    j=np.random.randint(i+1,n)
    c1=c_PMX(x,y,i,j)
    c2=c_PMX(y,x,i,j)
    return c1,c2

if __name__=="__main__":
    n=10
    x=np.random.permutation(n)
    y=np.random.permutation(n)
    print("parinte1:",x)
    print("parinte2:", y)
    c1,c2=PMX(x,y)
    print("copil1:  ", c1)
    print("copil2:  ", c2)
import numpy as np
import matplotlib.pyplot as grafic

#f. obiectiv
def foTSP(p,c):
    n=p.size
    val=0
    for i in range(n-1):
        val+=c[p[i],p[i+1]]
    val+=c[p[0],p[n-1]]
    return 100/val



def gen(fc,dim):
    c=np.genfromtxt(fc)
    n = c.shape[0]
    pop=np.zeros([dim,n],dtype="int")
    val=np.zeros(dim,dtype="float")
    for i in range(dim):
        pop[i] = np.random.permutation(n)
        val[i] = foTSP(pop[i],c)
    grafic.plot([i for i in range(dim)],val,"gs",markersize=12)
    return pop, val,c



def mutatie_inversiune(p):
    n=p.size
    i=np.random.randint(0,n-1)
    j=np.random.randint(i+1,n)
    r=p.copy()
    r[i:j+1]=[p[k] for k in range(j,i-1,-1)]
    return r


def mutatie_populatie(pcopii,vcopii,c,pm):
    mpo=pcopii.copy()
    mvo=vcopii.copy()
    dim=mpo.shape[0]
    for i in range(dim):
        r=np.random.uniform(0,1)
        if r<=pm:
            x=mpo[i]
            y=mutatie_inversiune(x)
            mpo[i]=y
            mvo[i]=foTSP(y,c)
    grafic.plot([i for i in range(dim)],mvo,"rs",markersize=10)
    return mpo,mvo

if __name__=="__main__":
    p,v,c=gen("costuri.txt",20)
    o,vo=mutatie_populatie(p,v,c,0.2)
    grafic.show()
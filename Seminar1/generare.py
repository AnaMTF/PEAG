import numpy as np

def gen_p(m,n):
    rez=np.zeros([m,n+1],dtype="double")
    rez[:m,:n]=np.random.uniform(0,1,[m,n])
    for i in range(m):
        rez[i,n]=np.sin(rez[i,0]) +np.cos(rez[i,1])+sum(rez[i,2:n])
    return rez, max(rez[:,n])

if __name__=="__main__":
    R, vmax = gen_p(23, 5)
    print(R)
    print(vmax)
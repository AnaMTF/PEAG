import numpy as np

def f_obiectiv(p):
    n=p.size
    #n=len(p)
    calitate= n*(n-1)/2

    for i in range(n-1):
        for j in range(i+1,n):
            if abs(p[i]-p[j])==abs(i-j): #distanta dintre i si j
                calitate-=1
        return calitate

def Vecini(p):
    n=p.size
    vecini_p=np.zeros(0,dtype="int")
    calitati_v=np.zeros(0)
    for i in range(n-1):
        for j in range (i+1, n):
            x=p.copy()
            # x[i]=p[j]
            # x[j]=p[i]
            x[i],x[j]=p[j],p[i]
            vecini_p=np.append(vecini_p,x)
            calitati_v = np.append(calitati_v,f_obiectiv(x))
    vecini_p=vecini_p.reshape(int(vecini_p.size/n),n)
    return vecini_p, calitati_v

def HC(n):
    x0=np.random.permutation(n)
    c_x0=f_obiectiv(x0)
    local=False
    while not local:
        vec_x0,cal_x0=Vecini(x0)
        best=np.argmax(cal_x0) #pozitia celui mai bun vecin
        if cal_x0[best]>c_x0: #maximul calitatii este cal_x0.max()=cal_x0[best]
            x0=vec_x0[best]
            c_x0=cal_x0[best]
        else:
            local=True
    return x0,c_x0

def rezolva(n,nr_incercari):
    x0, c_x0=HC(n)
    for i in range (nr_incercari-1):
        x,c_x=HC(n)
        if c_x>c_x0:
            x0,c_x0=x,c_x
    return x0,c_x0


if __name__ == "__main__":
    # p=np.array([3,1,2,4,0])
    # c_p = f_obiectiv(p)
    # print("Calitatea aranjarii: ", c_p)
    # V,C = Vecini(p)
    # print("Vecinii: ")
    # print(V)
    # print("Calitatile: ")
    # print(C)

    #problema celor n regine
    n=20
    sol,val_sol=HC(n)
    print("Solutia calculata: ", sol)
    if val_sol == n*(n-1)/2:
        print("Configuratie solutie")
    else:
        print("Numarul de perechi in pozitia de atac: ",n*(n-1)/2-val_sol)

    sol, val_sol = rezolva(n, 15)
    print("Solutia calculata: ", sol)
    if val_sol == n * (n - 1) / 2:
        print("Configuratie solutie")
    else:
        print("Numarul de perechi in pozitia de atac: ", n * (n - 1) / 2 - val_sol)






#consola: v=np.zeros(0)
#v=np.append(v,[1,2,3])
#v=np.zeros(0,dtype="int")
#v=np.append(v,[1,2,3])
#v=np.append(v,[10,20,30])
#a=v.reshape([2,3])
#t=v
#t[0]=1000
#t=v.copy()
#t[0]=1
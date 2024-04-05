import numpy as np
import matplotlib.pyplot as grafic

#f_obiectiv
def f_ob(x,val,cost,CMax):
    v_t=np.dot(x,val)
    c_t=np.dot(x,cost)
    return c_t<=CMax, v_t

#constructia vecinilor insotiti de calitati
def vecini(x,val,cost,CMax):
    #Vecini=np.zeros(0,dtype="int")
    Vecini=[]
    Calitati=np.zeros(0,dtype="float")
    n=x.size
    for i in range(n):
        y=x.copy()
        y[i]=not x[i]
        fez,v_t=f_ob(y,val,cost,CMax)
        if fez:
            #Vecini=np.append(Vecini,y)
            Vecini=Vecini+[y]
            Calitati=np.append(Calitati,v_t)
    #dim=Vecini.size
    #Vecini=Vecini.reshape(int(dim/n),n)
    Vecini=np.array(Vecini)
    return Vecini, Calitati


## HC pentru un punct initial
def HC(val,cost,CMax):
    n=val.size
    gen_ini=False
    list_print=np.zeros(0,dtype="float")
    while not gen_ini:
        x=np.random.randint(0,2,n)
        gen_ini,v_t=f_ob(x,val,cost,CMax)
    #aici x este o varianta initiala, fezabila
    list_print=np.append(list_print,v_t)
    local=False
    while not local:
        Vecini,Calitati=vecini(x,val,cost,CMax)
        if Calitati.size==0:
            local=True
        else:
            index=np.argmax(Calitati)
            if v_t<Calitati[index]:
                x=Vecini[index].copy()
                v_t=Calitati[index]
                list_print = np.append(list_print, v_t)
            else:
                local=True
    if list_print.size>3:
        deseneaza(list_print)
    return x,v_t


def deseneaza(list_print):
    n=list_print.size
    x=[i for i in range(n)]
    grafic.plot(x,list_print,"ro-",markersize=10)
    grafic.show()


# rezolvarea problemei - HC apelat de k ori, pentru k puncte initiale
def apel_HC(fis_val,fis_cost,CMax,k):
    val=np.genfromtxt(fis_val)
    cost=np.genfromtxt(fis_cost)
    n=val.size
    Puncte=np.zeros(0,dtype="int")
    Valori=np.zeros(0,dtype="float")
    for i in range(k):
        x,v_t=HC(val,cost,CMax)
        Puncte=np.append(Puncte,x)
        Valori=np.append(Valori,v_t)
    Puncte=Puncte.reshape(k,n)
    v_max=Valori.max()
    p_max=Puncte[np.argmax(Valori)]
    print("Maximul calculat ",v_max," la alegerea ",p_max)
    return p_max,v_max,Puncte,Valori

if __name__=="__main__":
    sol,val,P,C=apel_HC("valoare.txt","cost.txt",50,70) #- max 81
    #sol,val,P,C=apel_HC("valoare1.txt","cost1.txt",50,90) #- max 108
    #sol,val,P,C=apel_HC("valoare2.txt","cost2.txt",56.6,1500) #- max 128.2




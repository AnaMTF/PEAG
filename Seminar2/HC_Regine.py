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

if __name__ == "__main__":
    p=np.array([3,1,2,4,0])
    c_p = f_obiectiv(p)
    print("Calitatea aranjarii: ", c_p)
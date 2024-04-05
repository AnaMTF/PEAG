import copy

def verificareColoane(v, n):
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i] == v[j]:
                return False
    return True

def verificareDiagonale(v, n):
    for i in range(n-1):
        x=abs(v[i]-v[n-1])
        y=n-i-1
        if x == y:
            return False
    return True

def Backtracking(v, n, k):
    if k == n:
        print(v)
    else:
        for i in range(n):
            v[k]=i
            if verificareColoane(v, k+1):
                if verificareDiagonale(v, k+1):
                    Backtracking(v, n, k+1)

n=int(input("Introduceti numarul reginelor: "))
v=[0]*n
Backtracking(v, n, 0)
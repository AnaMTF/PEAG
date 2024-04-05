"""Cerință: 3.	Implementați algoritmul de sortare prin metoda bulelor pentru a ordona fiecare linie a unei matrice"""

def ex3(a):
    """Returnează o matrice în care fiecare linie este sortată."""
    for i in range(len(a)):
        for j in range(len(a[i])):
            for k in range(len(a[i]) - 1):
                if a[i][k] > a[i][k + 1]:
                    a[i][k], a[i][k + 1] = a[i][k + 1], a[i][k]
    return a
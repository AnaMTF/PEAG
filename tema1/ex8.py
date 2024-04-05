"""Cerință: 8.	Fie A și V construite la ex7. Aranjați liniile matricei A astfel încât elementele lui V să fie în ordine crescătoare."""

import numpy as np

def ex8():
    """Returnează o matrice A cu 20 de linii, vectori din S și un vector V cu 20 de elemente. Matricea este sortata crescator pe linii."""
    a = [[np.random.choice((0, 1)) for i in range(7)] for j in range(20)]
    a.sort(key=lambda x: sum(x))
    v = [sum(a[i]) for i in range(20)]
    return a, v

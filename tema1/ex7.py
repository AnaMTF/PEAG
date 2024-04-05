"""Cerință: 7.	Fie S mulțimea vectorilor binari de lungime 7.
Calculați, prin generare aleatoare, o matrice A cu 20 de linii, vectori din S și un vector V cu 20 de elemente,
fiecare V[i] reprezentând calitatea liniei i din A, definită prin suma biților vectorului linie i."""

import numpy as np


def ex7():
    """Returnează o matrice A cu 20 de linii, vectori din S și un vector V cu 20 de elemente."""
    a = [[np.random.choice((0, 1)) for i in range(7)] for j in range(20)]
    v = [sum(a[i]) for i in range(20)]
    return a, v

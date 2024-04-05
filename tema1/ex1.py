"""Cerință: 1.	Calculați numărul liniilor unei matrice cu proprietatea că au elementele în ordine crescătoare."""


def ex1(a):
    """Returnează numărul liniilor unei matrice cu proprietatea că au elementele în ordine crescătoare."""
    n = 0
    for i in range(len(a)):
        if a[i] == sorted(a[i]):
            n += 1
    return n

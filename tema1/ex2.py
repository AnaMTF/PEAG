"""Cerință: 2.	Determinați coloanele unei matrice cu proprietatea că au cel mai mic element egal cu 5."""


def ex2(a):
    """Returnează coloanele unei matrice cu proprietatea că au cel mai mic element egal cu 5."""
    n = []
    for i in range(len(a[0])):
        if min(a[j][i] for j in range(len(a))) == 5:
            n.append(i)
    if not n:
        return "Nu există"
    return n

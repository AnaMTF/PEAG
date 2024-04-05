"""Cerință: 4.	Scrieți o funcție recursivă pentru calculul cmmdc dintre două numere naturale nenule"""

def ex4(a, b):
    """Returnează cmmdc dintre două numere naturale nenule"""
    if b == 0:
        return a
    else:
        return ex4(b, a % b)

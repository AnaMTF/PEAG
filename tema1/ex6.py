"""Cerință: 6.	Verificați proprietatea unei permutări de a fi permutarea identică."""

def ex6(a):
    """Returnează True dacă permutarea este identică, False în caz contrar."""
    for i in range(len(a)):
        if a[i] != i:
            return False
    return True

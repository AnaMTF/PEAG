"""Cerință: 5.	Fie A și B două matrice pătratice și n un număr natural nenul. Calculați A transpusă, A+B, A*B și A^n. """

import numpy as np

def ex5(a, b, n):
    """Returnează A transpusă, A+B, A*B și A^n."""
    A_transpusa = np.transpose(a)
    A_plus_B = np.add(a, b)
    A_inmultit_cu_B = np.matmul(a, b)
    A_la_puterea_n = np.linalg.matrix_power(a, n)
    return A_transpusa, A_plus_B, A_inmultit_cu_B, A_la_puterea_n

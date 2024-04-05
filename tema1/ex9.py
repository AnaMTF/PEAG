"""Cerință: 9.	Creati o populatie initiala pentru urmatoarea functie de maxim si identificati cel mai bun individ din
aceasta 𝑓: {1,2, … ,2500} → ℝ, 𝑓(𝑥) = (𝑠𝑖𝑛(𝑥 − 2))^2 − 𝑥 ∗ 𝑐𝑜𝑠(𝑥)."""

import numpy as np

def fitness(x):
    return np.sin(x - 2) ** 2 - x * np.cos(x)

def ex9(dim):
    """Returnează o populație de dim vectori cu 2500 de elemente, fiecare element având valori între 1 și 2500."""
    populatia = np.random.randint(1, 2500, dim).tolist()
    best = sorted(populatia, key=lambda x: fitness(x), reverse=True)[0]
    return populatia, best

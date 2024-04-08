import numpy as np















































"""1. Fie 𝑓: 𝒫(𝑛) → ℕ 𝑝𝜖𝒫(𝑛), 𝑓(𝑝) = |{(𝑖,𝑗)⁄𝑖 < 𝑗, 𝑝(𝑖) = 𝑗 ş𝑖 𝑝(𝑗) = 𝑖 }| funcţia obiectiv a unei
probleme de maxim, unde 𝒫(𝑛) desemnează mulţimea permutărilor de n elemente.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Pentru o probabilitate de mutaţie dată, pm, scrieţi o funcţie de mutaţie utilizând operatorul de
mutaţie prin inserare care, pe baza populaţiei pop obţine o nouă populaţie, popm. Populaţia
rezultată are tot dim indivizi.
"""

import numpy as np

def fitness(p):
    """Calculates the fitness of a permutation p"""
    n = len(p)
    return sum([1 for i in range(n) for j in range(i+1, n) if p[i] == j and p[j] == i])

def generate_population(dim, n):
    """Generates a random population of permutations of n elements"""
    pop = np.zeros((dim, n+1), dtype=int)
    for i in range(dim):
        pop[i, :n] = np.random.permutation(n)
        pop[i, n] = fitness(pop[i, :n])
    return pop

def mutation(pop, pm):
    """Mutation operator"""
    dim, n = pop.shape
    popm = np.zeros((dim, n), dtype=int)
    for i in range(dim):
        if np.random.rand() < pm:
            # mutation
            j = np.random.randint(n-1)
            popm[i, :] = np.concatenate((pop[i, :j], pop[i, j+1:], pop[i, j:j+1]))
        else:
            # no mutation
            popm[i, :] = pop[i, :]
    return popm

def main1():
    """Main function"""
    dim = 10
    n = 5
    pm = 0.1
    pop = generate_population(dim, n)
    print(f"Populatia initiala, cu {dim} indivizi, permutari de ordin {n}\n\n",pop)
    popm = mutation(pop, pm)
    print(f"\n\nPopulatia rezultat, cu {pm} probabilitate de mutatie, tot cu {dim} indivizi, permutari de ordin "
          f"{n}\n\n",popm)

"""
10. Fie 𝑓:{1,2,…,350}→ℝ,𝑓(𝑥)=𝑥2 funcţia obiectiv a unei probleme de maxim. Fiecărui fenotip 𝑥∈{1,2,…,350} îi corespunde un genotip şir binar obţinut prin codificarea Gray.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
b. Aplicaţi funcţia de generare implementată mai sus pentru obţinerea a două populaţii, pop1, pop2. Scrieţi o funcţie Python care obţine o nouă populaţie prin aplicarea unei proceduri de tip GENITOR (cu înlocuirea a 2 indivizi) celor două populaţii, unde pop2 este considerată populaţia progeniturilor lui pop1. Populaţia rezultată are tot dim indivizi.
"""

import numpy as np

def fitness(x):
    """Calculează fitness-ul unui individ"""
    return x ** 2

def binary_to_gray(x):
    """Codifică un număr binar în codul Gray"""
    x = int(x, 2)
    return bin(x ^ (x >> 1))[2:]

def generate_population(dim):
    """Generează o populaţie aleatoare de dim indivizi"""
    pop = np.zeros((dim, 10), dtype=int)
    x = np.random.randint(1, 351, dim)
    for i in range(dim):
        pop[i, :9] = np.array(list(binary_to_gray(bin(x[i])[2:]).zfill(9)))
        pop[i, 9] = fitness(x[i])
    return pop

def genitor(pop1, pop2):
    """Procedura de tip GENITOR"""
    dim, n = pop1.shape
    poz1, poz2 = np.random.randint(0, dim, 2)
    pop1 = pop1[pop1[:, -1].argsort()]
    pop1[0, :] = pop2[poz1, :]
    pop1[1, :] = pop2[poz2, :]
    return pop1, poz1, poz2

def main10():
    """Funcţia principală"""
    dim = 10
    pop1 = generate_population(dim)
    print(f"Populatia initiala, cu {dim} indivizi\n\n", pop1)
    pop2 = generate_population(dim)
    print(f"\n\nPopulatia progeniturilor, cu {dim} indivizi\n\n", pop2)
    pop, poz1, poz2 = genitor(pop1, pop2)
    print(f"\n\nPopulatia rezultat, tot cu {dim} indivizi, unde primii 2 cei mai slabi cromozomi au fost "
          f"schimbati cu cromozomii {poz1} si {poz2} din pop2.\n\n", pop)

"""11. Fie 𝑓:{1,2,…,500}→ℝ,𝑓(𝑥)=(𝑠𝑖𝑛(𝑥−2))2−𝑥∙𝑐𝑜𝑠(2∙𝑥) funcţia obiectiv a unei probleme de maxim. Fiecărui fenotip 𝑥∈{1,2,…,500} îi corespunde un genotip şir binar obţinut prin reprezentarea standard în bază 2 a lui x.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Scrieţi o funcţie Python care, pentru populaţia generată pop obţine o populaţie de părinţi prin aplicarea selecţiei de tip turneu cu k indivizi (k parametru de intrare)."""

import numpy as np

def fitness(x):
    return (np.sin(x - 2) ** 2) - x * np.cos(2 * x)

def generate_population(dim):
    pop = np.zeros((dim, 10), dtype=int)
    num = np.random.randint(1, 501, dim)
    for i in range(dim):
        pop[i, :9] = [int(x) for x in bin(num[i])[2:].zfill(9)]
        pop[i, 9] = fitness(num[i])
    return pop

def tournament_selection(pop, k):
    parinti = np.zeros((len(pop), 10), dtype=int)
    for i in range(len(pop)):
        idx = np.random.randint(0, len(pop), k)
        parinti[i] = pop[idx[np.argmax(pop[idx, 9])]]
    return parinti

def main11():
    dim = 10
    k = 3
    pop = generate_population(dim)
    print(f"Populatia initiala, cu {dim} indivizi:\n",pop)
    parinti = tournament_selection(pop, k)
    print(f"Populatia parintilor, cu {dim} indivizi si {k} participanti la turnir\n\n", parinti)

"""2. Fie 𝑓:{1,2, … ,1500} × {−1,0, , … ,2500} → ℝ, 𝑓(𝑥, 𝑦) = 𝑦 ∗ (𝑠𝑖𝑛(𝑥 − 2))^2
funcţia obiectiv a
unei probleme de maxim. Fiecărui fenotip (𝑥, 𝑦) ∈ {1,2, … ,1500} × {−1,0, , … ,2500} îi
corespunde un genotip şir binar obţinut prin reprezentarea în bază 2 a fiecărei componente a
fenotipului.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Pentru o probabilitate de recombinare dată, pc, scrieţi o funcţie de recombinare utilizând
operatorul de încrucişare multi-punct pentru 3 puncte de încrucişare care, pe baza populaţiei pop
obţine o nouă populaţie, popc. Populaţia rezultată are tot dim indivizi (este utilizată şi
recombinarea asexuată şi calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări
cromozomiale).
"""
import numpy as np
def fitness(x, y):
    """Calculeaza calitatea unui individ"""
    return y * np.sin(x - 2)**2

def genereaza_popi(dim):
    """Genereaza o populatie de dim indivizi, fiecare reprezentat printr-un sir de 16 biti, pentru a acoperi tot
    intervalul de valori. Calitatea fiecarui individ este memorata la sfarsitul fiecarei reprezentari cromozomiale.
    Cum fiecare individ are o reprezentare pe 16 biti, un rand din matricea pop are 33 de elemente. Primele 16
    pozitii desemneaza reprezentarea binara a lui x, urmatoarele 16 pozitii reprezinta reprezentarea binara a lui y,
    iar ultima pozitie memoreaza calitatea individului. Calitatea va fi de tip float, deoarece functia fitness
    returneaza un numar real. Trebuie sa schimbam afisarea matricei, astfel incat sa fie afisate doar cu o zecimală."""
    pop = np.zeros((dim, 33), dtype=int)
    x = np.random.randint(1, 1501, size=dim)
    y = np.random.randint(-1, 2501, size=dim)
    for i in range(dim):
        pop[i, :16] = np.array(list(np.binary_repr(x[i], width=16)), dtype=int)
        pop[i, 16:32] = np.array(list(np.binary_repr(y[i], width=16)), dtype=int)
        pop[i, 32] = fitness(x[i], y[i])
    return pop

def recombinare(pop, pc):
    """Functia de recombinare multi-punct pentru 3 puncte de incrucisare. Pentru fiecare individ, se genereaza
    un numar aleatoriu intre 0 si 1. Daca numarul este mai mic decat probabilitatea de recombinare, atunci
    individul va fi supus recombinarii. Daca nu, individul va fi copiat in noua populatie. Pentru recombinare,
    se va folosi operatorul de incrucisare multi-punct pentru 3 puncte de incrucisare. Se va genera un vector
    cu 3 valori aleatoare, care vor fi pozitiile punctelor de incrucisare. Se va copia din individul parinte
    in individul copil, incepand cu pozitia 0 si pana la pozitia primului punct de incrucisare. Apoi se va
    copia din individul parinte in individul copil, incepand cu pozitia urmatoare celui de-al doilea punct de
    incrucisare si pana la pozitia urmatoare celui de-al treilea punct de incrucisare. In final, se va copia din
    individul parinte in individul copil, incepand cu pozitia urmatoare celui de-al treilea punct de incrucisare
    si pana la pozitia finala. Calitatea fiecarui individ va fi calculata si va fi memorata la sfarsitul fiecarei
    reprezentari cromozomiale. Populatia rezultata are dim indivizi."""
    popc = np.zeros((pop.shape[0], 33), dtype=int)
    for i in range(0, pop.shape[0], 2):
        if np.random.rand() < pc:
            p1 = np.random.choice([j for j in range(16)])
            p2 = np.random.choice([j for j in range(16)])
            while p2 == p1:
                p2 = np.random.choice([j for j in range(16)])
            p3 = np.random.choice([j for j in range(16)])
            while p3 == p1 or p3 == p2:
                p3 = np.random.choice([j for j in range(16)])
            puncte = [p1, p2, p3]
            puncte.sort()
            popc[i, :puncte[0]] = pop[i, :puncte[0]]
            popc[i, puncte[0]:puncte[1]] = pop[i+1, puncte[0]:puncte[1]]
            popc[i, puncte[1]:puncte[2]] = pop[i, puncte[1]:puncte[2]]
            popc[i, puncte[2]:] = pop[i+1, puncte[2]:]
            popc[i, 32] = fitness(int("".join(map(str, popc[i, :16])), 2), int("".join(map(str, popc[i, 16:32])), 2))
        else:
            popc[i, :] = pop[i, :]
            popc[i+1, :] = pop[i+1, :]
    return popc

def main2():
    """Functia main"""
    dim = 4
    pc = 0.7
    pop = genereaza_popi(dim)
    print(f"Populatia initiala, formata din {dim} indivizi.\n\n",pop)
    popc = recombinare(pop, pc)
    print(f"\nPopulatia dupa recombinare cu probabilitate de {pc}, formata tot din {dim} indivizi.\n\n", popc)

"""3. Fie 𝑓:[−1,1] × [0,0.2] × [0,1] × [0,5] → ℝ, 𝑓(𝑥1, 𝑥2, 𝑥3, 𝑥4) = 1 + 𝑠𝑖𝑛(2𝑥1 − 𝑥3) + (𝑥2 ∗𝑥4)^(1/3) funcţia
obiectiv a unei probleme de maxim. Un genotip este un vector 𝑥 =(𝑥1, 𝑥2, 𝑥3, 𝑥4)𝑇, 𝑥 ∈ [−1,1] × [0,0.2] × [0,1] × [0,5]

a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
b. Pentru o probabilitate de mutaţie dată, pm, scrieţi o funcţie mutaţie de tip fluaj cu pragul 𝑡 =0.6 (𝜎 =𝑡/3) care,
pe baza populaţiei pop obţine o nouă populaţie, cu indivizii eventual mutanţi ai lui pop."""

import numpy as np


def fitness(x):
    """Calculates the fitness of a vector x"""
    return 1 + np.sin(2 * x[0] - x[2]) + (x[1] * x[3]) ** (1 / 3)


def generate_population(dim):
    """Genereaza o populatie aleatoare de dimensiune dim."""
    pop = np.zeros((dim, 5))
    for i in range(dim):
        pop[i, 0] = np.random.uniform(-1, 1)
        pop[i, 1] = np.random.uniform(0, 0.2)
        pop[i, 2] = np.random.uniform(0, 1)
        pop[i, 3] = np.random.uniform(0, 5)
        pop[i, 4] = fitness(pop[i, :4])
    return pop


def mutation(pop, pm):
    """Mutation operator"""
    dim, n = pop.shape
    popm = np.zeros((dim, n), dtype=float)
    for i in range(dim):
        if np.random.rand() < pm:
            sign = np.random.randint(0, 2)
            if sign == 0:
                sign = -0.6
            else:
                sign = 0.6
            j = np.random.randint(0, 4)
            popm[i, j] = pop[i, j] + sign
            if j == 0:
                if popm[i, j] < -1:
                    popm[i, j] = -1
                if popm[i, j] > 1:
                    popm[i, j] = 1
            elif j == 1:
                if popm[i, j] < 0:
                    popm[i, j] = 0
                if popm[i, j] > 0.2:
                    popm[i, j] = 0.2
            elif j == 2:
                if popm[i, j] < 0:
                    popm[i, j] = 0
                if popm[i, j] > 1:
                    popm[i, j] = 1
            elif j == 3:
                if popm[i, j] < 0:
                    popm[i, j] = 0
                if popm[i, j] > 5:
                    popm[i, j] = 5
            popm[i, 4] = fitness(popm[i, :4])
        else:
            popm[i, :] = pop[i, :]
    return popm


def main3():
    """Main function"""
    dim = 10
    pm = 0.1
    pop = generate_population(dim)
    print(f"Populatia initiala, cu {dim} indivizi\n\n", pop)
    popm = mutation(pop, pm)
    print(f"\n\nPopulatia rezultat, cu {pm} probabilitate de mutatie, tot cu {dim} indivizi\n\n", popm)

"""4. Fie 𝑓:[−1,1] × [0,1] × [−2,1] → ℝ, 𝑓(𝑥1, 𝑥2, 𝑥3) = 1 + 𝑠𝑖𝑛(2𝑥1 − 𝑥3) + 𝑐𝑜𝑠(𝑥2) funcţia
obiectiv a unei probleme de maxim. Un genotip este un vector 𝑥 = (𝑥1, 𝑥2, 𝑥3)𝑇, 𝑥 ∈ [−1,1] × [0,1] × [−2,1]

a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
indivizii populaţiei sunt însoţiţi de funcţia merit (sunt vectori cu 4 componente).
b. Pentru o probabilitate de recombinare dată, pc, scrieţi o funcţie de recombinare utilizând
operatorul de recombinare aritmetică totală care, pe baza populaţiei pop obţine o nouă populaţie,
popc. Populaţia rezultată are tot dim indivizi (este utilizată şi recombinarea asexuată şi calitatea
fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale).
"""

import numpy as np


def fitness(x):
    """Calculează fitness-ul unui individ"""
    return 1 + np.sin(2 * x[0] - x[2]) + np.cos(x[1])


def generate_population(dim):
    """Generează o populaţie aleatoare de dim indivizi"""
    pop = np.zeros((dim, 4))
    for i in range(dim):
        pop[i][0] = np.random.uniform(-1, 1)
        pop[i][1] = np.random.uniform(0, 1)
        pop[i][2] = np.random.uniform(-2, 1)
        pop[i, 3] = fitness(pop[i, :3])
    return pop


def crossover(pop, pc, alpha=0.5):
    """Operator de recombinare aritmetică totală
    """
    dim, n = pop.shape
    popc = np.zeros((dim, n))
    for i in range(0, dim, 2):
        if np.random.rand() < pc:
            # crossover
            popc[i, :3] = alpha * pop[i, :3] + (1 - alpha) * pop[i + 1, :3]
            popc[i + 1, :3] = alpha * pop[i + 1, :3] + (1 - alpha) * pop[i, :3]
            popc[i, 3] = fitness(popc[i, :3])
            popc[i + 1, 3] = fitness(popc[i + 1, :3])
        else:
            popc[i, :] = pop[i, :]
            popc[i + 1, :] = pop[i + 1, :]
    return popc


def main4():
    dim = 10
    pc = 0.7
    alpha = 0.4
    pop = generate_population(dim)
    print(f"Populatia initiala, cu {dim} indivizi:\n", pop)
    popc = crossover(pop, pc, alpha)
    print(f"\nPopulatia finala, cu {dim} indivizi, probabilitate de recombinare de {pc} si coeficient de "
          f"recombinare {alpha}\n\n", popc)

"""5. Fie funcţia 𝑓(𝑥)=Σ𝑥𝑖7𝑖=1,𝑥=(𝑥1,…,𝑥7)∈{0,1}7 care trebuie maximizată (un genotip este un vector binar cu 7 componente).
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Pentru o probabilitate de recombinare dată, pc, scrieţi o funcţie de recombinare utilizând operatorul de încrucişare multi-punct pentru 2 puncte de încrucişare care, pe baza populaţiei pop obţine o nouă populaţie, popc. Populaţia rezultată are tot dim indivizi (este utilizată şi recombinarea asexuată şi calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale)"""

import numpy as np

def fitness(x):
    """Calculează fitness-ul unui individ"""
    return sum(x)

def generate_population(dim):
    """Generează o populaţie aleatoare de dim indivizi"""
    pop = np.zeros((dim, 8), dtype=int)
    for i in range(dim):
        pop[i, :7] = np.random.randint(0, 2, 7)
        pop[i, 7] = fitness(pop[i, :7])
    return pop

def crossover(pop, pc):
    """Operator de recombinare multi-punct"""
    dim, n = pop.shape
    popc = np.zeros((dim, n), dtype=int)
    for i in range(0, dim, 2):
        if np.random.rand() < pc:
            # crossover
            p1 = np.random.randint(1, 7)
            p2 = np.random.randint(1, 7)
            if p1 > p2:
                p1, p2 = p2, p1
            popc[i, :p1] = pop[i, :p1]
            popc[i, p1:p2] = pop[i + 1, p1:p2]
            popc[i, p2:] = pop[i, p2:]
            popc[i + 1, :p1] = pop[i + 1, :p1]
            popc[i + 1, p1:p2] = pop[i, p1:p2]
            popc[i + 1, p2:] = pop[i + 1, p2:]
            popc[i, 7] = fitness(popc[i, :7])
            popc[i + 1, 7] = fitness(popc[i + 1, :7])
        else:
            popc[i, :] = pop[i, :]
            popc[i + 1, :] = pop[i + 1, :]
    return popc

def main5():
    dim = 10
    pc = 0.7
    pop = generate_population(dim)
    print(f"Populatia initiala, cu {dim} indivizi:\n", pop)
    popc = crossover(pop, pc)
    print(f"\nPopulatia dupa recombinare cu probabilitate de {pc}, formata tot din {dim} indivizi.\n\n", popc)

"""6. Fie 𝑓:{1,2,…,350}→ℝ,𝑓(𝑥)=𝑥2 funcţia obiectiv a unei probleme de maxim. Fiecărui fenotip 𝑥∈{1,2,…,350} îi corespunde un genotip şir binar obţinut prin codificarea Gray.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
b. Pentru o probabilitate de recombinare dată, pc, scrieţi o funcţie de recombinare utilizând operatorul de încrucişare uni-punct care, pe baza populaţiei pop obţine o nouă populaţie, popc. Populaţia rezultată are tot dim indivizi (este utilizată şi recombinarea asexuată)."""

import numpy as np

def fitness(x):
    """Calculează fitness-ul unui individ"""
    return x ** 2

def binary_to_gray(x):
    """Codifică un număr binar în codul Gray"""
    x = int(x, 2)
    return bin(x ^ (x >> 1))[2:]

def generate_population(dim):
    """Generează o populaţie aleatoare de dim indivizi"""
    pop = np.zeros((dim, 10), dtype=int)
    x = np.random.randint(1, 351, dim)
    for i in range(dim):
        pop[i, :9] = np.array(list(binary_to_gray(bin(x[i])[2:]).zfill(9)))
        pop[i, 9] = fitness(x[i])
    return pop

def crossover(pop, pc):
    """Operator de recombinare uni-punct"""
    dim, n = pop.shape
    popc = np.zeros((dim, n), dtype=int)
    for i in range(0, dim, 2):
        if np.random.rand() < pc:
            p = np.random.randint(1, 9)
            popc[i, :p] = pop[i, :p]
            popc[i, p:] = pop[i + 1, p:]
            popc[i + 1, :p] = pop[i + 1, :p]
            popc[i + 1, p:] = pop[i, p:]
            popc[i, 9] = fitness(int("".join(map(str, popc[i, :9])), 2))
            popc[i + 1, 9] = fitness(int("".join(map(str, popc[i + 1, :9])), 2))
        else:
            popc[i, :] = pop[i, :]
            popc[i + 1, :] = pop[i + 1, :]
    return popc

def main6():
    """Funcţia principală"""
    dim = 10
    pc = 0.7
    pop = generate_population(dim)
    print(f"Populatia initiala, cu {dim} indivizi\n\n", pop)
    popc = crossover(pop, pc)
    print(f"\n\nPopulatia rezultat, cu {pc} probabilitate de recombinare, tot cu {dim} indivizi\n\n", popc)

"""7. Fie 𝑓:𝒫(𝑛)→ℕ 𝑝𝜖𝒫(𝑛),𝑓(𝑝)=|{(𝑖,𝑗)𝑖<𝑗,𝑝(𝑖)=𝑗 ş𝑖 𝑝(𝑗)=𝑖 ⁄}| funcţia obiectiv a unei probleme de maxim, unde 𝒫(𝑛) desemnează mulţimea permutărilor de n elemente.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Pentru o probabilitate de mutaţie dată, pm, scrieţi o funcţie de mutaţie utilizând operatorul de mutaţie prin amestec care, pe baza populaţiei pop obţine o nouă populaţie, popm. Populaţia rezultată are tot dim indivizi."""

import numpy as np


def fitness(p):
    """Calculeaza fitness-ul unei permutari p"""
    n = len(p)
    return sum([1 for i in range(n) for j in range(i + 1, n) if p[i] == j and p[j] == i])


def generate_population(dim, n):
    """Genereaza o populatie aleatoare de permutari de n elemente"""
    pop = np.zeros((dim, n + 1), dtype=int)
    for i in range(dim):
        pop[i, :n] = np.random.permutation(n)
        pop[i, n] = fitness(pop[i, :n])
    return pop


def mutation(pop, pm):
    """Operator de mutatie prin amestecare"""
    dim, n = pop.shape
    popm = np.zeros((dim, n), dtype=int)
    for i in range(dim):
        if np.random.rand() < pm:
            popm[i, :] = np.random.permutation(max(pop[i, :n]))
        else:
            popm[i, :] = pop[i, :]
    return popm


def main7():
    """Functia principala"""
    dim = 10
    n = 5
    pm = 0.1
    pop = generate_population(dim, n)
    print(f"Populatia initiala, cu {dim} indivizi, permutari de ordin {n} \n\n", pop)
    popm = mutation(pop, pm)
    print(
        f"\n\nPopulatia rezultat, cu {pm} probabilitate de mutatie, tot cu {dim} indivizi, permutari de ordin {n}\n\n",
        popm)

"""7. Fie 𝑓:𝒫(𝑛)→ℕ 𝑝𝜖𝒫(𝑛),𝑓(𝑝)=|{(𝑖,𝑗)𝑖<𝑗,𝑝(𝑖)=𝑗 ş𝑖 𝑝(𝑗)=𝑖 ⁄}| funcţia obiectiv a unei probleme de maxim, unde 𝒫(𝑛) desemnează mulţimea permutărilor de n elemente.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Pentru o probabilitate de mutaţie dată, pm, scrieţi o funcţie de mutaţie utilizând operatorul de mutaţie prin amestec care, pe baza populaţiei pop obţine o nouă populaţie, popm. Populaţia rezultată are tot dim indivizi."""

import numpy as np


def fitness(p):
    """Calculeaza fitness-ul unei permutari p"""
    n = len(p)
    return sum([1 for i in range(n) for j in range(i + 1, n) if p[i] == j and p[j] == i])


def generate_population(dim, n):
    """Genereaza o populatie aleatoare de permutari de n elemente"""
    pop = np.zeros((dim, n + 1), dtype=int)
    for i in range(dim):
        pop[i, :n] = np.random.permutation(n)
        pop[i, n] = fitness(pop[i, :n])
    return pop


def mutation(pop, pm):
    """Operator de mutatie prin amestecare"""
    dim, n = pop.shape
    popm = np.zeros((dim, n), dtype=int)
    for i in range(dim):
        if np.random.rand() < pm:
            popm[i, :] = np.random.permutation(max(pop[i, :n]))
        else:
            popm[i, :] = pop[i, :]
    return popm


def main():
    """Functia principala"""
    dim = 10
    n = 5
    pm = 0.1
    pop = generate_population(dim, n)
    print(f"Populatia initiala, cu {dim} indivizi, permutari de ordin {n} \n\n", pop)
    popm = mutation(pop, pm)
    print(
        f"\n\nPopulatia rezultat, cu {pm} probabilitate de mutatie, tot cu {dim} indivizi, permutari de ordin {n}\n\n",
        popm)

"""8. Fie 𝑓:𝒫(𝑛)→ℕ funcţia obiectiv definită pentru problema celor n regine astfel: 𝑝𝜖𝒫(𝑛),𝑓(𝑝)=𝑛×𝑛−12−|{(𝑖,𝑗)𝑖<𝑗,|𝑝(𝑖)−𝑝(𝑗)|=|𝑖−𝑗|⁄}|, unde 𝒫(𝑛) desemnează mulţimea permutărilor de n elemente.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Aplicaţi funcţia de generare implementată mai sus pentru obţinerea a două populaţii, pop1, pop2 cu câte dim indivizi. Scrieţi o funcţie Python care obţine o nouă populaţie prin aplicarea unei proceduri de tip elitist celor două populaţii, unde pop2 este considerată populaţia progeniturilor lui pop1. Populaţia rezultată are tot dim indivizi."""

import numpy as np

def fitness(p):
    """Calculeaza calitatea unei permutari p"""
    n = len(p)
    return n*(n-1)/2 - sum([abs(i-j) for i in range(n) for j in range(i+1, n) if abs(p[i]-p[j]) == abs(i-j)])

def generate_population(dim, n):
    """Genereaza o populatie aleatoare de permutari de n elemente"""
    pop = np.zeros((dim, n+1), dtype=int)
    for i in range(dim):
        pop[i, :n] = np.random.permutation(n)
        pop[i, n] = fitness(pop[i, :n])
    return pop

def elitist(pop1, pop2):
    """Procedura elitista"""
    dim, n = pop1.shape
    pop = np.zeros((dim, n), dtype=int)
    for i in range(dim):
        if pop1[i, n-1] > pop2[i, n-1]:
            pop[i, :] = pop1[i, :]
        else:
            pop[i, :] = pop2[i, :]
    return pop

def main8():
    """Functia principala"""
    dim = 10
    n = 5
    pop1 = generate_population(dim, n)
    print(f"Populatia initiala 1, cu {dim} indivizi, permutari de ordin {n} \n\n", pop1)
    pop2 = generate_population(dim, n)
    print(f"\n\nPopulatia initiala 1, cu {dim} indivizi, permutari de ordin {n} \n\n", pop2)
    pop = elitist(pop1, pop2)
    print(f"\n\nPopulatia rezultat, cu {dim} indivizi, permutari de ordin {n}\n\n", pop)

"""9. Fie 𝑓:{1,2,…,2500}→ℝ,𝑓(𝑥)=(𝑠𝑖𝑛(𝑥−2))2 funcţia obiectiv a unei probleme de maxim. Fiecărui fenotip 𝑥∈{1,2,…,2500} îi corespunde un genotip şir binar obţinut prin reprezentarea standard în bază 2 a lui x.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Scrieţi o funcţie Python care, pentru populaţia generată pop obţine o populaţie de părinţi prin aplicarea selecţiei de tip ruletă cu distribuţia de probabilitate FPS cu sigma-scalare."""

import numpy as np


def fitness(x):
    """Calculeaza fitness-ul unui individ x"""
    return np.sin(x - 2) ** 2


def generate_population(dim):
    """Generează o populaţie aleatoare de dim indivizi"""
    pop = np.zeros((dim, 13), dtype=float)
    for i in range(dim):
        pop[i, :12] = np.random.randint(0, 2, 12)
        integer = int("".join(map(str, pop[i, :12])).replace('.', ''), 2)
        pop[i, 12] = fitness(integer)
    return pop


def fps(qual):
    """Calculează probabilitatea de selecţie a unui individ, în funcţie de calitatea sa, fara sigma-scalare"""
    fps = np.zeros(len(qual))
    suma = np.sum(qual)
    for i in range(len(qual)):
        fps[i] = qual[i] / suma
    qfps = fps.copy()
    for i in range(1, len(qual)):
        qfps[i] = qfps[i - 1] + fps[i]
    return qfps


def sigmafps(qual):
    """Calculează probabilitatea de selecţie a unui individ, în funcţie de calitatea sa, cu sigma-scalare"""
    medie = np.mean(qual)
    deviatie = np.std(qual)
    new_qual = [max(0, qual[i] - medie + 2 * deviatie) for i in range(len(qual))]
    if np.sum(new_qual) == 0:
        return fps(qual)
    return fps(new_qual)


def roulette(pop):
    """Aplică selecţia de tip ruletă cu distribuţia de probabilitate FPS cu sigma-scalare"""
    pop_initiala = np.asarray(pop)
    parinti = pop_initiala.copy()
    fitnessuri = pop_initiala[:, parinti.shape[1] - 1]
    qfps = sigmafps(fitnessuri)
    for i in range(len(pop_initiala)):
        r = np.random.uniform(0, 1)
        pozitie = np.where(qfps >= r)[0][0]
        parinti[i, :] = pop_initiala[pozitie, :]
        parinti[i, parinti.shape[1] - 1] = fitness(int("".join(map(str, parinti[i, :12])).replace('.', ''), 2))
    return parinti


def main9():
    """Funcţia principală"""
    dim = 10
    pop = generate_population(dim)
    print(f"Populatia initiala, cu {dim} indivizi\n\n", pop)
    popp = roulette(pop)
    print(f"\n\nPopulatia rezultat, cu {dim} indivizi\n\n", popp)

"""S1. Fie f:P(n)→N, pϵP(n),f(p)=∑_(i=1)^p▒〖p_i*〖câștig〗_i 〗 funcţia obiectiv a unei probleme de maxim, unde P(n) desemnează mulţimea permutărilor de n elemente și câștig este un vector de intrare, cu n elemente, în care fiecare valoare arată câștigul unei alegeri .  
	Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată într-un vector calitate;
	Pentru o probabilitate de mutaţie dată, pm,  scrieţi o funcţie de mutaţie utilizând operatorul de mutaţie prin inversiune care, pe baza populaţiei pop obţine o nouă populaţie, popm. Populaţia rezultată are tot dim indivizi."""
import numpy as np

def fitness(p,castig):
    return np.dot(p,castig)

def cerinta_a(dim,castig):
    n=castig.size
    populatie=np.zeros([dim,n],dtype="int")
    calitati=np.zeros(dim)
    for i in range(dim):
        populatie[i]=np.random.permutation(n)
        calitati[i]=fitness(populatie[i],castig)
    return populatie, calitati

def inversiune(p):
    n=len(p)
    i=np.random.randint(0,n-1)
    j=np.random.randint(i+1,n)
    r=p.copy()
    r[i:j+1]=[p[k] for k in range(j,i-1,-1)]
    return r

def cerinta_b(populatie,calitati,pm,castig):
    dim=populatie.shape[0]
    populatie_m=populatie.copy()
    calitati_m=calitati.copy()
    for i in range(dim):
        r=np.random.uniform(0,1)
        if r<=pm:
            print('Mutatie in ',populatie[i], ' calitatea ',calitati[i])
            populatie_m[i]=inversiune(populatie[i])
            calitati_m[i]=fitness(populatie_m[i],castig)
            print('Rezulta    ',populatie_m[i], ' calitatea ',calitati_m[i])

    return populatie_m, calitati_m

if __name__=="__main__":
    castig=np.genfromtxt("castig.txt")
    dim=20
    pm=0.2
    populatie,calitati=cerinta_a(dim,castig)
    print(populatie, calitati)
    populatie_m,calitati_m=cerinta_b(populatie,calitati,pm,castig)

"""S2. Fie f:{1,2,…,1500}×{-1,0,,…,2500}×{10,11,…,250}×{10,11,…,250}→R,f(x,y,z,t)=〖y*(sin(x-2))〗^2+z+t funcţia obiectiv a unei probleme de maxim. Un candidat la soluție (genotip) este un vector (x,y,z,t)∈{1,2,…,1500}×{-1,0,,…,2500}×{10,11,…,250}×{10,11,…,250}.
	Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
	Pentru o probabilitate de recombinare dată, pc,  scrieţi o funcţie de recombinare utilizând operatorul de încrucişare uniform care, pe baza populaţiei pop obţine o nouă populaţie, popc. Populaţia rezultată are tot dim indivizi (este utilizată şi recombinarea asexuată şi calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale).
"""
import numpy as np


#functia fitness

def fitness(x):
    return x[1]*(np.sin(x[0]-2)**2)+x[2]+x[3]


def cerinta_a(dim):
    populatie=np.zeros([dim,5])
    print("POPULATIA INITIALA")
    for i in range(dim):
        populatie[i,:4]=np.random.randint([1, -1, 10,10], [1500, 2500, 250,250], 4)
        populatie[i,4]=fitness(populatie[i,:4])
        print(populatie[i])
    return populatie


def recombinare_unif(x,y):
    copil1=x.copy()
    copil2=y.copy()
    prob=np.random.uniform(0,1,4)
    for i in range(4):
        if prob[i]>0.5:
            copil1[i],copil2[i]=y[i],x[i]
    return copil1, copil2


def cerinta_b(populatie,pc):
    print("\n\nPOPULATIA DE COPII")
    dim=len(populatie)
    copii=populatie.copy()
    for i in range(0,dim-1,2):
        r=np.random.uniform(0,1)
        if r<=pc:
            #selectarea indivizilor, fara calitatile lor
            p1=populatie[i][:4].copy()
            p2=populatie[i+1][:4].copy()
            c1,c2=recombinare_unif(p1,p2)
            copii[i][:4]=c1
            copii[i][4]=fitness(c1)
            copii[i+1][:4] = c2
            copii[i+1][4] = fitness(c2)
        print(copii[i])
        print(copii[i+1])
    return copii

if __name__=="__main__":
    p=cerinta_a(10)
    c=cerinta_b(p,0.8)

"""S3. Fie funcţia f(x)=∑_(i=1)^17▒x_i ,x=(x_1,…,x_17 )∈{0,1}^17, x cu număr par de biți 1, care trebuie maximizată (un genotip este un0020vector binar cu 17 componente și număr par de biți).
	Scrieţi o funcţie Python  pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
	Scrieţi o funcţie Python care, pentru populaţia generată pop obţine o populaţie de părinţi prin aplicarea selecţiei de tip turneu cu k indivizi (k parametru de intrare).
"""
import numpy as np

def fitness(x):
    return sum(x), sum(x)%2==0

def cerinta_a(dim):
    populatie=np.zeros([dim,18])
    i=0
    while i<dim:
        populatie[i, :17]=np.random.randint(0,2,17)
        populatie[i,17],ok=fitness(populatie[i,:17])
        if ok:
            i+=1
    return populatie


def cerinta_b(populatie,k):
    dim=populatie.shape[0]
    populatie_p=populatie.copy()
    for i in range(dim):
        poz=np.random.randint(0,dim,k)
        #print(poz+1)
        ales=np.argmax(np.array([populatie[poz[j],17] for j in range(k)]))
        #print(populatie[poz[ales],17])
        # linia in care este calculat ales este echivalenta cu
        # ales=0
        # maxim=populatie[poz[0],17]
        # for j in range(1,k):
        #     if maxim<populatie[poz[j],17]:
        #         maxim=populatie[poz[j],17]
        #         ales=j
        populatie_p[i,:17]=populatie[poz[ales],:17].copy()
        populatie_p[i,17]=populatie[poz[ales],17]
    return populatie_p

if __name__=="__main__":
    dim=10
    populatie=cerinta_a(dim)
    print(populatie)
    populatie_p=cerinta_b(populatie,k=3)
    print(populatie_p)


import numpy as np

"""BIBLIOTECA FUNCTII MUTATIE"""


#ATENTIE! TOATE EVALUARILE INDIVIZILOR REZULTATI VOR FI REALIZATE DE APELATOR


# VECTORI BINARI
# mutatia bitflip

#I: x - valoarea care se modifica
#E: y - rezultatul mutatiei
def m_binar(x):
    y=not x
    return int(y)


#VECTORI NUMERE INTREGI
#resetare aleatoare

#I:a,b - resetarea se face pe multimea a, a+1,...,b-1
#E: y - noua valoare
def m_ra(a,b):
    y=np.random.randint(a,b)
    return y

#mutatia fluaj

#I: x - valoarea de modificat
#   a,b - limitele in care trebuie sa rezulte iesirea y, varianta a lui x modificata cu o unitate
#E:y - ca mai sus
def m_fluaj(x,a,b):
    #generare +1 sau -1
    p=np.random.randint(0,2)
    if p==0:
        sign=-1
    else:
        sign=1
    y=x+sign
    if y>b:
        y=b
    if y<a:
        y=a
    return y

#VECTORI NUMERE REALE
#mutatia uniforma

#I:a,b - intervalul in care se face resetarea
#E: y - noua valoare
def m_uniforma(a,b):
    y=np.random.uniform(a,b)
    return y

#mutatia neuniforma

#I: x - valoarea de modificat
#   sigma - pasul de fluaj
#   a,b - limitele in care trebuie sa rezulte iesirea y
#E:y - ca mai sus
def m_neuniforma(x,sigma,a,b):
    #generare zgomot
    p=np.random.normal(0,sigma)
    y=x+p
    if y>b:
        y=b
    if y<a:
        y=a
    return y


#PERMUTARI
# mutatia prin inversiune a permutarii x cu n componete

# I:x,n
# E:y - permutarea rezultat
def m_perm_inversiune(x,n):
    # generarea pozitiilor pentru inversiune
    poz = np.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = np.random.randint(0, n, 2)
    p1 = np.min(poz)
    p2 = np.max(poz)
    y=x.copy()
    y[p1:p2+1]=[x[i] for i in range(p2,p1-1,-1)]
    return y


# mutatia prin interschimbare a permutarii x cu n componete

# I:x,n
# E:y - permutarea rezultat
def m_perm_interschimbare(x,n):
    # generarea pozitiilor pentru inversiune
    poz = np.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = np.random.randint(0, n, 2)
    p1 = np.min(poz)
    p2 = np.max(poz)
    y=x.copy()
    y[p1]=x[p2]
    y[p2]=x[p1]
    return y


# mutatia prin inserare a permutarii x cu n componete
# I:x,n
# E:y - permutarea rezultat
def m_perm_inserare(x,n):
    # generarea pozitiilor pentru inversiune
    poz = np.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = np.random.randint(0, n, 2)
    p1 = np.min(poz)
    p2 = np.max(poz)
    y=x.copy()
    y[p1+1]=x[p2]
    if p1<n-2:
        y[p1+2:n]=np.array([x[i] for i in range(p1+1,n) if i != p2])
    return y

import numpy as np

"""CROSSOVER RECOMBINARI"""

# CROSSOVER VECTORI BINARI SAU INT

# crossover unipunct intre x si y, vectori cu n componente
# I :x,y,n ca mai sus
#E: c1,c2 - cei doi copii - cu n componente
def crossover_unipunct(x,y,n):
    #genereaza aleator punctul de crossover, intre 1 si n-1 pentru a avea efect
    # in pozitia n este calitata
    i = np.random.randint(1,n-1)
    c1=x.copy()
    c2=y.copy()
    # selectarea secventelor care compun primul copil
    c1[0:i] = x[0:i]
    c1[i:n] = y[i:n]
    # selectarea secventelor care compun cel de-al doilea copil
    c2[0:i] = y[0:i]
    c2[i:n] = x[i:n]
    return c1,c2


# crossover uniform intre x si y, vectori cu n componente
# I :x,y,n ca mai sus
#E: c1,c2 - cei doi copii
def crossover_uniform(x,y,n):
    #initializeaza copiii cu valorile parintilor
    c1=x.copy()
    c2=y.copy()
    #constructia copiilor
    for i in range(n):
        r = np.random.randint(0,2)
        # daca r==1 interschimba alelele din i
        if r == 1:
            c1[i] = y[i]
            c2[i] = x[i]
    return c1,c2



# CROSSOVER PERMUTARI - o permutare de dim n este cu elementele 0,1,...,n-1
#operatorul PMX
#I: permutarile x,y de dimensiune n
#E: copiii rezultati c1,c2
def crossover_PMX(x,y,n):
    #generarea secventei de crossover
    poz=np.random.randint(0,n,2)
    while poz[0]==poz[1]:
        poz=np.random.randint(0,n,2)
    p1=np.min(poz)
    p2=np.max(poz)
    c1=PMX(x,y,n,p1,p2)
    c2=PMX(y,x,n,p1,p2)
    return c1,c2

#aplica PMX pe x,y de dimensiune n, cu secventa de recombinare (p1,p2)
def PMX(x,y,n,p1,p2):
    #initializare copil - un vector cu toate elementele -1 - valori care s=sa nu fie in 0,...,n-1
    c=-np.ones(n,dtype=int)
    #copiaza secventa comuna in copilul c
    c[p1:p2+1]=x[p1:p2+1]
    # analiza secventei comune - in permutarea y
    for i in range(p1,p2+1):
        # plasarea alelei a
        a=y[i]
        if a not in c:
            curent=i
            plasat=False
            while not plasat :
                b=x[curent]
                # poz=pozitia in care se afla b in y
                [poz]=[j for j in range(n) if y[j]==b]
                if c[poz]==-1 :
                    c[poz]=a
                    plasat=True
                else:
                    curent=poz
    # z= vectorul alelelor din y inca necopiate in c
    z=[y[i] for i in range(n) if y[i] not in c]
    # poz - vectorul pozitiilor libere in c - cele cu vaori -1
    poz=[i for i in range(n) if c[i]==-1]
    #copierea alelelor inca necopiate din y in c
    m=len(poz)
    for i in range(m):
        c[poz[i]]=z[i]
    return c


#operatorul OCX
#I: permutarile x,y de dimensiune n
#E: copiii rezultati c1,c2
def crossover_OCX(x,y,n):
    #generarea secventei de crossover
    poz=np.random.randint(0,n,2)
    while poz[0]==poz[1]:
        poz=np.random.randint(0,n,2)
    p1=np.min(poz)
    p2=np.max(poz)
    c1=OCX(x,y,n,p1,p2)
    c2=OCX(y,x,n,p1,p2)
    return c1,c2

#aplica OCX pe x,y de dimensiune n, cu secventa de recombinare (p1,p2)
def OCX(x,y,n,p1,p2):
    #copiaza secventa comuna in c2
    c2=[x[i] for i in range(p1,p2+1)]
    #calculeaza z pe baza lui y:componentele incepand cu p2 pana la n si apoi de la 0 la p2-1, excluzand elementele care au fost deja copiate
    z1=[y[i] for i in range(p2,n) if y[i] not in c2]
    z2=[y[i] for i in range(p2) if y[i] not in c2]
    z=np.append(z1,z2)
    #calculeza secventa finala a individului rezultat  - din z de la 0 la n-p2
    c3=[z[i] for i in range(n-p2-1)]
    #calculeaza secventa de inceput a individului rezultat - din z de la n-p2...len(z)
    c1=[z[i] for i in range(n-p2-1,len(z))]
    #calculeaza copilul c
    c=np.append(c1,c2)
    c=np.append(c,c3)
    return c

#operatorul CX
#I: permutarile x,y de dimensiune n - completate cu fitnessul
#E: copiii rezultati c1,c2
def crossover_CX(x,y,n):
    ciclu=cicluri(x,y,n)
    c1=x.copy()
    c2=y.copy()
    for i in range(n):
        cat, rest = np.divmod(ciclu[i], 2)
        #sunt interschimbate alelele din ciclurile pare
        #primul ciclu este etichetat cu 1
        if not rest:
            c1[i]=y[i]
            c2[i]=x[i]
    return c1,c2

#calculul ciclurilor din
#I: x,y de dimensiune n
#in
#E: vectorul ciclu, unde ciclu[i]=nr. ciclului din care fac parte x[i] si y[i]
def cicluri(x,y,n):
    #numarul ciclului
    index=1
    ciclu=np.zeros(n)
    gata=0
    while not gata:
        p=np.where(ciclu==0)
        #daca exista gena inca neasignata unui ciclu
        if np.size(p):
            i=p[0][0]
            a=x[i]
            ciclu[i]=index
            b=y[i]
            while b!=a:
                r=np.where(x==b)
                j=r[0][0]
                ciclu[j]=index
                b=y[j]
            index+=1
        else:
            gata=1
    return ciclu


#EDGE CROSSOVER

#construieste tabela muchiilor pentru permutarile x si y de dimensiune n
def constr_tabel(x,y,n):
    #creaza o lista cu n elemente, toate 0
    muchii=[0]*n
    #pentru usurinta, bordeaza x cu ultimul/primul element
    x1=np.zeros(n+2, dtype='int')
    x1[1:n+1]=x[:]
    x1[0]=x[n-1]
    x1[n+1]=x[0]
    y1 = np.zeros(n + 2, dtype='int')
    y1[1:n + 1] = y[:]
    y1[0] = y[n - 1]
    y1[n + 1] = y[0]
    for i in range(1,n+1):
        a=x1[i]
        r=np.where(y==a)
        j=r[0][0]+1
        #gaseste vecinii lui a in x si y utilizand x1 si y1 si memoreaza ca multimi pentru - si intersectie
        vx={x1[i-1],x1[i+1]}
        vy={y1[j-1],y1[j+1]}
        dx=vx-vy
        dy=vy-vx
        cxy=vx & vy
        #trecem de la set la list
        lcxy=list(cxy)
        dx=list(dx)
        dy=list(dy)
        #lucram cu tip str
        for j in range(len(lcxy)):
            lcxy[j]=str(lcxy[j])+'+'
        for j in range(len(dx)):
            dx[j]=str(dx[j])
        for j in range(len(dy)):
            dy[j]=str(dy[j])
        muchii[a]=lcxy+list(dx)+list(dy)
    return muchii

# sterge un element dintr-o lista - cu chei unice, daca apare in lista
# altfel, lasa lista nemodficata
def sterge(x,a):
    #cauta aparitia - poate fi doar una
    p=[i for i in range(len(x)) if x[i]==a]
    if len(p):
        del(x[p[0]])
    return x

#alege alela de plasat, daca lp are mai mult de o valoare
def alege(lp,muchii,n):
    dim=len(lp)
    #cauta daca exista in lista muchiilor 'lp[k]+'
    #calculeaza lungimile listelor, in caz ca nu gaseste 'lp[k]'
    lliste=np.zeros(dim)
    gata=0
    k=0
    while k<dim and not gata:
        a=str(lp[k])+'+'
        i=0
        while i<n and not gata :
            l=muchii[i]
            p=[j for j in range(len(l)) if l[j]==a]
            if len(p):
                gata=1
                alela=lp[k]
            else:
                p=[j for j in range(len(l)) if l[j]==str(lp[k])]
                i=i+1
                lliste[k]=len(l)
        if not gata:
            k=k+1
    if not gata:
        #calculeaza lungimea minima si pentru ce alele se atinge
        x=[j for j in range(dim) if lliste[j]==min(lliste)]
        #alege prima alela de lungime minima
        #daca sunt mai multe, alege-o pe prima
        alela=lp[x[0]]
    return alela

# operatorul ECX - Edge crossover
def ECX(x,y,n):
    muchii=constr_tabel(x,y,n)
    #permutarea rezultata
    z=np.zeros(n, dtype='int')
    #alege initial prima alela - varianta:selecteaza aleator ap in 0...n-1
    #lp - lista alelelor posibile
    #ales - vectorul flag al alelelor alese
    ales=np.zeros(n)
    lp=[x[0]]
    for i in range(n):
        print(muchii)
        if len(lp)==0:
            #alege aleator o alela
            a=np.random.randint(n)
            while ales[a]:
                a = np.random.randint(n)
        else:
            if len(lp)>1:
                a=alege(lp,muchii,n)
            else:
                a=lp[0]
        #atribuie alela aleasa
        z[i]=a
        ales[a]=1
        print(a)
        #sterge alela din tabela de muchii
        for k in range(n):
            sterge(muchii[k],str(a))
            sterge(muchii[k],str(a)+'+')
        #alege lista posibilitatilor la urmatorul moment
        lp=[int(muchii[a][i][0]) for i in range(len(muchii[a]))]
    return z

#APEL ECX
#import numpy as np
#import FunctiiCrossoverIndivizi as c
#n=10
#x=np.random.permutation(n)
#y=np.random.permutation(n)
#z=c.ECX(y,x,10)


# CROSSOVER VECTORI NUMERE REALE

# crossover singular intre x si y, vectori cu n componente de tipul ndarray
# I :x,y,n ca mai sus
#    alpha - ponderea la mediere
#E: c1,c2 - cei doi copii - fara evaluare
def crossover_singular (x, y, n,alpha):
    #genereaza aleator gena in care este facuta recombinarea
    i = np.random.randint(0,n)
    c1 = x.copy()
    c2 = y.copy()
    c1[i]=(alpha*x[i]+(1-alpha)*y[i])
    c2[i] = (alpha * y[i] + (1 - alpha) * x[i])
    return c1, c2


# crossover simplu intre x si y, vectori cu n componente - de tipul ndarray
# I :x,y,n ca mai sus
#    alpha - ponderea la mediere
#E: c1,c2 - cei doi copii
def crossover_simplu (x, y, n,alpha):
    #genereaza aleator gena incepand cu care este facuta recombinarea
    i = np.random.randint(0,n)
    c1 = x.copy()
    c2 = y.copy()
    for j in range(i,n):
        c1[j]=(alpha*x[j]+(1-alpha)*y[j])
        c2[j] = (alpha * y[j] + (1 - alpha) * x[j])
    return c1, c2

# crossover total intre x si y, vectori cu n componente
# I :x,y,n ca mai sus
#    alpha - ponderea la mediere
#E: c1,c2 - cei doi copii - fara evaluare
def crossover_total (x, y, n,alpha):
    c1 = x.copy()
    c2 = y.copy()
    for j in range(n):
        c1[j]=(alpha*x[j]+(1-alpha)*y[j])
        c2[j] = (alpha * y[j] + (1 - alpha) * x[j])
    return c1, c2

import numpy as np

## BIBLIOTECA FUNCTII MUTATIE

#ATENTIE! TOATE EVALUARILE INDIVIZILOR REZULTATI VOR FI REALIZATE DE APELATOR

# VECTORI BINARI
# mutatia bitflip

#I: x - valoarea care se modifica
#E: y - rezultatul mutatiei
def m_binar(x):
    y=not x
    return int(y)


#VECTORI NUMERE INTREGI
#resetare aleatoare

#I:a,b - resetarea se face pe multimea a, a+1,...,b-1
#E: y - noua valoare
def m_ra(a,b):
    y=np.random.randint(a,b)
    return y

#mutatia fluaj

#I: x - valoarea de modificat
#   a,b - limitele in care trebuie sa rezulte iesirea y, varianta a lui x modificata cu o unitate
#E:y - ca mai sus
def m_fluaj(x,a,b):
    #generare +1 sau -1
    p=np.random.randint(0,2)
    if p==0:
        sign=-1
    else:
        sign=1
    y=x+sign
    if y>b:
        y=b
    if y<a:
        y=a
    return y

#VECTORI NUMERE REALE
#mutatia uniforma

#I:a,b - intervalul in care se face resetarea
#E: y - noua valoare
def m_uniforma(a,b):
    y=np.random.uniform(a,b)
    return y

#mutatia neuniforma

#I: x - valoarea de modificat
#   sigma - pasul de fluaj
#   a,b - limitele in care trebuie sa rezulte iesirea y
#E:y - ca mai sus
def m_neuniforma(x,sigma,a,b):
    #generare zgomot
    p=np.random.normal(0,sigma)
    y=x+p
    if y>b:
        y=b
    if y<a:
        y=a
    return y


#PERMUTARI
# mutatia prin inversiune a permutarii x cu n componete

# I:x,n
# E:y - permutarea rezultat
def m_perm_inversiune(x,n):
    # generarea pozitiilor pentru inversiune
    poz = np.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = np.random.randint(0, n, 2)
    p1 = np.min(poz)
    p2 = np.max(poz)
    y=x.copy()
    y[p1:p2+1]=[x[i] for i in range(p2,p1-1,-1)]
    return y


# mutatia prin interschimbare a permutarii x cu n componete

# I:x,n
# E:y - permutarea rezultat
def m_perm_interschimbare(x,n):
    # generarea pozitiilor pentru inversiune
    poz = np.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = np.random.randint(0, n, 2)
    p1 = np.min(poz)
    p2 = np.max(poz)
    y=x.copy()
    y[p1]=x[p2]
    y[p2]=x[p1]
    return y


# mutatia prin inserare a permutarii x cu n componete
# I:x,n
# E:y - permutarea rezultat
def m_perm_inserare(x,n):
    # generarea pozitiilor pentru inversiune
    poz = np.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = np.random.randint(0, n, 2)
    p1 = np.min(poz)
    p2 = np.max(poz)
    y=x.copy()
    y[p1+1]=x[p2]
    if p1<n-2:
        y[p1+2:n]=np.array([x[i] for i in range(p1+1,n) if i != p2])
    return y

import numpy as np



# CROSSOVER VECTORI BINARI SAU INT

# crossover unipunct intre x si y, vectori cu n componente
# I :x,y,n ca mai sus
#E: c1,c2 - cei doi copii - cu n componente
def crossover_unipunct(x,y,n):
    #genereaza aleator punctul de crossover, intre 1 si n-1 pentru a avea efect
    # in pozitia n este calitata
    i = np.random.randint(1,n-1)
    c1=x.copy()
    c2=y.copy()
    # selectarea secventelor care compun primul copil
    c1[0:i] = x[0:i]
    c1[i:n] = y[i:n]
    # selectarea secventelor care compun cel de-al doilea copil
    c2[0:i] = y[0:i]
    c2[i:n] = x[i:n]
    return c1,c2


# crossover uniform intre x si y, vectori cu n componente
# I :x,y,n ca mai sus
#E: c1,c2 - cei doi copii
def crossover_uniform(x,y,n):
    #initializeaza copiii cu valorile parintilor
    c1=x.copy()
    c2=y.copy()
    #constructia copiilor
    for i in range(n):
        r = np.random.randint(0,2)
        # daca r==1 interschimba alelele din i
        if r == 1:
            c1[i] = y[i]
            c2[i] = x[i]
    return c1,c2



# CROSSOVER PERMUTARI - o permutare de dim n este cu elementele 0,1,...,n-1
#operatorul PMX
#I: permutarile x,y de dimensiune n
#E: copiii rezultati c1,c2
def crossover_PMX(x,y,n):
    #generarea secventei de crossover
    poz=np.random.randint(0,n,2)
    while poz[0]==poz[1]:
        poz=np.random.randint(0,n,2)
    p1=np.min(poz)
    p2=np.max(poz)
    c1=PMX(x,y,n,p1,p2)
    c2=PMX(y,x,n,p1,p2)
    return c1,c2

#aplica PMX pe x,y de dimensiune n, cu secventa de recombinare (p1,p2)
def PMX(x,y,n,p1,p2):
    #initializare copil - un vector cu toate elementele -1 - valori care s=sa nu fie in 0,...,n-1
    c=-np.ones(n,dtype=int)
    #copiaza secventa comuna in copilul c
    c[p1:p2+1]=x[p1:p2+1]
    # analiza secventei comune - in permutarea y
    for i in range(p1,p2+1):
        # plasarea alelei a
        a=y[i]
        if a not in c:
            curent=i
            plasat=False
            while not plasat :
                b=x[curent]
                # poz=pozitia in care se afla b in y
                [poz]=[j for j in range(n) if y[j]==b]
                if c[poz]==-1 :
                    c[poz]=a
                    plasat=True
                else:
                    curent=poz
    # z= vectorul alelelor din y inca necopiate in c
    z=[y[i] for i in range(n) if y[i] not in c]
    # poz - vectorul pozitiilor libere in c - cele cu vaori -1
    poz=[i for i in range(n) if c[i]==-1]
    #copierea alelelor inca necopiate din y in c
    m=len(poz)
    for i in range(m):
        c[poz[i]]=z[i]
    return c


#operatorul OCX
#I: permutarile x,y de dimensiune n
#E: copiii rezultati c1,c2
def crossover_OCX(x,y,n):
    #generarea secventei de crossover
    poz=np.random.randint(0,n,2)
    while poz[0]==poz[1]:
        poz=np.random.randint(0,n,2)
    p1=np.min(poz)
    p2=np.max(poz)
    c1=OCX(x,y,n,p1,p2)
    c2=OCX(y,x,n,p1,p2)
    return c1,c2

#aplica OCX pe x,y de dimensiune n, cu secventa de recombinare (p1,p2)
def OCX(x,y,n,p1,p2):
    #copiaza secventa comuna in c2
    c2=[x[i] for i in range(p1,p2+1)]
    #calculeaza z pe baza lui y:componentele incepand cu p2 pana la n si apoi de la 0 la p2-1, excluzand elementele care au fost deja copiate
    z1=[y[i] for i in range(p2,n) if y[i] not in c2]
    z2=[y[i] for i in range(p2) if y[i] not in c2]
    z=np.append(z1,z2)
    #calculeza secventa finala a individului rezultat  - din z de la 0 la n-p2
    c3=[z[i] for i in range(n-p2-1)]
    #calculeaza secventa de inceput a individului rezultat - din z de la n-p2...len(z)
    c1=[z[i] for i in range(n-p2-1,len(z))]
    #calculeaza copilul c
    c=np.append(c1,c2)
    c=np.append(c,c3)
    return c

#operatorul CX
#I: permutarile x,y de dimensiune n - completate cu fitnessul
#E: copiii rezultati c1,c2
def crossover_CX(x,y,n):
    ciclu=cicluri(x,y,n)
    c1=x.copy()
    c2=y.copy()
    for i in range(n):
        cat, rest = np.divmod(ciclu[i], 2)
        #sunt interschimbate alelele din ciclurile pare
        #primul ciclu este etichetat cu 1
        if not rest:
            c1[i]=y[i]
            c2[i]=x[i]
    return c1,c2

#calculul ciclurilor din
#I: x,y de dimensiune n
#in
#E: vectorul ciclu, unde ciclu[i]=nr. ciclului din care fac parte x[i] si y[i]
def cicluri(x,y,n):
    #numarul ciclului
    index=1
    ciclu=np.zeros(n)
    gata=0
    while not gata:
        p=np.where(ciclu==0)
        #daca exista gena inca neasignata unui ciclu
        if np.size(p):
            i=p[0][0]
            a=x[i]
            ciclu[i]=index
            b=y[i]
            while b!=a:
                r=np.where(x==b)
                j=r[0][0]
                ciclu[j]=index
                b=y[j]
            index+=1
        else:
            gata=1
    return ciclu


#EDGE CROSSOVER

#construieste tabela muchiilor pentru permutarile x si y de dimensiune n
def constr_tabel(x,y,n):
    #creaza o lista cu n elemente, toate 0
    muchii=[0]*n
    #pentru usurinta, bordeaza x cu ultimul/primul element
    x1=np.zeros(n+2, dtype='int')
    x1[1:n+1]=x[:]
    x1[0]=x[n-1]
    x1[n+1]=x[0]
    y1 = np.zeros(n + 2, dtype='int')
    y1[1:n + 1] = y[:]
    y1[0] = y[n - 1]
    y1[n + 1] = y[0]
    for i in range(1,n+1):
        a=x1[i]
        r=np.where(y==a)
        j=r[0][0]+1
        #gaseste vecinii lui a in x si y utilizand x1 si y1 si memoreaza ca multimi pentru - si intersectie
        vx={x1[i-1],x1[i+1]}
        vy={y1[j-1],y1[j+1]}
        dx=vx-vy
        dy=vy-vx
        cxy=vx & vy
        #trecem de la set la list
        lcxy=list(cxy)
        dx=list(dx)
        dy=list(dy)
        #lucram cu tip str
        for j in range(len(lcxy)):
            lcxy[j]=str(lcxy[j])+'+'
        for j in range(len(dx)):
            dx[j]=str(dx[j])
        for j in range(len(dy)):
            dy[j]=str(dy[j])
        muchii[a]=lcxy+list(dx)+list(dy)
    return muchii

# sterge un element dintr-o lista - cu chei unice, daca apare in lista
# altfel, lasa lista nemodficata
def sterge(x,a):
    #cauta aparitia - poate fi doar una
    p=[i for i in range(len(x)) if x[i]==a]
    if len(p):
        del(x[p[0]])
    return x

#alege alela de plasat, daca lp are mai mult de o valoare
def alege(lp,muchii,n):
    dim=len(lp)
    #cauta daca exista in lista muchiilor 'lp[k]+'
    #calculeaza lungimile listelor, in caz ca nu gaseste 'lp[k]'
    lliste=np.zeros(dim)
    gata=0
    k=0
    while k<dim and not gata:
        a=str(lp[k])+'+'
        i=0
        while i<n and not gata :
            l=muchii[i]
            p=[j for j in range(len(l)) if l[j]==a]
            if len(p):
                gata=1
                alela=lp[k]
            else:
                p=[j for j in range(len(l)) if l[j]==str(lp[k])]
                i=i+1
                lliste[k]=len(l)
        if not gata:
            k=k+1
    if not gata:
        #calculeaza lungimea minima si pentru ce alele se atinge
        x=[j for j in range(dim) if lliste[j]==min(lliste)]
        #alege prima alela de lungime minima
        #daca sunt mai multe, alege-o pe prima
        alela=lp[x[0]]
    return alela

# operatorul ECX - Edge crossover
def ECX(x,y,n):
    muchii=constr_tabel(x,y,n)
    #permutarea rezultata
    z=np.zeros(n, dtype='int')
    #alege initial prima alela - varianta:selecteaza aleator ap in 0...n-1
    #lp - lista alelelor posibile
    #ales - vectorul flag al alelelor alese
    ales=np.zeros(n)
    lp=[x[0]]
    for i in range(n):
        print(muchii)
        if len(lp)==0:
            #alege aleator o alela
            a=np.random.randint(n)
            while ales[a]:
                a = np.random.randint(n)
        else:
            if len(lp)>1:
                a=alege(lp,muchii,n)
            else:
                a=lp[0]
        #atribuie alela aleasa
        z[i]=a
        ales[a]=1
        print(a)
        #sterge alela din tabela de muchii
        for k in range(n):
            sterge(muchii[k],str(a))
            sterge(muchii[k],str(a)+'+')
        #alege lista posibilitatilor la urmatorul moment
        lp=[int(muchii[a][i][0]) for i in range(len(muchii[a]))]
    return z

#APEL ECX
#import numpy as np
#import FunctiiCrossoverIndivizi as c
#n=10
#x=np.random.permutation(n)
#y=np.random.permutation(n)
#z=c.ECX(y,x,10)


# CROSSOVER VECTORI NUMERE REALE

# crossover singular intre x si y, vectori cu n componente de tipul ndarray
# I :x,y,n ca mai sus
#    alpha - ponderea la mediere
#E: c1,c2 - cei doi copii - fara evaluare
def crossover_singular (x, y, n,alpha):
    #genereaza aleator gena in care este facuta recombinarea
    i = np.random.randint(0,n)
    c1 = x.copy()
    c2 = y.copy()
    c1[i]=(alpha*x[i]+(1-alpha)*y[i])
    c2[i] = (alpha * y[i] + (1 - alpha) * x[i])
    return c1, c2


# crossover simplu intre x si y, vectori cu n componente - de tipul ndarray
# I :x,y,n ca mai sus
#    alpha - ponderea la mediere
#E: c1,c2 - cei doi copii
def crossover_simplu (x, y, n,alpha):
    #genereaza aleator gena incepand cu care este facuta recombinarea
    i = np.random.randint(0,n)
    c1 = x.copy()
    c2 = y.copy()
    for j in range(i,n):
        c1[j]=(alpha*x[j]+(1-alpha)*y[j])
        c2[j] = (alpha * y[j] + (1 - alpha) * x[j])
    return c1, c2

# crossover total intre x si y, vectori cu n componente
# I :x,y,n ca mai sus
#    alpha - ponderea la mediere
#E: c1,c2 - cei doi copii - fara evaluare
def crossover_total (x, y, n,alpha):
    c1 = x.copy()
    c2 = y.copy()
    for j in range(n):
        c1[j]=(alpha*x[j]+(1-alpha)*y[j])
        c2[j] = (alpha * y[j] + (1 - alpha) * x[j])
    return c1, c2

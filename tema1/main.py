import ex1
import ex2
import ex3
import ex4
import ex5
import ex6
import ex7
import ex8
import ex9
import numpy as np

MATRICEA_A = [[1, 2, 3],
              [4, 5, 6],
              [7, 5, 9]]
MATRICEA_B = [[6, 5, -3],
              [4, 5, 6],
              [9, 8, 7]]

A = np.random.randint(np.iinfo(np.int32).min, np.iinfo(np.int32).max)
B = np.random.randint(np.iinfo(np.int32).min, np.iinfo(np.int32).max)

if __name__ == '__main__':
    print(np.matrix(MATRICEA_A))
    print('Numarul liniilor care au valorile in ordine crescatoare este: {}\n'.format(ex1.ex1(MATRICEA_A)))
    print('Lista coloanelor din MATRICEA_A pe care cea mai mica valoare este 5: {}\n'.format(ex2.ex2(MATRICEA_A)))
    print(np.matrix(MATRICEA_B))
    print('Lista coloanelor din MATRICEA_B pe care cea mai mica valoare este 5: {}\n'.format(ex2.ex2(MATRICEA_B)))
    print('Matricea sortata crescator pe linii: \n{}\n'.format(np.matrix(ex3.ex3(MATRICEA_B))))
    print('CMMDC-ul dintre {} si {} este: {}\n'.format(A, B, ex4.ex4(A, B)))
    a, b, c, d = ex5.ex5(MATRICEA_A, MATRICEA_B, 5)
    print('MATRICEA_A transpura este \n{}\n\nMatricea A+B este \n{}\nMatricea A*B este \n{}\nMatricea A la puterea {} este \n{}\n'.
          format(np.matrix(a), np.matrix(b), np.matrix(c), 5, np.matrix(d)))
    print('Permutarea {} '.format([0,1,4,3,2]) + ('este' if ex6.ex6([0,1,4,3,2]) else 'nu este') + ' permutarea identica.\n')
    print('Permutarea {} '.format([0,1,2,3,4]) + ('este' if ex6.ex6([0,1,2,3,4]) else 'nu este') + ' permutarea identica.\n')
    e, f = ex7.ex7()
    print('Matricea A este \n{}\nVectorul V este {}\n'.format(np.matrix(e), f))
    g, h = ex8.ex8()
    print('Matricea A, ale carei linii sunt sortate dupa fitness este \n{}\nVectorul V este {}\n'.format(np.matrix(g), h))
    i, j = ex9.ex9(10)
    print('Populatia este {} si cel mai bun individ este {} avand fitness-ul {}.'.format(i, j, ex9.fitness(j)))

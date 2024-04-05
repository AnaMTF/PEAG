L = [1,2,3,4,2,3,4,2,2,3]
print(L)
cheie = 10
cheie2 = 2
if cheie in L:
    print("Apartine")
else:
    print("Nu apartine")

indici = [i for i in range(len(L)) if L[i] == cheie]
print("Lista: ", L)

if cheie2 in L:
    print("Apartine")
else:
    print("Nu apartine")

indici = [i for i in range(len(L)) if L[i] == cheie2]
print(indici)

L.append(2)
print("Lista: ", L)

if cheie2 in L:
    print("Apartine")
else:
    print("Nu apartine")

indici = [i for i in range(len(L)) if L[i] == cheie2]
print(indici)

L.remove(2)
print("Lista: ", L)

if cheie2 in L:
    print("Apartine")
else:
    print("Nu apartine")

indici = [i for i in range(len(L)) if L[i] == cheie2]
print(indici)

while cheie2 in L:
    L.remove(2)

print("Lista: ", L)
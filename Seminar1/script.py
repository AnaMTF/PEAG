import numpy as np

#print('Hello')
# x=int(input("Introduceti x "))
# print(type(x))

# v=np.zeros(10, dtype="int")
# v=np.zeros(10)
# print(v)

# v=np.genfromtxt("vector.crocodil",dtype="int")
# # print(v)
# dim=v.size
# #dim=len(v)
# if dim%2==0:
#     print("Dimensiune para")
# else:
#     print("Dimensiune impara")
#
# i=0
# while (i<dim):  #cu sau fara paranteze
#     print(v[i])
#     i=i+1
#     #i+=1
#
# print(v[1:4]) #v de la a doua componenta la a 4 a
#
# for i in range(dim):
#     print(v[i])

m=4
n=7
a=np.random.randint(1,11,[m,n])
# print(a)
np.savetxt("matrice.txt",a,"%i")  #.7f inseamna primele 7 decimale
#Listas
lista=[] #definir una lista vacia
print(lista)
Lista1 = [1,2,3,4,5,"hola",4.5] #una lista heterogenea
print(Lista1)

#enlazar listas
lista2 = [0,1,2,3]
lista3 = ["A", "B","C"]
lista4 = [lista2,lista3]
print(lista4)
print(lista4[1][1])#muestro de la lista2 el elemento en el indice 1
print(lista4[1][0])
print(lista4[0][3])

#Concatenacion
lista8 = ["A","B","C","E"]
lista9 = [1,2,3,4,5]
lista10 = lista8 + lista9
print(lista10)
print(lista10[2])

#El metodo extend agrega una lista al final de otra lista, la operacion afecta la lista invocante
nombres1 =["Antonio","Maria","Mabel"]
nombres2 =["Barry","John","Guttag"]
#nombres3 =["Barry","John","Guttag"]
nombres1.extend(nombres2)
print(nombres1)
print(nombres2)

#Repetir
lista11 =[1,2,3,4,5]
lista12 =lista11*3
print(lista12)

#Comparacion
#Usando los operadores convencionales (<, <=,>,>=,==,!=)
print(["Rojas", 123] < ["Rosas", 123])
print(["Rosas", 123] == ["rosas", 123])
print(["Rosas", 123] > ["Rosas", 23])

#Es posible determinar si un elemento se
lista13 =["cien","años","de","soledad"]
if "de" in lista13:
    print("si esta en la lista")
else:
    print("No esta en la lista")

#Iterando una lista
lista15 =["hola","amigos","mios"]
for palabra in lista15:#para cada palabra de la lista
    print(palabra, end=",")#parametro end evita salto de linea
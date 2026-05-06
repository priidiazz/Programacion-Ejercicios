lista = [1, 2, 3, 4, 5]
lista += [6, 7, 8, 9, 10]
print(lista)
lista.extend([11, 12, 13, 14, 15])
print(lista)

mi_lista = [10, 20, 30, 40, 50]
mi_lista_cortada = mi_lista[1:4]
print(mi_lista[:3])
print(mi_lista[2:4])
print(mi_lista_cortada)
print("Mi lista al reves: ", mi_lista[::-1])

print(lista[8])
lista.remove(3)
lista.insert(2, "Rosario")
print(lista)

matriz = [ [A, B, C], [D, E, F], [G, H, I] ]
print(matriz[0])

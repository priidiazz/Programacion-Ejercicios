# Crear un programa que reciba el nombre del empleado y los años que lleva en la empresa y devuelva el bono que le corresponde. Debe retornar el nombre del empleado junto con la palabras "tiene un bono de..."
#---------------------------------

print("Ingrese su nombre, por favor:")
nombre = input()
print("Ingrese cuantos años lleva en la empresa, por favor:")
años = int(input())

if(años<=5): 
    bono= 5000
    print(nombre, "tiene un bono de ", bono)
elif(años>5 and años<20):
    bono= 10000
    print(nombre, "tiene un bono de ", bono)
else:
    bono= 15000
    print(nombre, "tiene un bono de ", bono)
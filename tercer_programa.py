# El usuario ingresa un numero y el programa muestra si es negativo y menor que 10
print("Ingrese un numero:")
numero = float(input())

if numero<0 and numero<10:
   print ("el numero es negativo y menor que 10")
elif numero>0 and numero<10:
   print ("el numero es mayor que 0 y menor que 10")
else:
   print ("el numero es mayor que 0 y mayor que 10")
   
      
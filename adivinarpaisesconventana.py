import random

paises = ["ARGENTINA", "BRASIL", "CHILE", "URUGUAY", "PARAGUAY", "PERU"]
caracteristicas = ["Tiene el mejor asado del mundo.", "Creadores del jogo bonito.", "Pais con mas sismos de Sudamérica.", "El pais de la banda Cuarteto de Nos.", "Su bebida nacional es el Tereré.", "Cuna de la civilización Inca."]
contar = 5
aleatorio = random.randint(0,5)

while contar > 0:
    print("Tenes ", contar, " intentos.")
    print(caracteristicas[aleatorio])
    intento = input("¿A qué pais corresponde?")
    intento_may = intento.upper()

    if intento_may == paises[aleatorio]:
        print("¡Correcto!")
        break
    else:
        contar = contar - 1
        print("¡Incorrecto! Te quedan ", contar, " intentos disponibles.")
    
else:
   print("¡Perdiste! Te quedaste sin intentos.")
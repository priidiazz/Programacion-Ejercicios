# Crear una lista de paises y una lista de caracteristicas.
# El usuario debe adivinar un pais mostrandole una caracteristica.
import random

paises = ["ARGENTINA", "BRASIL", "CHILE", "URUGUAY", "PARAGUAY", "PERU"]
caracteristicas = ["Tiene el mejor asado del mundo.", "Creadores del jogo bonito.", "Pais con mas sismos de Sudamérica.", "El pais de la banda Cuarteto de Nos.", "Su bebida nacional es el Tereré.", "Cuna de la civilización Inca."]
aleatorio = random.randint(0,5)
intentos = 5
pais_random = ""

if aleatorio == 0:
    pais_random = paises[0]
    carac_pais = caracteristicas[0]
elif aleatorio == 1:
    pais_random = paises[1]
    carac_pais = caracteristicas[1]
elif aleatorio == 2:
    pais_random = paises[2]
    carac_pais = caracteristicas[2]
elif aleatorio == 3:
    pais_random = paises[3]
    carac_pais = caracteristicas[3]
elif aleatorio == 4:
    pais_random = paises[4]
    carac_pais = caracteristicas[4]
else:
    pais_random = paises[5]
    carac_pais = caracteristicas[5]

while intentos > 0:
    print("Su pista es: ", carac_pais)
    pais_ing = input("Ingrese un pais Sudamericano.")
    pais_ing_may = pais_ing.upper()
    if pais_ing_may == pais_random:
        print("Felicitaciones! Adivinaste el pais.")
        break
    else:
        intentos = intentos - 1
        print("Incorrecto! Le quedan ", intentos, " intentos.")
else:
    print("Te quedaste sin intentos restantes. El pais secreto era ", pais_random)
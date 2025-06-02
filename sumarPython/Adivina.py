import random

numero_secreto = random.randint(1, 100)
intentos = 0

print("¡Adivina el número entre 1 y 100!")

while True:
    intento = int(input("Tu intento: "))
    intentos += 1

    if intento < numero_secreto:
        print("Demasiado bajo.")
    elif intento > numero_secreto:
        print("Demasiado alto.")
    else:
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
        break


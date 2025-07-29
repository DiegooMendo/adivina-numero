import random

print("🎲 Bienvenido al juego: Adivina el Número 🎯")
print("Estoy pensando en un número entre 1 y 100...")

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = input("Introduce tu número: ")

    if not intento.isdigit():
        print("❌ Por favor, ingresa solo números.")
        continue

    intento = int(intento)
    intentos += 1

    if intento < numero_secreto:
        print("🔻 Muy bajo. Intenta otra vez.")
    elif intento > numero_secreto:
        print("🔺 Muy alto. Intenta otra vez.")
    else:
        print(
            f"🎉 ¡Correcto! El número era {numero_secreto}. Lo adivinaste en {intentos} intentos.")
        break

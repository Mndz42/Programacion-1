import numpy as np
#Genera la bajara de cartas
numParejas = 6
baraja = np.repeat(np.arange(1, numParejas + 1), 2)
np.random.shuffle(baraja)
descubiertas = np.zeros(baraja.size, dtype=bool)

while descubiertas.sum() < baraja.size:
    print("MEMORAMA")

    for i in range(baraja.size):
        print(f"{i + 1:^5}", end="")
    print()
    for i in range(baraja.size):
        if descubiertas[i]:
            print(f"{baraja[i]:^5}", end="")
        else:
            print(f"{'?':^5}", end="")
    print("\n")

    primera = int(input("Primera carta: ")) - 1
    while primera < 0 or primera >= baraja.size or descubiertas[primera]:
        print("ERROR: Posición no válida")
        primera = int(input("Primera carta: ")) - 1

    segunda = int(input("Segunda carta: ")) - 1
    while segunda < 0 or segunda >= baraja.size or descubiertas[segunda] or segunda == primera:
        print("ERROR: Posición no válida")
        segunda = int(input("Segunda carta: ")) - 1

    print(f"\nCarta {primera + 1}: {baraja[primera]}    Carta {segunda + 1}: {baraja[segunda]}")

    if baraja[primera] == baraja[segunda]:
        print("Pareja encontrada")
        descubiertas[primera] = True
        descubiertas[segunda] = True
    else:
        print("No son iguales")

print("Ganaste")
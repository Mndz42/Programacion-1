import numpy as np

cantidad = 10
while True:
    luces = np.zeros(cantidad, dtype=np.uint8)

    for posicion in range(cantidad):
        if np.random.randint(2) == 1:
            inicio = max(0, posicion - 1)
            fin = min(cantidad, posicion + 2)
            luces[inicio:fin] = 1 - luces[inicio:fin]

    if np.any(luces == 1):
        break

while np.any(luces == 1):
    print("\nPosición:", end=" ")
    for i in range(luces.size):
        print(f"{i + 1:>3}", end=" ")

    print("\nEstado:  ", end=" ")
    for luz in luces:
        simbolo = "●" if luz == 1 else "○"
        print(f"{simbolo:>3}", end=" ")

    print("\n● Encendida   ○ Apagada\n")

    posicion = int(input(f"Elige una luz [1-{cantidad}]: ")) - 1
    while posicion < 0 or posicion >= cantidad:
        print("ERROR: Posición no válida")
        posicion = int(input(f"Elige una luz [1-{cantidad}]: ")) - 1

    inicio = max(0, posicion - 1)
    fin = min(cantidad, posicion + 2)
    luces[inicio:fin] = 1 - luces[inicio:fin]

print("Apagaste todas las luces")
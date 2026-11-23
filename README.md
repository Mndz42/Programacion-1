# Programación 1
Este repositorio contiene los programas y ejercicios
desarrollados durante la materia de Programación 1.
Los ejercicios están organizados por temas, y cada
programa se encuentra en su propia carpeta.

## Contenido

| Programa | Función |
| --- | --- |
| `contraseña segura/contraseñaFunc.py` | Valida una contraseña según criterios específicos para saber si es segura. |
| `dia de la semana\fechaFunc.py` | Indica qué día de la semana fue en una fecha ingresada por el usuario. |
| `juego luces\juegoluces.py` | Genera un tablero de luces que el usuario debe apagar todas, sabiendo que cada selección cambia la luz elegida y las 2 de su alrededor. |
| `juego memorama\memorama.py` | Genera un tablero del clásico memorama donde se voltean 2 cartas por turno hasta encontrar todos los pares. |
| `cifrado cesar\encriptado.py` | Cifra una frase aplicando un desplazamiento ingresado por el usuario. |

## Requisitos
Necesitas Python 3 instalado, además de la librería numpy para el programa del memorama.

## Cómo ejecutar los programas
Todos los programas se ejecutan en la terminal. Con la carpeta Programación-1(icc) abierta,
escribe `py "(RUTA DEL PROGRAMA)"`  
Ejemplo:  
`py "contraseña segura\contraseñaFunc.py"`

## Ejecución del programa

### Contraseña segura

Este programa permite validar si una contraseña es segura de acuerdo a criterios específicos.

**Requisitos:**
- Tener instalado Python 3.

**Ubicación:** `contraseña segura/contraseñaFunc.py`

**Para ejecutarlo:**

```bash
py "contraseña segura\contraseñaFunc.py"
```


## Ejemplo de funcionamiento

Al ejecutar `contraseñaFunc.py`, el programa solicita una contraseña y
te indica si es segura o no.

**Ejemplo de entrada y salida:**

```text
Ingresa tu contraseña: Hola1234!
La contraseña es segura
```

![Ejecución del programa](capturas\capturalol.png)

## Funcionamiento
### Cifrado cesar
Ejecuta el programa en la terminal, ingresa el mensaje a cifrar y el desplazamiento.

### Contraseña segura
Ejecuta el programa en la terminal e ingresa los datos solicitados,
se te dirá si tu contraseña es segura.

### Dia de la semana
Ejecuta el programa en la terminal e ingresa una fecha de acuerdo a los rangos indicados.

### Juego luces
Ejecuta el programa en la terminal, se muestra un tablero con luces
prendidas y apagadas, ingresa el número de la posición de la luz que
quieres cambiar, el programa termina cuando se apagan todas las luces.

### Memorama
Ejecuta el programa en la terminal,
aparece un tablero, el usuario debe ingresar qué cartas del tablero quiere voltear,
después de elegirlas se revelan, si son iguales quedan reveladas, si no se voltean de nuevo.

## Autor
Santiago Mendez Sandoval
def cifrar_cesar(frase, desplazamiento):
  alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&.,:;'
  mensaje = ""
  for c in frase:
   # if c in minusculas:
     # mensaje = mensaje + minusculas[(minusculas.index(c) + desplazamiento) % 26]
   # elif c in mayusculas:
     # mensaje = mensaje + mayusculas[(mayusculas.index(c) + desplazamiento) % 26]
    #else:
     # mensaje = mensaje + c
       mensaje = mensaje + alfabeto[(alfabeto.index(c) - desplazamiento) % (len(alfabeto)-1)] 
  return mensaje

frase = input("Escribe una frase: ")

while True:
  try:
    desplazamiento = int(input("Desplazamiento (entero positivo): "))
    if desplazamiento > 0:
      break
    print("Debes escribir un número entero positivo")
  except ValueError:
    print("Debes escribir un número entero")

print("Mensaje cifrado:", cifrar_cesar(frase, desplazamiento))
#Funciones para verificar la contraseña
def tiene_minuscula(contraseña):
    for c in contraseña:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            return True
    return False

def tiene_mayuscula(contraseña):
    for c in contraseña:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return True
    return False

def tiene_digito(contraseña):
    for c in contraseña:
        if c in '0123456789':
            return True
    return False

def tiene_especial(contraseña):
    for c in contraseña:
        if c in '!"#$%&?¡=)(/*-+_{':
            return True
    return False

def es_segura(contraseña):
    return (tiene_minuscula(contraseña)
            and tiene_mayuscula(contraseña)
            and tiene_digito(contraseña)
            and tiene_especial(contraseña))


print("Este programa valida que tu contraseña cumpla con los criterios")
print(f"Debe tener al menos 5 caracteres, una mayúscula, una minúscula, un número y un carácter especial")
print()

while True:
    contraseña = input("Ingrese su contraseña: ")
    if len(contraseña)>=5:
        break
    print("Se esperan al menos 5 caracteres")

if es_segura(contraseña):
    print("Contraseña segura")
else:
    print("Contraseña insegura")
    
if not tiene_minuscula(contraseña):
    print("- Falta una letra minuscula")
if not tiene_mayuscula(contraseña):
    print("- Falta una letra mayúscula")
if not tiene_digito(contraseña):
    print("- Falta un numero")
if not tiene_especial(contraseña):
    print(f"- Falta un carácter especial")
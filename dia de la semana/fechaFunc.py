#Funciones para calcular el dia de la semana
def nombre_mes(m):
  if m== 1:
    return "Enero"
  elif m==2:
    return "Febrero"
  elif m== 3:
    return "Marzo"
  elif m== 4:
    return "Abril"
  elif m== 5:
    return "Mayo"
  elif m== 6:
    return "Junio"
  elif m==7:
    return "Julio"
  elif m==8:
    return "Agosto"
  elif m==9:
    return "Septiembre"
  elif m==10:
    return "Octubre"
  elif m==11:
    return "Noviembre"
  elif m==12:
    return "Diciembre"
#-----------------------------------------------------------------------
def año_bisiesto(año):
  if año % 4==0 and año %100!=0 or año%400==0: # año bisiesto
    return True
  else:
    return False
#-----------------------------------------------------------------------
def dias_mes(mes, año):
  match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        return 31
    case 4 | 6 | 9 | 11:
        return 30
    case 2:
        if año_bisiesto(año):
            return 29
        else:
            return 28
#-----------------------------------------------------------------------
def nombre_dia_semana(dia, mes, año):
  a = (14 - mes) // 12
  b = año - a
  c = mes + 12 * a - 2
  indicador = dia + b + b // 4 - b // 100 + b // 400 + (31 * c) // 12
  residuo = indicador % 7

  match residuo:
    case 0:
      return "Domingo"
    case 1:
      return "Lunes"
    case 2:
      return "Martes"
    case 3:
      return "Miércoles"
    case 4:
      return "Jueves"
    case 5:
      return "Viernes"
    case 6:
      return "Sábado"
#-----------------------------------------------------------------------
while True:
  try:
    año = int(input("Escribe un año en [1900,2026]: "))
    if año>=1900 and año<=2026:
      break
    print("Se espera un número entero en [1900,2026]")
  except ValueError:
    print("Debes escribir un número entero")


while True:
  try:
    mes = int(input("Escribe un mes: "))
    if mes>=1 and mes<=12:
      break
    else:
      print("Debes escribir un número entero en [1,12]")
  except ValueError:
    print("Debes escribir un número entero")
    
while True:
    try:
        dia = int(input(f"Escribe el dia: [1,{dias_mes(mes,año)}]: "))
        if dia >= 1 and dia <= dias_mes(mes,año):
            break
        else:
            print(f"ERROR: Se espera un valor entre 1 y {dias_mes(mes,año)}")
    except ValueError:
        print("ERROR: Se espera un numero entero")

nombreMes = nombre_mes(mes)
diaSemana = nombre_dia_semana(dia, mes, año)
print(f"La fecha es {dia} de {nombreMes} del {año}")
print(f"Ese día fue {diaSemana}")
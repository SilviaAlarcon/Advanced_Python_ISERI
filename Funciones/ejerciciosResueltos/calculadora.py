def suma(numero1, numero2):
  return numero1 + numero2

def resta(numero1, numero2):
  return numero1 - numero2

def producto(numero1, numero2):
  return numero1 * numero2

def division():
  numero1 = float(input('Escribe un numerador: '))
  numero2 = float(input('Escribe un denominador: '))
  if(numero2 != 0):
    division = numero1 / numero2
    return division
  else:
    while numero2 == 0:
      print('El denominador debe ser diferente de 0')
      nuevoNumero = float(input('Ingresa otro número: '))
      if(nuevoNumero != 0):
        numero2 = nuevoNumero
        division = numero1 / numero2
        return division
      else:
        numero2 = 0
'''1.Hacer un módulo con las funciones básicas para una calculadora, 
suma, resta, producto y división, en la función de división si el denomidador 
es igual a cero debe de volver a leer el valor del denominador hasta que sea 
distinto de cero (se recomienda utilizar el ciclo while y el condicional if)'''

from calculadora import *

print('La suma de los números es: ' + str(suma(10, 5)))
print('La resta de los números es: ' + str(resta(20, 12)))
print('La multiplicación de los números es: ' + str(producto(8, 7)))
print('La división de los números es: ' + str(division()))
#Trabajo práctico 2 - Int. a la Algoritmia
#Ejercicio 2: Desarrollar un programa que permita ingresar dos números enteros A y
#B a través del teclado. Imprimir su suma y su diferencia.

"""
A = int(input("Ingresar un número: "))
B = int(input("Ingresar un número: "))

suma = A + B
resta = A - B

print("La suma de sus números es: ", suma)
print("La resta de sus números es: ", resta)
"""

#Ejercicio 3: Calcular el promedio de las notas que obtiene un alumno al rendir los dos parciales.
"""
nota = int(input("Ingrese la nota del primer parcial: "))
nota2 = int(input("Ingrese la nota del segundo parcial: "))

promedio = (nota + nota2) / 2

print(promedio)
"""

#Ejercicio 4: Escribir un programa que permita ingresar la edad de una persona en
#años y la convierta a días, imprimiendo el resultado. Considerar que todos los años tienen 365 días.
"""
edad = int(input("Ingrese su edad en años: "))

edadDias = edad * 365

print("Su edad en días es: ", edadDias)
"""

#Ejercicio 5: Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales). Calcular qué porcentaje invirtió cada una.
"""
inversor1 = int(input("ingrese cuanto dinero invirtió: "))
inversor2 = int(input("ingrese cuanto dinero invirtió: "))
inversor3 = int(input("ingrese cuanto dinero invirtió: "))
total = inversor1 + inversor2 + inversor3

porcentaje1 = inversor1 * 100 / total
porcentaje2 = inversor2 * 100 / total
porcentaje3 = inversor3 * 100 / total

print("El inversor 1 puso $", porcentaje1, "el segundo inversor puso $", porcentaje2, "y el tercero $" , porcentaje3)
"""
#Ejercicio 6: Ingresar tres números enteros, calcular su promedio y mostrarlo por pantalla.
"""
numero = int(input("Ingrese un número entero: "))
numero += int(input("Ingrese un número entero: "))
numero += int(input("Ingrese un número entero: "))

promedio = numero / 3

print(promedio)
"""
#Ejercicio 7: Una persona invierte su capital en un banco y desea saber cuánto dinero ganará en un mes, teniendo en cuenta que el banco paga 2% mensual.
#¿Cuánto ganará en seis meses si deja su dinero invertido?
"""
capital = int(input("Ingrese su capital a invertir: "))
meses = int(input("Ingrese la cantidad de meses a invertir: "))
interesMensual = 2
interesTotal = capital * interesMensual * meses / 100
capitalTotal = capital + interesTotal
print(interesTotal)
print(capitalTotal)
"""
#Ejercicio 8:Leer una medida en metros e imprimir esta medida expresada en centímetros, pulgadas, pies y yardas. Los factores de conversión son:
#1 pie = 12 pulgadas
#1 yarda = 3 pies
#1 pulgada = 2,54 cm.
#1 metro = 100 cm

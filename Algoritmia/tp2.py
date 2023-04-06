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
"""
medida = int(input("Ingresar una medida en metros: "))
medidaCentimetros = medida * 100
medidaPulgadas = medidaCentimetros  / 2.54
medidaPies = medidaPulgadas / 12
medidaYarda = medidaPies / 3

print("Su medida en centimetros es:  ", medidaCentimetros, ",en pulgadas ", medidaPulgadas, ",en pies ", medidaPies, ",y en yardas es ", medidaYarda)
"""
#Ejercicio 9: Una inmobiliaria paga a sus vendedores un salario de $50000, más una comisión de $5000 por cada venta realizada, más el 5% del valor de las
#ventas. Realizar un programa que imprima el número del vendedor y el salario que le corresponde en un determinado mes. Se leen el número
#del vendedor, la cantidad de ventas que realizó y el valor total de las mismas
"""
vendedor   = 1
salario = 50000
ventas =int(input("ingrese la cantidad de ventas realizadas en el mes: "))
valorVentas = int(input("Ingresar el valor total de las ventas: "))
total=salario + ventas * 5000 + valorVentas * 5 / 100

print("El vendedor número", vendedor, "realizó ", ventas, " ventas por un total de ", valorVentas, "el sueldo a cobrar es ", total)
"""

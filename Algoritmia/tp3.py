#Ingresar dos números enteros e indicar si son iguales o distintos.
"""
a = int(input("Ingrese número entero "))
b = int(input("Ingrese número entero "))

if a == b:
    print("Los números ingresados son iguales")
else:
    print("Usted ingreso números distintos")
"""
#Leer un número entero e imprimir un mensaje indicando si es par o impar.

"""
a = int(input("Ingrese número entero "))

if a % 2 == 0:
    print("El numero ingresado es par")
else:
    print("El número es impar")
"""
#Desarrollar un programa que solicite un número de mes (por ejemplo 4) y
#escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido y
#mostrar un mensaje de error en caso de que no lo sea.

"""
a = int(input("Ingresar en número el mes correspondiente"))
if a == 1:
    print("Enero")
elif a == 2:
    print("Febrero")
elif a == 3:
    print("Marzo")
elif a == 4:
    print("Abril")
elif a == 5:
    print("Mayo")
elif a == 6:
    print("Junio")
elif a == 7:
    print("Julio")
elif a == 8:
    print("Agosto")
elif a == 9:
    print("Septiembre")
elif a == 10:
    print("Octubre")
elif a == 11:
    print("Noviembre")
elif a == 12:
    print("Diembre")
else:
    print("El número de mes ingresado es incorrecto")
"""


#Una editorial determina el precio de un libro según la cantidad de páginas que contiene.
#El costo básico del libro es de $500, más $3,20 por página con encuadernación rústica. Si el número de páginas supera las 300 la encuadernación
#debe ser en tela, lo que incrementa el costo en $200. Además, si el número de
#páginas sobrepasa las 600 se hace necesario un procedimiento especial de encuadernación que incrementa el costo en otros $336. Desarrollar un programa
#que calcule el costo de un libro dado el número de páginas.

"""
libro = int(input("Ingrese el número de páginas del libro para calcular su valor "))
encuadernacion_rustica, encuadernacion_tela, encuadernacion_especial, precio_por_pagina = 500, 700, 836, 3.20

if libro < 300:
    print("Su precio es: ", encuadernacion_rustica + libro * precio_por_pagina)
elif libro > 300 and libro < 600:
    print("Su precio es: ", encuadernacion_tela + libro * precio_por_pagina )
else:
    print("Su precio es: ", encuadernacion_especial + libro * precio_por_pagina)
"""
#Una remisería requiere un programa que calcule el precio de un viaje a partir de
#la cantidad de kilómetros que desea recorrer el usuario. Para eso cuenta con la siguiente tarifa:
#· Viaje mínimo $250. Sólo se cobra cuando el importe por kilómetro no alcanza este mínimo.
#· Si recorre entre 0 y 10 km: $30 por km
#· Si recorre 10 km o más: $20 por km

"""
a = int(input("Ingresar cantidad de kilometros de viaje "))

if a <= 10 and a*30 < 250:
    print("$250")
elif a <= 10 and a*30 > 250:
    print(a*30)
elif a > 10 and a*20 < 250:
    print("250")
else:
    print(a*20)
"""
#Ejercicio 7:Leer un número correspondiente a un año e imprimir un mensaje indicando si es bisiesto o no.
#Un año es bisiesto cuando es divisible por 4. Sin embargo, aquellos años que sean divisibles por 4 y
#también por 100 no son bisiestos, a menos que también sean divisibles por 400.
#Por ejemplo, 1900 no fue bisiesto pero sí el 2000.
"""
año = int(input("Ingrese un año "))
if año %4 == 0 and año % 100 == 0 and año % 400 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")
"""
#Ejercicio 8:Leer tres números correspondientes al día, mes y año de una fecha
#e imprimir un mensaje indicando si la fecha es válida o no.
"""
dia = int(input("Ingrese una fecha "))
mes = int(input("Ingrese un mes "))
año= int(input("Ingrese un año "))

if dia >= 1 and dia <=31 and mes >= 1 and mes <=12 and  año >= 1930 and año <=2023:
    print("La fecha: ", dia, "/", mes, "/", año, "es válida")
else:
    print("La fecha ingresada no es válida")
"""
#Ejercicio 9: Diseñar un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y su antigüedad en años.
#Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7%
#del bruto por cada año de antigüedad. También se le realizan los siguientes descuentos: Jubilación: 11%, Obra Social: 3%, Sindicato: 3%
"""
sueldo = int(input( "Ingrese su sueldo bruto "))
antiguedad = int(input( "Ingrese su/s año/s de antiguedad "))  / 100 * sueldo
estadoCivil =  int(input( "Ingrese 1 si es soltero y 2 si esta casado "))
jubilacion = sueldo*11/100
obraSocial = sueldo*3/100
sindicato = sueldo*3/100

if estadoCivil == 1:
                   print("Su sueldo neto es: ", sueldo + antiguedad * 5 - jubilacion - obraSocial - sindicato)
else:
                   print("Su sueldo neto es: ", sueldo + antiguedad * 7 - jubilacion - obraSocial  - sindicato)
                   
"""


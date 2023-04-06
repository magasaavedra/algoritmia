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
if estadoCivil == 2:
                   print("Su sueldo neto es: ", sueldo + antiguedad * 7 - jubilacion - obraSocial  - sindicato)
                   
"""


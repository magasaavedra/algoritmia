"""Ingresar 3 valores correspondientes a la longitud de los lados de un triandolo .
Informar:
a) si los valores ingresados forman un triangulo
b) si se forma un triángulo, qué triángulo es?
"""
a = int(input("Ingresar lado "))
b = int(input("Ingresar lado "))
c = int(input("Ingresar lado "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Los valores ingresados forman un triángulo escaleno")
    elif a == b != c or b == c != a or a == c != b:
        print("Los valores ingresados forman un triángulo isoseles")
    else:
        print("Los valores ingresados forman un triángulo equilatero")
else:
    print("Los valores ingresados no forman un triángulo")
        



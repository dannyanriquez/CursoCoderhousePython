

def calculadora (a,b, operacion):
    if operacion == "1":
       resultado = a + b
       print(f"el resultado es {resultado}")
    elif  operacion == "2":
       resultado = a - b
       print(f"el resultado es {resultado}")
    elif  operacion == "3":
        resultado = a * b
        print(f"el resultado es {resultado}")
    elif  operacion == "4":
        if b == 0:
            print("No se puede dividir por 0")
        else:
            resultado = a / b
            print(f"el resultado es {resultado}")
    else:
        resultado = print("por favor verificar datos ingresados")
    
    return resultado

\

operacion = input("Seleccion la operacion:\n 1 : Suma\n 2 : Resta\n 3 : Multiplicacion\n 4 : Division\n")

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el primer numero: "))


calculadora(a, b, operacion) #IMPORTANTE Respetar el orden en la  funcion como en el parametro


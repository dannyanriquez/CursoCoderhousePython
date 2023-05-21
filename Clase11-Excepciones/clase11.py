# ERRORES Y EXCEPCIONES
#dividir por cero

def dividir(a,b):
    if b != 0 :
        return a / b


num1 = int(input("num1: "))
num2 = int(input("num2: "))

print(dividir(num1,num2))

###############
#TRY - Capturar un error en el caso de que el cliente no ingrese un numeero
#lo que este dentro de esa seccion esta solo a la obedencia del try.
#si falla, ejecuta el except

ok = 1

while ok == 1 :
    try:
        num1 = int(input("numero1: "))
        print(num1)

    except:
        print("esto no es un numero")

print("error controlado")


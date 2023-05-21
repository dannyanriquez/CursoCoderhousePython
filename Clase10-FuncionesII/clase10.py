#PARAMETROS. Se definen cuando se define la funcion

def suma(num1, num2):
    return num1 + num2

#ARGUMENTOS. Se definen cuando se llama a la funcion 

resultado = suma(7,5)

###############

def suma (num1, num2):   #2 - Recibo Parametros
    return num1 + num2 

respuesta = suma(10,20)  #1 - envio argumentos
print(respuesta)

##################
#EJEMPLO DE ARGUMENTOS DESORDENADOS DESDE LA FUNCION - Podemos ordenar por nombre de parametro

def setNombreCompleto(PrimerNombre, SegNombre, PriApellido, SegApellido):
    return f"{PrimerNombre} {SegNombre} {PriApellido} {SegApellido}"


print(setNombreCompleto(PriApellido="Carcamo",PrimerNombre="Derick",SegApellido="Juarez", SegNombre="Josue"))



##############################
#ARGUMENTOS DEFINIDOS DESDE VARIABLES

def setNombreCompleto(PrimerNombre):
    PrimerNombre = "Matias"

    return PrimerNombre


PrimerNombre = "Daniel"


print(setNombreCompleto(PrimerNombre))


print(PrimerNombre)

# Defino las variables a utilizar, nombre, segundo nombre, apellido y apellido
#Por medio de los ARGUMENTOS, le envio UNA COPIA de la informacion a la funcion.
#LA Funcion recibe una copia de las variables
#Dentro  de la funcion hay una variable igual (Primer Nombre), por lo cual se altera y convierte en Matias.
#Solo Cuando se ejecuta la funcion me cambia PRIMER NOMBRE
#La Variable Original Primer Nombre no se modifica, sigue siendo Daniel



###############################

#LOS ARGS Y KWARGS LOS UTILIZO CUANDO NOSE QUE CANTIDAD DE ARGUMENTOS DESDE EL USUARIO VOY A RECIBIR

# Diferencia, uno recibe lista, otro recibe tipo diccionario clave valor



#.........................


#EJEMPLO DE *ARGS
#esta funcion va a recibir X cantidad de argumentos. se define con el asterisco antes del argumento
#se utiliza cuando no sabemos con exactitud cuantos parametros vamos a recibir
#me convierte los argumentos en lista, por lo cual lo puedo recorrer o acceder a sus indices

def promedio_edad(*edades):
    edadPromedio = 0         #variable inicia en cero
    for edad in edades:      #recorro la lista edades
        edadPromedio += edad #a edadPromedio(esta en cero) le sumo lo encontrado en el bucle
    
    edadPromedio /= len(edades) #la suma de todas las edades la divido por la cantidad de indices que trae el parametro
    return edadPromedio


print(promedio_edad(29,50,17,98,39,43,18))


####################

#EJEMPLO DE *KWargs- 

# su composicion es como si fuera un diccionario
#necesita clave:valor

def data2(**kwargs):
    for key,value in kwargs.items():
        print(value)


data2(num1= 1, num2 = 2, num3 = 3) #Le enviamos clave, valor

###################################

#FUNCION RECURSIVA

#recursividad es que la funcion se llama a si misma, como un loop infinito pero con un final.

num = input("num: ")

def recur_factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return("NA")
    else:
        return n*recur_factorial(n-1)
    


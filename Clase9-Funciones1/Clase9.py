# DEF: en python palabra reservada para definir funciones de finidas por el uusario

"""

ESTRUCTURA


def NOMBRE (PARAMETROS):
    Sentencia
    return[EXPRESION]

"""

def saludar():
    print("Hola Mundo")


saludar()


#FUNCION CON PARAMETRO
#dentro el parentesis le asigno el parametro, en este caso una variable.
#Ejecuta la funcion devolviendo el parametro asignado. 
def saludar_con_parametro(nombre):
    print(f"Hola {nombre} del team CODER")


nombre = input("Nombre: ")

#ejecuto la funcion
saludar_con_parametro(nombre)


##############

#defino funcion apellido.

def apellido():       
    apellido = "Anriquez"
    return apellido #Retorna informacion, cada vez que llamamos esta func devuelve ANRIQUEZ



#invoco la funcion apellido y la variable me devuelve su retorno. 

def saludar_con_parametro2(nombre): #Le doy el parametro nombre que se completa mediante un input
    lastName = apellido() #creo variable y que me retorne la info que tiene la funcion apellido
    saludar = f"Hola {nombre} {lastName}"  # completa nombre con parametro y  apellido con la funcion
    return saludar #retorna toda la informacion ya completa

nombre = input("Nombre:") #Solicito nombre Al usuario

saludar = saludar_con_parametro2(nombre) #guardo el resultado de la funcion en una variable 

print(saludar)



#El retorno se utiliza para que la funcion devuelva una informacion que luego puede ser utilizada y por ejemplo ser guardada en una variable. 


#EJEMPLO BANCO




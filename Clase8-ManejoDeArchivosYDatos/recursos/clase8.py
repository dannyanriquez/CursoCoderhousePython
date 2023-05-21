
"""


file = open("./Clase8-ManejoDeArchivosYDatos/recursos/usuarios.txt" , "w") #direccionamos el archivo a escribir

# puede ser "w" de escribir. "r" de read o "a" de append


file.write("Primera Linea escrita\n")
file.write("Segunda Linea escrita\n")

file.close() #importante siempre cerrar el recurso para no consumir espacio de memoria




"""
"""
#EJEMPLO PARA ESCRIBIR EN UN TXT
import os

print("FAKEBOOK")
opcion = int(input("digite 1 para inciar sesion o 2 para registrarte\n"))


os.system("cls") #libreria integrada de python desde el sist operativo, ejecuto el cls directamente en python.


if(opcion == 1):
    print("iniciar sesion")
    email = input("ingrese su correo\n")
    pwd = input("ingrese contraseña\n")
    os.system("cls") 
    file = open("./Clase8-ManejoDeArchivosYDatos/recursos/usuarios.txt" , "r")#la R proviene de Read, consulta en el TXT si el usuario ya existe
    
    for linea in file.readlines(): #como el registro esta en modo lectura, con un for recorro la informacion del txt papra verificar usuario
        data = linea.split("|") #va a buscar nuestra info, y la separa cada vez que encuentre la barra y lo guarda en la variable DATA
        if(data[0] == email and data[1] == pwd): #hago un comparativo del mail y contraseña, ambas tienen que ser iguales al registro
            print(f"sesion iniciada, bienvenido {data[2]} {data[3]}")
            file.close() #cierro el archivo
            break #si encontro el usuario con break deja de buscar
        else:
            print("usuario o contraseña incorrectos") # sino encuentra el usuario tira un else



elif(opcion == 2):
    print("Registrarse")
    email = input("ingrese su correo\n")
    pwd = input("ingrese contraseña\n")
    name = input("ingrese su nombre\n")
    lastName = input("ingrese su apellido\n")
    os.system("cls")

    file = open("./Clase8-ManejoDeArchivosYDatos/recursos/usuarios.txt" , "a") #la A proviene de Append, agrega el nuevo usuario al TXT
    file.write(f"{email}|{pwd}|{name}|{lastName}\n")
    file.close()

    print("registro Exitoso")


else:
    print("opcion no valida, seleccionar la opcion correcta.")

"""

#EJEMPLO PARA ESCRIBIR EN UN JSON

import json
import os

print("FAKEBOOK")
opcion = int(input("digite 1 para inciar sesion o 2 para registrarte\n"))

newdata = {} #creamos un diccionario vacio
newdata["usuarios"] = [] #dentro de Newdata tomamos el valor usuarios y lo asignamos a una lista vacia, esto sera un usuario individual



os.system("cls") #libreria integrada de python desde el sist operativo, ejecuto el cls directamente en python.


if(opcion == 1):
    print("iniciar sesion")
    email = input("ingrese su correo\n")
    pwd = input("ingrese contraseña\n")
    os.system("cls") 
    with open("./Clase8-ManejoDeArchivosYDatos/recursos/usuarios.json" , "r") as file: #con el whit indico que solo lo que esta adentro se ejecuta
            #La sentencia with se usa para ajustar la ejecución de un bloque con métodos definidos por un administrador de contexto
        
        data = json.load(file) #indico que la variable data la cargue coomo un archivo json

        for user in data["usuarios"]: #recorro data y le indico que me traiga el valor de usuarios
            if(user["email"] == email and user["pwd"] == pwd): #hago un comparativo del mail y contraseña, ambas tienen que ser iguales al registro
                print(f"sesion iniciada, bienvenido {email}")
                file.close() #cierro el archivo
                break #si encontro el usuario con break deja de buscar
            else:
                print("usuario o contraseña incorrectos") # sino encuentra el usuario tira un else



elif(opcion == 2):
    print("Registrarse")

    newdata = {
        "email" : input("correo: "),
        "pwd" : input("Contraseña: "),
        "name" : input("Nombre: "),
        "LastName" : input("Apellido: "),
    }

    os.system("cls")

    with open("./Clase8-ManejoDeArchivosYDatos/recursos/usuarios.json" , "r") as file:
        data = json.load(file)
        file.close()
    data["usuarios"].append(newdata)
    
    
    with open("./Clase8-ManejoDeArchivosYDatos/recursos/usuarios.json" , "w") as file:
        json.dump(file)
        file.close()
    print("registro Exitoso")

else:
    print("opcion no valida, seleccionar la opcion correcta.")




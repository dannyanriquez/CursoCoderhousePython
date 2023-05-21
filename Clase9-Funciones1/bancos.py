print("TRANSACCION")
print(" O: Operador\n V: Verificador\n A: Autorizador\n")
opcion = input("Seleccione una opcion: ").upper()


def recuperaUsuario(opcion): #recibo el parametro desde el if
    with open("./Clase9-Funciones1/datoUsuarios.txt") as datos: #datos es un alias como en el for, representa al txt
        for data in datos:#creamos un for para recorrer datos
            detalles = data.split("|") #con el split indicamos que tiene que separar la data cada vez que encuentre el simbolo y la informacion la convierte en UNA LISTA- 
            if(detalles[0] == opcion): #si la posicion 0 del TXT (Verificador, autorizador, etc)es el rol seleccionado por el usuario
                return detalles[0], detalles[1],detalles[2],detalles[3],detalles[4]
                


#segun la opcion seleccionada por el usuario, le mando la info a la funcion con la variable opcion

if (opcion == "O"):
    usuario = recuperaUsuario("operador")
elif (opcion == "V"):
    usuario = recuperaUsuario("verificador")
elif (opcion == "A"):
    usuario = recuperaUsuario("autorizador")
else:
    print("Dato ingresado incorrecto")



print(f"el {usuario[0]}, {usuario[3]} {usuario[4]} responsable con correo {usuario[1]}")
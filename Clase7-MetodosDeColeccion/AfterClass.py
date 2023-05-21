
#PROGRAMA DE REGISTROS DE VISITANTES

ListaPersonas = [] #lista de personas
Ident = 0 #identificador de usuarios


Login = input("bienvenido a nuestra feria: \n si desea registrarse seleccione la opcion 1\n Si desea buscar su numero de usuario seleccione la opcion 2\n")



while (Login == "1"):  #si  el usuario desea registrarse, se ejecuta el bucle.
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    edad = int(input("Edad: "))
    mail = input("mail: ").lower()
    Ident +=1 #La variable empieza en cero y cada vez que se registre un usuario va usmando un entero
    ListaPersonas.append({
        "Nombre" : nombre,
        "Apellido" : apellido, #creo la clave y completo el valor con la variable completada por el usuario
        "Edad": edad,
        "Mail": mail,
        "ID" : Ident}) #usuario ingresa datos y lo agrego a la lista como un diccionario
    print("Gracias por registrarse" ,nombre, ",su numero de visitante es: ",Ident)

    Login = input("Que desea Hacer?:\n Seleccione 1 para registrar otro usuario \n Seleccione 2 para buscar un usuario\n")
    



while (Login == "2"):
    buscar = input("Para buscar, Ingrese su correo electronico\n") #genero un input para que el usuario ingrese id a buscar

    for persona in ListaPersonas:  #genero un for dentro de la lista personas
        if (persona["Mail"].lower() == buscar.lower()): #le digo al programa que compare el mail ingresado con la lista
            print("Usuario encontrado, Gracias por utilizar nuestro sistema")#si el id  es encontrado printea ambos resultados
            print(persona)
            Login = ""   
        else:
            print("persona no encontrada")
           




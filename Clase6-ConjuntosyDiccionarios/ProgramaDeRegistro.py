
#crear un registro de paises de una convencion, queremos saber que 
#paises nos visitaron



mysetPais = set() #colecciono los paises
myListaPais = [] #Lista de usuarios
seguir = input("desea registrar su pais? escriba SI o NO\n")


#mientras seguir sea igual a "SI", se seguira ejecutando el bucle
#con upper la respuesta del usuario se convierte a mayuscula
while (seguir.upper() == "SI"):
    pais = input("Pais:") #pido al usuario que registre Ssu pais
    seguir = input("desea seguir? escriba SI o NO\n") #pido respuesta para seguir ejecutando
    mysetPais.add(pais.upper()) #guardo los datos en un set, si son paises repetidos solo se registra una vez
    myListaPais.append(pais.upper()) #guardo datos en lista, no se reemplazan paises repetidos

print(f"asistieron {len(mysetPais)} paises a la convencion") #cantidad de paises que asistieron con len, contabiliza por uno los repetidos
print(f"asistienon {len(myListaPais)} paises a la convencion")#cantidad de paises que asistieron con len, contabiliza todos los repetidos


#enumerate sirve para enumerar los resultados
#imprimo con un for recorriendo el set, indico indice y pais como dos datos nuevos a imprimir
print("\n################# LISTA #################")
for indice, pais in enumerate(mysetPais):
    print(f"{indice+1}.- {pais}")


print("\n################# LISTA #################")
for indice, pais in enumerate(myListaPais):
    print(f"{indice+1}.- {pais}")




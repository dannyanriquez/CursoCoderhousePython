#Tipos de coleccion de datos - REPASO

list = [] 
tuple = ()
myset = set()
diccionario = {}

#Recordemos
#Lista, son mutables

myLista = [1,1,2,3,4,5]
#Declaracion vacia
myLista = []



#Tupla, son inmutables
myTupla = (1,1,2,3,4)
#Declaracion vacia
myTupla = ()

#-----------------------------------------------------------
#sets - Reglas
# Solo acepta objetos inmutables dentro (tuplas)
#Tambien heterogeneo osea puede tener cualquier tipo de dato dentro
#No tiene elementos duplicados
# ordena de menor a mayor del 1 al 10 o en orden alfabetico
#No se puede hacer Slicing, ni manejar por indices


mySet = set() #declaracion de un set vacio
mySet = {1,2,3,4} #declarar un set iniciado
print(mySet)




# CONVERTIR UNA LISTA A SET
ListaEjemplo = ["Pablo", "Miguel", "Marcos", 2, 3]
SetEjemplo = set(ListaEjemplo)

# CONVERTIR UNA TUPLA A SET
tuplaEjemplo = ("Pablo", "Miguel", "Marcos", 2, 3)
SetEjemplo = set(tuplaEjemplo)

#SE PUEDE CONVERTIR UN SET A LISTA O TUPLA
ReverseList = list(SetEjemplo)
ReverseList = tuple(SetEjemplo)


#Para agregar,quitar o contar indices dentro del set

setApppends = set(1,4,6,7)

#agregar un Valor, se puede solo 1 a la vez. 
# Para Varios elementos una opcion esonvertir a lista o tupla
setApppends.add(5) 

#Existen tres metodos para remover elementos dentro del set

setApppends.discard(10) #si elemento no existe ignora y no tira error
setApppends.remove(5) #si elemento no existe imprime error

print(len(setApppends)) #contar elementos dentro del set

#ELIMINAR ELEMENTOS CON .pop
#como el set no es ordenado (no tiene indice) no podemos indicar una posicion a eliminar
#se usa para vaciar el SEt y con el while hacemos el bucle y nos indica que va borrando
#segun 3wSchools pop hace un borrado Random

ejemploPop = {"Derick", 3,2,5,4,1,"allan"}

while ejemploPop: #recorro el set eliminando uno por uno los items. El set primero se ordena
    print("se esta borrando:", ejemploPop.pop())



#BUSCAR DENTRO DEL SET utilizando IN

# los resultados son logicos. TRUE o FALSE
print(2 in setApppends) #consulto si este dato esta dentro

#utilizando logica para consultar resultado

if (2 in setApppends):
    print("SI existe dentro del set")
else:
    print("NO existe dentro del set")



#LIMPIAR EL SET

setApppends.clear()
print(setApppends)

#AGREGAR VARIOS ELEMENTOS
SetEjemploDos = {1,2,3,4,5,6,7}

SetEjemploDos.update({4,5,6,8,9})
print(SetEjemploDos) #ordena e imprime


# distinto de listas o tuplas
# NO se puede agregar utilizando este operador  += , si o si usar uptdate


# sin poner  las llaves, cada letra ocupa un indice
SetEjemploDos.update("Dani")

# Con las llaves, la palabra completa ocupa un indice
SetEjemploDos.update({"Leonardo"})

#EN AMBOS CASOS ORDENA POR ORDEN ALFABETICO

# En el caso de agregar numeros,  debe ir con llaves ya que un numero no es iterable
SetEjemploDos.update({11})

print(SetEjemploDos) 




#-----------------------------------------------------------

#DICCIONARIOS

#se compone por Clave:valor
#formato similar al Json en JS. cuando se comunican el Json se puede convertir a diccionario
#el valor se puede repetir, no la clave
#Listas, tuplas y set no pueden convertirse a diccionario

myDiccionario = {} #declarar un dic vacio
colores = {"amarillo":"white","azul":"blue", "rojo": "red"} #declarar un dic inicializado
print(colores)


#Accediendo a a una clave, me devuelve el valor
print(colores["azul"])

#Corregir el valor
colores["amarillo"] = "yellow"
print(colores)

#agregar clave y valor a diccionario
colores["negro"] = "black"
print(colores)

#agregar varios clave/valor
colores.update({"uno":1, "dos":2})
print(colores)


#opcion sin comillas - se pueden agregar todo tipo de dato. Ambas formas son validas
colores.update(booleano = True, booleano2 = False)
print(colores)

#eliminar una clave/valor de un diccionario utilizando del o pop
#el comportamiento es igual al discard (si clave no se encuentra ignora y no ejecuta error)
#para eliminar se debe declarar la clave
del colores["Amarillo"]

#Elimina y da retroalimentacion de lo que elimino. Solo varia la sintaxis
print(colores.pop("uno"))


#----------------------------------



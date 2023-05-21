#METODOS EN STRINGS

#---------------
#Metodo Upper() - retorna caracteres a mayuscula

soyTexto2 = "Hola DeVs COdEr"
print(soyTexto2.upper())


#---------------
#Metodo lower() - retorna caracteres a minuscula

soyTexto2 = "Hola DeVs COdEr"
print(soyTexto2.lower())


#---------------
#Metodo capitalize() - retorna primer caracter de la oracion a mayuscula

soyTexto2 = "Hola DeVs COdEr"
print(soyTexto2.capitalize())


#---------------
#Metodo title() - retorna primer carater de cada palabra a mayuscula

soyTexto2 = "Hola DeVs COdEr"
print(soyTexto2.title())


#---------------
#Metodo count() - retorna X cantidad de veces que encuentra el parametro

soyTexto2 = "Hola DeVs COdEr"
print(soyTexto2.count("e"))

#encuentra solo 1 "e" porque es case sensitive
#ejemplo para primero pasar a minuscula luego contabilizar todas las "e"

print(soyTexto2.lower().count("e"))


#---------------
#Metodo find() - retorna el indice de donde arranca la palabra buscada

soyTexto3 = "Hola amigo como estas amigo!"
print(soyTexto3.find("amigo"))

#si aplicamos la "r" adelante contabiliza la busqueda de derecha a izquierda
#devuelve el primer indice de la ultima palabra encontrada

soyTexto3 = "Hola amigo como estas amigo!"
print(soyTexto3.rfind("amigo"))

#si devuelve -1 es porque no encontro la palabra


#--------------------------------------------------
#join() - #va a poner entre caracteres un "-"
separador = "-"

soyTexto3 = "Hola amigo como estas amigo!"
print(separador.join(soyTexto3))


#--------------------------------------------------
#replace() - reemplaza todas las palabras seleccionadas encontradas
# entre parentesis, primer valor palabra a reemplazar, segundo valor palabra reemlplazante
cadena = "Hola, nosotros vivimos en el planeta marte"
print(cadena)
cadena = cadena.replace("marte", "tierra")
print(cadena)

#si la palabra a reemplazar se repite, podemos seleccionar cual reemplazar
#con el 3 (bandera) le indico que si reemplace esa cantidad de veces 
cadena = "Hola, nosotros vivimos en el planeta marte tiene agua marte marte marte"

cadena = cadena.replace("marte","tierra",3)
print(cadena)


#--------------------------------------------------
#split() - me convierte la oracion en una lista, cada palabra esun indice
cadena = "Hola, nosotros vivimos en el planeta marte tiene agua marte marte marte"
print(cadena.split())

#ahora podemos recorrer esta lista con el for
for palabras in cadena.split():
    print(palabras)

#--------------------------------------------------
#clear() - sirve para limpiar una lista 

mylista = ["a","b","c","d"] #lista Random
mylista.clear()  #limpio la lista
print(mylista)


#--------------------------------------------------
#extend() - concatenar listas

numeros = [1,2,3,4]  
numeros += [5,6,7,8] #concateno en una misma lista utilizando metodo basico
print(numeros)

#ejemplo de extend
numeros2 = [1,2,3,4]
numeros3 = [5,6,7,8]

numeros2.extend(numeros3)
print(numeros2)


#--------------------------------------------------
#insert() - agregar elemento de una lista indicando su posicion
mylistanumeros = [1,2,4,5]
mylistanumeros[2] = 3 #reemplazo un indice utilizando metodo basico
print(mylistanumeros)

#ejemplo de insert - recibe dos parametros, posicion y dato
mylistanumeros = [1,2,4,5]
mylistanumeros.insert(2,3)
print(mylistanumeros)

#para agregar un elemento en el ultimo lugar sin contar podemos utilizar el len
#seria la cantidad mas uno. es mas recomendable utilizar append

mylistanumeros = [1,2,4,5]
mylistanumeros.insert(len(mylistanumeros),6)
print(mylistanumeros)


#--------------------------------------------------
#reverse() - invierte tal cual la lista comenzando de derecha a izquierda
NuevaLista = [1,2,3,4,5]
NuevaLista.reverse()
print(NuevaLista)


#--------------------------------------------------
#sort() - ordena la lista - No se pueden combinar tipo de datos, tira error
listaDesordenada = [2,4,64,77,890,4235,6]
listaDesordenada.sort()
print(listaDesordenada)

#Tambien se puede ordenar en reversa de mayor a menor

listaDesordenada = [2,4,64,77,890,4235,6]
listaDesordenada.sort(reverse=True)
print(listaDesordenada)




#::::::::::::::::::::::::::::::::::::::::::::::::::
#Metodos de coleccion en set

#--------------------------------------------------
#copy - Genera una copia para poder asignar a otra variable
mySet = {1,2,3,4,5}

mySet2 = mySet.copy()
print(mySet2)



#--------------------------------------------------
#isdisjoint() - comparar sets (regla de set no pueden tener valores repetidos)
set1 = {1,2,3}
set2 = {3,4,5}

print(set1.isdisjoint(set2))

#hace una comparacion si es distinta, en este caso se repite el 3
#por lo cual devuelve el booleano false

#La función Python set isdisjoint() verifica si los dos conjuntos son 
# disjuntos o no, si es disjunto, devuelve True; de ​​lo contrario, 
# devolverá False. Se dice que dos conjuntos son disjuntos cuando 
# su intersección es nula. En palabras simples, no tienen ningún 
# elemento común entre ellos. 

#--------------------------------------------------
#issubset() -Devuelve True si todos los elementos del set3
# están presentes en el set4


set3 = {-1,99}
set4 = {1,2,3,4,5}

print(set3.issubset(set4))

#--------------------------------------------------
#issuperset() -Devuelve True si TODOS los elementos del set4
# están presentes en el set5



set4 = {1,2,3}
set5 = {1,2}

print(set4.issuperset(set5))

#en este caso da False porque el set4 no esta dentro de set5

set5 = {1,2,3}
set6 = {1,2}

print(set5.issuperset(set6))

#en este caso da True porque los elementos del set6 SI esta dentro del set5



#--------------------------------------------------
#union() -Devuelve un Set que contiene todos los elementos de ambos conjuntos, 
# se excluyen los duplicados:


set7 = {1,4,6}
set8 = {1,3,4,53,6}

setFinal = set7.union(set8)
print(setFinal)

#--------------------------------------------------
# difference() Devuelve un conjunto que contiene los elementos que solo existen en el conjunto
# set7 no en el conjunto set8

set7 = {1,4,5,34,6}
set8 = {1,3,4,53,6}

resultado = set7.difference(set8)

print(resultado)


#--------------------------------------------------
# difference_update() Devuelve un conjunto que contiene los elementos que solo existen en el conjunto
# set7 y no en el conjunto set8 y lo guarda en el set7

set7 = {1,4,5,34,6}
set8 = {1,3,4,53,6}

set7.difference_update(set8)
print(set7)


#--------------------------------------------------
# intersection() Devuelve un conjunto que contiene los elementos que existen tanto en 
# set7 como en set8

set7 = {1,4,5,34,6}
set8 = {1,3,4,53,6}

print(set7.intersection(set8))

#--------------------------------------------------
# intersection:update() Devuelve un conjunto que contiene los elementos que existen tanto en 
# set7 como en set8, guarda en resultado en set7.

set7 = {1,4,5,34,6}
set8 = {1,3,4,53,6}

set7.intersection_update(set8)
print(set7)

#::::::::::::::::::::::::::::::::::::::::::::::::::

#Metodos de coleccion en diccionarios

#Keys - Metodo para obtener todas las claves-. 

colores = { 
    
    "amarillo":"yellow", 
    "azul":"blue", 
    "verde":"green" 

}

print(colores.keys())



#values - Metodo para obtener todos los valores. 

colores = { 
    
    "amarillo":"yellow", 
    "azul":"blue", 
    "verde":"green" 

}

print(colores.values())


#como obtener un valor de un indice
color = list(colores.values()) # convierto el diccionario en lista y traigo los valores
             
print(color[0]) #selecciono el indice a imprimit dentro de la nueva lista



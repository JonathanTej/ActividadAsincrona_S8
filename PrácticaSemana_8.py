#Creación de datos para 10 humanos. 
# print ("Aqui definiremos los 10 Humanos")
Human1= "ana"
Human2= "alicia"
Human3= "jonathan"
Human4="mauricio"
Human5="nestor"
Human6="juan"
Human7="lisandro"
Human8="marilyn"
Human9="rené"
Human10="carlos"
#Aqui difiniremos su Pais  y Gentilicio
Ana="El Pais de Ana es Chile y el gentilicio es Chilenos"
Alicia="El Pais de Alicia de Corea y su gentilicio es Coreanos"
Jonathan="El Pais de Jonathan es Rusia y su gentilicio es Rusos "
Mauricio="El Pias de Mauricio es Italia y su gentilicio es Italianos"
Nestor= " El Pais de Nestor China y su gentilicio es Chinos"
Juan="El Pais de Juan es Alemania y su gentilicio es Alemanes"
Lisandro="El Pais de Lisandro de Brasil y su gentilicio es Brasileños"
Marilyn="El Pis de Marilyn es Costa Rica y Su gentilicio es Costarricenses"
René="El Pais de René es Canadá y su gentilicio es  Canadienses"
Carlos="El Pais de Carlos es Guatemala y su gentilicio es Guatemaltecos"  
#En este apartado definiremos los animales y sus variables . 
ani1= "Perro"
ani2= "Gato,"
ani3= "Tigre,"
ani4= "Leopardo,"
ani5= "Pantera"
ani6= "Murcielago,"
ani7= "Vaca,"
ani8= "Carpincho"
ani9= "Raton"
ani10= "Ardilla"
#En este apartado definiremos el tipo de animales que conforman la especie elegida.
Esp1= "canino"
Esp2= "felino"
Esp3= "mamifero"
Esp4= "roedor"

print("Menu de opciones:\n")
print("PRESIONE 1 : Para selecionar el nombre de un humano y Determinar su País y Gentilicio \n")
print("PRESIONE 2 : Para elegir la especie de Animales  \n")

opcion = int(input("¿Cual es la opcion que deseas seleccionar?: "))

if opcion == 1:
    print("Ha seleccionado la opción de humanos")
    
    print("MENÚ DE NOMBRES HUMANOS A LOS QUE SE DETERMINARÁ EL PAIS Y GENTILICIO : Ana , Alicia , Jonathan, Mauricio, Nestor, Juan, Marilyn, Lisandro, René, Carlos")

    NombreH=input("Ingrese el nombre del humano :").lower()
        #CREANDO CONTROL IF EILIF PARA HUMANOS

    if NombreH == Human1:
        print("El pais y gentilicio de Ana son :" , Ana )
    elif NombreH == Human2:
        print("El pais y gentilicio de Alicia son :" , Alicia)
    elif NombreH == Human3:
        print("El pais y gentilicio de Jonathan son :" ,Jonathan)
    elif NombreH == Human4:
         print("El pais y gentilicio de Mauricio son :" , Mauricio)
    elif NombreH== Human5:
        print("El pais y gentilicio de Nestor son :", Nestor )
    elif NombreH==Human6:
        print("El pais y gentilicio de Juan son :" , Juan)
    elif NombreH==Human7:
        print("El pais y gentilicio de Lisandro son :" ,Lisandro)
    elif NombreH== Human8:
        print("El pais y gentilicio de Marilyn son : " , Marilyn) 
    elif NombreH==Human9:
        print("El pais y gentilicio de René son : " , René)   
    elif NombreH==Human10: 
         print("El pais y gentilicio de Carlos son :", Carlos)
    else :
        print("El dato ingresado no se encuentra en la lista")
    
elif opcion == 2:
    print("Ha seleccionado la opción de animales \n")
    print("EL MENU DE LAS ESPECIES ANIMALES ES : Canino, Felino, Mamifero y Roedor. \n")
    
    #Creando estructura if eilif para animles.
    Animal= input("Ingrese el nombre de una especie antes mencionada: ").lower()

    if Animal==Esp1:
        print("El animal clasificado en esta especie es:",ani1)
    elif Animal==Esp2:
        print("Los animales clasificados en esta especie son: ",ani2, ani3, ani4, ani5)
    elif Animal==Esp3:
        print("Los animales clasificados en esta especie son: ",ani6, ani7, ani8)
    elif Animal==Esp4:
        print("Los animales clasificados en esta especie son: ",ani9,"y", ani10)
    else:
        print("El nombre de la especie ingresada no se encuentra en la lista.")
    
    
else:
    print("La opción que ha seleccionado es invalida \n")

#Capturamos el nombre del humano en el menú e ingresamos desde el teclado 
print("Fin del Programa")

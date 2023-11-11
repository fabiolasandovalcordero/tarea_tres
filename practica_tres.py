examen=[]

def menu():
    print ("Las opciones del Menu son las siguientes: ")
    print ("1. Agregar preguntas.")
    print ("2. Modificar preguntas.")
    print ("3. Eliminar preguntas.")
    print ("4. Crear examen.")
    print ("0. Salir.")
    
def elegir_opcion():
    opc= int(input("Ingrese la opcion que desea realizar: "))
    return opc

def agregar_pregunta():
    enunciado= input("Ingrese el enunciado de la pregunta: ")
    opciones= input("Ingrese las opciones: ").split("\n")
    respuesta= int(input("Ingrese la opcion correcta:"))
    pregunta=(enunciado,opciones,respuesta)
    examen.append(pregunta)
    return examen

def modificar_pregunta():
    indice=int(input("Ingrese la pregunta que desea modificar: "))
    pregunta=examen[indice]
    enunciado= input("Ingrese la modificacion de la pregunta: ")
    opciones= input("Ingrese las opciones: ").split("\n")
    respuesta= int(input("Ingrese la opcion correcta:"))
    pregunta["Enunciado"]= enunciado
    pregunta["Opciones"]= opciones
    pregunta["Respuesta correcta"]= respuesta
    examen.pop(pregunta)
    return examen

def eliminar_preguntas():
    pregunta=int(input("Ingrese la pregunta que desea modificar: "))
    examen.remove(pregunta)
    return examen

def crear_examen():
    nuevo_examen=list(examen)
    return nuevo_examen

#-------------------------
pregunta=["Enunciado","Opciones","Respuesta correcta"]

while True:
    menu()
    opc= elegir_opcion()
    if opc == 1:
        agregar_pregunta()
    elif opc == 2:
        modificar_pregunta()
    elif opc == 3:
        eliminar_preguntas()
    elif opc ==4:
        examen_creado = crear_examen()
        print("Su examen es el siguiente:", examen_creado)
    else:
        print("La opcion digitada no es correcta, intente de nuevo")


#Proyecto 2: Gestor de Tareas
import os

def crear_tarea():

    nuevo_dato = str(input('Introduzca la nueva tarea: '))
    with open('lista.txt','a') as archivo:
        archivo.write(nuevo_dato+'\n')

def eliminar_tarea(pos): 
    with open('lista.txt','r') as archivo: 
        lineas = archivo.readlines() 
        lineas.pop(pos) 
    with open('lista.txt','w') as archivo: 
        archivo.writelines(lineas)

def visualizar_tarea():
    with open('lista.txt','r') as archivo:
        lista = archivo.read()
    return print(lista)    


while True:
    print('1.Crear tarea.\n2.Eliminar tarea\n3.Visualizar tarea')
    opc =int(input('Introduce la opcion deseada: '))
    
    if opc == 1:
        os.system('cls')
        crear_tarea()
        input('Presione Enter para continuar...')
        os.system('cls')
    
    elif opc == 2:
        os.system('cls')
        pos = int(input('Introduzca el indice de la lista a eliminar: '))
        eliminar_tarea(pos)
        input('Presione Enter para continuar...')
        os.system('cls')
    elif opc == 3:
        os.system('cls')
        visualizar_tarea()
        input('Presione Enter para continuar...')
        os.system('cls')
    elif opc == 4:
        print('Saliendo...')
        break    
    else: 
        print('Introduzca una de las opciones ...')
        

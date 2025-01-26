#Proyecto 3: Conversor de Unidades

def convert_longitud(dato,opc2):
    if opc2 == 1: return dato/10
    elif opc2 == 2: return dato/100
    elif opc2 == 3: return dato/1000

def convert_peso(dato,opc2):
    if opc2 == 1: return dato/1000
    elif opc2 == 2: return dato/1000000



while True:
    print('1.Conversor Longitud \n2.Conversor Peso \n3.Salir \n')
    opc = int(input('Introduzca la opcion deseada: '))
    
    if opc == 1:
        dato = float(input('Introduzca el dato en cm a convertir: '))
        
        print('1.Convertir a dm \n2.Convertir a m \n3.Convertir a km')
        opc2 = int(input('Elija a que convertirlo: '))
        
        print(convert_longitud(dato,opc2))
    elif opc == 2:
        dato = float(input('Introduzca el dato en g a convertir: '))

        print('1.Convertir a kg \n2.Convertir a T ')
        opc2 = int(input('Elija a que convertirlo: '))

        print(convert_peso(dato,opc2))
    elif opc == 3:
        print('Saliendo...')
        break
    else: 
        print('Seleccione una de las opciones')
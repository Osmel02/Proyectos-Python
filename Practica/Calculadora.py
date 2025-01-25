# Proyecto 1: Calculadora de Operaciones Básicas
import os

def calculadora(opc,dato1,dato2):
    if opc == 1: return dato1+dato2
    elif opc == 2: return dato1-dato2
    elif opc == 3: return dato1*dato2
    elif opc == 4: return dato1/dato2
    

    
while True:
    print(' 1.Sumar\n 2.Restar\n 3.Multiplicar\n 4.Dividir\n 5.Salir')
    opc = int(input('Introduzca la opc deseada: '))
      
    
    if opc in [1,2,3,4]:
        dato1 = float(input('Dato1: '))
        dato2 = float(input('Dato2: '))  
        
        os.system('cls')
        print(f'El resultado es: {calculadora(opc,dato1,dato2)}')
        input('Presione Enter para continuar ...')
        os.system('cls')
    elif opc == 5: 
        os.system('cls')
        print('Saliendo ...')
        break
        
    else : print('Escoja una de las opciones ...')   
import os

def area_poligono(tipo):
    if tipo == 1: #triangulo
        base = float(input('Introduzca la base: '))
        altura = float(input('Intruduzca la altura: '))
        area = base * altura / 2
        return area
    elif tipo == 2: # cuadrado
        lado = float(input('Introduzca el lado del cuadrado: '))
        area = lado * lado
        return area
    elif tipo == 3:
        lado_1 = float(input('Introduzca el lado 1: '))
        lado_2 = float(input('Introduzca el lado 2: '))
        area = lado_1 * lado_2
        return area

while True:
    
    os.system('cls')
    print('1. Area del triangulo')
    print('2. Area del cuadrado')
    print('3. Area del rectangulo')
    print('4. Salir')
    opc = int(input('Introduzca la opcion deseada: '))
    

    if opc in [1,2,3]:
        resultado = area_poligono(opc)
        os.system('cls')
        print(f'Resultado del area: {resultado}')
    elif opc == 4:
        os.system('cls')
        input(print('Presione enter para salir.'))
        break 
    else:
        print('Debe seleccionar una opcion valida ...')
    input('Presione enter para continuar...')
def anagrama(palabra1,palabra2):
    if len(palabra1) != len(palabra2):
        return False
    
    lista1 = sorted(palabra1)
    lista2 = sorted(palabra2)
    
    if lista1 == lista2: return True
    else: return False


palabra1= str(input('Palabra1: '))
palabra2= str(input('Palabra2: '))
print(anagrama(palabra1,palabra2))
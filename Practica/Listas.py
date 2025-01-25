lista = [3,3,4,5,6]
lista2 =lista.copy()
print(lista2)
if lista == lista2 : print('Son iguales')

tupla = tuple(lista)
conjunto = set(lista)
print(tupla)
print(conjunto)
conjunto2 = {2,3,3,4,5,44}
print(conjunto2)

diccionario = {
    1: 'Hop',
    2: 'Cash',
    3: 'Exit'
}
print(diccionario.values())
string = str("Mi nombre es Osmel")
print(len(string))
set.clear(conjunto2)
print(conjunto2)
conjunto.clear()
print(conjunto)


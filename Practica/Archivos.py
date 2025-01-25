texto = "Mi nombre es Osmel ."

with open('Nuevo_archivo.txt','w') as archivo:
    archivo.write(texto)
   
with open('Nuevo_archivo.txt','a') as archivo:
    archivo.write('\nHola de nuevo \n')
       
with open('Nuevo_archivo.txt','r') as archivo:
    contenido = archivo.read()
    print(contenido)
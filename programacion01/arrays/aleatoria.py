mi_lista = [-1] * 5

while True:
    index = int(input("ingrese la posicion"))
    
    numero = int(input("ingrese un numero"))
    
    mi_lista[index - 1] = numero
    
    seguir = input("continua? yes/no")
    if seguir == "no":
        break
    
for i in range(len(mi_lista)):
    if mi_lista[i] != -1:
        print(mi_lista[i])    
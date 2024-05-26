c = 0
def swap(a: int, b: int):  #Esta funcion llamada Swap toma dos valores y los intercambia
    return b,a

def particionar(array, low, high): #La funcion particionar elige el ultimo elemento de la lista y lo utiliza como pivote, significa que va a usarla para dividir la lista,
                                        #en dos partes, una menor y otra mayor que el pivote

    pivote = array[high] #El pivote se selecciona como el último elemento de la lista.
    i = low - 1
        
    for j in range(low, high): # La función itera sobre los elementos de la lista desde el primer elemento (low) hasta el penúltimo elemento. Esto excluye el pivote, ya que ya está al final.    
           if array[j] <= pivote: # Se verifica si el elemento actual (array[j]) es menor o igual al pivote
            i += 1
            array[i], array[j] = swap(array[i], array[j])
    
    array[i + 1], array[high] = swap(array[i + 1], array[high] ) # Se intercambia el elemento en la posición i con el elemento en la posición j.,
                                                                    #Mueve el elemento menor o igual al pivote a la izquierda, mientras que mantiene los elementos mayores en su posición actual.
    
    return i + 1 #Retorna la posición del pivote
    
def quick_sort(array, low, high):  #Toma tres parámetros: la lista que se va a ordenar, low que es el índice más bajo actual y high que es el índice más alto actual.
    global c
    c += 1
    if low < high: 
        pi = particionar(array, low, high) #Se llama a la función particionar para seleccionar un pivote y dividir la lista en dos partes:,
                                            #una con elementos menores o iguales al pivote y otra con elementos mayores al pivote.
        quick_sort(array, low, pi - 1)     #Se llama a la función quick_sort para ordenar cada parte de la lista.  El proceso continúa hasta que la lista tiene un solo elemento (low >= high),
                                            #lo que significa que ya está ordenado y no es necesario hacer más particiones.
                                            #En cada llamada recursiva se incrementa la variable global c, que cuenta el número de veces que se realiza el proceso. Esto proporciona el rendimiento del algoritmo.
        quick_sort(array, pi + 1, high)
        

import time

vector = [5,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,1,9,7,3,1,9,7,3,1,9,7, #Esta es la lista que se va a ordenar
          3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3]
start = time.time()  #Se inicia un temporizador antes de llamar a la función de ordenamiento para medir el tiempo en milisegundos de ejecución.
quick_sort(vector, 0 , len(vector) - 1) #Se llama a la función de ordenamiento con el array vector y los índices más bajo y más alto.
end = time.time()  #Se detiene el temporizador despues de la ejecución de la función de ordenamiento.
print(end)
print(start) #Se imprime el tiempo de ejecución en milisegundos
print(f"Tiempo: {(end - start)*1000}") #Se imprime el tiempo de ejecución en milisegundos
print(c)
print(len(vector)) #Se imprime la longitud del array
print(vector) #Se imprime el array

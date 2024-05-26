import time

numeros_desordenados = [ #puse una listota para probar time
    985, 724, 360, 551, 782, 843, 175, 670, 315, 831, 901, 128, 732, 592, 493, 316,
    254, 961, 443, 695, 588, 99, 218, 39, 965, 703, 860, 797, 235, 986, 67, 550, 
    786, 777, 823, 252, 297, 782, 60, 662, 428, 374, 923, 365, 135, 54, 401, 675,
    855, 609, 380, 259, 102, 377, 657, 161, 206, 36, 370, 717, 869, 712, 514, 608,
    334, 824, 414, 947, 286, 651, 426, 432, 938, 149, 654, 200, 683, 253, 571, 818,
    68, 455, 747, 845, 800, 15, 691, 151, 676, 773, 853, 122, 593, 42, 45, 820, 690,
    503, 178, 956, 525, 181, 232, 867, 809, 535, 642, 866, 92, 926, 458, 401, 458,
    574, 243, 280, 476, 505, 942, 834, 219, 624, 976, 41, 305, 993, 388, 935, 686,
    513, 210, 657, 21, 936, 193, 980, 712, 925, 991, 170, 313, 325, 690, 120, 210,
    227, 791, 325, 690, 187, 466, 923, 735, 238, 489, 572, 373, 874, 586, 763, 866,
    546, 596, 202, 929, 840, 309, 825, 69, 724, 357, 516, 114, 71, 777, 162, 924, 
    14, 509, 431, 570, 151, 454, 897, 815, 660, 568, 869, 39, 883, 684, 736, 445, 
    906, 159, 777, 889, 610, 249, 85, 154, 337, 112, 97, 640, 760, 850, 102, 165,
    416, 464, 294, 859, 296, 321, 573, 312, 343, 179, 980, 374, 508, 429, 994, 225,
    54, 688, 229, 869, 305, 198, 120, 283, 588, 767, 635, 254, 676, 673, 325, 888,
    84, 777, 21, 383, 712, 202, 700, 157, 174, 241, 577, 755, 615, 685, 60, 594, 
    902, 230, 352, 670, 51, 874, 500, 971, 423, 366, 884, 370, 522, 334, 242, 527,
    104, 352, 935, 459, 719, 867, 402, 177, 68, 282, 97, 972, 147, 307, 501, 685,
    147, 810, 987, 413, 856, 897, 592, 491, 882, 105, 209, 254, 180, 794, 508, 722,
    213, 931, 749, 324, 541, 535, 14, 1000, 635, 138, 435, 860, 526, 251, 877, 759,
    333, 142, 121, 920, 470, 771, 889, 830, 739, 126, 732, 573, 776, 846, 708, 525,
    777, 573, 275, 674, 413, 590, 448, 127, 792, 376, 418, 404, 731, 656, 485, 394,
    361, 733, 332, 901, 29, 634, 382, 524, 915, 28, 196, 58, 1000, 331, 946, 726, 
    535, 692, 758, 246, 642, 98, 779, 590, 727, 930, 224, 131, 308, 72, 34, 414, 
    535, 111, 432, 53, 174, 50, 147, 809, 209, 108, 623, 588, 666, 897, 333, 445, 
    15, 320, 786, 126, 647, 841, 743, 434, 975, 699, 943, 650, 117, 428, 712, 835, 
    109, 848, 905, 151, 26, 17, 929, 442, 768, 541, 402, 262, 897, 810, 716, 363, 
    998, 767, 975, 832, 685, 215, 986, 472, 668, 147, 241, 887, 698, 7, 970, 785, 
    833, 679, 66, 13, 963, 671, 297, 112, 681, 291, 967, 850, 234, 464, 974, 138, 
    429, 348, 950, 380, 549, 878, 447, 685, 542, 131, 538, 930, 616, 124, 898, 786, 
    985, 724, 360, 551, 782, 843, 175, 670, 315, 831, 901, 128, 732, 592, 493, 316,
    254, 961, 443, 695, 588, 99, 218, 39, 965, 703, 860, 797, 235, 986, 67, 550, 
    786, 777, 823, 252, 297, 782, 60, 662, 428, 374, 923, 365, 135, 54, 401, 675,
    855, 609, 380, 259, 102, 377, 657, 161, 206, 36, 370, 717, 869, 712, 514, 608,
    334, 824, 414, 947, 286, 651, 426, 432, 938, 149, 654, 200, 683, 253, 571, 818,
    68, 455, 747, 845, 800, 15, 691, 151, 676, 773, 853, 122, 593, 42, 45, 820, 690,
    503, 178, 956, 525, 181, 232, 867, 809, 535, 642, 866, 92, 926, 458, 401, 458,
    574, 243, 280, 476, 505, 942, 834, 219, 624, 976, 41, 305, 993, 388, 935, 686,
    513, 210, 657, 21, 936, 193, 980, 712, 925, 991, 170, 313, 325, 690, 120, 210,
    227, 791, 325, 690, 187, 466, 923, 735, 238, 489, 572, 373, 874, 586, 763, 866,
    546, 596, 202, 929, 840, 309, 825, 69, 724, 357, 516, 114, 71, 777, 162, 924, 
    14, 509, 431, 570, 151, 454, 897, 815, 660, 568, 869, 39, 883, 684, 736, 445, 
    906, 159, 777, 889, 610, 249, 85, 154, 337, 112, 97, 640, 760, 850, 102, 165,
    416, 464, 294, 859, 296, 321, 573, 312, 343, 179, 980, 374, 508, 429, 994, 225,
    54, 688, 229, 869, 305, 198, 120, 283, 588, 767, 635, 254, 676, 673, 325, 888,
    84, 777, 21, 383, 712, 202, 700, 157, 174, 241, 577, 755, 615, 685, 60, 594, 
    902, 230, 352, 670, 51, 874, 500, 971, 423, 366, 884, 370, 522, 334, 242, 527,
    104, 352, 935, 459, 719, 867, 402, 177, 68, 282, 97, 972, 147, 307, 501, 685,
    147, 810, 987, 413, 856, 897, 592, 491, 882, 105, 209, 254, 180, 794, 508, 722,
    213, 931, 749, 324, 541, 535, 14, 1000, 635, 138, 435, 860, 526, 251, 877, 759,
    333, 142, 121, 920, 470, 771, 889, 830, 739, 126, 732, 573, 776, 846, 708, 525,
    777, 573, 275, 674, 413, 590, 448, 127, 792, 376, 418, 404, 731, 656, 485, 394,
    361, 733, 332, 901, 29, 634, 382, 524, 915, 28, 196, 58, 1000, 331, 946, 726, 
    535, 692, 758, 246, 642, 98, 779, 590, 727, 930, 224, 131, 308, 72, 34, 414, 
    535, 111, 432, 53, 174, 50, 147, 809, 209, 108, 623, 588, 666, 897, 333, 445, 
    15, 320, 786, 126, 647, 841, 743, 434, 975, 699, 943, 650, 117, 428, 712, 835, 
    109, 848, 905, 151, 26, 17, 929, 442, 768, 541, 402, 262, 897, 810, 716, 363, 
    998, 767, 975, 832, 685, 215, 986, 472, 668, 147, 241, 887, 698, 7, 970, 785, 
    833, 679, 66, 13, 963, 671, 297, 112, 681, 291, 967, 850, 234, 464, 974, 138, 
    429, 348, 950, 380, 549, 878, 447, 685, 542, 131, 538, 930, 616, 124, 898, 786, 
    849, 794, 752, 68, ]

def ordenamiento_danza(numeros): #Algoritmo de burbuja
    start_time = time.time()  # tiempo de inicio
    
    lista_numeros = len(numeros)  # Esto guarda la longitud de la lista
    # Se itera sobre todos los elementos
    for i in range(lista_numeros): 
        for j in range(0, lista_numeros - i - 1): 
            if numeros[j] > numeros[j+1]: #numero[j] es el primer elemento / numero[j] > numero[j+1] verifica si el número actual es mayor que el siguiente número
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j] # Si es mayor, se realiza un intercambio de valores entre numeros[j] y numeros[j+1]
    
    end_time = time.time()  # Finaliza el tiempo
    elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido
    print("Tiempo de ejecución Algoritmo Ordenamiento_Danza:", elapsed_time, "segundos")
    
    return numeros


ordenados = ordenamiento_danza(numeros_desordenados)
#print(ordenados)

import time

def selection_sort(numeros):
    start_time = time.time()  # tiempo de inicio
    
    lista_numeros = len(numeros) # Esto guarda la longitud de la lista
    for i in range(lista_numeros): # Se itera sobre todos los elementos
        min_idx = i # El primer elemento de la lista es el menor
        for j in range(i+1, lista_numeros): # Se itera sobre todos los elementos
            if numeros[j] < numeros[min_idx]: # Verifica si el elemento actual es menor que el menor
                min_idx = j # El elemento actual es el menor
        numeros[i], numeros[min_idx] = numeros[min_idx], numeros[i] # Realiza el intercambio del elemento menor con el elemento actual
    
    end_time = time.time()  # Finaliza el tiempo
    elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido
    print("Tiempo de ejecución de Algoritmo de Selección:", elapsed_time, "segundos")
    
    return numeros

ordenamiento = selection_sort(numeros_desordenados)
#print(ordenados)


def quick_sort(numeros):
    if len(numeros) <= 1: # Verifica si la lista tiene solo un elemento
        return numeros
    
    pivote = numeros[0] #selecciona el primer elemento como pivote
    menores = [] # Lista vacia para los elementos menores o iguales al pivote
    mayores = [] # Lista vacia para los elementos mayores al pivote
    
    # Iterar sobre los elementos de la lista (excepto el primero) para clasificar
    for numero in numeros[1:]: #Recorre todos los elementos de la lista excepto el primero
        if numero <= pivote: # Verifica si el elemento es menor o igual al pivote
            menores.append(numero) # Agrega el elemento a la lista de elementos menores o iguales al pivote
        else:
            mayores.append(numero) # Agrega el elemento a la lista de elementos mayores al pivote
    
    return quick_sort(menores) + [pivote] + quick_sort(mayores) # Llama recursivamente a quick_sort con la lista menores y con la lista de mayores, 
                                                                    #y combina las listas ordenadas menores y mayores con el pivote en el medio.
def quick_sort_time(numeros):
    start_time = time.time()  # Tiempo de inicio
    tiempo = quick_sort(numeros) # Llama a la función quick_sort para ordenar la lista
    end_time = time.time()  # Tiempo de finalización
    elapsed_time = end_time - start_time  # Tiempo transcurrido
    print("Tiempo de ejecución Algoritmo de quick Sort:", elapsed_time, "segundos")
    return tiempo

ordenados = quick_sort(numeros_desordenados)
ordenados = quick_sort_time(numeros_desordenados)
#print(ordenados)



# import time
# start = time.time()
# vector = [1,4,3,5,2]
# largo = len(vector)
# c = 0

# for i in range(largo - 1):
#     minimo_indice = i

#     for j in range( i + 1,largo):
#         if vector[j] < vector[minimo_indice]:
#             c += 1
#             minimo_indice = j
    
#     auxiliar = vector[i]
#     vector[i] = vector[minimo_indice]
#     vector[minimo_indice] = auxiliar
    
# end = time.time()
# print(c)
# print((end - start) * 1000)   

# print(vector)         
   
A = [4,3,2,5,6,3,6]
for i in range(0,len(A)):
    #buscar el menor
    min_index = i
    for j in range(i + 1,len(A)):
        if A[min_index ] > A[j]:
            min_index = j
    #intercambiar
    auxiliar = A[min_index]
    A[i] = A[min_index]
    A[min_index] = auxiliar    
    
print(A)        

# poneme al mas pequeño o al mas grande(dependiendo como lo quiero ordenar) al encontrarlo se posisiciona al principio del array(original)
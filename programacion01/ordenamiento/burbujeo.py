import time

array = [1,4,3,5,2]
start = time.time()

for i in range(0,len(array) - 1):
    for j in range(i + 1,len(array)):
        if array[i] < array[j]:
            auxiliar = array[i]
            array[i] = array[j]
            array[j] = auxiliar

end = time.time()
print(start)
print(end)

print((end - start) * 1000)    
print(array)
     

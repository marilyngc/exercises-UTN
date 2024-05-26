# This Python code snippet is implementing a simple sorting algorithm known as Bubble Sort.
vector = [3,8,1,4,7]
for i in range(0,len(vector)):
    for j in range( i + 1, len(vector) ):
        if vector[i] < vector[j]:
            auxiliar = vector[i]
            vector[i] = vector[j]
            vector[j] = auxiliar

print(vector)            
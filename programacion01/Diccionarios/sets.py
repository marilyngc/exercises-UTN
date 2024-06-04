mi_set = {5,6,7,5,5,9,8,1,-6}

mi_set.add(100)

mi_set.remove(9)

## para que no se rompa ##
mi_set.discard(5)

## elimina el elemento 0 #######
elemento = mi_set.pop()


### vacia el set #######
mi_set.clear()


########### CONJUNTOS ###########

set_a = {3,4,5}
set_b = {6,2,3}

union = set_a.union(set_b)
print(union)

interseccion = set_a.intersection(set_b)
print(interseccion)

diferencia = set_a.difference(set_b)
print(diferencia)
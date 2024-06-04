tupla = (5,6,[0,7,8])

tupla[2][0] = 250
print(tupla)

### "crear" ###

tupla = (5, )
print(len(tupla))


negro = (0,0,0)

tupa_dos = (4,9,6,4)
# a = tupla[0]
# b = tupla[1]
# c = tupla[2]

a,b,c = tupla
print(a,b,c)

### metodos de consulta ###


### para consultar cuantas veces aparece el 4
print(tupa_dos.count(4))

### para consultar la posicion ###
print(tupa_dos.index(9))


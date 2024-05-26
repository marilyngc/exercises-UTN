
from class_personaje import Personaje

def mostrar_personaje(un_personaje:Personaje):
    print(f"{un_personaje.nombre} - {un_personaje.poder_pelea} - {un_personaje.super_poder}")



personaje_1 = Personaje("IroMan",True,True,"Tener plata",500)
personaje_2 = Personaje("Thor",False,True,"Trueno",700)

lista_heroes:list[Personaje] = []
lista_heroes.append(personaje_1)
lista_heroes.append(personaje_2)

for heroe in lista_heroes:
    print(heroe.describirse())

# mostrar_personaje(personaje_1)
# mostrar_personaje(personaje_2)

lista_heroes.pop(2)

# ###### VOLAR ####
# personaje_1.saber_volar(1000,200)

# ######## ATACAR #########
# personaje_2.atacar(personaje_1) # personaje 2 ataca a personaje 1


# print(personaje_1.describirse())
# print(personaje_2.describirse())

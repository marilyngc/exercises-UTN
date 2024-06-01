from class_boligrafo import Boligrafo


escritura_uno = Boligrafo( 1, "Azul")
escritura_dos = Boligrafo( 2, "Rojo")

lista_escritura :list[Boligrafo] = []
lista_escritura.append(escritura_uno)
lista_escritura.append(escritura_dos)

for escritura in lista_escritura:
    print(escritura.escribir("hola"))
    print(escritura.recargar(50))
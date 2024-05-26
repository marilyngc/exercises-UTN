class Personaje:
    # ATRIBUTOS (CARACTERISTICAS)
    
    
    # METODOS (COMPORTAMIENTO)
    def __init__(self,nombre: str,nano:bool,vuela:bool,poder:str,pelea:int): ## SELF => algo propio
        self.nombre = nombre
        self.usa_nanotecnologia = nano
        self.puede_volar = vuela
        self.super_poder = poder
        self.poder_pelea = pelea
    #Proedad(modifica el valor del dato y/o mostrarlo)
    def describirse(self) -> str:
        cadena = f"{self.nombre} - {self.super_poder} - {self.poder_pelea}"
        if self.usa_nanotecnologia:
            cadena += "- Usa nanotecnologia"    
        else:
            cadena += "- NO usa nanotecnologia"
        
        return cadena    
    
    def saber_volar(self,altura,velocidad):
        if self.puede_volar:
            cadena = f"Estoy volando a {altura} mts de altura, a una velocidad de {velocidad} km/H"    
        else:
            cadena = f"Usted {self.nombre} no puede volar"    
        return cadena    
    
    def atacar(self, enemigo: 'Personaje'):
        if self.poder_pelea > enemigo.poder_pelea:
            enemigo.poder_pelea -= self.poder_pelea 
            enemigo.poder_pelea = 0
            cadena = f"GANÓ: {self.nombre}"
        elif self.poder_pelea < enemigo.poder_pelea:
            self.poder_pelea  -=  enemigo.poder_pelea
            cadena = f"GANÓ: {enemigo.nombre}"
        else:
            cadena = f"EMPATARON"
        return cadena                
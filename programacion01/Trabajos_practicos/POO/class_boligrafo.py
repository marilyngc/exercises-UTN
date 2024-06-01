from package_input.validate import *

class Boligrafo:
    
    def __init__(self,grosor_tinta, color,):
        self.capacidad_tinta = 100
        self.grosor_tinta = grosor_tinta
        self.color = color
        self.cantidad_tinta = 80
    
    def escribir(self,texto:str) -> str:
        cantidad_caracteres = len(texto)
        cantidad_tinta_grosor = validar_grosor(cantidad_caracteres, self.grosor_tinta)
        tinta_suficiente = validar_tinta( self.cantidad_tinta, cantidad_tinta_grosor)

        if tinta_suficiente:
            self.cantidad_tinta -= cantidad_tinta_grosor
            mensaje =f"usted ingresó: {texto}, queda de tinta: {self.cantidad_tinta}"

        else:
            mensaje = "No alcanza la tinta"   
        return mensaje
            
    def recargar(self,cantidad_ingresada):
        cantidad_num = int(cantidad_ingresada)
        mensage = validar_recarga(cantidad_num, self.cantidad_tinta, self.capacidad_tinta)
        
        return mensage      
            
        
        
            
                      
        
        
           
    
        
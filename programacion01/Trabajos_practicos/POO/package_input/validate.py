def validar_tinta( cantidad, grosor) -> bool:
    tinta_valida = False

    if grosor < cantidad:
        tinta_valida = True
    else:
        tinta_valida = False
    
    return tinta_valida        

def validar_grosor(texto, grosor):
    if grosor == 1:
        caracteres_totales = texto * 1
    else:
        caracteres_totales = texto * 2
    return caracteres_totales    

def validar_recarga(cantidad_recibida, cantidad_tinta, capacidad_tinta):
    suma_cantidades = cantidad_recibida + cantidad_tinta
    if suma_cantidades < capacidad_tinta:
        cantidad_tinta += cantidad_recibida
        mensaje = f"lapicera recargada con {cantidad_recibida}, tinta total: {suma_cantidades}"
        
    else:
        resto_cantidad = suma_cantidades - capacidad_tinta
        cantidad_tinta = capacidad_tinta
        mensaje = f"se recargó la lapicera con {cantidad_recibida} y sobró: {resto_cantidad}"
    
    return mensaje
        
            
            
            
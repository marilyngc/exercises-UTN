"""Desarrollar una función que reciba como parametros el precio de un producto, la cantidad y el porcentaje de descuento que se aplicara si la cantidad de productos supera las 10 unidades. La funcion retornara el precio de la compra con descuento (si corresponde).  (Enviar aqui link de GDB)"""

bandera_descuento = False
def calcular_precio(precio:int,cantidad:int,porcentaje_descuento: int) -> int:
    global bandera_descuento
    precio_por_unidad = precio * cantidad
    if cantidad > 10:
        bandera_descuento = True
        calculo_descuento = (precio_por_unidad * porcentaje_descuento) / 100
        precio_con_descuento = precio_por_unidad - calculo_descuento
        return precio_con_descuento 
    else:   
        return precio_por_unidad 

precio_final = calcular_precio(20,11,10)

if bandera_descuento == True:
    print(f"su precio CON descuento es: {precio_final}")
else:
    print(f"su precio SIN descuento es: {precio_final}")
        
 
    
   
   
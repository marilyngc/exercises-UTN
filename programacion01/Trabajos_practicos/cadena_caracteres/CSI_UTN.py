
crimen_ADN = "CGTTTAATG"
nombres = ["Jusn Perez","Maria Rodriguez","Carlos Sanchez"]
muestras = ["CGGGGCTAAAATTTTTTACGATCG","AACGTTTAATGTTCTAAGCTGCG","CGGGGCTAAAATTTTTTACGATCG"]


def encontrar_culpable(muestra:str,sospechosos:list,nombre:list)-> str:
    for i in range(len(sospechosos)):
        if muestra in sospechosos[i]:
            return nombre[i]
    return "Son todos inocentes"    
        
print(encontrar_culpable(crimen_ADN,muestras,nombres))        
    

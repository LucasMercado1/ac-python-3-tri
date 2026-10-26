def definir_nivel(valor):
    if valor < 50:
        return "Necessita Substituição"
    elif valor < 80:
        return "Regular"
    else:
        return "Excelente Estado"
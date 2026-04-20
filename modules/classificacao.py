from gerador_upcs import pressao 

def classificar_zona(ajuste_pressão):
    if 120<= ajuste_pressão <=180:
        zona="Verde (Estável)"
    elif ajuste_pressão <=250:
        zona="Amarela (Oscilando)"
    else:
        zona= "vermelha (Crítica)"
   
    return(zona)


upc=pressao() 
classificar_zona(upc)
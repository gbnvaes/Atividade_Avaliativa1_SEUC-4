import random

random.seed(9)

def pressao():
    upc = random.randint(1, 250)
    return upc

def classificar_zona(ajuste_pressao):
    if 120 <= ajuste_pressao <= 180:
        zona = "Verde (Estável)"
    elif ajuste_pressao <= 250:
        zona = "Amarela (Oscilando)"
    else:
        zona = "Vermelha (Crítica)"
    return zona

def verificar_travamento(zona_atual, zona_anterior):
    if zona_atual == "Vermelha (Crítica)" and zona_anterior == "Vermelha (Crítica)":
        return True
    return False

def metricas_finais(total_pressao, menor_pressao, maior_pressao, cont_verde, i, total_leituras, travamento):
    if i == 0:
        print("Nenhuma leitura realizada")
        return
    media = total_pressao / i
    porc_verde = (cont_verde * 100) / i

    print(f"Média das pressões ajustadas: {media: .2f} UPCs")
    print(f"Menor pressão registrada: {menor_pressao: .2f} UPCs")
    print(f"Maior pressão registrada: {maior_pressao: .2f} UPCs")
    print(f"Porcentagem na Zona Verde: {porc_verde: .2f}%")
    
    if travamento:
        porc_leituras = (i * 100 ) / total_leituras
        print(f"Percentual de leituras realizadas: {porc_leituras: .2f}%")


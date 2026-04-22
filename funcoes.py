import random

random.seed(9)

def pressao():
    upc = random.randint(1, 250)
    if upc > 150:
        upc *= 1.08
    else:
        upc *= 0.96
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


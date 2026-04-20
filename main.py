from funcoes import *

total_leituras = int(input("Digite o número total de leituras do turno: "))

soma_ajustada = 0
menor_pressao = 9999
cont_verde = 0
leituras_realizadas = 0
travamento_ocorreu = False
zona_anterior = ""

for i in range(total_leituras):
    leituras_realizadas += 1
    
    valor_atual = pressao()
    zona_atual = classificar_zona(valor_atual)
    
    print(f"Leitura {leituras_realizadas}: {valor_atual:.2f} UPC - Zona: {zona_atual}")
    
    if verificar_travamento(zona_atual, zona_anterior):
        print("!!! SISTEMA INTERROMPIDO: Risco de fadiga de material detectado !!!")
        travamento_ocorreu = True
        break
    
    soma_ajustada += valor_atual
    
    if valor_atual < menor_pressao:
        menor_pressao = valor_atual
        
    if zona_atual == "Verde (Estável)":
        cont_verde += 1
        
    zona_anterior = zona_atual

exibir_metricas(soma_ajustada, menor_pressao, cont_verde, leituras_realizadas, total_leituras, travamento_ocorreu)
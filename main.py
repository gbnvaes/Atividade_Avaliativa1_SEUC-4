from funcoes import *
zona_atual = ""
total_leituras = int(input("Digite o número total de leituras do turno: "))
total_pressao = 0
menor_pressao = None
cont_verde = 0 

for i in range(1,total_leituras + 1):
    upc = pressao()
    total_pressao += upc
    if menor_pressao == None or menor_pressao < upc:
        menor_pressao = upc

    zona_anterior = zona_atual
    zona_atual = classificar_zona(upc)
    if zona_atual == "Verde (Estável)":
        cont_verde += 1
    verificar = verificar_travamento(zona_atual, zona_anterior)
    if verificar:
        print("O sistema atingiu o limite de zona vermelha\n")
        break

print(f"A média das pressões já ajustadas: {total_pressao:.2f}")
print(f"A menor pressão registrada durante todo o processo: {menor_pressao:.2f}")
porc_verde = (cont_verde * 100)/i
print(f"A porcentagem de leituras que ficaram na Zona Verde: {porc_verde:.2f}")
poc_leituras = (i*100)/total_leituras
print(f"Percentual de leituras realizadas: {poc_leituras:.2f}")





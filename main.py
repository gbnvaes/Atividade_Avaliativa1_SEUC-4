from funcoes import *
import os
zona_atual = None
total_leituras = int(input("Digite o número total de leituras do turno: "))
total_pressao = 0
menor_pressao = None
cont_verde = 0 
travamento = False
i = 0
opcao = 0
while opcao !=1 and opcao!=2:
    os.system('cls')
    opcao = int(input("Digite [1] para Digitar a pressão e [2] para gerar pressões random:"))

for i in range(1,total_leituras + 1):
    if opcao == 1:
        upc = int(input("Pressão: "))
    else:
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
        travamento = True 
        print("O sistema atingiu o limite de zona vermelha\n")
        break

metricas_finais(total_pressao, menor_pressao, cont_verde, i, total_leituras, travamento)





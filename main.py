from funcoes import *
import os
zona_atual = None 
total_pressao = 0
menor_pressao = None
maior_pressao = None
cont_verde = 0 
travamento = False
i = 0
opcao = 0
total_leituras = 0 

while total_leituras <= 0:
    total_leituras = int(input("Digite o número total de leituras do turno: "))
    if total_leituras <= 0:
        print("O número de leituras deve ser maior que zero. Tente Novamente. ")

while opcao !=1 and opcao!=2:
    os.system('cls')
    opcao = int(input("Digite [1] para Digitar a pressão e [2] para gerar pressões random: "))

for i in range(1,total_leituras + 1):
    if opcao == 1:
        upc = 0
        while upc <= 0:
            upc = int(input(f"Leitura {i}/{total_leituras} - Pressão (UPC): "))
            if upc <= 0:
                print("Pressão inválida. Digite um valor maior que zero.")
    else:
        upc = pressao()
    if upc > 150:
        upc *= 1.08
    else:
        upc *= 0.96
    total_pressao += upc

    if menor_pressao == None or upc < menor_pressao:
        menor_pressao = upc
    if maior_pressao == None or upc > maior_pressao:
        maior_pressao = upc

    zona_anterior = zona_atual
    zona_atual = classificar_zona(upc)

    print(f"  → Pressão ajustada: {upc:.2f} UPCs | Zona: {zona_atual}")

    if zona_atual == "Verde (Estável)":
        cont_verde += 1
        
    verificar = verificar_travamento(zona_atual, zona_anterior)
    if verificar:
        travamento = True 
        print("O sistema atingiu o limite de zona vermelha\n")
        break
print()
metricas_finais(total_pressao, menor_pressao, maior_pressao, cont_verde, i, total_leituras, travamento)





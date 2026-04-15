# Atividade_Avaliativa1_SEUC-4

O TIME deverá desenvolver um programa em linguagem PYTHON que solicite ao operador o número total
de leituras da pressão hidrodinâmica que serão realizadas no seu turno. Cada leitura passará por um
processamento lógico imediato.
Regras de Negócio e Restrições desse processamento:
  • Ajuste Térmico: Leituras acima de 150 UPCs sofrem um acréscimo de 8% (expansão térmica).
      • Leituras abaixo ou iguais a 150 UPCs sofrem uma redução de 4% (contração).
      
  • Classificação de Estabilidade:
      • Zona Verde (Estável): Entre 120 UPCs e 180 UPCs (após o ajuste).
      • Zona Amarela (Oscilação): Fora da Zona Verde, mas abaixo de 250 UPCs (após o ajuste).
      • Zona Vermelha (Crítica): Qualquer valor acima de 250 UPCs (após o ajuste).
      
  • Protocolo de Travamento: Se o sistema detectar duas leituras consecutivas na Zona Vermelha,
  o escoamento deve ser interrompido imediatamente por segurança.
  
  • Métricas Finais: Ao encerrar (por conclusão ou travamento), o sistema deve exibir:
    1. A média das pressões já ajustadas.
    2. A menor pressão registrada durante todo o processo.
    3. A porcentagem de leituras que ficaram na "Zona Verde".
    4. Se houve travamento, o percentual de leituras realizadas

import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")


def calcular_imc (pesos, alturas):
    lista_resultados_imc= []
    for peso in pesos:
        for altura in alturas:
            imc = peso / (altura ** 2)
            lista_resultados_imc.append(imc)
    return lista_resultados_imc


def resultado_imc(imcs):
    lista_classificacoes_imc = []
    for imc in imcs:
        if  imc < 18.5:
            lista_classificacoes_imc.append("Abaixo do peso")
        elif imc < 25:
            lista_classificacoes_imc.append("Peso normal")
        elif imc <30:
            lista_classificacoes_imc.append("Sobrepeso")
        elif imc <35:
            lista_classificacoes_imc.append("Obesidade grau I")
        elif imc < 40:
            lista_classificacoes_imc.append("Obesidade grau II")
        else:
            lista_classificacoes_imc.append("Obesidade grau III")
    return lista_classificacoes_imc

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome= input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break

    sobrenome = input("Digite seu sobrenome: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))


   
    # Adicionando os dados às listas
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    
imcs = calcular_imc(pesos, alturas)
resultados = resultado_imc(imcs)
    

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome completo:", nomes[i], sobrenomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print("Imc:", round(imcs[i],2))
    print("Classificação do IMC:", resultados[i])
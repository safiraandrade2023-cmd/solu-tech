from datetime import datetime

print("SISTEMA DE CONTROLE DE PRODUÇÃO")
print("  INDÚSTRIA DE ALIMENTOS   ")

print("\nENTRADAS")
nome_produto = input("Nome do produto: ")
cogido_produto = input("Código do produto: ")
linha_produto = input("Linha de produção: ")

quantidade_produzida = int(input("Quantidade produzida: "))
quantidade_utilizada = int(input("Quantidade de mercadoria utilizada: "))
embalagens_analisadas = int(input("Quantidade de embalagens analisadas: "))
embalagens_falha = int(input("Quantidade de embalagens com falha: "))

peso = float(input("Peso do produto (g): "))
peso_minimo = float(input("Peso mínimo permitido (g): "))
peso_maximo = float(input("Peso máximo permitido (g): "))

estoque_anterior = int(input("Estoque disponível antes da produção: "))

data_validade = input("Data de validade (DD/MM/AAAA): ")

data_inspecao = datetime.now().strftime("%d/%m/%Y %H:%M")

preco_produto = float(input("Preço do produto (R$): "))

#Limite definido pela indústria
limite_falhas = int(input("Limite máximo de embalagens com falha: "))


print("\nPROCESSAMENTO")

if embalagens_analisadas == 0:
    percentual_falhas = 0
else:
    percentual_falhas = (embalagens_falha / embalagens_analisadas) * 100
print("Percentual de falhas:", percentual_falhas)
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

#Tipo de falha
if embalagens_falha > 0:
    tipo_falha = "falha na embalagem"
else:
    tipo_falha = "nenhuma falha encontrada"

#Verificação das embalagens
if embalagens_falha > limite_falhas:
    alerta_embalagem = "ALERTA: quantidade de embalagens com falha acima do limite!"
else:
    alerta_embalagem = "quantidade de falhas dentro do limite"

#Desperdicio
if quantidade_utilizada > quantidade_produzida:
    despercidio = quantidade_utilizada - quantidade_produzida
else:
    despercidio = 0
#Valor do desperdicio
valor_desperdicio = despercidio * preco_produto

#Valor do desprdicio
valor_desperdicio = despercidio * preco_produto

#Estoque atual
estoque_atual = estoque_anterior + quantidade_produzida

#Verificação do peso
if peso < peso_minimo:
    alerta_peso = "ALERTA: peso abaixo do minimo permitido"
elif peso > peso_maximo:
    alerta_embalagem = "ALERTA: peso acima do maximo permitido"
else:
    alerta_peso = "Peso dentro do padrão"

#Verificação da validade
data_validade_convertida = datetime.strftime(data_validade, "%d/%m/%Y")
hoje = datetime.now()

if data_validade_convertida < hoje:
    situacao_validade = "PRODUTO VENCIDO!"
else:
    situacao_validade = "produto dentro da validade"
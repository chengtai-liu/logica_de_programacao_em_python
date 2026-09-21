# Criar uma lista de dicionários com pelo menos 5 produtos
produtos = [
    {"nome": "Notebook", "categoria": "Computadores", "preco": 3500, "quantidade": 5},
    {"nome": "Mouse", "categoria": "Acessórios", "preco": 80, "quantidade": 20},
    {"nome": "Teclado", "categoria": "Acessórios", "preco": 150, "quantidade": 8},
    {"nome": "Monitor", "categoria": "Monitores", "preco": 1200, "quantidade": 12},
    {"nome": "Headset", "categoria": "Acessórios", "preco": 250, "quantidade": 6}
]


# 1. Exibir todos os produtos cadastrados
for produto in produtos:
    print(produto)


# 2. Exibir o nome, preço e quantidade em estoque de cada produto
for produto in produtos:
    print("Nome:", produto["nome"])
    print("Preço:", produto["preco"])
    print("Quantidade:", produto["quantidade"])


# 3. Calcular a quantidade total de itens armazenados no estoque
quantidade_total = 0

for produto in produtos:
    quantidade_total += produto["quantidade"]

print("Quantidade total:", quantidade_total)


# 4. Calcular o valor total do estoque
valor_total = 0

for produto in produtos:
    valor_total += produto["preco"] * produto["quantidade"]

print("Valor total do estoque:", valor_total)


# 5. Identificar os produtos que possuem menos de 10 unidades disponíveis
for produto in produtos:
    if produto["quantidade"] < 10:
        print(produto["nome"])


# 6. Verificar se determinado produto está cadastrado
produto_procurado = "Mouse"
encontrado = False

for produto in produtos:
    if produto["nome"] == produto_procurado:
        encontrado = True

if encontrado:
    print("Produto cadastrado.")
else:
    print("Produto não cadastrado.")


# 7. Alterar a quantidade em estoque de um produto
for produto in produtos:
    if produto["nome"] == "Mouse":
        produto["quantidade"] = 30

print(produtos)


# 8. Adicionar um novo produto
novo_produto = {
    "nome": "Webcam",
    "categoria": "Acessórios",
    "preco": 300,
    "quantidade": 10
}

produtos.append(novo_produto)

print(produtos)


# 9. Exibir um relatório final com todos os produtos
# e suas respectivas informações
for produto in produtos:
    print("Nome:", produto["nome"])
    print("Categoria:", produto["categoria"])
    print("Preço:", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print("--------------------")
# Criar uma tupla com as informações do produto
produto = ("Notebook", "Eletrônicos", 3500.00, "P001")


# 1. Exibir cada informação individualmente
print(produto[0])
print(produto[1])
print(produto[2])
print(produto[3])


# 2. Exibir todas as informações utilizando uma estrutura de repetição
for informacao in produto:
    print(informacao)


# 3. Informar a quantidade de informações armazenadas
quantidade = len(produto)
print(quantidade)


# 4. Tentar alterar uma das informações da tupla
produto[0] = "Computador"


# 5. Observar e explicar o que acontece ao tentar modificar um elemento
# Ocorre um erro porque uma tupla é imutável.
# Os elementos de uma tupla não podem ser alterados.
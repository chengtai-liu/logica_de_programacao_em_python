# Criar um dicionário com os dados do funcionário
funcionario = {
    "nome": "Carlos",
    "idade": 30,
    "cargo": "Programador",
    "salario": 5000,
    "setor": "Tecnologia"
}


# 1. Exibir cada informação do funcionário
print(funcionario["nome"])
print(funcionario["idade"])
print(funcionario["cargo"])
print(funcionario["salario"])
print(funcionario["setor"])


# 2. Alterar o salário do funcionário
funcionario["salario"] = 5500
print(funcionario["salario"])


# 3. Adicionar uma nova informação ao cadastro
funcionario["email"] = "carlos@email.com"
print(funcionario)


# 4. Remover uma informação do cadastro
del funcionario["email"]
print(funcionario)


# 5. Verificar se determinada chave existe
if "cargo" in funcionario:
    print("A chave cargo existe.")
else:
    print("A chave cargo não existe.")


# 6. Percorrer o dicionário exibindo as chaves e seus respectivos valores
for chave, valor in funcionario.items():
    print(chave, ":", valor)
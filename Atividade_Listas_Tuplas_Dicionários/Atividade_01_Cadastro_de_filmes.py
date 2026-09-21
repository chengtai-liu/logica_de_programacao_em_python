
# 1. Criar uma lista contendo inicialmente 5 filmes
filmes = [
    "Titanic",
    "Avatar",
    "Vingadores",
    "Toy Story",
    "Homem-Aranha"
]


# 2. Exibir todos os filmes cadastrados
print(filmes)


# 3. Exibir o primeiro filme da lista
print(filmes[0])


# 4. Exibir o último filme da lista
print(filmes[-1])


# 5. Adicionar um novo filme ao final da lista
filmes.append("Batman")
print(filmes)


# 6. Inserir um novo filme em uma posição específica
filmes.insert(2, "Superman")
print(filmes)


# 7. Remover um filme da lista
filmes.remove("Avatar")
print(filmes)


# 8. Alterar o nome de um dos filmes
filmes[0] = "Titanic 2"
print(filmes)


# 9. Exibir a quantidade de filmes cadastrados
print(len(filmes))


# 10. Verificar se um determinado filme está presente na lista
if "Batman" in filmes:
    print("Batman está na lista.")
else:
    print("Batman não está na lista.")
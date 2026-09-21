#Listas, Tuplas e Dicionários

# 1. Listas
#Listas são utilizadas para armazenar varios valores dentro
#de uma única variável
nomes = ["ana" , "carlos" , "João" , "maria"]
print(nomes)

# 2. Acessando Elementos da Lista
print(nomes[0])

#podemos acessar o último elemento usando o -1
print(nomes[-1])

# 3. Alterando Elementos

nomes[0] = "Pedro"
print(nomes)

# 4. Adicionar Elementos

#append() adiciona um elemento no final da lista
nomes.append("Lucas")
print(nomes)

#insert() adiciona um elemento em uma posição especifica.
nomes.insert(1, "mariana")
print(nomes)

# 5. Removendo Elementos
#remove um elemento pelo valor

nomes.remove("Lucas")
print(nomes)

#pop() remove um elemento pelo indice
nomes.pop(0)
print(nomes)

# 6. Tamanho da Lista
#len() informa a quantidade de elementos
print(len(nomes))

#7. Percorrendo uma Lista
for nome in nomes :
    print(nome)

# 8. verificando se um elemento existe

if "João" in nomes:
    print("João esta na lista")
else:
    print("João não esta na lista")

#9. Lista com diferentes tipos de dados
dados = ["João", 18 , 1.75 , True]
print(dados)

#10. Lista de números
notas = [7.5, 8.0, 6.5, 9.0]

soma = 0

for nota in notas:
    soma = soma + nota

media = soma / len(notas)
print(f"Média: {media}")

#11. Tuplas
#Tuplas são semelhantes ás listas.
#As tuplas não ser alteradas.

coordenadas = (10 , 20)
print(coordenadas)

print(coordenadas[0])

#12 Dicionários


#Dicionários armazenam informaçoes no formato: chave: valor
aluno = {
    "nome": "Carlos",
    "idade": 17,
    "nota": 8.5
}

print(aluno)

# 1. Criar uma lista contendo 5 notas
notas = [8, 7, 9, 6, 10]


# 2. Exibir todas as notas
print(notas)


# 3. Calcular a soma das notas
soma = sum(notas)
print(soma)


# 4. Calcular a média das notas
media = soma / len(notas)
print(media)


# 5. Identificar a maior nota
maior = max(notas)
print(maior)


# 6. Identificar a menor nota
menor = min(notas)
print(menor)


# 7. Verificar se existe uma nota igual a 10
if 10 in notas:
    print("Existe uma nota igual a 10.")
else:
    print("Não existe uma nota igual a 10.")


# 8 e 9. Informar se o estudante foi aprovado ou reprovado
# Média igual ou superior a 7 = aprovado

if media >= 7:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")
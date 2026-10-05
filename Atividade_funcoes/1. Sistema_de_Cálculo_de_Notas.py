#1. Receber o nome do estudante.
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


#2. Receber três notas.
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


#3. Calcular a média das notas.
def exibir_resultado(nome, nota1, nota2, nota3, media, situacao):
    print("\n===== RESULTADO =====")
    print(f"Nome do estudante: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


nome = input("Digite o nome do estudante: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

#4. Verificar a situação do estudante.
media = calcular_media(nota1, nota2, nota3)

situacao = verificar_situacao(media)

exibir_resultado(nome, nota1, nota2, nota3, media, situacao)
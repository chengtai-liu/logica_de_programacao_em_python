#Oque é uma função:

# Uma função é um bloco de código criado para relizar
# uma determinada traefa.
# Ela permite organizar e retilizar código.

#1. Criando uma dunção
#utiliar a palavra def para uma função

def saudacao():
    print("Olá seja bem-vindo!")

saudacao()

#2. Crinado uma função com parâmetro

#parâmetros permitem enviar informações para a função
def saudacao(nome):
    print(f"ola {nome}")

saudacao("Ana")
saudacao("João")

#3. Mais de um parâmtro
def apresentar(nome , idade):
print(f"nome: {nome}")
print(f"idade: {idade}")

apresentar("Maria", 17)
apresentar("João", 20)

#4. funçao com calculo

def somar(numero1 , numero2):
    resutado = numero1 + numero2
    print(f"Resultado: {resutado}")

somar(10 , 20)
somar(10 , 90)

#5 Retornando um valor
#Return devolve um valor par ao local onde
#a função for chamada

def somar(numero1 , numero2):
    return numero1 + numero2

print(somar(10 , 20))

#6 Função com condição
def Verificar(numero1 , numero2):
    if idade >= 18:
        return "Maior de idade"
    else:
        "menor de idade"

print(Verificar(20))

#7 Parâmetro com Vaor padrão
def saudacoa(nome ="Aluno"):
    print(f"Ola {nome}")

saudacao("João")
saudacao()

#8 Função utilizando lista
def calcularMrdia(notas:):
    soma = 0
    for nota in notas:
        soma += nota

        return soma / len(notas)
notas = [8 , 7 , 9 , 10]
media = calcularMrdia(notas)
print(f"Média: {media}")

# 9. Funções para organizar um progarma
def cadastrar_produto():

    nome = input("Digite o nome do produto:")
    preco = float(input("Digite o preço:"))
    return nome, preco

def exibir_produto(nome, preco):

    print("\n===== PRODUTO =====")
    print(f"Nome: {nome}")
    print(f"Preço: R$ {preco:.2f}")

    nome, preco = cadastrar_produto()
    exibir_produto(nome, proco)

class Produto:
    def __init__(self, nome, preco, quantidade=0):
        self.nome = nome
        self.__preco = preco
        self.__quantidade = quantidade


    @property
    def preco(self):
        return self.__preco


    @property
    def quantidade(self):
        return self.__quantidade


    def entrada(self, qtd):
        if qtd > 0:
            self.__quantidade += qtd
            print(f"Entrada de {qtd}. Estoque: {self.__quantidade}")
        else:
            print("Quantidade inválida!")


    def saida(self, qtd):
        if qtd <= 0:
            print("Quantidade inválida!")
        elif qtd <= self.__quantidade:
            self.__quantidade -= qtd
            print(f"Saída de {qtd}. Estoque: {self.__quantidade}")
        else:
            print(f"Estoque insuficiente! Disponível: {self.__quantidade}")


    def aplicar_desconto(self, porcentagem):
        if 1 <= porcentagem <= 50:
            self.__preco -= self.__preco * porcentagem / 100
            print(f"Novo preço: R$ {self.__preco:.2f}")
        else:
            print("Desconto deve ser entre 1% e 50%!")


    def valor_em_estoque(self):
        return self.__preco * self.__quantidade




# Testes
fone = Produto("Fone Bluetooth", 150.0, 10)
mouse = Produto("Mouse", 80.0)


fone.saida(3)
fone.saida(20)
fone.entrada(-5)


fone.aplicar_desconto(80)
fone.aplicar_desconto(10)


print(f"R$ {fone.valor_em_estoque():.2f}")


mouse.entrada(5)
mouse.saida(2)
print(f"R$ {mouse.valor_em_estoque():.2f}")


try:
    fone.quantidade = 1000
except AttributeError:
    print("Não é permitido alterar a quantidade diretamente!")
class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"{self.nome} diz: Au au!")

    def mostrar_info(self):
        print(f"Nome: {self.nome}, Raça: {self.raca}, Idade: {self.idade}")


# Criando dois cachorros diferentes
cachorro1 = Cachorro("Rex", "Pastor Alemão", 3)
cachorro2 = Cachorro("Bob", "Labrador", 5)

# Chamando os dois métodos para cada cachorro
cachorro1.latir()
cachorro1.mostrar_info()

cachorro2.latir()
cachorro2.mostrar_info()

# Alterando a idade diretamente pelo atributo
cachorro1.idade = 4

# Mostrando a informação novamente
cachorro1.mostrar_info()
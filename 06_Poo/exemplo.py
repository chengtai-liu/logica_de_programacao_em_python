# CLASSE: O modelo(a planta)
class Celular:
    def __init__(self, marca, modelo, cor, bateria = 100):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        if self.bateria == 0:
            print("Sem bateria! Coloque para carrgar")
        else:
            self.ligado = True
            print(f"{self.modelo} Ligado!")

# OS Objetos: Criados a partir da clase (as "casas")
Celular1 = Celular("Sansung", "Galaxy s23", "Preto")
Celular2 = Celular("Motorola", "MotoG", "Azul", 30)

#Acessando e alterando atributos
print(Celular1.marca)

#Tábem podemos alterar diretamente
Celular1.cor ="branco"
print(Celular1.cor)

#chamado métodos
Celular2.ligar()
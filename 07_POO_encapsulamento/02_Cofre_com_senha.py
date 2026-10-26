class Cofre:
    def __init__(self, senha):
        self.__senha = senha
        self.__itens = []
        self.__aberto = False
        self.__tentativas = 0
        self.__bloqueado = False


    def abrir(self, senha):
        if self.__bloqueado:
            print("Cofre bloqueado!")
            return


        if senha == self.__senha:
            self.__aberto = True
            self.__tentativas = 0
            print("Cofre aberto.")
        else:
            self.__tentativas += 1
            print(f"Senha incorreta! Tentativa {self.__tentativas} de 3.")


            if self.__tentativas >= 3:
                self.__bloqueado = True
                self.__aberto = False


    def fechar(self):
        self.__aberto = False
        print("Cofre fechado.")


    def guardar(self, item):
        if self.__aberto:
            self.__itens.append(item)
            print(f"{item} guardado.")
        else:
            print("Abra o cofre primeiro!")


    def ver_itens(self):
        if self.__aberto:
            print(f"Itens: {self.__itens}")
        else:
            print("Abra o cofre primeiro!")




# Testes
cofre = Cofre("1234")


cofre.guardar("Relógio")


cofre.abrir("0000")
cofre.abrir("1234")


cofre.guardar("Relógio")
cofre.ver_itens()
cofre.fechar()


cofre.ver_itens()


cofre.abrir("1")
cofre.abrir("2")
cofre.abrir("3")


cofre.abrir("1234")
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = nota


    @property
    def nota(self):
        return self.__nota


    def definir_nota(self, valor):
        if 0 <= valor <= 10:
            self.__nota = valor
        else:
            print("Nota inválida!")


    def situacao(self):
        if self.__nota >= 7:
            return "Aprovado"
        return "Reprovado"




# Testes
aluno1 = Aluno("Marina", 6.5)
aluno2 = Aluno("Pedro", 9)


print(aluno1.situacao())
aluno1.definir_nota(15)
aluno1.definir_nota(8)
print(aluno1.nota)
print(aluno1.situacao())


print(aluno2.situacao())
aluno2.definir_nota(-2)
print(aluno2.nota)


try:
    aluno1.nota = 10
except AttributeError:
    print("Não é permitido alterar a nota diretamente!")
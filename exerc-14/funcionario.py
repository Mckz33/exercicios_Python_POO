class Funcionario():
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome
    def getSalario(self):
        return self.salario
    def setSalario(self, salario):
        self.salario = self.salario * salario / 100 + self.salario

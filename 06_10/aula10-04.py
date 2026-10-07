class Funcionario:

    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.horas_trabalhadas = 0
        self.salario = 0

    def registrar_hora_trabalhada(self, horas):

        if self.horas_trabalhadas >= 0:
            self.horas_trabalhadas = horas
        return f'Horas Trabalhadas atualizadas para {self.horas_trabalhadas}'

    def calcular_salario(self):
        self._salario = self.horas_trabalhadas * self.valor_hora_trabalhada
        return f'Salario calculado e atualizado: {self._salario}'

    def main(self):
        print(f'Nome: {self.nome}')
        print(f'Cargo: {self.cargo}')
        print(f'Horas Trabalhadas: {self.horas_trabalhadas}')
        print(f'Salario: {self.calcular_salario()}')

new_funcionario = Funcionario('João', 'Desenvolvedor', 50)
new_funcionario.calcular_salario()
new_funcionario.registrar_hora_trabalhada(200)
new_funcionario.calcular_salario()
new_funcionario.main()
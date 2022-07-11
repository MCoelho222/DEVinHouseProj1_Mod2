from veiculosclass import Veiculos

class Camionete(Veiculos):

    def __init__(self, pais, fabricante, tipo, ano, nome, valor, combustivel, potencia, cacamba, cpf=0):
        super().__init__(pais, fabricante, tipo, ano, nome, valor, cpf)
        self.chassi = super()._chassi
        self.placa = super()._placa
        self.combustivel = combustivel
        self.potencia = potencia
        self.cacamba = cacamba
        self.cor = 'Roxa'

    def salvarveiculo(self) -> None:
        return super().salvarveiculo()

    def listarInfo(self) -> list:
        return super().listarInfo()

    def vender(self, valor, cpf) -> None:
        return super().vender(valor, cpf)

# if __name__ == "__main__":

#     a = Camionete('Brasil', 'Ford', 'camionete', '2020', 'Ranger', '140.000,00', 'Diesel', '120 cv', '100 L')
#     b = dict(a.__dict__)
#     b['tipo'] = 'bike'
#     a.__dict__ = b
#     print(a.__dict__)
#     # a.listarInfo()
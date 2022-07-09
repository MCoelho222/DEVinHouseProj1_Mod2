from veiculosclass import Veiculos

class Camionete(Veiculos):

    def __init__(self, tipo, chassi, ano, nome, placa, valor, combustivel, potencia, cacamba, cpf=0):
        super().__init__(tipo, chassi, ano, nome, placa, valor, cpf)
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

if __name__ == "__main__":

    a = Camionete('Camionete', 'BDGFHR2475657', 2020, 'Ranger', 'FGT6G05', 140000, 'Diesel', '120 cv', '100 L', '008.528.229-44')
    a.salvarveiculo()
    a.listarInfo()
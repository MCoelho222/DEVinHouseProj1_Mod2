from veiculosclass import Veiculos

class Carro(Veiculos):

    def __init__(self, tipo, chassi, ano, nome, placa, valor, cor, combustivel, potencia, nportas, cpf=0):
        super().__init__(tipo, chassi, ano, nome, placa, valor, cor, cpf)
        self.portas = nportas
        self.potencia = potencia
        self.combustivel = combustivel

    def salvarveiculo(self) -> None:
        return super().salvarveiculo()

    def listarInfo(self) -> list:
        return super().listarInfo()

    def vender(self, valor, cpf) -> None:
        return super().vender(valor, cpf)

if __name__ == "__main__":

    a = Carro('Carro', 'BDGFHR2475657', 2020, 'Ranger', 'ZXS9H58', 140000, 'PRETA', 'Gasolina', 120, 4, '008.528.229-44')
    a.salvarveiculo()
    a.listarInfo()
from veiculosclass import Veiculos

class Carro(Veiculos):

    def __init__(self, pais, fabricante, tipo, ano, nome, valor, cor, combustivel, potencia, nportas, cpf=0):
        super().__init__(pais, fabricante, tipo, ano, nome, valor, cor, cpf)
        self.chassi = super()._chassi
        self.placa = super()._placa
        self.portas = nportas
        self.potencia = potencia
        self.combustivel = combustivel

    def salvarveiculo(self) -> None:
        return super().salvarveiculo()

    def listarInfo(self) -> list:
        return super().listarInfo()

    def vender(self, valor, cpf) -> None:
        return super().vender(valor, cpf)

# if __name__ == "__main__":

#     a = Carro('Brasil', 'Ford', 'carro', '2020', 'Ranger', '140.000,00', 'branco', 'Gasolina', '120 CV', '4')
#     a.salvarveiculo()
#     a.listarInfo()
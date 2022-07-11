from veiculosclass import Veiculos

class Motocicleta(Veiculos):

    def __init__(self, pais, fabricante, tipo, ano, nome, valor, cor, potencia, nrodas, cpf=0):
        
        super().__init__(pais, fabricante, tipo, ano, nome, valor, cor, cpf)
        self.chassi = super()._chassi
        self.placa = super()._placa
        self.potencia = potencia
        self.rodas = nrodas
    
    def salvarveiculo(self) -> None:
        return super().salvarveiculo()

    def listarInfo(self) -> list:
        return super().listarInfo()

    def vender(self, valor, cpf) -> None:
        return super().vender(valor, cpf)

# if __name__ == "__main__":

#     a = Motocicleta('Brasil', 'Honda', 'moto', '2020', 'Ranger', '140.000,00', 'preta', '120 CV', '2')
#     a.salvarveiculo()
#     a.listarInfo()


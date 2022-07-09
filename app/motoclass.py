from veiculosclass import Veiculos

class Motocicleta(Veiculos):

    def __init__(self, tipo, chassi, ano, nome, placa, valor, cor, potencia, nrodas, cpf=0):
        
        super().__init__(tipo, chassi, ano, nome, placa, valor, cor, cpf)
        self.potencia = potencia
        self.rodas = nrodas
    
    def salvarveiculo(self) -> None:
        return super().salvarveiculo()

    def listarInfo(self) -> list:
        return super().listarInfo()

    def vender(self, valor, cpf) -> None:
        return super().vender(valor, cpf)

if __name__ == "__main__":

    a = Motocicleta('Motocicleta', 'BDGFHR2475657', 2020, 'Ranger', 'ABC6G10', 140000, 'PRETA', 120, 2, '008.528.229-44')
    a.salvarveiculo()
    a.listarInfo()


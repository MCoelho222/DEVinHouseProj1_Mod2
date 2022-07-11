from os.path import join, abspath, dirname
from randitems import criaChassi, criaPlaca

class Veiculos:

    def __init__(self, pais, fabricante, tipo, ano, nome, valor, cor, cpf=0):
        
        self._tipo = tipo
        self.pais = pais
        self.fabricante = fabricante
        self._chassi = criaChassi(pais, fabricante)
        self._ano = ano
        self._nome = nome
        self._placa = criaPlaca()
        self.valor = valor
        self.cor = cor
        self._cpf = cpf

    @property
    def _tipo(self):
        return self.tipo

    @_tipo.setter
    def _tipo(self, novo_tipo):
        self.tipo = novo_tipo

    @property
    def _chassi(self):
        return self.chassi
    
    @_chassi.setter
    def _chassi(self, cod):
        self.chassi = cod
    
    @property
    def _ano(self):
        return self.ano
    
    @_ano.setter
    def _ano(self, novo_ano):
        self.ano = novo_ano

    @property
    def _nome(self):
        return self.nome
    
    @_nome.setter
    def _nome(self, novo_nome):
        self.nome = novo_nome

    @property
    def _placa(self):
        return self.placa
    
    @_placa.setter
    def _placa(self, novo_placa):
        self.placa = novo_placa
    
    @property
    def _cpf(self):
        return self.cpf
    
    @_cpf.setter
    def _cpf(self, novo_cpf):
        self.cpf = novo_cpf
    
    def listarInfo(self) -> None:
        info = dict(self.__dict__)
        for key, value in info.items():
            print(f'{key}: {value}')     

    def salvarveiculo(self) -> None:

        ROOT_PATH = dirname(dirname(abspath(__file__)))
        DATA_PATH = join(ROOT_PATH, 'data')
        FILE_PATH = join(DATA_PATH, f'{self.tipo}_{self.placa}.txt')
        veiculo = open(FILE_PATH, 'w')
        objkeys = list(self.__dict__.keys())

        for i in range(len(objkeys)):
            if objkeys[i][0] == '_':
                key = objkeys[i][1:]
            else:
                key = objkeys[i]
            veiculo.write(f'{key}: {self.__dict__.get(objkeys[i])}\n')
        veiculo.close()

    def vender(self, valor, cpf) -> None:

        self.valor = valor
        self.cpf = cpf

# if __name__ == "__main__":

#     a = Veiculos('Brasil', 'Ford', 'Moto', '2020', 'Jeep', '200.000,00', 'cinza')
#     a.salvarveiculo()
#     a.listarInfo()

    
    


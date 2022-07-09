import numpy as np
from motoclass import Motocicleta
from carroclass import Carro
from camioneteclass import Camionete
from randitems import criaChassi, criaPlaca


esq = '-' * 40
dir_ = '-' * 40
welcome = f'WELCOME TO DEVINCAR{dir_}\n'
print(f'{esq}{welcome}')

def sectionmsg(texto):
    traces = '-' * (len(welcome) - len(texto))
    print(f'{esq}{texto}{traces}\n')

action1 = int(input("""O que você deseja fazer? \n
[1] Cadastrar um veículo
[2] Vender um veículo\n
R: """))

if action1 == 1:
    sectionmsg('CADASTRO DE VEÍCULO')
    print('Que tipo de veículo você quer cadastrar? \n')
    print('[1] Moto/Triciclo')
    print('[2] Carro')
    print('[3] Camionete\n')
    action2 = int(input('R: '))
    
    if action2 == 1:

        sectionmsg('CADASTRO DE MOTO/TRICICLO')
        print('\n PREENCHA O FORMULÁRIO ABAIXO: \n')
        questions = ['País de origem', 'Fabricante', 'Ano de fabricação', 'Nome do veículo', 'Cor', 'N° de rodas', 'Potência', 'Valor']
        answers = []
        for i in range(len(questions)):
            ans = input(f'{questions[i]}: ')
            answers.append(ans)
        print('\n')
        
        chassi = criaChassi(answers[0], answers[1])
        placa = criaPlaca()

        if int(answers[5]) > 2:
            tipo = 'triciclo'
        else:
            tipo = 'moto'
        ano = answers[2]
        nome = answers[3]
        cor = answers[4]
        rodas = answers[5]
        potencia = answers[6]
        valor = answers[7]
        veiculo = Motocicleta(tipo, chassi, ano, nome, placa, valor, cor, potencia, rodas)
        veiculo.salvarveiculo()
        print('Veículo cadastrado com sucesso!')

    if action2 == 2:

        sectionmsg('CADASTRO DE CARRO')
        print('\n PREENCHA O FORMULÁRIO ABAIXO: \n')
        questions = ['País de origem', 'Fabricante', 'Ano de fabricação', 'Nome do veículo', 'Cor', 'N° de portas', 'Potência', 'Combustível', 'Valor']
        answers = []
        for i in range(len(questions)):
            ans = input(f'{questions[i]}: ')
            answers.append(ans)
        print('\n')
        
        chassi = criaChassi(answers[0], answers[1])
        placa = criaPlaca()

        tipo = 'Carro'
        ano = answers[2]
        nome = answers[3]
        cor = answers[4]
        portas = answers[5]
        potencia = answers[6]
        combustivel = answers[7]
        valor = answers[8]
        veiculo = Carro(tipo, chassi, ano, nome, placa, valor, cor, combustivel, potencia, portas)
        veiculo.salvarveiculo()
        print('Veículo cadastrado com sucesso!')

    if action2 == 3:
        sectionmsg('CAMIONETE')
        print('\n PREENCHA O FORMULÁRIO ABAIXO: \n')
        questions = ['País de origem', 'Fabricante', 'Ano de fabricação', 'Nome do veículo', 'Caçamba', 'Potência', 'Combustível', 'Valor']
        answers = []
        for i in range(len(questions)):
            ans = input(f'{questions[i]}: ')
            answers.append(ans)
        print('\n')
        
        chassi = criaChassi(answers[0], answers[1])
        placa = criaPlaca()

        tipo = 'Camionete'
        ano = answers[2]
        nome = answers[3]
        cacamba = answers[4]
        potencia = answers[5]
        combustivel = answers[6]
        valor = answers[7]
        veiculo = Camionete(tipo, chassi, ano, nome, placa, valor, combustivel, potencia, cacamba)
        veiculo.salvarveiculo()
        print('Veículo cadastrado com sucesso!')
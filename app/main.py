import os
import numpy as np
from os.path import join, abspath, dirname
from motoclass import Motocicleta
from carroclass import Carro
from camioneteclass import Camionete
from randitems import criaChassi, criaPlaca

ROOT_PATH = dirname(dirname(abspath(__file__)))
DATA_PATH = join(ROOT_PATH, 'data')
#-------------------------------WELCOME--------------------------------------------
esq = ' ' * 40
dir_ = ' ' * 40
welcome = f'***BEM-VINDO À DEVINCAR***{dir_}'
goodbye = '***OBRIGADO POR UTILIZAR DEVINCAR***'
whatsnext = '\nDeseja continuar? [s/n]: '
titletraces = '-' * (len(welcome) + 40)
print(titletraces)
print(f'{esq}{welcome}')
print(titletraces)
#--------------------------------FUNÇÕES-------------------------------------------
def sectionmsg(texto):
    lefttraces = '-' * 40
    traces = '-' * (len(welcome) - len(texto))
    print(f'{lefttraces}{texto}{traces}\n')

def finalizador(obj):
    sectionmsg('CONFIRA AS INFORMAÇÕES')
    obj.listarInfo()
    print('\nO que você deseja fazer?\n')
    print('[1] Salvar')
    print('[2] Editar')
    print('[3] Cancelar\n')
    f_action = int(input('R: '))
    if f_action == 1:
        obj.salvarveiculo()
        print('\nVeículo cadastrado com sucesso!\n')
    
    if f_action == 2:
        sectionmsg('***EDITANDO INFORMAÇÕES***')
        while True:
            print('\nQual item você deseja editar?\n')
            infosdict = dict(obj.__dict__) #dicionário do objeto
            infos = list(infosdict.keys()) #Lista das chaves do objeto
            nums = [x for x in range(1, len(infos) + 1)] # Lista dos números para imprimir nas opções de edição
            for i in range(len(nums)): # Loop para imprimir as "[num] opção"
                print(f'[{nums[i]}] {infos[i]}')
            
            item = int(input('\nR: '))
            print('\nInsira o novo valor:\n')
            keytoedit = infos[item - 1]
            novovalor = input(f'{keytoedit.capitalize()}: ')
            infosdict[keytoedit] = novovalor
            obj.__dict__ = infosdict

            print('Editar mais algum item? [s/n] \n')
            continuar = input('R: ')
            if continuar == 'n':
                obj.salvarveiculo()
                print('\nEdição concluída com sucesso!\n')
                break
    if f_action == 3:
        pass

def disponiveis(tipo) -> int:
    print(f'\nQual {tipo} você quer vender?\n')
    i = 1
    files = []
    for file in os.listdir(DATA_PATH):
        if file.endswith('.txt'):
            if file.split('_')[0] == tipo:
                FILE_PATH = join(DATA_PATH, file)
                cpfcheck = open(FILE_PATH, 'r')
                for line in cpfcheck.readlines():
                    linecut = line.split(':')
                    if linecut[0] == 'cpf' and linecut[1] == ' 0\n':
                        files.append(file)
                        placa = file.split('_')[1][:-4]
                        print(f'{[i]} {placa}')
                        i += 1
    ans = int(input('R: '))
    return files[ans -  1]

def vender(file):
    FILE_PATH = join(DATA_PATH, file)
    dados = open(FILE_PATH, 'r')
    print('\nDADOS DO VEÍCULO\n')
    lines = dados.readlines()
    dados.close()
    for line in lines:
        print(line.split('\n')[0])
    print('\nDADOS DA VENDA\n')
    cpf = input('CPF do comprador: ')
    valor = input('Valor: ')
    for i in range(len(lines)):
        if lines[i].split(':')[0] == 'valor':
            lines[i] = f'valor: {valor}\n'
        if lines[i].split(':')[0] == 'cpf':
            lines[i] = f'cpf: {cpf}\n'
    dados = open(FILE_PATH, 'w')
    for i in range(len(lines)):
        dados.write(lines[i])
    dados.close()
    print('\nVenda concluída com sucesso!!\n')
    
while True:
    #--------------------------------MAIN-----------------------------------
    print('\nO que você deseja fazer?\n')
    print('[1] Cadastrar')
    print('[2] Vender')
    print('[3] Listar todos os veículos')
    print('[4] Listar veículos vendidos')
    print('[5] Listar veículos disponíveis')
    print('[6] Veículo vendido com MAIOR preço')
    print('[7] Veículo vendido com MENOR preço\n')
    action1 = int(input('R: '))

    if action1 == 1:
        #----------------------------CADASTRO-------------------------------
        sectionmsg('***CADASTRO DE VEÍCULO***')
        print('Que tipo de veículo você quer cadastrar? \n')
        print('[1] Moto/Triciclo')
        print('[2] Carro')
        print('[3] Camionete\n')
        action2 = int(input('R: '))
        
        if action2 == 1:
            #--------------------------------CADSTRO MOTO/TRICICLO----------------------------
            sectionmsg('CADASTRO DE MOTO/TRICICLO')
            print('PREENCHA O FORMULÁRIO ABAIXO: \n')
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
            finalizador(veiculo)
            ans = input(whatsnext)
            if ans == 'n' or ans == 'N':
                sectionmsg(goodbye)
                break
            else:
                continue

        if action2 == 2:
            #--------------------------------CADASTRO CARRO----------------------------
            sectionmsg('CADASTRO DE CARRO')
            print('PREENCHA O FORMULÁRIO ABAIXO: \n')
            questions = ['País de origem', 'Fabricante', 'Ano de fabricação', 'Nome do veículo', 'Cor', 'N° de portas', 'Potência', 'Combustível', 'Valor']
            answers = []
            for i in range(len(questions)):
                ans = input(f'{questions[i]}: ')
                answers.append(ans)
            print('\n')
            
            chassi = criaChassi(answers[0], answers[1])
            placa = criaPlaca()

            tipo = 'carro'
            ano = answers[2]
            nome = answers[3]
            cor = answers[4]
            portas = answers[5]
            potencia = answers[6]
            combustivel = answers[7]
            valor = answers[8]
            veiculo = Carro(tipo, chassi, ano, nome, placa, valor, cor, combustivel, potencia, portas)
            finalizador(veiculo)
            ans = input(whatsnext)
            if ans == 'n' or ans == 'N':
                sectionmsg(goodbye)
                break
            else:
                continue

        if action2 == 3:
            #--------------------------------CADASTRO CAMIONETE----------------------------
            sectionmsg('CAMIONETE')
            print('PREENCHA O FORMULÁRIO ABAIXO: \n')
            questions = ['País de origem', 'Fabricante', 'Ano de fabricação', 'Nome do veículo', 'Caçamba', 'Potência', 'Combustível', 'Valor']
            answers = []
            for i in range(len(questions)):
                ans = input(f'{questions[i]}: ')
                answers.append(ans)
            print('\n')
            
            chassi = criaChassi(answers[0], answers[1])
            placa = criaPlaca()

            tipo = 'camionete'
            ano = answers[2]
            nome = answers[3]
            cacamba = answers[4]
            potencia = answers[5]
            combustivel = answers[6]
            valor = answers[7]
            veiculo = Camionete(tipo, chassi, ano, nome, placa, valor, combustivel, potencia, cacamba)
            finalizador(veiculo)
            ans = input(whatsnext)
            if ans == 'n' or ans == 'N':
                sectionmsg(goodbye)
                break
            else:
                continue

    if action1 == 2:
        #-------------------------------VENDAS DE VEÍCULOS--------------------------------------
        sectionmsg('***VENDA DE VEÍCULOS***')
        print('Que tipo de veículo você quer vender?\n')
        print('[1] Moto/Triciclo')
        print('[2] Carro')
        print('[3] Camionete')
        action3 = int(input('R: '))
        
        if action3 == 1:
            file_veiculo = disponiveis('moto')
            vender(file_veiculo)
            ans = input(whatsnext)
            if ans == 'n' or ans == 'N':
                sectionmsg(goodbye)
                break
            else:
                continue
        if action3 == 2:
            file_veiculo = disponiveis('carro')
            vender(file_veiculo)
            ans = input(whatsnext)
            if ans == 'n' or ans == 'N':
                sectionmsg(goodbye)
                break
            else:
                continue
        if action3 == 3:
            file_veiculo = disponiveis('camionete')
            vender(file_veiculo)
            ans = input(whatsnext)
            if ans == 'n' or ans == 'N':
                sectionmsg(goodbye)
                break
            else:
                continue

    if action1 == 3:
        #-------------------------------LISTA DE TODOS OS VEÍCULOS-----------------
        sectionmsg('***TODOS OS VEÍCULOS***')
        i = 1
        for file in os.listdir(DATA_PATH):
            if file.endswith('.txt'):
                FILE_PATH = join(DATA_PATH, file)
                veiculo = open(FILE_PATH, 'r')
                print(f'VEÍCULO {i} =>\n')
                for line in veiculo.readlines():
                    print(line.split('\n')[0])
                print('-'*20)
                i += 1
        ans = input(whatsnext)
        if ans == 'n' or ans == 'N':
            sectionmsg(goodbye)
            break
        else:
            continue

    if action1 == 4:
        #-------------------------------LISTA DE VEÍCULOS VENDIDOS-------------------
        sectionmsg('***VEÍCULOS VENDIDOS***')
        i = 1
        files = []
        for file in os.listdir(DATA_PATH):
            if file.endswith('.txt'):
                FILE_PATH = join(DATA_PATH, file)
                veiculo = open(FILE_PATH, 'r')
                lines = veiculo.readlines()
                for line in lines:
                    linecut = line.split(':')
                    if linecut[0] == 'cpf' and linecut[1] != ' 0\n':
                        files.append(file)
        for file in files:
            FILE_PATH = join(DATA_PATH, file)
            veiculo = open(FILE_PATH, 'r')
            lines = veiculo.readlines()
            print(f'VEÍCULO {i} =>\n')
            for line in lines:
                print(line.split('\n')[0])
            print('-'*20)
            i += 1
        ans = input(whatsnext)
        if ans == 'n' or ans == 'N':
            sectionmsg(goodbye)
            break
        else:
            continue

    if action1 == 5:
        #-------------------------------LISTA DE VEÍCULOS DISPONÍVEIS-------------------
        sectionmsg('***VEÍCULOS DISPONÍVEIS***')
        i = 1
        files = []
        for file in os.listdir(DATA_PATH):
            if file.endswith('.txt'):
                FILE_PATH = join(DATA_PATH, file)
                veiculo = open(FILE_PATH, 'r')
                for line in veiculo.readlines():
                    linecut = line.split(':')
                    if linecut[0] == 'cpf' and linecut[1] == ' 0\n':
                        files.append(file)
        for file in files:
            FILE_PATH = join(DATA_PATH, file)
            veiculo = open(FILE_PATH, 'r')
            lines = veiculo.readlines()
            print(f'VEÍCULO {i} =>\n')
            for line in lines:
                print(line.split('\n')[0])
            print('-'*20)
            i += 1
        ans = input(whatsnext)
        if ans == 'n' or ans == 'N':
            sectionmsg(goodbye)
            break
        else:
            continue

    if action1 == 6:
        #-------------------------------VEÍCULO VENDIDO COM MAIOR PREÇO-------------------
        placas = []
        valores = []
        files = []
        for file in os.listdir(DATA_PATH):
            if file.endswith('.txt'):
                FILE_PATH = join(DATA_PATH, file)
                veiculo = open(FILE_PATH, 'r')
                for line in veiculo.readlines():
                    linecut = line.split(':')
                    if linecut[0] == 'placa':
                        placas.append(linecut[1])
                    if linecut[0] == 'valor':
                        valores.append(linecut[1])
        numeros = [] # Valores convertidos para float
        for i in range(len(valores)):
            partes = valores[i].split('.')
            if len(partes) == 2:
                mil = valores[i].split('.')[0]
                cem = valores[i].split('.')[1].split(',')[0]
                cents = valores[i].split('.')[1].split(',')[1]
                num = float(f'{mil}{cem}.{cents}')
                numeros.append(num)
            if len(partes) == 3:
                million = valores[i].split('.')[0]
                mil = valores[i].split('.')[1]
                cem = valores[i].split('.')[2].split(',')[0]
                cents = valores[i].split('.')[2].split(',')[1]
                num = float(f'{million}{mil}{cem}.{cents}')
                numeros.append(num)
        arr_numeros = np.array(numeros)
        maximo = np.max(arr_numeros)
        max_index = numeros.index(maximo)
        veiculomax = placas[max_index]
        for file in os.listdir(DATA_PATH):
            if file.endswith('.txt'):
                FILE_PATH = join(DATA_PATH, file)
                veiculo = open(FILE_PATH, 'r')
                for line in veiculo.readlines():
                    linecut = line.split(':')
                    if linecut[0] == 'placa' and linecut[1] == veiculomax:
                        files.append(file)
        for file in files:
            FILE_PATH = join(DATA_PATH, file)
            veiculo = open(FILE_PATH, 'r')
            lines = veiculo.readlines()
            print('-'*20)
            print(f'VEÍCULO =>\n')
            for line in lines:
                print(line.split('\n')[0])
            print('-'*20)
        ans = input(whatsnext)
        if ans == 'n' or ans == 'N':
            sectionmsg(goodbye)
        else:
            continue

    if action1 == 7:
        #-------------------------------VEÍCULO VENDIDO COM MENOR PREÇO-------------------
        placas = []
        valores = []
        files = []
        for file in os.listdir(DATA_PATH):
            if file.endswith('.txt'):
                FILE_PATH = join(DATA_PATH, file)
                veiculo = open(FILE_PATH, 'r')
                for line in veiculo.readlines():

                    linecut = line.split(':')
                    if linecut[0] == 'placa':
                        placas.append(linecut[1])
                    if linecut[0] == 'valor':
                        valores.append(linecut[1])
        numeros = [] # Valores convertidos para float
        for i in range(len(valores)):
            partes = valores[i].split('.')
            if len(partes) == 2:
                mil = valores[i].split('.')[0]
                cem = valores[i].split('.')[1].split(',')[0]
                cents = valores[i].split('.')[1].split(',')[1]
                num = float(f'{mil}{cem}.{cents}')
                numeros.append(num)
            if len(partes) == 3:
                million = valores[i].split('.')[0]
                mil = valores[i].split('.')[1]
                cem = valores[i].split('.')[2].split(',')[0]
                cents = valores[i].split('.')[2].split(',')[1]
                num = float(f'{million}{mil}{cem}.{cents}')
                numeros.append(num)
        arr_numeros = np.array(numeros)
        minimo = np.min(arr_numeros)
        min_index = numeros.index(minimo)
        veiculomin = placas[min_index]
        for file in os.listdir(DATA_PATH):
            if file.endswith('.txt'):
                FILE_PATH = join(DATA_PATH, file)
                veiculo = open(FILE_PATH, 'r')
                for line in veiculo.readlines():

                    linecut = line.split(':')
                    if linecut[0] == 'placa' and linecut[1] == veiculomin:
                        files.append(file)
        for file in files:
            FILE_PATH = join(DATA_PATH, file)
            veiculo = open(FILE_PATH, 'r')
            lines = veiculo.readlines()
            print('-'*20)
            print(f'VEÍCULO =>\n')
            for line in lines:
                print(line.split('\n')[0])
            print('-'*20)
        ans = input(whatsnext)
        if ans == 'n' or ans == 'N':
            sectionmsg(goodbye)
            break
        else:
            continue


    




import os
import numpy as np
import datetime
from os.path import join, abspath, dirname
from motoclass import Motocicleta
from carroclass import Carro
from camioneteclass import Camionete

ROOT_PATH = dirname(dirname(abspath(__file__)))
DATA_PATH = join(ROOT_PATH, 'data')
date = datetime.date.today()
year = int(date.strftime("%Y"))
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
def answers(max) -> int:
    """---------------------------------------------------------
    RETORNA => int: resposta dos inputs e oferece sair do programa
    max => int: número máximo de opções
    ---------------------------------------------------------"""
    print('\nEscolha uma das opções ou digite SAIR')
    while True:
        try:
            lista = [x for x in range(1, max + 1)]
            item = input('\nR: ')
            if item.lower() == 'sair':
                item = item.lower()
                break
            item = int(item)
            lista.index(item)
            break
        except ValueError:
            print('Digite um número que esteja entre as opções')
            continue
    return item
    
def sectionmsg(texto) -> None:
    """---------------------------------------------------------
    IMPRIME mensagem de abertura da seção
    texto => str: texto a ser exibido
    ---------------------------------------------------------"""
    lefttraces = '-' * 40
    traces = '-' * (len(welcome) - len(texto))
    print(f'{lefttraces}{texto}{traces}\n')

def filteredByCpf(status, tipo='all') -> list:
    """------------------------------------------------------------
    RETORNA => list: veículos vendidos ou disponíveis, filtrando pelo cpf
    status => str: 'disponiveis' ou 'vendidos'
    tipo => str: 'moto'; 'triciclo'; 'carro'; 'camionete'
    tipo = 'all' => RETORNA todos os tipos
    ------------------------------------------------------------"""
    files = []
    for file in os.listdir(DATA_PATH):
        if file.endswith('.txt'):
            if file.split('_')[0] == tipo or tipo == 'all':
                FILE_PATH = join(DATA_PATH, file)
                veiculo = open(FILE_PATH, 'r')
                for line in veiculo.readlines():
                    linecut = line.split(':')
                    if status == 'disponiveis':
                        if linecut[0] == 'cpf' and linecut[1] == ' 0\n':
                            files.append(file)
                    if status == 'vendidos':
                        if linecut[0] == 'cpf' and linecut[1] != ' 0\n':
                            files.append(file)     
    return files

def endRegister(obj, op) -> int:
    """---------------------------------------------------------
    RESUMO => apresenta questionários finais de cada operação
    RETORNA => int: a opção escolhida (salvar, editar, cancelar)
    obj => dict: dicionário do objeto instanciado na operação
    op => str: operação sendo executada ('cadastro' ou 'venda')
    ---------------------------------------------------------"""
    sectionmsg('***CONFIRA AS INFORMAÇÕES***')
    obj.listarInfo()
    print('\nO que você deseja fazer?\n')
    print('[1] Salvar')
    print('[2] Editar')
    print('[3] Cancelar')
    f_action = answers(3)
    if f_action == 1:
        obj.salvarveiculo()
        print('\nOperação concluída com sucesso!\n')
    
    if f_action == 2:
        sectionmsg('***EDITANDO INFORMAÇÕES***')
        while True:
            print('\nQual item você deseja editar?\n')
            infosdict = dict(obj.__dict__) #dicionário do objeto
            infos = list(infosdict.keys()) #Lista das chaves do objeto
            infos_arr = np.array(infos)
            infos = infos_arr[infos_arr != 'chassi'] # máscara para não mostrar chassi
            infos = infos[infos != 'placa'] # máscara para não mostrar placa
            infos = infos[infos != 'tipo'] # máscara para não mostrar tipo
            if op == 'cadastro':
                infos = infos[infos != 'cpf'] # máscara para não mostrar cpf
            if obj.tipo == 'camionete':
                infos = infos[infos != 'cor'] # mascara para não mostrar cor
            nums = [x for x in range(1, len(infos) + 1)] # Lista dos números para imprimir nas opções de edição
            for i in range(len(nums)): # Loop para imprimir "[num] opção"
                print(f'[{nums[i]}] {infos[i]}')
            item = answers(len(infos))
            if item == 'sair':
                break
            print('\nInsira o novo valor:\n')
            edit = infos[item - 1]
            
            if edit == 'pais' or edit == 'fabricante' or edit == 'nome' or edit == 'combustivel' or edit == 'cor':
                while True:
                    ans = input(f'{edit.capitalize()}: ')
                    try:
                        test = int(ans)
                        print('=> Use apenas letras')
                        continue
                    except ValueError:
                        infosdict[edit] = ans.title()
                        break
            
            if edit == 'ano':
                while True:
                    ans = input(f'{edit.capitalize()}: ')
                    try:
                        test = int(ans)
                        if len(ans) == 4 and test <= year:
                            infosdict[edit] = ans
                            break
                        else:
                            if test > year:
                                print('O ano deve ser menor ou igual ao ano atual')
                            else:
                                print('Use o formato YYYY')
                            continue
                    except ValueError:
                        print('=> Use apenas números inteiros')
                        continue 

            if edit == 'potencia':
                while True:
                    ans = input(f'{edit.capitalize()}: ')
                    try:
                        test = int(ans)
                        infosdict[edit] = f'{str(test)} CV'
                        break
                    except ValueError:
                        print('=> Use apenas números inteiros')
                        continue  
            
            if edit == 'portas':
                while True:
                    ans = input(f'{edit.capitalize()}: ')
                    try:
                        test = int(ans)
                        if test < 2 or test > 6:
                            print('Escolha entre 2 a 6 portas')
                            continue
                        infosdict[edit] = ans
                        break
                    except ValueError:
                        print('=> Use apenas números')
                        continue
            
            if edit == 'rodas':
                while True:
                    ans = input(f'{edit.capitalize()}: ')
                    try:
                        test = int(ans)
                        if test < 2 or test > 3:
                            print('Escolha 2 ou 3 rodas')
                            continue
                        infosdict[edit] = ans
                        break
                    except ValueError:
                        print('=> Use apenas números')
                        continue
            
            if edit == 'cacamba':
                while True:
                    ans = input(f'{edit.capitalize()}: ')
                    try:
                        test = int(ans)
                        infosdict[edit] = f'{str(test)} L'
                        break
                    except ValueError:
                        print('=> Use apenas números inteiros')
                        continue
            
            if edit == 'valor':
                while True:
                    ans = input(f'{edit.capitalize()}: ')
                    dots = len(ans.split('.'))
                    comma = len(ans.split(','))
                    if (dots == 2 or dots == 3) and comma == 2:
                        infosdict[edit] = ans
                        break
                    else:
                        print('Digite o valor no formato x.xxx,xx')
                        continue
            
            obj.__dict__ = infosdict
            if 'rodas' in infos:
                if infosdict['rodas'] == '2':
                    infosdict['tipo'] = 'moto'
                else:
                    infosdict['tipo'] = 'triciclo'
            print('Editar mais algum item? [s/n] \n')
            continuar = input('R: ')
            if continuar == 'n':
                obj.salvarveiculo()
                print('\nEdição concluída com sucesso!\n')
                break
    
    if f_action == 3:
        pass
    return f_action

def sellthis(tipo) -> str:
    """---------------------------------------------------------
    RETORNA => str: o nome do arquivo que contém as informações
    do veículo a ser vendido
    tipo => str: 'moto'; 'triciclo'; 'carro'; 'camionete'
    ---------------------------------------------------------"""
    print(f'\nQual {tipo} você quer vender?\n')
    i = 1
    files = filteredByCpf('disponiveis', tipo)
    for file in files:
        placa = file.split('_')[1][:-4]
        print(f'{[i]} {placa}')
        i += 1
    ans = answers(len(files))
    try:
        return files[ans -  1]
    except TypeError:
        return 'sair'

def vender(file) -> None:
    """---------------------------------------------------------
    RESUMO => resolve as operações de venda
    file => str: nome do arquivo que contém as informações do
    veículo a ser vendido
    ---------------------------------------------------------"""
    FILE_PATH = join(DATA_PATH, file)
    dados = open(FILE_PATH, 'r')
    print('\nDADOS DO VEÍCULO\n')
    lines = dados.readlines()
    dados.close()
    obj = {}
    for line in lines:
        obj[line.split(':')[0]] = line.split(':')[1][1:].split('\n')[0]
        print(line.split('\n')[0])
    if file.split('_')[0] == 'moto' or file.split('_')[0] == 'triciclo':
        veiculo = Motocicleta(obj['pais'], obj['fabricante'], obj['tipo'], obj['ano'], obj['nome'], obj['valor'], obj['cor'], obj['potencia'], obj['rodas'], obj['cpf'])
        veiculo._chassi = obj['chassi']
        veiculo._placa = obj['placa']
    if file.split('_')[0] == 'carro':
        veiculo = Carro(obj['pais'], obj['fabricante'], obj['tipo'], obj['ano'], obj['nome'], obj['valor'], obj['cor'], obj['combustivel'], obj['potencia'], obj['portas'], obj['cpf'])
        veiculo._chassi = obj['chassi']
        veiculo._placa = obj['placa']
    if file.split('_')[0] == 'camionete':
        veiculo = Camionete(obj['pais'], obj['fabricante'], obj['tipo'], obj['ano'], obj['nome'], obj['valor'], obj['combustivel'], obj['potencia'], obj['cacamba'], obj['cpf'])
        veiculo._chassi = obj['chassi']
        veiculo._placa = obj['placa']
    print('\nDADOS DA VENDA\n')
    while True:
        print('Digite o CPF do comprador no formato xxx.xxx.xxx-xx')
        cpf = input('CPF: ')
        if len(cpf) == 14:
            break
    while True:
        print('Digite o VALOR da venda no formato x.xxx,xx')
        valor = input('Valor: ')
        dots = len(valor.split('.'))
        comma = len(valor.split(','))
        if (dots == 2 or dots == 3) and comma == 2:
            break
    veiculo.vender(valor, cpf)
    endRegister(veiculo, 'venda')
    
while True:
    #--------------------------------MAIN-----------------------------------
    if len(os.listdir(DATA_PATH)) > 0:
        print('\nO que vamos fazer?\n')
        print('[1] Cadastrar')
        print('[2] Vender')
        print('[3] Listar todos os veículos')
        print('[4] Listar veículos vendidos')
        print('[5] Listar veículos disponíveis')
        print('[6] Veículo vendido com MAIOR preço')
        print('[7] Veículo vendido com MENOR preço')
    else:
        print('\nNão há veículos para vender, escolha [1] para cadastrar\n')
        print('[1] Cadastrar')

    action1 = answers(7)
    if action1 == 'sair':
        break

    if action1 == 1:
        #----------------------------CADASTRO-------------------------------
        sectionmsg('***CADASTRO DE VEÍCULO***')
        print('Que tipo de veículo você quer cadastrar? \n')
        print('[1] Moto/Triciclo')
        print('[2] Carro')
        print('[3] Camionete')
        action2 = answers(3)
        if action2 == 'sair':
            break
        if action2 == 1:
            #--------------------------------CADASTRO MOTO/TRICICLO----------------------------
            sectionmsg('***CADASTRO DE MOTO/TRICICLO***')
            print('PREENCHA O FORMULÁRIO ABAIXO: \n')
            questions = ['País de origem', 'Fabricante', 'Ano de fabricação', 'Nome do veículo', 'Cor', 'N° de rodas', 'Potência (CV)', 'Valor']
            answer = []
            for i in range(len(questions)):
                if i == 0 or i == 1 or i == 3 or i == 4:
                    while True:
                        ans = input(f'{questions[i]}: ')
                        try:
                            test = int(ans)
                            print('=> Use apenas letras')
                            continue
                        except ValueError:
                            answer.append(ans.title())
                            break
                if i == 2:
                    while True:
                        ans = input(f'{questions[i]}: ')
                        try:
                            test = int(ans)
                            if len(ans) == 4 and test <= year:
                                answer.append(ans)
                                break
                            else:    
                                if test > year:
                                    print('O ano deve ser menor ou igual ao ano atual')
                                else:
                                    print('Use o formato YYYY')
                                continue
                        except ValueError:
                            print('=> Use apenas números')
                            continue    
                if i == 5:
                    while True:
                        ans = input(f'{questions[i]}: ')
                        try:
                            test = int(ans)
                            if test < 2 or test > 3:
                                print('Escolha 2 ou 3')
                                continue
                            answer.append(ans)
                            break
                        except ValueError:
                            print('=> Use apenas números')
                            continue  
                if i == 6:
                    while True:
                        ans = input(f'{questions[i]}: ')
                        try:
                            test = int(ans)
                            answer.append(f'{str(test)} CV')
                            break
                        except ValueError:
                            print('=> Use apenas números inteiros')
                            continue  
                if i == 7:
                    while True:
                        ans = input(f'{questions[i]}: ')
                        dots = len(ans.split('.'))
                        comma = len(ans.split(','))
                        if (dots == 2 or dots == 3) and comma == 2:
                            answer.append(ans)
                            break
                        else:
                            print('Digite o valor no formato x.xxx,xx')
                            continue
         
            if int(answer[5]) > 2:
                tipo = 'triciclo'
            else:
                tipo = 'moto'
            ano = answer[2]
            nome = answer[3]
            cor = answer[4]
            rodas = answer[5]
            potencia = answer[6]
            valor = answer[7]
            veiculo = Motocicleta(answer[0], answer[1], tipo, ano, nome, valor, cor, potencia, rodas)
            endRegister(veiculo, 'cadastro')
            ans = input(whatsnext)
            if ans == 'n' or ans == 'N':
                sectionmsg(goodbye)
                break
            else:
                continue

        if action2 == 2:
            #--------------------------------CADASTRO CARRO----------------------------
            sectionmsg('***CADASTRO DE CARRO***')
            print('PREENCHA O FORMULÁRIO ABAIXO: \n')
            questions = ['País de origem', 'Fabricante', 'Ano de fabricação', 'Nome do veículo', 'Cor', 'N° de portas', 'Potência (CV)', 'Combustível', 'Valor']
            answer = []
            for i in range(len(questions)):
                if i == 0 or i == 1 or i == 3 or i == 4 or i == 7:
                    while True:
                        ans = input(f'{questions[i]}: ')
                        try:
                            teste = int(ans)
                            print('=> Use apenas letras')
                            continue
                        except ValueError:
                            answer.append(ans.title())
                            break
                if i == 2:
                    while True:
                        ans = input(f'{questions[i]}: ')
                        try:
                            test = int(ans)
                            if len(ans) == 4 and test <= year:
                                answer.append(ans)
                                break
                            else:    
                                if test > year:
                                    print('O ano deve ser menor ou igual ao ano atual')
                                else:
                                    print('Use o formato YYYY')
                                continue
                        except ValueError:
                            print('=> Use apenas números')
                            continue
                if i == 5:
                    while True:
                        ans = input(f'{questions[i]}: ')
                        try:
                            test = int(ans)
                            if test < 2 or test > 6:
                                print('Escolha entre 2 a 6 portas')
                                continue
                            answer.append(ans)
                            break
                        except ValueError:
                            print('=> Use apenas números')
                            continue  
                if i == 6:
                    while True:
                        ans = input(f'{questions[i]}: ')
                        try:
                            test = int(ans)
                            answer.append(f'{str(test)} CV')
                            break
                        except ValueError:
                            print('=> Use apenas números inteiros')
                            continue  
                if i == 8:
                    while True:
                        ans = input(f'{questions[i]}: ')
                        dots = len(ans.split('.'))
                        comma = len(ans.split(','))
                        if (dots == 2 or dots == 3) and comma == 2:
                            answer.append(ans)
                            break
                        else:
                            print('Digite o valor no formato x.xxx,xx')
                            continue
            
            tipo = 'carro'
            ano = answer[2]
            nome = answer[3]
            cor = answer[4]
            portas = answer[5]
            potencia = answer[6]
            combustivel = answer[7]
            valor = answer[8]
            veiculo = Carro(answer[0], answer[1], tipo, ano, nome, valor, cor, combustivel, potencia, portas)
            endRegister(veiculo, 'cadastro')
            ans = input(whatsnext)
            if ans == 'n' or ans == 'N':
                sectionmsg(goodbye)
                break
            else:
                continue

        if action2 == 3:
            #--------------------------------CADASTRO CAMIONETE----------------------------
            sectionmsg('***CADASTRO DE CAMIONETE***')
            print('PREENCHA O FORMULÁRIO ABAIXO: \n')
            questions = ['País de origem', 'Fabricante', 'Ano de fabricação', 'Nome do veículo', 'Caçamba (Litros)', 'Potência (CV)', 'Combustível', 'Valor']
            answer = []
            for i in range(len(questions)):
                if i == 0 or i == 1 or i == 3 or i == 6:
                    while True:
                        ans = input(f'{questions[i]}: ')
                        try:
                            teste = int(ans)
                            print('=> Use apenas letras')
                            continue
                        except ValueError:
                            answer.append(ans.title())
                            break
                if i == 2:
                    while True:
                        ans = input(f'{questions[i]}: ')
                        try:
                            test = int(ans)
                            if len(ans) == 4 and test <= year:
                                answer.append(ans)
                                break
                            else:    
                                if test > year:
                                    print('O ano deve ser menor ou igual ao ano atual')
                                else:
                                    print('Use o formato YYYY')
                                continue
                        except ValueError:
                            print('=> Use apenas números')
                            continue
                if i == 4:
                    while True:
                        ans = input(f'{questions[i]}: ')
                        try:
                            test = int(ans)
                            answer.append(f'{str(test)} L')
                            break
                        except ValueError:
                            print('=> Use apenas números inteiros')
                            continue  
                
                if i == 5:
                    while True:
                        ans = input(f'{questions[i]}: ')
                        try:
                            test = int(ans)
                            answer.append(f'{str(test)} CV')
                            break
                        except ValueError:
                            print('=> Use apenas números inteiros')
                            continue  
                if i == 7:
                    while True:
                        ans = input(f'{questions[i]}: ')
                        dots = len(ans.split('.'))
                        comma = len(ans.split(','))
                        if (dots == 2 or dots == 3) and comma == 2:
                            answer.append(ans)
                            break
                        else:
                            print('Digite o valor no formato x.xxx,xx')
                            continue
            
            tipo = 'camionete'
            ano = answer[2]
            nome = answer[3]
            cacamba = answer[4]
            potencia = answer[5]
            combustivel = answer[6]
            valor = answer[7]
            veiculo = Camionete(answer[0], answer[1], tipo, ano, nome, valor, combustivel, potencia, cacamba)
            endRegister(veiculo, 'cadastro')
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
        print('[1] Moto')
        print('[2] Carro')
        print('[3] Camionete')
        print('[4] Triciclo')
        action3 = answers(4)
        if action3 == 'sair':
            break
        if action3 == 1:
            sectionmsg('***VENDER MOTO***')
            file_veiculo = sellthis('moto')
            if file_veiculo == 'sair':
                break
            vender(file_veiculo)
            ans = input(whatsnext)
            if ans == 'n' or ans == 'N':
                sectionmsg(goodbye)
                break
            else:
                continue
        if action3 == 2:
            sectionmsg('***VENDER CARRO***')
            file_veiculo = sellthis('carro')
            if file_veiculo == 'sair':
                break
            vender(file_veiculo)
            ans = input(whatsnext)
            if ans == 'n' or ans == 'N':
                sectionmsg(goodbye)
                break
            else:
                continue
        if action3 == 3:
            sectionmsg('***VENDER CAMIONETE***')
            file_veiculo = sellthis('camionete')
            if file_veiculo == 'sair':
                break
            vender(file_veiculo)
            ans = input(whatsnext)
            if ans == 'n' or ans == 'N':
                sectionmsg(goodbye)
                break
            else:
                continue

        if action3 == 4:
            sectionmsg('***VENDER TRICICLO***')
            file_veiculo = sellthis('triciclo')
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
        files = filteredByCpf('vendidos')
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
        files = filteredByCpf('disponiveis')
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
        sectionmsg('***VEÍCULO VENDIDO COM MAIOR VALOR***')
        valores = []
        files = filteredByCpf('vendidos')
        for file in files:
            FILE_PATH = join(DATA_PATH, file)
            veiculo = open(FILE_PATH, 'r')
            for line in veiculo.readlines():
                linecut = line.split(':')
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
        veiculomax = files[max_index]
        FILE_PATH = join(DATA_PATH, veiculomax)
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

    if action1 == 7:
        #-------------------------------VEÍCULO VENDIDO COM MENOR PREÇO-------------------
        sectionmsg('***VEÍCULO VENDIDO COM MENOR VALOR***')
        valores = []
        files = filteredByCpf('vendidos')
        for file in files:
            FILE_PATH = join(DATA_PATH, file)
            veiculo = open(FILE_PATH, 'r')
            for line in veiculo.readlines():
                linecut = line.split(':')
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
        veiculomin = files[min_index]
        FILE_PATH = join(DATA_PATH, veiculomin)
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


    




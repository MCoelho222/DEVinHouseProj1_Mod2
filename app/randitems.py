import numpy as np

def criaChassi(pais, fabricante):
    print('Qual o continente de origem do veículo?')
    print('[1] Ásia')
    print('[2] África')
    print('[3] Europa')
    print('[4] América do Norte')
    print('[5] América do Sul')
    print('[6] América do Norte\n')
    continente = input('R: ')
    
    cod1 = 0
    def rand(a, b, options) -> str:
        n_rand = np.random.randint(a, b)
        return options[n_rand]

    if continente == '1':
        options = ['J', 'K', 'L', 'M', 'N', 'P', 'R']
        rand(0, len(options), options)

    if continente == '2':
        options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        rand(0, len(options), options)

    if continente == '3':
        options = ['S', 'T', 'U', 'V', 'X', 'Z']
        rand(0, len(options), options)
    
    if continente == '4':
        cod1 = np.random.randint(1, 6)

    if continente == '5':
        cod1 = np.random.randint(8, 10)

    if continente == '6':
        cod1 = np.random.randint(6, 8)

    cod2 = pais[0].upper()
    cod3 = fabricante[0].upper()

    options_ = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V', 'X', 'Z', 'W', 'Y']
    i = 0
    cod4 = ''
    while i < 7:
        cod = np.random.randint(0, len(options_))
        cod4 = cod4 + options_[cod]
        i += 1
    cod4 = f'{cod4}{np.random.randint(0, 10)}'

    options_.extend([x for x in range(0, 10)])
    cod5 = rand(0, len(options_), options_)

    j = 0
    cod6 = ''
    while j < 5:
        num = np.random.randint(0, 10)
        cod6 = cod6 + str(num)
        j += 1
    
    return f'{cod1}{cod2}{cod3}{cod4}{cod5}{cod6}'


def criaPlaca():
    options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O' 'P', 'R', 'S', 'T', 'U', 'V', 'X', 'Z', 'W', 'Y']
    i = 0
    cod1 = ''
    while i < 3:
        num = np.random.randint(0, len(options))
        cod1 = cod1 + options[num]
        i += 1
    cod2 = np.random.randint(1, 10)
    num = np.random.randint(0, 10)
    cod3 = options[num]
    cod4 = np.random.randint(0, 10)
    cod5 = np.random.randint(0, 10)
    return f'{cod1}{cod2}{cod3}{cod4}{cod5}'


if __name__ == "__main__":

    print(criaChassi('Congo', 'Tesla'))
    print(criaPlaca())
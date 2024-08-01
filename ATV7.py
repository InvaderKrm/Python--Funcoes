#valor
def valor():
    preco = float(input('Vamos converter moedas? Insira um valor: '))
    return preco

#Caso escolha Reais
def rpd(preco): #Reais para Dólares
    return preco * 0.17
def rpi(preco): #Reais para Ienes
    return preco * 26.13

#Caso escolha Dólares
def dpr(preco): #Dólares para Reais
    return preco * 5.74
def dpi(preco): #Dólares para Ienes
    return preco * 149.61

#Caso escolha Ienes
def ipr(preco): #Ienes para Reais
    return
def ipd(preco): #Ienes para Dólares
    return

while True:
    preco = valor()
    inicial = input('Considere as moedas:\n(1) Reais;\n(2) Dólares:\n(3) Ienes;\nEm qual delas o valor inserido se encaixa? ')

    #Reais
    if inicial == '1':
        c = input('Para qual moeda você deseja converter?\n(1) Dólares;\n(2) Ienes;\n')
        if c == '1':
            print(f'{preco:.2f} BRL é igual a {rpd(preco):.2f} USD!')
        elif c == '2':
            print(f'{preco:.2f} BRL é igual a {rpi(preco):.2f} JPY!')
        else:
            print('Opção inválida.')
    #Dólares
    elif inicial == '2':
        c = input('Para qual moeda você deseja converter?\n(1) Reais;\n(2) Ienes;\n')
        if c == '1':
            print(f'{preco:.2f} USD é igual a {dpr(preco):.2f} BRL!')
        elif c == '2':
            print(f'{preco:.2f} USD é igual a {dpi(preco):.2f} JPY!')
        else:
            print('Opção inválida.')
    #Ienes
    elif inicial == '3':
        c = input('Para qual medida você deseja converter?\n(1) Fahrenheit;\n(2) reais;\n')
        if c == '1':
            print(preco,'graus Kelvin é igual a',kpf(preco),'graus Fahrenheit!')
        elif c == '2':
            print(preco,'graus Kelvin é igual a',kpc(preco),'graus reais!')
        else:
            print('Opção inválida.')
    else:
        print('Opção inválida.')
    break
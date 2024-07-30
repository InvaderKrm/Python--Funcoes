#temperatura
def valor():
    temperatura = int(input('Vamos converter temperaturas? Insira uma temperatura: '))
    return temperatura

#Caso escolha Celcius
def cpf(temperatura): #Celcius para Fahrenheit
    return temperatura * 1.8 + 32
def cpk(temperatura): #Celcius para Kelvin
    return temperatura + 273.15

#Caso escolha Fahrenheit
def fpc(temperatura): #Fahrenheit para Celcius
    fahrenheit = (temperatura-32) * (5/9)
    arredondamento_f = round(fahrenheit, 2)
    return arredondamento_f
def fpk(temperatura): #Fahrenheit para Kelvin
    return fpc(temperatura) + 273.15

#Caso escolha Kelvin
def kpc(temperatura): #Kelvin para Celcius
    kelvin = temperatura - 273.15
    arredondamento = round(kelvin, 2)
    return arredondamento
def kpf(temperatura): #Kelvin para Fahrenheit
    kelvin_f = kpc(temperatura) * 1.8 + 32
    arredondamento_kf = round(kelvin_f, 2)
    return arredondamento_kf

while True:
    temperatura = valor()
    inicial = input('Considere os tipos de temperatura:\n(1) Celcius;\n(2) Fahrenheit:\n(3) Kelvin;\nEm qual deles a temperatura inserida se encaixa? ')

    #Celcius
    if inicial == '1':
        c = input('Para qual medida você deseja converter?\n(1) Fahrenheit;\n(2) Kelvin;\n')
        if c == '1':
            print(temperatura,'graus Celcius é igual a',cpf(temperatura),'graus Fahrenheit!')
        elif c == '2':
            print(temperatura,'graus Celcius é igual a',cpk(temperatura),'graus Kelvin!')
        else:
            print('Opção inválida.')
    #Fahrenheit
    elif inicial == '2':
        c = input('Para qual medida você deseja converter?\n(1) Celcius;\n(2) Kelvin;\n')
        if c == '1':
            print(temperatura,'graus Fahrenheit é igual a',fpc(temperatura),'graus Celcius!')
        elif c == '2':
            print(temperatura,'graus Fahrenheit é igual a',fpk(temperatura),'graus em Kelvin!')
        else:
            print('Opção inválida.')
    #Kelvin
    elif inicial == '3':
        c = input('Para qual medida você deseja converter?\n(1) Fahrenheit;\n(2) Celcius;\n')
        if c == '1':
            print(temperatura,'graus Kelvin é igual a',kpf(temperatura),'graus Fahrenheit!')
        elif c == '2':
            print(temperatura,'graus Kelvin é igual a',kpc(temperatura),'graus Celcius!')
        else:
            print('Opção inválida.')
    else:
        print('Opção inválida.')
    break


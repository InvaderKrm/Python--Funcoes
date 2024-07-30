def numeros ():
    a = int(input('::Vamos calcular com Pyhton? Insira dois números e depois escolha o tipo de operação que deseja realizar!\nPrimeiro número: '))
    b = int(input('Segundo número: '))
    return a, b

def adicao (a,b):
    return a + b
def subtracao (a,b):
    return a - b
def multiplicacao (a,b):
    return a * b
def divisao (a,b):
    if b == 0:
        return 'Não é possível dividir por zero.'
    return a / b

while True:
        a,b = numeros()
        escolha = input('::Considere os tipos de operação a seguir:\nAdição (1)\nSubtração (2)\nMultiplicação (3)\nDivisão (4)\n::Qual é a sua escolha? ')

        if escolha == '1':
            print('o resultado da adição é:',adicao(a,b))
        elif escolha == '2':
            print('O resultado da subtração é:',subtracao(a,b))
        elif escolha == '3':
            print('O resultado da multiplicação é:',multiplicacao(a,b))
        elif escolha == '4':
            if b==0:
                print(divisao(a, b))
            else:
                print('O resultado da divisão', divisao(a, b))
        else:
            print('Opção inválida.')
        break
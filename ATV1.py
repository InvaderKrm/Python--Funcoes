def numeros ():
    a = int(input('::Vamos calcular com Pyhton? Insira dois números e depois escolha o tipo de operação que deseja realizar!\nPrimeiro número: '))
    b = int(input('Segundo número: '))
    return a, b

def adicao (a, b):
    return a + b
def subtracao (a, b):
    return a - b
def multiplicacao (a, b):
    return a * b
def divisao (a, b):
    if b == 0:
        return "Não é possível dividir por zero."
    return a / b

def main():
    while True:
        a, b = numeros()
        escolha = input("::Considere os tipos de operação a seguir:\nAdição (1)\nSubtração (2)\nMultiplicação (3)\nDivisão (4)\n::Qual é a sua escolha? ")

        if escolha == '1':
            adicao()
        elif escolha == '2':
            subtracao()
        elif escolha == '3':
            multiplicacao()
        elif escolha == '4':
            divisao()
        else:
            print("Opção inválida.")
if __name__ == "__main__":
    main()

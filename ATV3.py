import math

def valor():
    n = int(input('digite o numero: '))
    resultado = print(math.factorial(n))
    return resultado, n

while True:
    resultado = valor()
    print('O fatorial do numero',n,'é igual a',resultado)


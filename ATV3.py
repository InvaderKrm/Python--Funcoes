import math

def valor():
    n = int(input('digite o numero: '))
    return n

def fatorial(n):
    print(math.factorial(n))
    
while True:
    n = valor()
    resultado = fatorial(n)
    print('O fatorial do numero',n,'é igual a',resultado)

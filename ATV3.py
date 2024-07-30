import math
def valor():
    n = int(input('digite o numero: '))
    return n
def fatorial(n):
    if n < 0:
        print("O fatorial não está definido para números negativos")
    else:
        print(math.factorial(n))
while True:
    n = valor()
    print('O fatorial do numero',n,'é igual a',fatorial(n))

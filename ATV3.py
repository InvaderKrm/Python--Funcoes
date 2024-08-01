def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


n = int(input('Digite um número: '))
if n > 0:
    print(f'O fatorial do número {n} é igual a {fatorial(n)}.')
else:
    print('Não é possível calcular o fatorial de números negativos.')

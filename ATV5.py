def perguntas():
    quantidade = int(input('Você deseja calcular a média de quantos números? '))
    return quantidade

def valores(quantidade):
    lista = []
    for i in range(quantidade):
        numeros = int(input(f" - Digite o {i + 1}º número: "))
        lista.append(numeros)
    return lista      

def calculo(lista):
    media = sum(lista)/len(lista)
    return media

while True:
    print('Vamos calcular a média de alguns números com Python!')
    quantidade = perguntas()
    lista = valores(quantidade)
    media = calculo(lista)
    print('A média dos números é igual a',int(media))
    break
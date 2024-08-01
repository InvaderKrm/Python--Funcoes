import random

def sorteio():
    menor = 1 
    maior = 5
    sorteado = random.randint(menor, maior)
    return sorteado

while True:
    sorteado = sorteio()
    print('//numero sorteado:',sorteado)
    advinha_1 = int(input("Um número de 1 a 5 foi sorteado! Você terá 2 chances para acertar!\nAdvinhe que número é esse: "))
    if advinha_1 < 6 and advinha_1 > 0:
        if advinha_1 == sorteado:
          print('Você acertou! O número sorteado é',sorteado)
        else:
            advinha_2 = int(input('Você errou! Tente novamente: '))
            if advinha_2 < 6 and advinha_2 > 0:
                if advinha_2 == sorteado:
                    print('Você acertou! O número sorteado é',sorteado)
                else:
                    print('Você errou de novo, suas chances acabaram! O número sorteado era',sorteado)
            else:
                print('O número inserido não se encontra entre as opções.')
    else:
        print('O número inserido não se encontra entre as opções.')



    break
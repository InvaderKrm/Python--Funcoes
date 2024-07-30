def media(numeros):
    soma=sum(lista)
    quantidade=len(lista)
    media = soma/quantidade
    return media

for i in range(3):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)
    break
print('A média dos números é igual a:',media(numeros))
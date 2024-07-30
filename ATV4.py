def contador(s):
    vogais = "aeiouAEIOUáéíóúÁÉÍÓÚâêôÂÊÔãõÃÕàèìòùÀÈÌÒÙ"
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
    return contador

palavra = str(input('Digite uma palavra: '))
print('O número de vogais na palavra',palavra,'é',contador(palavra))
from random import randint
computador = randint(0,5)
print('-=-' * 20)
print('Advinhe o número entre 0 e 5.')
print('-=-' * 20)
jogador = int(input('Digite o número: '))
if jogador == computador:
    print('Parabéns!')
else:
    print('Errou! ! ! O número era {}'.format(computador))
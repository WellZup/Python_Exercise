'''
Até 9 anos Mirim
Até 14 anos Infantil
Até 19 anos Jr
Até 25 anos Sênior
Acima Master
'''

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento'))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')

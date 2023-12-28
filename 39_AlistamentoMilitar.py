from datetime import date

atual = date.today().year
nascimento = int(input('Ano de Nascimento'))
idade = atual - nascimento

print('Nascidos em {} tem {} anos em {}'.format(nascimento, idade, atual))

if idade == 18:
    print('Você deve se alistar!')
elif idade < 18:
    saldo = 18 - idade
    print('Faltam {} anos para se alistar.'.format(saldo))
elif idade > 18:
    saldo = 18 - idade
    print('Já deveria ter se alistado há {} anos.'.format(saldo))
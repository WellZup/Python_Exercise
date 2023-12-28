velocidade = float(input('Qual a velocidade do veiculo? '))
if velocidade > 80:
    print('Multado! Excesso de velocidade')
    multa = (velocidade - 80) * 7
    print('Valor da multa a ser paga será de R${:.2f}'.format(multa))
print('Dirija com segurança!')
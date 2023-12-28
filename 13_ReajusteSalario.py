salario = float(input('Qual o valor do sálario para reajuste: R$'))
novo = salario + (salario * 15 / 100)
print('O novo sálario com reajuste de 15% será de: R${:.2f}'.format(novo))

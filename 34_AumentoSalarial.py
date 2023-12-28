salario = float(input('Qual o salário do funcionário? '))
if salario <= 2000:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print('O novo salário de quem recebia R${:.2f}, agora será de R${:.2f}'.format(salario, novo))
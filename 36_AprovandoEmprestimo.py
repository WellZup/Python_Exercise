#A perstação do empréstimo não pode ser superior a 30% do salário

emprestimo = float(input('Valor do emprestimo: R$'))
salario = float(input('Salário do '))
anos = int(input('Quantos anos para quitar o emprestimo? '))
prestacao = emprestimo / (anos * 12)
minimo = salario * 30 / 100
print('Para o empréstimo de R${:.2f} em {} anos'.format(emprestimo,anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado!')
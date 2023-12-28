preco = float(input('Digite o preço do produto? R$'))
novoValor = preco - (preco * 5 / 100)
print('O novo valor, com 5% de desconto será de R${}'.format(novoValor))
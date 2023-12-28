print('-=' * 20)
print('Verificando se os segmentos digitados pode se tornar um triangulo:')
print('-=' * 20)
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos digitados podem formar um triângulo!')
else:
    print('Os segmentos informados não podem formar um triângulo! ')
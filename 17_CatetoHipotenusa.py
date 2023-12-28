import math
#from math import hypot
#cateto oposto = co
co = float(input('Cumprimento do cateto oposto: '))
#cateto adjacente = ca
ca = float(input('Cumprimento do cateto adjacente: '))

#hipotenusa = hi
#hi = (co ** 2 + ca ** 2) ** (1/2)
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
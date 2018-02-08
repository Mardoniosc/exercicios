_author_ = 'Mardonio'

try:
    numero1 = input('Informe primeiro numero: ')
    numero2 = input('Informe segundo numero: ')
except:
    print 'Somente numeros inteiros sao validos'

for i in range(numero1,numero2,1):
    print i
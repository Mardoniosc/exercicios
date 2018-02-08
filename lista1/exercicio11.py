numero1 = float(raw_input('Digite primeiro numero: '))
numero2 = float(raw_input('Digite segundo numero: '))

decimal = numero1/numero2
inteiro = int(numero1/numero2)

print '%.2f %i' % (decimal, inteiro)
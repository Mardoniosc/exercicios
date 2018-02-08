assinatura = '#================================================================================#' \
             '\n# Desenvolvido por: Mardonio Costa                                               #' \
             '\n# E-mail: Mardonio@live.com                                                      #' \
             '\n#                                                                                #' \
             '\n# Finalidade: Verifica numero primo em intervalo expecifico                      #' \
             '\n#                                                                                #' \
             '\n#                                                               Data: 30/01/2018 #' \
             '\n# Release: 1.0.0                                                                 #' \
             '\n#================================================================================#\n\n'
_author_ = assinatura
print _author_

try:
    print ('Informe um intervalo para verificacao de numeros primos\n')
    inicio = int(input('Informe o primeiro numero: '))
    fim = int(input('Informe o segundo numero: '))
    if(inicio>0):
        if(fim>=inicio):
            for i in range(inicio, fim, 1):
                n = 1
                while (i >= n):
                    p = i % n
                    if (p == 0):
                        if (n == 1):
                            n += 1;
                            continue
                        elif (n == i):
                            print '%i eh numero primo' % i
                        else:
                            break
                    n += 1;
except:
    print 'Somente numero inteiros maiores que 0 sao validos'
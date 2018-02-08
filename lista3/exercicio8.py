assinatura = '#================================================================================#' \
             '\n# Desenvolvido por: Mardonio Costa                                               #' \
             '\n# E-mail: Mardonio@live.com                                                      #' \
             '\n#                                                                                #' \
             '\n# Finalidade: Pula 3 numeros                                                     #' \
             '\n#                                                                                #' \
             '\n#                                                               Data: 30/01/2018 #' \
             '\n# Release: 1.0.0                                                                 #' \
             '\n#================================================================================#\n\n'
_author_ = assinatura
print _author_
try:
    print('Informe um intervalo a ser impressora na tela')
    inicio = input('Informe o primeiro numero: ')
    fim = input('Informe o segundo numero: ')
    print('Infome 3 numeros do intervalo que nao devem ser impressos')
    primeiro = input('Informe o primeiro numero: ')
    segundo = input('Informe o segundo numero: ')
    terceiro = input('Informe o terceiro numero: ')
    while(inicio<=fim):
        if(primeiro==inicio or segundo==inicio or terceiro==inicio):
            inicio += 1
            continue
        else:
            print inicio
            inicio += 1
except:
    print 'Somente numeros inteiros sao validos'
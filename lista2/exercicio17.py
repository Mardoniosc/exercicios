assinatura = '#================================================================================#' \
             '\n# Desenvolvido por: Mardonio Costa                                               #' \
             '\n# E-mail: Mardonio@live.com                                                      #' \
             '\n#                                                                                #' \
             '\n# Finalidade: Informa mes do numero digitado                                     #' \
             '\n#                                                                                #' \
             '\n#                                                               Data: 27/01/2018 #' \
             '\n# Release: 1.0.0                                                                 #' \
             '\n#================================================================================#\n\n'
_author_ = assinatura
print _author_

try:
    mesdoano = int(raw_input('Digite o mes do ano: '))
    if(mesdoano>=1 and mesdoano <=12):
        if(mesdoano == 1):
            print 'Janeiro'
        elif(mesdoano == 2):
            print 'fevereiro'
        elif(mesdoano == 3):
            print 'Marco'
        elif(mesdoano == 4):
            print 'Abril'
        elif(mesdoano == 5):
            print 'Maio'
        elif(mesdoano == 6):
            print 'Junho'
        elif(mesdoano == 7):
            print 'Julho'
        elif(mesdoano == 8):
            print 'Agosto'
        elif(mesdoano == 9):
            print 'Setembro'
        elif(mesdoano == 10):
            print 'Outubro'
        elif(mesdoano == 11):
            print 'Novembro'
        elif(mesdoano == 12):
            print 'Dezembro'
    else:
        print 'Favor digitar um numero entre 1 e 12!'
except ValueError:
    print 'Somente numeros inteiros sao aceitos.'
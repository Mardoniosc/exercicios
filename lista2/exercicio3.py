assinatura = '#================================================================================#' \
             '\n# Desenvolvido por: Mardonio Costa                                               #' \
             '\n# E-mail: Mardonio@live.com                                                      #' \
             '\n#                                                                                #' \
             '\n# Finalidade: Numero Maior                                                       #' \
             '\n#                                                                                #' \
             '\n#                                                               Data: 27/01/2018 #' \
             '\n# Release: 1.0.0                                                                 #' \
             '\n#================================================================================#\n\n'
_author_ = assinatura
print _author_

numero1 = int(raw_input('Digite primeiro numero: '))
numero2 = int(raw_input('Digite segundo numero: '))

if (numero1>numero2):
    print 'O primeiro numero digitado eh maior'
else:
    print 'O segundo numero digitado eh maior'
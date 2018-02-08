assinatura =   '#================================================================================#' \
             '\n# Desenvolvido por: Mardonio Costa                                               #' \
             '\n# E-mail: Mardonio@live.com                                                      #' \
             '\n#                                                                                #' \
             '\n# Finalidade: Positivo negativo                                                  #' \
             '\n#                                                                                #' \
             '\n#                                                               Data: 27/01/2018 #' \
             '\n# Release: 1.0.0                                                                 #' \
             '\n#================================================================================#\n\n'
_author_ = assinatura

print _author_
numero = int(raw_input('Digite um numero: '))
if numero == 0:
    print 'Numero digitado eh 0'

else:

    if(numero < 0):
        print 'Numero digitado eh negativo'
    else:
        print 'Numero digitado eh positivo'


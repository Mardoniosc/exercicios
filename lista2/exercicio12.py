assinatura = '#================================================================================#' \
             '\n# Desenvolvido por: Mardonio Costa                                               #' \
             '\n# E-mail: Mardonio@live.com                                                      #' \
             '\n#                                                                                #' \
             '\n# Finalidade:                                                                    #' \
             '\n#                                                                                #' \
             '\n#                                                               Data: 27/01/2018 #' \
             '\n# Release: 1.0.0                                                                 #' \
             '\n#================================================================================#\n\n'
_author_ = assinatura
print _author_
numero = input("Digite um numero: ")

tipo = type(numero)

if (tipo==int):
    print 'Valor digitado eh inteiro'
else:
    print 'Valor digitado eh decimal'

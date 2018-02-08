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

caracter = raw_input('Digite um caracter: ')
vogais = ('a','e','i','o','u','A','E','I','O','U')

if (caracter in vogais):
    print 'Caracter digitado eh vogal!!'
else:
    print 'Caracter digitado eh consoante'
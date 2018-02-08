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

numero1 = input('Digite o primeiro numero: ')
numero2 = input('Digite o segundo numero: ')
numero3 = input('Digite o terceiro numero: ')


if (numero1 > numero2):
    if(numero1>numero3):
        print numero1
    else:
        print numero3
elif(numero2>numero3):
    print numero2
else:
    print numero3
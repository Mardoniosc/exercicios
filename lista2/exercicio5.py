assinatura = '#================================================================================#' \
             '\n# Desenvolvido por: Mardonio Costa                                               #' \
             '\n# E-mail: Mardonio@live.com                                                      #' \
             '\n#                                                                                #' \
             '\n# Finalidade: Idade que a mae teve o bebe                                        #' \
             '\n#                                                                                #' \
             '\n#                                                               Data: 27/01/2018 #' \
             '\n# Release: 1.0.0                                                                 #' \
             '\n#================================================================================#\n\n'
_author_ = assinatura
print _author_

suaidade = int(raw_input('Digite sua idade: '))
maeidade = int(raw_input('Digite a idade de sua mae: '))

idadedamae = maeidade - suaidade
print 'Sua mae te teve quando tinha %i anos de idade!!' % idadedamae

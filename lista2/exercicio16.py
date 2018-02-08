assinatura = '#================================================================================#' \
             '\n# Desenvolvido por: Mardonio Costa                                               #' \
             '\n# E-mail: Mardonio@live.com                                                      #' \
             '\n#                                                                                #' \
             '\n# Finalidade:                                                                    #' \
             '\n#                                                                                #' \
             '\n#                                                               Data: 00/01/2018 #' \
             '\n# Release: 1.0.0                                                                 #' \
             '\n#================================================================================#\n\n'
_author_ = assinatura
print _author_

primeirocteto = float(raw_input('Digite o primeiro octeto do endereco IP versao 4: '))

if(primeirocteto >=0 and primeirocteto <=127 ):
    print 'Classe A'
elif (primeirocteto >= 128 and primeirocteto <= 191):
    print 'Classe B'
elif(primeirocteto >=192 and primeirocteto <=223 ):
    print 'Classe C'
elif(primeirocteto >=224 and primeirocteto <=239 ):
    print 'Classe D'
elif(primeirocteto >=240 and primeirocteto <=256 ):
    print 'Classe E'
else:
    print 'Numero digitado nao corresponde a nenhuma classe'
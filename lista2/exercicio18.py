assinatura = '#================================================================================#' \
             '\n# Desenvolvido por: Mardonio Costa                                               #' \
             '\n# E-mail: Mardonio@live.com                                                      #' \
             '\n#                                                                                #' \
             '\n# Finalidade: Validar data                                                       #' \
             '\n#                                                                                #' \
             '\n#                                                               Data: 27/01/2018 #' \
             '\n# Release: 1.0.0                                                                 #' \
             '\n#================================================================================#\n\n'
_author_ = assinatura
print _author_
try:
    data = raw_input("digite uma data 00/00/0000: ")
    tamanhodata = len(data)
    dia = int(data[0]+data[1])
    mes = int(data[3]+data[4])
    ano = int(data[6]+data[7]+data[8]+data[9])

    if (tamanhodata != 10):
        print 'Tamanho/formato de data invalido'
    elif(data[2]=='/' and data[5]=='/'):
        if(dia>=1 and dia<=31) and (mes>=1 and mes<=12) and (ano>=0 and ano<=3000):
            print 'Data digita eh: ',data
        else:
            print 'Dia mes ou ano digitado esta invalido!!'

except:
    print 'Formato de data digitado esta invalido!!'
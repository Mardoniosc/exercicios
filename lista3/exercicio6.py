assinatura = '#================================================================================#' \
             '\n# Desenvolvido por: Mardonio Costa                                               #' \
             '\n# E-mail: Mardonio@live.com                                                      #' \
             '\n#                                                                                #' \
             '\n# Finalidade: Verifica numeros primeiros de 1 a 100                              #' \
             '\n#                                                                                #' \
             '\n#                                                               Data: 30/01/2018 #' \
             '\n# Release: 1.0.0                                                                 #' \
             '\n#================================================================================#\n\n'
_author_ = assinatura
print _author_

for i in range(1,100,1):
    n = 1
    while (i>=n):
        p = i%n
        if (p==0):
           if(n==1):
               n += 1;
               continue
           elif(n==i):
                print '%i eh numero primo' % i
           else:
               break
        n += 1;

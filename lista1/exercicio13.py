dias = int(raw_input('Informe a quantidade de dias: '))
horas = int(raw_input('Informe a quantidade de horas: '))
minutos = int(raw_input('Informe a quantidade de minutos: '))
segundo = int(raw_input('Informe a quantidade de segundo: '))

totaldesegundos = segundo+(60*(minutos+(60*(horas+(dias*24)))))

print totaldesegundos,'Segundos'    
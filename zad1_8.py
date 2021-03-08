rok = int(input('Podaj rok: '))

if (rok % 400 == 0):
    print('Rok jest przestepny')
elif (rok % 100 == 0):
    print('Rok nie jest przestepny')
elif (rok % 4 == 0):
    print('Rok jest przestepny')
else:
    print('Rok nie jest przestepny')
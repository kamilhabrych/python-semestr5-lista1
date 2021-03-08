f = float(input('Podaj liczbe zmiennoprzecinkowa: '))

d = int('%1d' % f)
x = d % 10
z = float('%.1f' % f) - d
y = int(z * 10)

print('Cyfra przed przecinkiem: ', x)
print('Cyfra po przecinku: ', y)
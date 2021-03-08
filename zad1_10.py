f = float(input('Podaj liczbe zmiennoprzecinkowa f: '))
g = float(input('Podaj liczbe zmiennoprzecinkowa g: '))

x = int(f)
y = int(g)

f = f - x + y
g = g - y + x

print(round(f,3))
print(round(g,3))
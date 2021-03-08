x = 2 ** (1/2)
y = 3 ** (1/3)
z = 5 ** (1/5)

print(x)
print(y)
print(z)
print()

if x>y and x>z:
    print(x,'jest największa')
elif y>x and y>z:
    print(y,'jest największa')
elif z>x and z>y:
    print(z,'jest największa')

print()

if x<y and x<z:
    print(x,'jest najmniejsza')
elif y<x and y<z:
    print(y,'jest najmniejsza')
elif z<x and z<y:
    print(z,'jest najmniejsza')
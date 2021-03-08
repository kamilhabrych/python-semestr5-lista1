i = int(input('Podaj i: '))
j = int(input('Podaj j: '))

x = i**j
y = j**i

if x > y:
    print(i,'do',j,'równe',x,'jest większe od',j,'do',i,'równe',y)
elif y > x:
    print(j,'do',i,'równe',y,'jest większe od',i,'do',j,'równe',x)
else:
    print('Potęgi sa równe')
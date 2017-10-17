names = ['Jep', 'Ger', 'Joll', 'Sam']

for name in names:
    print('Hello there, ' + name)
    print(' '.join(['Hello there,', name]))

print(', '.join(names))

who = 'Garyy'
how_many = 12
print(who, 'bought', how_many, 'apple today!')
print('{} bought apples today!'.format(who, how_many))
# skenario ke1
cities = ['Tegal', 'Bumiayu', 'Ajibarang', 'Purwokerto']
#the bad way
i = 1
for city in cities:
    print(i, city)
    i += 1
print('')
# the good way
for i, city in enumerate(cities):
    print(i, city)
print('')

# skenario ke2
x_list = [1,2,3]
y_list = [2,4,6]
# the bad way
for i in range(len(x_list)):
    x = x_list[i]
    y = y_list[i]
    print(x, y)
print('')
#the good way
for x in zip(x_list, y_list):
    print(x, y)
print('')
# skenario ke3
x = 10
y = -10
print('Before: x = %d, y = %d' % (x, y))
# the bad way
y = x
#x = tmp
# the good way
x, y = y, x
print('After: x = %d, y = %d' % (x, y))